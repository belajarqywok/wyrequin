import unittest
from src.utilities import utilities

class utility_tests(unittest.TestCase) :
    utils: utilities = utilities()

    # is file included
    def test_is_file_included (self) -> None :
        filename_request: str = "packet-capture.csv"

        self.assertTrue(
            expr = self.utils.is_file_included(filename_request),
            msg = "is file included"
        )

    # is file not included
    def test_is_file_not_included (self) -> None :

        filename_request: str = "packet-capture.txt"

        self.assertFalse(
            expr = self.utils.is_file_included(filename_request),
            msg = "is file not included"
        )
