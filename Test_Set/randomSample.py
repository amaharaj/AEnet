import os
import random 
import sys

# execute as: python randomSample.py <number of samples>

samples = sys.argv[1]
samples = int(samples)

for i in range(samples):
   a = random.randint(1,19815)
   n = '%06d' % a
   os.system("cp ../structure{0}.xsf .".format(n) )
