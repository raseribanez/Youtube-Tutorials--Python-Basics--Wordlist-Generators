#!/usr/bin/env/python
# Ben Woodfield
import itertools

chrs = 'abcd' # Change your required characters here
n = 5 # Change your word length here

for xs in itertools.product(chrs, repeat=n):
   print ''.join(xs)


