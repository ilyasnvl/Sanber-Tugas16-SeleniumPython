import unittest
from unittest.suite import TestSuite
import employe

if __name__ == "__main__":

    # inisiasi test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #add test
    suite.addTest(loader.loadTestsFromModule(employe))

    #create runner
    runner = unittest.TextTestRunner()
    runner.run(suite)
