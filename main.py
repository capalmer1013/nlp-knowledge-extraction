__author__ = 'cpalmer'
import objects
import open_file
import parse_string

list_of_adjectives = open_file.get_adjectives()
list_of_adverbs = open_file.get_adverbs()
list_of_nouns = open_file.get_nouns()
list_of_verbs = open_file.get_verbs()

states = [' is ']
state_dict = {}

object_dict = {}

list_of_sentences = []

filename = input("Enter Filename: ")

file_as_string = open_file.get_file_as_string(filename)

for state in states:
    list_of_indices = parse_string.find_indices(file_as_string, state)
    state_dict[state] = list_of_indices

for state in state_dict:
    for index in state_dict[state]:
        list_of_sentences.append(parse_string.get_sentence(file_as_string, index))

list_of_indices = []
for sentence in list_of_sentences:
    for state in states:
        list_of_indices = parse_string.find_indices(sentence, state)
        for index in list_of_indices:
            previous_word = parse_string.get_previous_word(sentence, index)
            next_word = parse_string.get_next_word(sentence, index)

            while len(previous_word) > 0 and not previous_word[0].isalpha():
                previous_word = previous_word[1:]

            while len(previous_word) > 0 and not previous_word[-1].isalpha():
                previous_word = previous_word[:-1]

            previous_word = previous_word.lower()

            if previous_word+'\n' in list_of_nouns:
                if previous_word in object_dict:
                    object_dict[previous_word].properties.append(next_word)
                else:
                    object_dict[previous_word] = objects.Object(previous_word)
                    object_dict[previous_word].properties.append(next_word)

for item in object_dict:
    print(item)
    for attribute in object_dict[item].properties:
        print("->"+attribute)