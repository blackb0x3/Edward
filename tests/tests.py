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
