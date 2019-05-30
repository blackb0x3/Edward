import os, random

from flask_restful import Resource, abort, reqparse
from flask import send_file
from pymongo import MongoClient
from typing import Dict

from scripts import Sorts
from scripts.Chart import CompareChart, TestChart
from config import ROOT_DIR, DEFAULT_MIN_COLLECTION_SIZE, DEFAULT_MAX_COLLECTION_SIZE

sorts = {
    "insertion-sort":          Sorts.InsertionSort,
    "selection-sort":          Sorts.SelectionSort,
    "optimised-bubble-sort":   Sorts.OptimisedBubbleSort,
    "traditional-bubble-sort": Sorts.TraditionalBubbleSort,
    "recursive-quick-sort":    Sorts.RecursiveQuickSort,
    "iterative-quick-sort":    Sorts.IterativeQuickSort,
    "top-down-merge-sort":     Sorts.TopDownMergeSort,
    "bottom-up-merge-sort":    Sorts.BottomUpMergeSort,
    "heap-sort":               Sorts.HeapSort,
    "shell-sort":              Sorts.ShellSort,
    "counting-sort":           Sorts.CountingSort,
    "bucket-sort":             Sorts.BucketSort
}

algorithmmap = {**sorts} # type: Dict[str, Algorithm]


class AlgorithmListController(Resource):
    def get(self):
        return {
            "available_algorithms": list(algorithmmap.keys())
        }, 200


