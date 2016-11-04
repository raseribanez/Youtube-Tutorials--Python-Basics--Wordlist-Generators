# Ben Woodfield
# This simple list generator DOES repeat characters in each result

import itertools
res = itertools.product('abc', repeat=3)
for i in res: 
    print ''.join(i)
