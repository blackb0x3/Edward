import os, random, numpy as np

from flask_restful import Resource, abort, reqparse
from flask import send_file
from pymongo import MongoClient
from typing import Dict

from scripts import Sorts, Search
from scripts.Chart import CompareChart, TestChart
from config import ROOT_DIR, DEFAULT_MIN_COLLECTION_SIZE, DEFAULT_MAX_COLLECTION_SIZE

ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY = "name"
ALGORITHM_OBJECT_CLASS_DICT_KEY = "class"

sorts = {
    "insertion-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "INSERTION SORT",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.InsertionSort
    },
    "selection-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Selection Sort",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.SelectionSort
    },
    "traditional-bubble-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Traditional Bubble Sort",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.TraditionalBubbleSort
    },
    "optimised-bubble-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Optimised Bubble Sort",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.OptimisedBubbleSort
    },
    "recursive-quick-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Quick Sort - Recursive Version",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.RecursiveQuickSort
    },
    "iterative-quick-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Quick Sort - Iterative Version",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.IterativeQuickSort
    },
    "top-down-merge-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Merge Sort - Top Down Approach",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.TopDownMergeSort
    },
    "bottom-up-merge-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Merge Sort - Bottom Up Appproach",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.BottomUpMergeSort
    },
    "heap-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Heap Sort",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.HeapSort
    },
    "shell-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Shell Sort",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.ShellSort
    },
    "counting-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Counting Sort",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.CountingSort
    },
    "bucket-sort": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Bucket Sort",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Sorts.BucketSort
    }
}

search = {
    "linear-search": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Linear Search",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Search.LinearSearch
    },
    "bi-linear-search": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Bi-linear Search",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Search.BilinearSearch
    },
    "binary-search": {
        ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY : "Binary Search",
                         ALGORITHM_OBJECT_CLASS_DICT_KEY : Search.BinarySearch
    }
}

