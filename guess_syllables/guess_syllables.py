from itertools import chain
import json
import re

import nltk

try:
    pronunciations = nltk.corpus.cmudict.dict()
except LookupError:
    nltk.download('cmudict')
    pronunciations = nltk.corpus.cmudict.dict()

with open('syllable_dictionary.json') as f:
    syllable_dict = json.load(f)

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


leading_digraphs = {'kn': 'N', 'wr': 'R', 'wh': 'W', 'ts': '$'}
tailing_digraphs = {'mb': 'M', 'ck': 'K', 'gh': 'G'}
vowel_digraphs = {'ay': 'A', 'ai': 'I', 'ea': 'Y', 'ee': 'E',
                  'oa': 'O', 'ue': 'U', 'oo': '0', 'ei': '!'}
consonant_digraphs = {'ch': 'C', 'sh': 'S', 'ph': 'P', 'th': 'T',
                      'qu': 'Q'}

def replace_digraphs(word: str) -> str:
    """
    Transform a word, attempting to replace any sounds represented by a
    digraph with a single character.

    The idea here is to transform the word such that each character encodes
    a single sound to make it easier to work with for our purposes
    """
    global leading_digraphs, tailing_digraphs, vowel_digraphs, consonant_digraphs
    if len(word) < 2:
        return word

    word = word.lower()
    if word[:2] in leading_digraphs:
        word = leading_digraphs[word[:2]] + word[2:]
    if word[-2:] in tailing_digraphs:
        word = word[:-2] + tailing_digraphs[word[-2:]]

    digraphs = chain(consonant_digraphs.items(),
                     vowel_digraphs.items())
    for digraph, replacement in digraphs:
        word = word.replace(digraph, replacement)

    return word


def sammy_guess(word: str) -> int:
    """
    Given some word (presumably not in the CMU pronunciation dict), try to
    guess the number of syllables it contains.
    """
    if len(word) < 2:  # i think a 2-letter word can have 2 syllables?
        return 1

    # convert str to list since strings are immutable
    characters = list(replace_digraphs(word))
    vowels = 'aeiou' + ''.join(vowel_digraphs.values())

    # parse leading 'rh' as a vowel sound (e.g. "rhotic")
    if ''.join(characters[:-2]) == 'rh':
        characters[:2] = ('e', 'r')
    # parse trailing 'thm' as containing a vowel sound (e.g. "algorithm")
    if ''.join(characters[-3:]) == 'thm':
        characters[:3] = ('T', 'u', 'm')

    last_char = characters[-1]
    # parse trailing 'y' as a vowel sound (e.g. "happy")
    if last_char == 'y':
        characters[-1] = 'Y'
    # parse trailing 'e' as silent (e.g. "glue")
    elif last_char == 'e':
        # check if 2nd to last character is a consonant without raising
        # IndexError if len(characters) is 1
        if characters[len(characters) - 2] not in vowels:
            characters.pop()

    # transform the word into a sequence of Vs and Cs, where V represents a
    # vowel and C represents a consonant.
    #
    # i suppose replacing most of the consonant digraphs is a little
    # redundant since all i'm doing is counting the Vs, but when i was
    # coming up with this solution i had planned on trying to calculate the
    # syllable boundaries but gave up (for now..)
    for idx, char in enumerate(characters):
        characters[idx] = 'V' if char in vowels else 'C'

    return max((1, characters.count('V')))


def guess_syllables(word):
    global syllable_dict

    syllables = []
    found = False
    # if word is in dictionary add that syllable count
    if word in syllable_dict:
        syllables.append(syllable_dict[word])
        found = True

    try:
        # if the word is in the CMU guess other possible counts
        # (accounts for variations in pronunciation)
        syllables.extend(phone_syllables(word))
        found = True
    except:
        pass

    # if it was in the dictionary we can exit now. no need to guess
    if found:
        return sorted(list(set(syllables)))

    # if it wasn't in the dictionary or in the CMU dictionary we guess
    syllables.append(sammy_guess(word))
    return sorted(list(set(syllables)))