import unittest
import new_calulator


class TestCalculator(unittest.TestCase):
    """
    Always write good test not write a lot tests
    """
    def test_add(self):
      self.assertEqual(new_calulator.add(30, 30), 60)
      #check edge cases
      self.assertEqual(new_calulator.add(-3, 3), 0)
      self.assertEqual(new_calulator.add(-5, -5), -10)

    def test_subtract(self):
      self.assertEqual(new_calulator.subtract(30, 30), 0)

    def test_multiply(self):
      self.assertEqual(new_calulator.multiply(20, 3), 60)

    def test_divide(self):
      self.assertEqual(new_calulator.divide(15, 5), 3)
      # use context manager for testing exceptions
      with self.assertRaises(ValueError):
          new_calulator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()