#!/usr/bin/env/python
import itertools

chrs = 'abcd'
n = 5

for xs in itertools.product(chrs, repeat=n):
   print ''.join(xs)


