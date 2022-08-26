import unittest
import test

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(test)

testResult = unittest.TestResult()

unittest.TextTestRunner(verbosity=1).run(suites)

print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)
