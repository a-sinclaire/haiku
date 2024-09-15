import re

import nltk

try:
    pronunciations = nltk.corpus.cmudict.dict()
except LookupError:
    nltk.download('cmudict')
    pronunciations = nltk.corpus.cmudict.dict()

def phone_syllables(word):
    global pronunciations

    if word not in pronunciations:
        raise Exception('Unknown word.')

    syllables_in_pronunciations = []
    for pronunciation in pronunciations[word]:
        current_syllable_count = 0
        for phoneme in pronunciation:
            phoneme_is_vowel = re.search(r'[0-9]+', phoneme)  # phoneme is vowel if it has a number after it
            if phoneme_is_vowel is not None:
                current_syllable_count += 1
        syllables_in_pronunciations.append(current_syllable_count)
    return sorted(list(set(syllables_in_pronunciations)))


def regex_syllables(word):
    vowel_groups = re.findall(r'[aeiou]+.e|[aeiou]+|y$', word)
    syllable_guess = len(vowel_groups)
    if syllable_guess < 1:
        raise Exception('No syllables detected.')
    return [syllable_guess]


def sammy_guess(word):
    pass


def guess_syllables(word):
    try:
        return phone_syllables(word)
    except:
        try:
            return regex_syllables(word)
        except:
            return [1]