import unittest

import trafficSimulator as ts

class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(3 + 3, 6)


if __name__ == '__main__':
    unittest.main()
