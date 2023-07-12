# ENEL 101: ASSIGNMENT 1 --------

import math
import cmath

# Question 1 ---------------
x = 1.1
y = 3.1

z = math.sqrt(math.sin(x * (math.pow(y,3))))
print("Q1: ", round(z,3))
print("\n")

# Question 2 --------------
z = (pow(math.pi,2) * pow(math.tan(0.2),3) + math.exp(0.43))
print("Q2: ",round(z,3))
print("\n")

# Question 3 -------------
x = 3 * math.sin(0.3)
y = 4 * pow(x,2) + math.cos(x)
z = math.sqrt(x) + y
print("Q3: ",round(z,3))
print("\n")

# Question 4 ------------
print("Q4: ",math.comb(52, 4))
print("\n")

# Question 5 ------------
x = [1,3,6,7] 
y = [1,2,3,4]
z = []

for i in range(0, len(x)):
    z.append(x[i] * y[i])

print("Q5: ",z)
print("\n")

# Question 6 -----------
x = [1,3,6,7]  
y = [1,2,3,4] 
z = []
 
for i in range (0, len(x)):
  z.append(round(math.exp(0.01*x[i]*y[i]),2)) 
print("Q6: ",z)
print("\n")

# Question 7 ------------
x = [1,3,6,7]  
y = [1,2,3,4] 
z = []
 
for i in range (0, len(x)):
  z.append("{:.2e}".format(round(math.exp(10*x[i]*y[i]),2))) 
  
print("Q7: ",z)
print("\n")

# Question 8 ------------
with open("f1.txt", "w") as file:
    for num in z:
        file.write(num + "\n")

# Question 9 -----------
with open("f1.txt", "r") as file:
  num = file.readlines()

new_z = [str(float(num) * 2) for num in z]

with open("f2.txt", "w") as file:
    file.write("\n".join(new_z))

# Question 10 ----------
x = -2  
y = complex(0,3)
z = [pow(x,y), (x * pow(y,2)), cmath.exp(cmath.sqrt(x))]

print("Q10: ")
print(f"   Real      Imag      Magnitude  Angle (radians) ")
print(f"{z[0].real:.2e}  {z[0].real:.2e}  {abs(z[0]):.2e}   {cmath.phase(z[0]):.2f}")
print(f"{z[1].real:.2e}   {z[1].real:.2e}   {abs(z[1]):.2e}   {cmath.phase(z[1]):.2f}")
print(f"{z[2].real:.2e}   {z[2].real:.2e}   {abs(z[2]):.2e}   {cmath.phase(z[2]):.2f}")
print("\n")

# Question 11 -----------

x = [ 0, 3.3, 4/3,math.sin(.2)]
z = [num**2 for num in x]

print("Q11: ",z)

#Then calculate z as a list of each of the elements of x squared using a comprehension.