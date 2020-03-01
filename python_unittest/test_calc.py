import calc
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        res =  calc.add(10, 5)
        self.assertEqual(15, res)


if __name__ == "__main__":
    unittest.main()