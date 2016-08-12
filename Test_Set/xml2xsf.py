import numpy as np

# converts xml file to xsf file
# currently requires number_of_atoms and basis_vectors written as  
# they would be in an xsf file

with open('number_of_atoms','r') as f:
   first_line=f.readline()

with open('basis_vectors','r') as f:
   coord_1 = f.readline()
   coord_2 = f.readline()
   coord_3 = f.readline()

n=first_line.split()
number_of_atoms = n[1]

p1 = coord_1.split() 
p2 = coord_2.split()
p3 = coord_3.split()

Prim_Vec1 = []
Prim_Vec2 = []
Prim_Vec3 = []

for i in range(3):
   vector1 = "p" + str(i) + "x"
   vector2 = "p" + str(i) + "y"
   vector3 = "p" + str(i) + "z"
   prim_vector1 =  "primvec" + str(i) + "x"
   prim_vector2 =  "primvec" + str(i) + "y"
   prim_vector3 =  "primvec" + str(i) + "z"
   prim_vector1 = p1[i] 
   Prim_Vec1.append(prim_vector1)
   prim_vector2 = p2[i]
   Prim_Vec2.append(prim_vector2)
   prim_vector3 = p3[i]
   Prim_Vec3.append(prim_vector3)
#   print "x: ", prim_vector1, "y: ", prim_vector2, "z: ", prim_vector3

print Prim_Vec1
print Prim_Vec2
print Prim_Vec3

data1 = open('Tot_E','r')
energy = data1.readlines()
data2 = open('positions','r')
position = data2.readlines()
data3 = open('forces','r') 
forces = data3.readlines()
data4 = open('atom_types','r')
atoms = data4.readlines()

A = []
E = []
P = []
F = []

def reShape(array):
   a = np.array(array)
   np.reshape(a,(len(array), 1))
   return a

def posFor(pos_array, for_array, index, filename):
   for i in range(int(number_of_atoms)):
     # filename.write("PRIMCOORD")
     # filename.write(str(number_of_atoms) + " " + str(1) + "\n")
      filename.write(str(A[i]) + "        " + str(P[i+int(number_of_atoms)*index]) + "  " + str(F[i+int(number_of_atoms)*index]) + "\n")

def genFiles(pos_array, for_array, energy, index):
   filename = "name" + str(index)
   filename = open('output'+ str(index), 'w')
   filename.write("# total energy = " + str(energy) + " eV " + "\n")
   filename.write("\n" + "CRYSTAL" + "\n" + "PRIMVEC" + "\n")
   filename.write("        " + str(Prim_Vec1[0]) + "     " + str(Prim_Vec1[1]) + "     "  + str(Prim_Vec1[2]) + "     " + "\n" ) 
   filename.write("        " + str(Prim_Vec2[0]) + "     " + str(Prim_Vec2[1]) + "     "  + str(Prim_Vec2[2]) + "     " + "\n" )
   filename.write("        " + str(Prim_Vec3[0]) + "     " + str(Prim_Vec3[1]) + "     "  + str(Prim_Vec3[2]) + "     " + "\n" )
   filename.write("PRIMCOORD" + "\n")
   filename.write(str(number_of_atoms) + " " + str(1) + "\n")
   posFor(P,F,index,filename)
   filename.close()

for line in position:
   p = line.split()
   x,y,z = float(p[1]), float(p[2]), float(p[3])
   pos = str(x)+"  "+str(y)+"  "+str(z)
   P.append(pos)

Pos = reShape(P)

for line in forces:
   f = line.split()
   fx,fy,fz = float(f[1]), float(f[2]), float(f[3])
   force = str(fx)+"  "+str(fy)+"  "+str(fz)
   F.append(force)

For = reShape(F)

for line in atoms:
   at = line.split()
   Atoms = at[0]
   A.append(Atoms)

index = 0
for line in energy:
   e = line.split()
   Tot_E = e[2]
   genFiles(P,F,Tot_E,index)
   print index
   index += 1


data1.close()
data2.close()
data3.close()
data4.close()
