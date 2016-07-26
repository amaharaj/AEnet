#!/bin/bash

args=("$@")
samples=${args[0]}

if [[ $# -eq 3 ]]
then
   cp $(printf '%s\n' ${args[1]}structure?????.xsf | awk -v samples="$samples" 'NR%samples == 1') ${args[2]}
else
    echo "Get's every nth structure of structures in previous directory"
    echo " " 
    echo "Usage: ./sampleMDTraj.sh <sampling frequency> <structure directory> <destination directory> "
fi 
