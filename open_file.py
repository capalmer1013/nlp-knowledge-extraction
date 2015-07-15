__author__ = 'cpalmer'
import os
import sys
current_path = os.path.dirname(os.path.abspath(__file__))


def get_nouns():
    list_of_nouns = []
    f = open(current_path+"/parts_of_speech/nouns.txt", 'r')

    for line in f:
        list_of_nouns.append(line)

    return list_of_nouns


def get_adjectives():
    list_of_adjectives = []
    f = open(current_path+"/parts_of_speech/adjectives.txt", 'r')

    for line in f:
        list_of_adjectives.append(line)

    return list_of_adjectives


def get_adverbs():
    list_of_adverbs = []
    f = open(current_path+"/parts_of_speech/adverbs.txt", 'r')

    for line in f:
        list_of_adverbs.append(line)

    return list_of_adverbs


def get_verbs():
    list_of_verbs = []
    f = open(current_path+"/parts_of_speech/verbs.txt", 'r')

    for line in f:
        list_of_verbs.append(line)

    return list_of_verbs


def get_file_as_string(filename):
    try:
        with open(current_path+'/'+filename) as inputFileHandle:
            return inputFileHandle.read()

    except IOError:
        sys.stderr.write("[myScript] - Error: Could not open %s\n" % current_path+'/'+filename)
        sys.exit(-1)