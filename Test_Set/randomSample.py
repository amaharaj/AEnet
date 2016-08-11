import os
import random 
import sys

# execute as: python randomSample.py <number of samples>
# randomly selects structure files 
# currently needs manual input for number of structure files (to be fixed)

samples = sys.argv[1]
samples = int(samples)
nfiles = 19815

for i in range(samples):
   a = random.randint(1,nfiles)
   n = '%06d' % a
   os.system("cp ../structure{0}.xsf .".format(n) )
