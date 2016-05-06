#!/bin/bash

# run as "./checkDuplicates file" to see if there are any lines which have been printed multiple times

args=("$@")

sort ${args[0]} | uniq -d | grep -nFxf - ${args[0]}

