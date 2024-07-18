import json
import logging
import nltk
import re
import itertools
import syllables


logging.basicConfig(level=logging.ERROR)
logging.disable(level=logging.ERROR)


def tokenize(text):
    text = text.translate((str.maketrans('-[]', '   ')))  # separate hyphenated words in two
    text = text.translate(str.maketrans('', '', "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"))  # remove punctuation
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower().split(' ')


class HaikuDetector:
    def __init__(self):
        self.pronunciations = nltk.corpus.cmudict.dict()
        with open('syllable_dictionary.json') as f:
            self.syllable_dict = json.load(f)

    def print_info(self, poem):
        for line in poem:
            print(f'({[sum(x) for x in self.num_syllables(line)]}) {" ".join(tokenize(line))} {self.num_syllables(line)}')
        print()

    def guess_syllables(self, word):
        if word in self.syllable_dict:
            return self.syllable_dict[word]
        print(f'{word} not found in pronunciation dictionary')
        return syllables.estimate(word)

    def num_syllable(self, word):
        if word not in self.pronunciations:
            return [self.guess_syllables(word)]

        syllables_in_pronunciations = []
        # if len(self.pronunciations[word]) > 1:
        #     logging.info(f'more than one pronunciation found for {word}: {self.pronunciations[word]}')
        for pronunciation in self.pronunciations[word]:
            current_syllable_count = 0
            for phoneme in pronunciation:
                phoneme_is_vowel = re.search(r'[0-9]+', phoneme)  # phoneme is vowel if it has a number after it
                if phoneme_is_vowel is not None:
                    current_syllable_count += 1
            syllables_in_pronunciations.append(current_syllable_count)
        return sorted(list(set(syllables_in_pronunciations)))

    def num_syllables(self, line):
        syllable_dict = {}
        words = tokenize(line)
        for word in words:
            syllable_dict[word] = self.num_syllable(word)

        my_list = []
        for word in words:
            my_list.append(syllable_dict[word])

        return list(itertools.product(*my_list))

    def is_haiku(self, poem):
        if len(poem) != 3:
            # logging.error('Not 3 lines.')
            # self.print_info(poem)
            return False
        if 5 not in [sum(x) for x in self.num_syllables(poem[0])]:
            # logging.error(f'First line has {[sum(x) for x in self.num_syllables(poem[0])]} syllables instead of 5')
            # self.print_info(poem)
            return False
        if 7 not in [sum(x) for x in self.num_syllables(poem[1])]:
            # logging.error(f'Second line has {[sum(x) for x in self.num_syllables(poem[1])]} syllables instead of 7')
            # self.print_info(poem)
            return False
        if 5 not in [sum(x) for x in self.num_syllables(poem[2])]:
            # logging.error(f'Third line has {[sum(x) for x in self.num_syllables(poem[1])]} syllables instead of 5')
            # self.print_info(poem)
            return False
        return True


def main():
    buffer = ''
    inline = ' '
    while inline != '':
        buffer += '%s\n' % inline
        inline = input()

    lines = buffer.split('\n')
    lines = [x for x in lines if (x != '' and x != ' ')]
    hd = HaikuDetector()
    print(f'is a haiku: {hd.is_haiku(lines)}')


if __name__ == '__main__':
    # main()
    # print(tokenize('Chess-like decision process'))
    hd = HaikuDetector()
    # print(hd.num_syllables('my chaotic family'))
    print(hd.pronunciations["you'll"])
