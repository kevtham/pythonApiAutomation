import unittest

class CommonUtils(unittest.TestCase):
    
    instance = None
    
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CommonUtils()
        return cls.instance

    def assertEqualCheck(self, actual, expected, message):
        try:
            return self.assertEqual(actual, expected)
        except AssertionError:
            raise AssertionError("Assertion failed for the reason %s" %message)
    
    def assert_True(self, input):
        return self.assert_True(input)
    
    def assert_False(self, input):
        return self.assert_False(input)
    
    def assertEmptyCheck(self, value):
        if(value):
            return True
        else:
            return False

util = CommonUtils.get_instance()