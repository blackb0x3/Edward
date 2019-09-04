import unittest


class GetAlgorithmTests(unittest.TestCase):
    def given_valid_algorithm_key_when_performing_get_then_expect_ok(self, parameter_list):
        pass

    def given_invalid_algorithm_key_when_performing_get_then_expect_404(self, parameter_list):
        pass

    def given_no_args_when_performing_get_all_then_expect_list_of_algorithm_keys(self, parameter_list):
        pass

    def given_no_args_when_performing_get_then_expect_400(self, parameter_list):
        pass

    def given_valid_unavailable_algorithm_key_when_performing_get_then_expect_502(self, parameter_list):
        pass
