import unittest
from main import *

class StringMultiplicationTDD(unittest.TestCase):
    def test_multiplystr(self):
        self.assertEqual("132", multiplystr("12","11"))
        self.assertEqual("25", multiplystr("5","5"))
        self.assertEqual("6", multiplystr("2","3"))
    def test_multiplystr_edge(self):
        self.assertEqual("0", multiplystr("0","0"))
        self.assertEqual("0", multiplystr("0","3"))
        self.assertEqual("0", multiplystr("3","0"))
        self.assertEqual("3024", multiplystr("1008","3"))
    
    def test_multiplystr_big_nums(self):
        self.assertEqual("2830869077153280552556547081187254342445169156730", multiplystr("1020303004875647366210", "2774537626200857473632627613"))
        self.assertEqual("81129638414606663681390495662081",multiplystr("9007199254740991", "9007199254740991"))

if __name__ == '__main__':
    unittest.main()