import unittest
from main import add,look_and_say


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_look_and_say(self):
        # 1 becomes 11 (1 copy of digit 1).
        # 11 becomes 21 (2 copies of digit 1).
        # 21 becomes 1211 (one 2 followed by one 1).
        # 1211 becomes 111221 (one 1, one 2, and two 1s).
        # 111221 becomes 312211 (three 1s, two 2s, and one 1).
        self.assertEqual(look_and_say("1"), "11")
        self.assertEqual(look_and_say("11"), "21")
        self.assertEqual(look_and_say("21"), "1211")
        self.assertEqual(look_and_say("111221"), "312211")


if __name__ == "__main__":
    unittest.main()
