import logging
import unittest

from datasets import load_dataset
import haiku

logging.basicConfig(level=logging.ERROR)
logging.disable(level=logging.ERROR)

ds = load_dataset("statworx/haiku")


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.hd = haiku.HaikuDetector()

    def test_syllables(self):
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables("dog")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables("asdf")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("letter")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables("washington")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables("dock")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("dangle")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables("thrive")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables("fly")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("placate")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("renege")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables("reluctant")])

        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("firelight")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("frolicked")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables("doomscrolling")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables("treasuring")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables("re echoes")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("gunna")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables("unresolve")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables("bloodshot")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables("tempura")])
        self.assertIn(5, [sum(x) for x in self.hd.num_syllables("ozymandias")])


# def test_haikus():
#     count = 0
#     total = 0
#     hd = haiku.HaikuDetector()
#     for poem in ds['train']['text'][:250]:
#         lines = poem.split('/')
#         total += 1
#         if hd.is_haiku(lines):
#             count += 1
#     print(f'{count} / {total}')


if __name__ == '__main__':
    unittest.main()
    # test_haikus()

