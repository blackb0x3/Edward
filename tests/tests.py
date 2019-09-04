import requests, unittest


class AlgorithmListControllerTests(unittest.TestCase):
    def test_get(self):
        # given no parameters
        # when performing a GET to /api/algorithms
        # then expect HTTP 200 OK - list of available algorithm keys
        pass


class AlgorithmTypesControllerTests(unittest.TestCase):
    def test_get_valid_arg(self):
        # given valid algorithm type key
        # when performing a GET to /api/algorithmType/<algorithm_type>
        # then expect list of available algorithm keys of that type
        pass

    def test_get_no_args(self):
        # given no args
        # when performing a GET to /api/algorithmType/<algorithm_type>
        # then expect HTTP 400 response
        pass

    def test_get_invalid_arg(self):
        # given invalid algorithm type key
        # when performing a GET to /api/algorithmType/<algorithm_type>
        # then expect HTTP 404 response
        pass


class AlgorithmControllerTests(unittest.TestCase):
    def test_get_valid_arg_available(self):
        # given valid algorithm key
        # when performing a GET to /api/algorithms/<algorithm_key>
        # if algorithm is available
        # then expect HTTP 200 OK - algorithm JSON metadata
        pass

    def test_get_valid_arg_unavailable(self):
        # given valid algorithm key
        # when performing a GET to /api/algorithms/<algorithm_key>
        # if algorithm is unavailable
        # then expect HTTP 501 NOT IMPLEMENTED
        pass

    def test_get_invalid_arg(self):
        # given invalid algorithm key
        # when performing a GET to /api/algorithms/<algorithm_key>
        # then expect HTTP 404 response
        pass

    def test_post_not_implemented(self):
        # given valid POST request
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 501
        pass

    def test_post_no_action(self):
        # given POST request with no 'action' entry in JSON
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_pot_invalid_action(self):
        # given POST request with invalid 'action' entry in JSON
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_post_invalid_min_size(self):
        # given POST request with invalid 'min_size' entry in 'options' JSON
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_post_invalid_max_size(self):
        # given POST request with invalid 'max_size' entry in 'options' JSON
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_post_invalid_jump(self):
        # given POST request with invalid 'jump' entry in 'options' JSON
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_post_invalid_repeats(self):
        # given POST request with invalid 'repeats' entry in 'options' JSON
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_post_algorithm_type(self):
        # given POST request comparing two algorithms which solve different problems
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_post_max_min_size(self):
        # given POST request where max_size is lower than min_size
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 400
        pass

    def test_post_valid_request_run(self):
        # given valid post body with 'run' action
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 200 OK - experiment result
        pass

    def test_post_valid_request_test(self):
        # given valid post body with 'test' action
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 200 OK - experiment result
        pass

    def test_post_valid_request_compare(self):
        # given valid post body with 'compare' action
        # when performing a POST to /api/algorithms/<algorithm_key>
        # then expect HTTP 200 OK - experiment result
        pass
