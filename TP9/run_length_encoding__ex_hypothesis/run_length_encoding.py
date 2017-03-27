# SVL 16-17 - M. Nebut
# CTD property-based testing
# ex d'utilisation d'Hypothesing, le code est tiré de
# https://hypothesis.readthedocs.io/en/master/quickstart.html

'''
Run-length encoding (RLE) is a very simple form of lossless data
compression in which runs of data (that is, sequences in which the same
data value occurs in many consecutive data elements) are stored as a
single data value and count, rather than as the original run.

On peut encode une chaîne de taille quelconque :
>>> encode('a')
[('a', 1)]
>>> encode('aaa')
[('a', 3)]
>>> encode('aaabbaaaaceef')
[('a', 3), ('b', 2), ('a', 4), ('c', 1), ('e', 2), ('f', 1)]
>>> encode('')
[]

puis la décoder :
>>> decode([])
''
>>> decode([('a', 1)])
'a'
>>> decode([('a', 3)])
'aaa'
>>> decode([('a', 3), ('b', 2), ('a', 4), ('c', 1), ('e', 2), ('f', 1)])
'aaabbaaaaceef'
'''

def encode(input_string):
    if input_string == '':
        return []
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q
