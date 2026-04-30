import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        """Test basic addition"""
        self.assertEqual(1 + 1, 2)
    
    def test_subtraction(self):
        """Test basic subtraction"""
        self.assertEqual(5 - 3, 2)
    
    def test_multiplication(self):
        """Test basic multiplication"""
        self.assertEqual(3 * 4, 12)

if __name__ == '__main__':
    unittest.main()
