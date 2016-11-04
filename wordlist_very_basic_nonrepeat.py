# Ben Woodfield
# This basic list generator DOES NOT repeat characters in each result

import itertools
res = itertools.permutations('abc',3)
for i in res: 
   print ''.join(i)
