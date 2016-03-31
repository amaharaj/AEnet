import numpy as np

with open('number_of_atoms','r') as f:
   first_line=f.readline()

n=first_line.split()
number_of_atoms = n[1]
print number_of_atoms

data1 = open('Tot_E','r')
energy = data1.readlines()
data2 = open('positions','r')
position = data2.readlines()
data3 = open('forces','r') 
forces = data3.readlines()
data4 = open('atom_types','r')
atoms = data4.readlines()

outfile = open('water.xml','w')

A = []
E = []
P = []
F = []

def reShape(array):
   a = np.array(array)
   np.reshape(a,(len(array), 1))
   return a

def posFor(pos_array, for_array, index):
   for i in range(int(number_of_atoms)):
      outfile.write(str(A[i]) + "        " + str(P[i+int(number_of_atoms)*index]) + "  " + str(F[i+int(number_of_atoms)*index]) + "\n")

def genFiles(index):
   for i in range(index):
      filename = "name" + str(i)
      filename = open('output'+ str(i), 'w')
      filename.close()

for line in position:
   p = line.split()
   x,y,z = float(p[1]), float(p[2]), float(p[3])
   pos = str(x)+"  "+str(y)+"  "+str(z)
   P.append(pos)

#Pos = reShape(P)

for line in forces:
   f = line.split()
   fx,fy,fz = float(f[1]), float(f[2]), float(f[3])
   force = str(fx)+"  "+str(fy)+"  "+str(fz)
   F.append(force)

#For = reShape(F)

for line in atoms:
   at = line.split()
   Atoms = at[0]
   A.append(Atoms)

index = 0
for line in energy:
   e = line.split()
   Tot_E = e[2]
 #  outfile.write("\n" + "# total energy = " + str(Tot_E) + " eV " + "\n")
 #  posFor(P,F,index)
   index += 1
   genFiles(index)

data1.close()
data2.close()
data3.close()
data4.close()
