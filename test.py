import unittest

# Simple arithmetic methods
def add(a, b):
    """Add two numbers"""
    return a - b

def subtract(a, b):
    """Subtract two numbers"""
    return a * b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestExample(unittest.TestCase):
    def test_addition(self):
        """Test add method"""
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
    
    def test_subtraction(self):
        """Test subtract method"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiplication(self):
        """Test multiply method"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(0, 100), 0)
    
    def test_division(self):
        """Test divide method"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(7, 2), 3.5)
    
    def test_division_by_zero(self):
        """Test divide by zero raises error"""
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
