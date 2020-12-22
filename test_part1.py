import inspect
import os
import sys
import unittest

# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# top_dir = os.path.dirname(current_dir)
#
# print(f"top_dir: {top_dir}")
# if top_dir not in sys.path:
#     sys.path.insert(0, top_dir)

import part1


class TestCoinProblemPart1(unittest.TestCase):

    def test_2_euros_34_cents(self):
        euros_amount = 2.34
        expected_result = [2.0, 0.2, 0.1, 0.02, 0.02]
        self.assertEqual(part1.main(['part1.py', str(euros_amount)]), expected_result)

    def test_33_cents(self):
        euros_amount = 0.33
        expected_result = [0.2, 0.1, 0.02, 0.01]
        self.assertEqual(part1.main(['part1.py', str(euros_amount)]), expected_result)

    def test_5_euros_99_cents(self):
        euros_amount = 5.99
        expected_result = [2.0, 2.0, 1.0, 0.5, 0.2, 0.2, 0.05, 0.02, 0.02]
        self.assertEqual(part1.main(['part1.py', str(euros_amount)]), expected_result)

    def test_8_euros(self):
        euros_amount = 8
        expected_result = [2.0, 2.0, 2.0, 2.0]
        self.assertEqual(part1.main(['part1.py', str(euros_amount)]), expected_result)


if __name__ == "__main__":
    unittest.main()
