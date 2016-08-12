#!/bin/bash

# script to generate footer to the generate.in file
# run this script and then `cat header file > generate.in`

rm file
counter=0
# read all contents of directory into a single file
for entry in `ls ../xsf/`; do
   echo ../xsf/$entry >> file
   counter=$((counter + 1))
done

# add header to beginning of file
echo $counter | cat - file | sponge file
echo "FILES" | cat - file | sponge file
