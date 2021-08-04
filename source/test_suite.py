import unittest
from unittest.suite import TestSuite
from tests.add_computer import AddComputerTest
from tests.case_sensitivity import CaseSensitivityTest
from tests.delete_computer import DeleteComputerTest
from tests.previous_next_buttons import NextButtonTest, PreviousButtonTest
from tests.sorting import SortingTest


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(AddComputerTest))
    test_suite.addTest(unittest.makeSuite(CaseSensitivityTest))
    test_suite.addTest(unittest.makeSuite(DeleteComputerTest))
    test_suite.addTest(unittest.makeSuite(NextButtonTest))
    test_suite.addTest(unittest.makeSuite(PreviousButtonTest))
    test_suite.addTest(unittest.makeSuite(SortingTest))
    return test_suite

mySuit=suite()

runner=unittest.TextTestRunner(verbosity=2) # verbosity=2 for seing more information about testcases
runner.run(mySuit)