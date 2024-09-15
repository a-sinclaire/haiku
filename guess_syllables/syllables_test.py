import time
import json

import syllables

from guess_syllables import *

with open('syllable_dictionary.json') as f:
    word_list = json.load(f)
cmu_word_list = dict([(w, c) for w, c in word_list.items() if w in pronunciations])

def list_wrap(something):
    return something if type(something) is list else [something]

# test phone_syllables
def test_func(func, word_list):
    start = time.process_time_ns()
    results = []
    for word, syl in word_list.items():
        try:
            results.append(syl in list_wrap(func(word)))
        except:
            results.append(False)
    dur = time.process_time_ns() - start
    accuracy = 100 * results.count(True) / len(results)
    print(f'{func.__name__}')
    print(f'{results.count(True)} / {len(results)} ({accuracy:.2f}%)')
    print(f'{dur/1000000000:.4f}s')
    print()

def main():
    test_func(phone_syllables, word_list)
    test_func(regex_syllables, word_list)
    test_func(sammy_guess, word_list)
    test_func(syllables.estimate, word_list)
    test_func(guess_syllables, word_list)

    print('---Test on words only in CMU---')
    test_func(phone_syllables, cmu_word_list)
    test_func(regex_syllables, cmu_word_list)
    test_func(sammy_guess, cmu_word_list)
    test_func(syllables.estimate, cmu_word_list)
    test_func(guess_syllables, cmu_word_list)

if __name__ == '__main__':
    main()