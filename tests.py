import json
import logging
import unittest

import haiku

logging.basicConfig(level=logging.ERROR)
logging.disable(level=logging.ERROR)


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.hd = haiku.HaikuDetector()

    def test_syllables(self):
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables_line("dog")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables_line("asdf")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables_line("letter")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("washington")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables_line("dock")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables_line("dangle")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables_line("thrive")])
        self.assertIn(1, [sum(x) for x in self.hd.num_syllables_line("fly")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables_line("placate")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables_line("renege")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("reluctant")])

        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("firelight")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables_line("frolicked")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("doomscrolling")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("treasuring")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("re echoes")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables_line("gunna")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("unresolve")])
        self.assertIn(2, [sum(x) for x in self.hd.num_syllables_line("bloodshot")])
        self.assertIn(3, [sum(x) for x in self.hd.num_syllables_line("tempura")])
        self.assertIn(5, [sum(x) for x in self.hd.num_syllables_line("ozymandias")])

    def test_haikus(self):
        hd = haiku.HaikuDetector()
        with open('haiku_list.json') as f:
            haiku_list = json.load(f)
        results = []
        for poem in haiku_list:
            # lines = poem.split('/')
            # lines = [x for x in lines if (x != '' and x != ' ')]
            results.append(hd.is_haiku(poem))
        accuracy = 100 * results.count(True) / len(results)
        print(f'{results.count(True)} / {len(results)} ({accuracy:.2f}%)')


if __name__ == '__main__':
    unittest.main()