class AlgorithmController(Resource):
    valid_actions = [
        "run",
        "test",
        "compare"
    ]

    mongo_client = MongoClient("mongodb://localhost:27017")
    db = mongo_client.Edward
    results_collection = db.algorithm_results

    def check_algorithm_exists(self, algorithmname):
        if algorithmname not in algorithmmap.keys():
            abort(404, message="Algorithm '{}' doesn't exist.".format(algorithmname))

        return True

    def _run(self, algname, coll):
        algorithm = algorithmmap[algname](data=coll)
        algorithm.run()
        return algorithm.__dict__(), 200

    def _test(self, algname, options):
        min_size = options['min_size'] # TODO must be at least 5
        max_size = options['max_size'] # TODO must be at least 10
        jump     = options['jump'] # TODO must be at least 1
        #repeats = options['repeats'] # TODO must be at least 3

        algorithm_results = {}
        algorithm_results_json = {}

        for size in range(min_size, max_size + 1, jump):
            results_for_this_size = []
            results_for_this_size_json = []

            repeats = options['repeats'] # TODO must be at least 3

            while repeats > 0:
                # get algorithm class from map, instantiate and run
                algorithm = algorithmmap[algname](size=size)
                algorithm.run()

                results_for_this_size.append(algorithm)
                results_for_this_size_json.append(algorithm.__dict__())
                repeats -= 1

            algorithm_results.update({size: results_for_this_size})
            algorithm_results_json.update({size: results_for_this_size_json})

        if options['makegraph'] is True:
            algorithm_results_json['graph'] = TestChart.new(algorithm_results)
        else:
            algorithm_results_json['graph'] = None

        insertion_success = AlgorithmController.results_collection.insert_one(algorithm_results_json)

        algorithm_results_json["results_cache_id"] = insertion_success.inserted_id

        return algorithm_results_json, 200

    def _compare(self, algname, other_algs, **kwargs):
        original_algorithm_class = algorithmmap[algname]
        other_algorithm_classes = {k: algorithmmap[k] for k in set(other_algs)}

        # check if all algorithms solve the same computational problem
        # compare action will not work otherwise
        same_algorithms = all([original_algorithm_class.__base__ is classdef.__base__ for classdef in other_algorithm_classes])

        if same_algorithms is False:
            abort(400, message="The algorithms being compared do not solve the same computational problem.")

        other_results = dict()
        other_results_json = dict()

        for name in other_algs:
            other_results.update({ name: dict() })
            other_results_json.update({ name: dict() })

        # global var
        collection_to_use = kwargs.get("coll", None)

        empty_collection_types = [
            list(),
            tuple(),
            dict()
        ]

        options = kwargs.get('options', dict())

        if collection_to_use is None or collection_to_use in empty_collection_types:
            # must be at least 5
            min_size = options.get('min_size', DEFAULT_MIN_COLLECTION_SIZE)

            if min_size < DEFAULT_MIN_COLLECTION_SIZE:
                min_size = DEFAULT_MIN_COLLECTION_SIZE

            max_size = options.get('max_size', DEFAULT_MAX_COLLECTION_SIZE)

            if max_size < DEFAULT_MAX_COLLECTION_SIZE:
                max_size = DEFAULT_MAX_COLLECTION_SIZE

            if max_size <= min_size:
                abort(400, message="The max size ({0}) is less than the min size ({1})".format(max_size, min_size))

            size_to_use = random.randint(min_size, max_size)

            original_algorithm = original_algorithm_class(size=size_to_use)

            # get generated collection from first algorithm
            # avoids second algorithm generating another one
            # keeps experiment fair
            collection_to_use = original_algorithm.oldcollection

        original_results = list()
        original_results_json = list()

        other_results = dict()
        other_results_json = dict()

        repeats = options.get("repeats", 5)

        while repeats > 0:
            original_algorithm = original_algorithm_class(data=collection_to_use)
            other_algorithms = [(name, classdef(data=collection_to_use)) for name, classdef in other_algorithm_classes.items()]

            original_algorithm.run()
            original_results.append(original_algorithm)
            original_results_json.append(original_algorithm.__dict__())

            for name, algorithm in other_algorithms:
                if name not in other_results.keys():
                    other_results[name] = list()

                if name not in other_results_json.keys():
                    other_results_json[name] = list()

                algorithm.run()
                other_results[name].append(algorithm)
                other_results_json[name].append(algorithm.__dict__())

            repeats -= 1

        results = {
            "original_algorithm": {
                "name": algname,
                "result": original_results
            },
            "other_algorithms": other_results
        }

        results_json = {
            "original_algorithm": {
                "name": algname,
                "result": original_results_json
            },
            "other_algorithms": { name: other_results_json[name] for name in other_algorithm_classes.keys()}
        }

        if options['makegraph'] is True:
            results_json['graph'] = CompareChart.new(results, algname, set(other_algs))
        else:
            results_json['graph'] = None

        insertion_success = AlgorithmController.results_collection.insert_one(results_json)

        results_json["results_cache_id"] = insertion_success.inserted_id

        return results_json, 200

    def get(self, algorithmname):
        """
        Algorithm metadata - space complexity, time complexity, description etc.
        """

        self.check_algorithm_exists(algorithmname)

        try:
            return algorithmmap[algorithmname].metadata(), 200
        except NotImplementedError:
            abort(501, message="There is no metadata available for the {0} algorithm.".format(algorithmname))

    def post(self, algorithmname):
        """
        Runs the algorithm on a set of data.
        """

        self.check_algorithm_exists(algorithmname)

        try:
            algorithmmap[algorithmname].metadata()
        except NotImplementedError:
            abort(501, message="The {0} algorithm has not been implemented yet.".format(algorithmname))

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("action", type=str, required=True, location='json')
        parser.add_argument("makegraph", type=bool, default=False, store_missing=True, location='json')
        parser.add_argument("options", type=dict, default=dict(), store_missing=True, location='json')
        parser.add_argument("collection", type=list, required=False, store_missing=True, location='json')
        parser.add_argument("first_algorithm", type=str, required=False, store_missing=False, location='json')
        parser.add_argument("second_algorithm", type=str, required=False, store_missing=False, location='json')

        # contains all post data from request
        args = parser.parse_args()

        action = args['action']

        if action == "":
            abort(400, message="No action specified.")
        else:
            if action not in AlgorithmController.valid_actions:
                abort(400, message="Invalid action '{}'".format(action))

            default_options = {
                'min_size': 5,
                'max_size': 20,

                'jump': 1,
                'repeats': 5
            }

            # use pure default options if no options are provided
            # use default options with overrides from http request
            options_not_provided = args['options'] is None or args['options'] == {}
            options = default_options if options_not_provided else {**default_options, **args['options']}

            # don't make graph unless specified otherwise
            options['makegraph'] = False if args['makegraph'] is None else args['makegraph']

            if action == "run":
                #abort(503, message="The {} action is not available.".format(action))
                return self._run(algname=algorithmname, coll=args['collection'])

            if action == "test":
                #abort(503, message="The {} action is not available.".format(action))
                return self._test(algname=algorithmname, options=options)

            if action == "compare":
                #abort(503, message="The {} action is not available.".format(action))
                return self._compare(algname=algorithmname, other_algs=args['other_algorithms'], coll=args['collection'], options=options)


class GraphController(Resource):
    def get(self, graphid):
        return send_file(os.path.join(ROOT_DIR, "images/graphs/", graphid + ".png"), mimetype="image/png")
