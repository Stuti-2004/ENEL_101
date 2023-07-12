# ENEL 101: ASSIGNMENT 1 --------

import numpy as np
import math
import cmath
import random

# Question 1 ----------------
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[4],[5],[6]])
c = 2 * a.dot(b)
print("Q1: \n",c)
print("\n")

# Question 2 ----------------
a = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
c = np.sin((a.dot(a).dot(a)) + a)
print("Q2: \n",c)
print("\n")

#Question 3 ----------------

a = np.array([[1, 2, 3], [4, complex(0,5), 6], [7, 8, 9]])

c = np.abs(((a.dot(a).dot(a)) + a))
print("Q3: \n",c)
print("\n")

# Question 4 --------------
x = np.array([[1], [2], [3]]) 
y = np.array([1, 0, 1])

z1 = np.outer(x,y)
z2 = y.dot(x)
 
print("Q4:")
print("z1")
print(z1)
print("\nz2")
print(z2)
print("\n")

# Question 5 --------------
reshaped_x = np.reshape(x, (3, 1))  # Convert a to a column vector matrix
reshaped_y = np.reshape(y, (1, 3))  # Convert b to a row vector matrix

outer_product = np.dot(reshaped_x, reshaped_y)  # Inner product of b and a
inner_product = np.dot(reshaped_y, reshaped_x)  # Outer product of b and a

print("Q5:")
print("Inner product:")
print(inner_product)

print("\nOuter product:")
print(outer_product)

# Question 6---------------
x = 0.85
y = 2

diag_matrix = np.diag([x, x * y, x / y])
print("\nQ6:\n", diag_matrix)

# Question 7 -------------
x = np.array([i for i in range(2, 38, 5)])
z = np.sum(x)
print("\nQ7:\n",z)

# Question 8 -----------
x = np.random.randint(0, 10, size=(3, 3))
y = np.sort(x.reshape(1,9))
print("\nQ8:")
print(y)

# Question 9 ----------
x = np.random.randint(0, 10, size=(3, 2, 2))
y = np.sort(x.reshape(1,12))

print("\nQ9:")
print(y)

# Question 10 --------
x = np.arange(1,25)
y = np.resize(x, [3,8])
print("\nQ10:")
print(y)

# Question 11 --------
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.multiply(y, 3)

z1 = x.dot(z)
print("\nQ11:")
print(math.exp(z1))

# Question 12 -------
x = np.array([1,0,0])
y = np.array([1,2,3])
z = np.array([2,2,2])

u = y - x # choose vector u to be xy
v = z - x # choose vector v to be xz

print("\nQ12:")
cross_prod = np.cross(u,v)
print(abs(math.sqrt(sum(pow(element, 2) for element in cross_prod))))

# Question 13 -------
x = np.array([[1, 2, 0],[2,7,1],[0,0,5]])
y = np.array([[1],[2],[3]])

z = np.multiply(np.multiply(y.transpose(),x),y)
w = np.multiply(y.transpose(),y)
print("\nQ13:")
print("z:")
print(z)
print("w:")
print(w)

# Question 14 ---------
#For this question generate x as a numpy array and write the elements out to a text file. Show a
#screen shot of the text file. Then read the text file content back in and assign the elements to y. Then
#form z=x-y and show that it is all zeros. x is given as

x = np.array([[1,2,0],[2,7,1],[0,0,5]])

np.savetxt("array.txt", x)
y = np.loadtxt('array.txt')
 
z = x - y
print("\nQ14:")
print(z)



#y = np.array[int(i for i in num)].reshape(3,3)