algorithmmap = {**sorts, **search} # type: Dict[str, Algorithm]


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
        algorithm = algorithmmap[algname][ALGORITHM_OBJECT_CLASS_DICT_KEY](data=coll)
        algorithm.run()
        return algorithm.__dict__(), 200

    def _test(self, algname, options, verbose):
        min_size = int(options['min_size']) # TODO must be at least 5
        max_size = int(options['max_size']) # TODO must be at least 10
        jump     = int(options['jump']) # TODO must be at least 1
        #repeats = options['repeats'] # TODO must be at least 3

        algorithm_results = {}
        algorithm_results_json = {}

        for size in range(min_size, max_size + 1, jump):
            results_for_this_size = []
            results_for_this_size_json = []

            repeats = int(options['repeats']) # TODO must be at least 3

            while repeats > 0:
                # get algorithm class from map, instantiate and run
                algorithm = algorithmmap[algname][ALGORITHM_OBJECT_CLASS_DICT_KEY](size=size)
                algorithm.run()

                results_for_this_size.append(algorithm)
                results_for_this_size_json.append(algorithm.__dict__())
                repeats -= 1

            algorithm_results.update({size: results_for_this_size})
            algorithm_results_json.update({size: results_for_this_size_json})

        ############################## OBSOLETE!! #############################
        #if options['makegraph'] is True:
        #    algorithm_results_json['graph'] = TestChart.new(algorithm_results)
        #else:
        #    algorithm_results_json['graph'] = None
        ########################### END OF OBSOLETE ###########################

        ################################### TO BE FIXED ###################################
        #insertion_success = AlgorithmController.results_collection.insert_one(algorithm_results_json)

        #algorithm_results_json["results_cache_id"] = insertion_success.inserted_id
        ################################### TO BE FIXED ###################################

        if verbose is False:
            to_return = self.cut_down_test_results(algorithm_results)
        else:
            to_return = algorithm_results_json

        return to_return, 200

    def _compare(self, algname, other_algs, **kwargs):
        # gets the class from the global algorithms dictionary - algorithmmap
        original_algorithm_class = algorithmmap[algname][ALGORITHM_OBJECT_CLASS_DICT_KEY]

        # gets the other algorithm classes via the provided 'other_algs' list of algorithm keys
        other_algorithm_classes = {k: algorithmmap[k][ALGORITHM_OBJECT_CLASS_DICT_KEY] for k in set(other_algs)}

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

        #insertion_success = AlgorithmController.results_collection.insert_one(results_json)

        #results_json["results_cache_id"] = insertion_success.inserted_id

        return results_json, 200

    def cut_down_test_results(self, algorithm_results):
        to_return = {}
        execution_times = {}
        for size, algorithms in algorithm_results.items():
            average_execution_time = np.average([algorithm.timetaken.total_seconds() for algorithm in algorithms])
            execution_times.update({size: average_execution_time})

        to_return['sizes'] = list(execution_times.keys())
        to_return['times'] = list(execution_times.values())
        return to_return

    def get(self, algorithmname):
        """
        Algorithm metadata - space complexity, time complexity, description etc.
        """

        self.check_algorithm_exists(algorithmname)

        try:
            return algorithmmap[algorithmname][ALGORITHM_OBJECT_CLASS_DICT_KEY].metadata(), 200
        except NotImplementedError:
            abort(501, message="There is no metadata available for the {0} algorithm.".format(algorithmname))

    def post(self, algorithmname):
        """
        Runs the algorithm on a set of data.
        """

        self.check_algorithm_exists(algorithmname)

        try:
            algorithmmap[algorithmname][ALGORITHM_OBJECT_CLASS_DICT_KEY].metadata()
        except NotImplementedError:
            abort(501, message="The {} algorithm has not been implemented yet.".format(algorithmname))

        # TODO RequestParser is obsolete - update with new request parser.
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("action", type=str, required=True, location='json')
        parser.add_argument("makegraph", type=bool, default=False, store_missing=True, location='json')
        parser.add_argument("options", type=dict, default=dict(), store_missing=True, location='json')
        parser.add_argument("collection", type=list, required=False, store_missing=True, location='json')
        parser.add_argument("first_algorithm", type=str, required=False, store_missing=False, location='json')
        parser.add_argument("second_algorithm", type=str, required=False, store_missing=False, location='json')
        parser.add_argument("verbose", type=bool, required=False, default=False, location='json')

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

            # error checking in options parameter
            if int(options['min_size']) < 5:
                abort(400, message="The smallest test collection must have at least 5 elements.")

            if int(options['max_size']) < 10:
                abort(400, message="The largest test collection must have at least 10 elements.")

            if int(options['jump']) < 1:
                abort(400, message="Invalid number of collection sizes to jump. Must be greater than or equal to 1.")

            if int(options['repeats']) < 3:
                abort(400, message="You must repeat each collection size at least 3 times.")

            # obsolete - graphs are produced in the front-end
            #options['makegraph'] = False if args['makegraph'] is None else args['makegraph']

            # TODO set endpoint responses in .htaccess file for each action, instead of updating codebase
            if action == "run":
                #abort(503, message="The {} action is not available.".format(action))
                return self._run(algname=algorithmname, coll=args['collection'])

            if action == "test":
                #abort(503, message="The {} action is not available.".format(action))
                return self._test(algname=algorithmname, options=options, verbose=args['verbose'])

            if action == "compare":
                #abort(503, message="The {} action is not available.".format(action))
                return self._compare(algname=algorithmname, other_algs=args['other_algorithms'], coll=args['collection'], options=options)


class GraphController(Resource):
    def get(self, graphid):
        return send_file(os.path.join(ROOT_DIR, "images/graphs/", graphid + ".png"), mimetype="image/png")

  
class AlgorithmTypesController(Resource):
    def _get_keys_with_frontend_names(self, keys: list):
        return dict([(key, algorithmmap[key][ALGORITHM_TYPE_CONTROLLER_INTERNAL_NAME_DICT_KEY]) for key in keys])

    def get(self, algorithmtype):
        if algorithmtype == "sorting":
            return self._get_keys_with_frontend_names(list(sorts.keys())), 200
        elif algorithmtype == "searching":
            return self._get_keys_with_frontend_names(list(search.keys())), 200
        else:
            abort(400, message="Algorithm type '{0}' does not yet exist within the API.")
