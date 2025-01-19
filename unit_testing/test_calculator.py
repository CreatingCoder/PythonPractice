import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1,6), 7)


if __name__ == '__main__':
    unittest.main()
