import requests, unittest

BASE_URL = "http://localhost:5000"

# when writing tests, assert the structure of the responses, rather than actual data


class AlgorithmListControllerTests(unittest.TestCase):
    def test_get(self):
        # given no parameters
        # when performing a GET to /api/algorithms
        response_with_http = requests.get(f"{BASE_URL}/api/algorithms")
        response = response_with_http.json()

        # then expect HTTP 200 OK - list of available algorithm keys
        self.assertTrue(response_with_http.ok())
        self.assertTrue(response_with_http.status_code == 200)
        correct_key = "available_algorithms"
        self.assertTrue(correct_key in response.keys())
        self.assertTrue(type(response[correct_key]) is list)
        self.assertTrue(len(response[correct_key]) > 0)
        self.assertTrue(all([type(entry).__name__ == "str" for entry in response[correct_key]]))


class AlgorithmTypesControllerTests(unittest.TestCase):
    def test_get_valid_arg(self):
        # given valid algorithm type key
        algorithm_type_to_use = "sorting"

        # when performing a GET to /api/algorithmType/<algorithm_type>
        response_with_http = requests.get(f"{BASE_URL}/api/algorithmType/{algorithm_type_to_use}")
        response = response_with_http.json()

        # then expect list of available algorithm keys of that type
        self.assertTrue(response_with_http.ok())
        self.assertTrue(response_with_http.status_code == 200)
        self.assertTrue(type(response) is dict)
        self.assertTrue(len(response.keys()) > 0)
        self.assertTrue(all([type(key).__name__ == "str" for key in response.keys()]))
        self.assertTrue(all([type(val).__name__ == "str" for val in response.values()]))

    def test_get_no_args(self):
        # given no args
        # when performing a GET to /api/algorithmType
        response_with_http = requests.get(f"{BASE_URL}/api/algorithmType")

        # then expect HTTP 404 response
        self.assertFalse(response_with_http.ok())
        self.assertTrue(response_with_http.status_code == 404)

    def test_get_invalid_arg(self):
        # given invalid algorithm type key
        invalid_key = "abcdefg"

        # when performing a GET to /api/algorithmType/<algorithm_type>
        response_with_http = requests.get(f"{BASE_URL}/api/algorithmType")
        response = response_with_http.json()

        # then expect HTTP 400 response
        self.assertFalse(response_with_http.ok())
        self.assertTrue(response_with_http.status_code == 400)
        self.assertEqual(response["message"], f"Algorithm type '{invalid_key}' does not exist within the API.")


class AlgorithmControllerTests(unittest.TestCase):
    def test_get_valid_arg_available(self):
        # given valid algorithm key
        available_key = "insertion-sort"

        # when performing a GET to /api/algorithms/<algorithm_key>
        response_with_http = requests.get(f"{BASE_URL}/api/algorithms/{available_key}")
        response = response_with_http.json()

        # if algorithm is available
        # then expect HTTP 200 OK - algorithm JSON metadata
        self.assertTrue(response_with_http.ok())
        self.assertTrue(response_with_http.status_code == 200)

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

if __name__ == "__main__":
    unittest.main()
