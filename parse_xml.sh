#!/bin/bash

#awk '/<calculation>/{flag=1;next}/<\/calculation>/{flag=0}flag' water_300.xml > md
egrep '<atoms>' water_300.xml > number_of_atoms
awk '/<energy>/{flag=1;next}/<\/energy>/{flag=0}flag' md > energies
awk '/<varray name="positions" >/{flag=1;next}/<\/varray>/{flag=0}flag' md > positions
awk '/<varray name="forces" >/{flag=1;next}/<\/varray>/{flag=0}flag' md > forces
