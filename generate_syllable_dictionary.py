import json

#  http://www.delphiforfun.org/programs/Syllables.htm
with open('Syllables.txt', encoding='utf-16') as f:
    lines = f.readlines()

syllables_dict = {}

for line in lines:
    try:
        word = line.split('=')[0]
        pronunciation = line.split('=')[1]
        num_syllables = len(pronunciation.split('�'))

        syllables_dict[word] = num_syllables
    except:
        print(line)

with open('SyllablesUpdate.txt') as f:
    lines = f.readlines()

for line in lines:
    try:
        word = line.split('=')[0]
        pronunciation = line.split('=')[1]
        num_syllables = len(pronunciation.split(' '))

        syllables_dict[word] = num_syllables
    except:
        print('2', line)

syllables_dict['unresolve'] = 3
syllables_dict['ozymandias'] = 5

with open('syllable_dictionary.json', 'w') as f:
    json.dump(dict(sorted(syllables_dict.items())), f)
