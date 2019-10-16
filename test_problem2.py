import problem2
import unittest

class TestStringMethods(unittest.TestCase):

    def test_circle_area(self):
        self.assertEqual(problem2.circle_area(1),3.14,"Circle area is incorrect")
    
    def test_circle_circumference(self):
        self.assertEqual(problem2.circle_circumference(1),6.28,"Circle circumference is incorrect")
        
    def test_square_area(self):
        self.assertEqual(problem2.square_area(1),1,"Square area is incorrect")

    def test_square_perimeter(self):
        self.assertEqual(problem2.square_perimeter(1),4,"Square perimeter is incorrect")

    def test_rectangle_area(self):
        self.assertEqual(problem2.rectangle_area(2,3),6,"Rectangle area is incorrect")

    def test_rectangle_perimeter(self):
        self.assertEqual(problem2.rectangle_perimeter(2,3),10,"Rectangle perimeter is incorrect")
    
if __name__ == '__main__':
    unittest.main()
    
    
