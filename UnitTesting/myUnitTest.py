import unittest


def add(x, y):
  """Returns the sum of two numbers."""
  return x + y

class TestAdd(unittest.TestCase):

  def test_add_positive(self):
    result = add(5, 3)
    self.assertEqual(result, 8)

  def test_add_negative(self):
    result = add(-2, 7)
    self.assertEqual(result, 5)
  def test_add_two_negatives(self):
    result = add(-2,-5)
    self.assertEqual(result,-7)

if __name__ == "__main__":
  unittest.main()