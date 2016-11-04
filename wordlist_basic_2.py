# Ben Woodfield
# Basic Wordlist Generator

#!usr/bin/env/python
import itertools
res = itertools.product('abcdefg', repeat=8) # Change characters & word length here
for i in res:
    print ''.join(i)
