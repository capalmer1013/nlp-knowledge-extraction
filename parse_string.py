__author__ = 'cpalmer'


def find_indices(string, sub, listindex=[], offset=0):
    listindex = []
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex


def get_sentence(string, index):
    i = index
    while string[i] != '.' and string[i] != '?' and string[i] != '!':
        i -= 1
    begining = i
    i = index
    while string[i] != '.' and string[i] != '?' and string[i] != '!':
        i += 1
    end = i
    return string[begining+1:end+1]


def get_previous_word(string, index):
    if index > 0:
        i = index
        i -= 2
        while i >= 0 and string[i] != ' ':
            i -= 1
        return string[i + 1:index]
    else:
        return"N/A"


def get_next_word(string, index):
    if index <= len(string):
        i = index
        i += 4
        while i <= len(string) and string[i] != ' ' and string[i] != '!'and string[i] != '.' and string[i] != '?':
            i += 1
        return string[index+4:i]
    else:
        return"N/A"