from flask_restful import Resource, abort, reqparse, output_json

from scripts.Sorts import *
from scripts.Graph import Graph

algorithmmap = {
    "insertion-sort": InsertionSort,
    "selection-sort": SelectionSort,
    "optimised-bubble-sort": OptimisedBubbleSort,
    "traditional-bubble-sort": TraditionalBubbleSort,
}

class AlgorithmController(Resource):
    valid_actions = [
        "run",
        "test"
    ]

    def check_algorithm_exists(self, algorithmname):
        if algorithmname not in algorithmmap.keys():
            abort(404, message="Algorithm '{}' doesn't exist.".format(algorithmname))

        return True

    def run_algorithm(self, algorithm: Algorithm):
        algorithm.run()

        if algorithm.has_worked():
            return algorithm
        else:
            return self.run_algorithm(algorithm=algorithm)

    def get(self, algorithmname=None):
        """
        Algorithm metadata - space complexity, time complexity, description etc.
        """

        if algorithmname is None:
            return {
                "available_algorithms": algorithmmap.keys()
            }, 200
        else:
            self.check_algorithm_exists(algorithmname)

            try:
                return algorithmmap[algorithmname].metadata(), 200
            except NotImplementedError as err:
                abort(501, message="There is no metadata available for the {} algorithm.".format(algorithmname))

    def post(self, algorithmname):
        """
        Runs the algorithm on a set of data.
        """

        self.check_algorithm_exists(algorithmname)

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("action", type=str, required=True)
        parser.add_argument("makegraph", type=bool)
        parser.add_argument("options", type=dict)
        parser.add_argument("collection", type=list)
        args = parser.parse_args()

        action = args['action']

        if action == "":
            abort(400, message="No action specified.")
        else:
            if action not in AlgorithmController.valid_actions:
                abort(400, "Invalid action '{}'".format(action))

            default_options = {
                'min_size': 5,
                'max_size': 20,
                'jump': 1,
                'repeats': 5
            }

            # use pure default options if no options are provided
            options_not_provided = args['options'] is None or args['options'] == {}
            options = default_options if options_not_provided else {**default_options, **args['options']}

            # don't make graph unless specified otherwise
            makegraph = False if args['makegraph'] is None else args['makegraph']

            if action == "run":
                algorithm = algorithmmap[algorithmname](args['collection'])
                algorithm.run()
                return algorithm.__dict__(), 200

            if action == "test":
                # Uncomment during controller debugging
                #abort(503, message="The {} action is not available.".format(action))
                min_size = options['min_size'] # TODO must be at least 5
                max_size = options['max_size'] # TODO must be at least 10
                jump     = options['jump'] # TODO must be at least 1
                repeats  = options['repeats'] # TODO must be at least 3

                algorithm_results = {}

                for size in range(min_size, max_size + 1, jump):
                    results_for_this_size = []

                    for i in range(repeats):
                        algorithm = algorithmmap[algorithmname](size=size)
                        results_for_this_size.append(self.run_algorithm(algorithm=algorithm).__dict__())

                    algorithm_results.update({size: results_for_this_size})

                if makegraph is True:
                    graphfile = Graph.new(algorithm_results)
                    algorithm_results['graph'] = graphfile
                else:
                    algorithm_results['graph'] = None

                return algorithm_results, 200
