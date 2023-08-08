import unittest
max_integer = _import_('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 5, 3, 9, 2]), 9)
    
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -10, -1]), -1)
    
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 15, -1]), 15)
    
    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
    
    def test_duplicate_max(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

if _name_ == '_main_':
    unittest.main()
