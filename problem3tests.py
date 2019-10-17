import unittest
from problem3 import *

#I am assuming that for the inputs and edge cases do not 
# have any leading zeros and only contains inputs from 0-9. 
# I am also assuming that the length of the inputs can be any length
 
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
        self.assertEqual("2641570682124889608296169469210917700", multiplystr("183757846069483648670", "14375281048549310"))
        self.assertEqual("12077380425291552952910211095709372185056715237945960335085637549092884139671029401773",multiplystr("34895748579824375982758972489375298758924758927", "346098906509038592839209849042809284099"))

if __name__ == '__main__': 
    unittest.main()