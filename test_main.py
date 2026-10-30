from main import *

import random

# 4 pts
def test_qsort_fixed():
	assert(qsort([5,4,3,2,1], lambda a: a[0])) == [1,2,3,4,5]

# 4 pts
def test_qsort_random():
	assert(qsort([5,4,3,2,1], lambda a: random.choice(a))) == [1,2,3,4,5]
