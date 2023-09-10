#! /usr/bin/python3
import unittest
from utils import utils  

tool = utils
class TestReversed(unittest.TestCase):

    def test_strings(self):
        error_raised = False
        try:
            tool.reversed("123.123")
        except TypeError:
            error_raised = True
        except:
            pass
        self.assertTrue(error_raised)
    
    def test_negative_int(self):
        error_raised = False
        try:
            tool.reversed(-123)
        except TypeError:
            error_raised = True
        except:
            pass
        self.assertFalse(error_raised)

    def test_floats(self):
        error_raised = False
        try:
            tool.reversed(123.123)
        except TypeError:
            error_raised = True
        except:
            pass
        self.assertTrue(error_raised)

    def test_integers(self):
        error_raised = False
        try:
            tool.reversed(123)
        except TypeError:
            error_raised = True
        except:
            pass
        self.assertFalse(error_raised)

    def test_format_strings(self):
        error_raised = False
        try:
            tool.formatter("123.123")
        except TypeError:
            error_raised = True
        except:
            pass
        self.assertTrue(error_raised)

    def test_format_floats(self):
        error_raised = False
        try:
            tool.formatter(123.123)
        except TypeError:
            error_raised = True
        except:
            pass
        self.assertTrue(error_raised)

    def test_format_integers(self):
        error_raised = False
        try:
            tool.formatter(123)
        except TypeError:
            error_raised = True
        except:
            pass
        self.assertFalse(error_raised)

if __name__ == '__main__':
    unittest.main()