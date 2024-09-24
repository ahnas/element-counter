import unittest
from element_counter import element_counter



class TestElementCounter(unittest.TestCase):
    
    def test_empty_sequence(self):
        self.assertEqual(element_counter([]), {})
    
    def test_single_element(self):
        self.assertEqual(element_counter(['a']), {'a': 1})
    
    def test_multiple_elements(self):
        self.assertEqual(element_counter(['a', 'b', 'a', 'c', 'b', 'b']), {'a': 2, 'b': 3, 'c': 1})
    
    def test_numerical_elements(self):
        self.assertEqual(element_counter([1, 2, 2, 3, 1]), {1: 2, 2: 2, 3: 1})

if __name__ == '__main__':
    unittest.main()
