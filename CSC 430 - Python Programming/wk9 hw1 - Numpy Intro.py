# Written by Patrick Keener on 11/12/2020
# Video Link:  https://youtu.be/2zDx5-Bv_Dw
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#
# DSC 430: Python Programming
# Assignment 0901: Numpy Intro

# Step 1
import numpy as np

# Step 2
a = np.arange(100)
print("Step 2:\n{}\n".format(a))

# Step 3
b = np.arange(0, 100, 10)
print("Step 3:\n{}\n".format(b))

# Step 4
maxNum = 10
increment = .1
numIncrements = int(maxNum/increment) + 1
c  = np.linspace(0, maxNum, numIncrements)
print("Step 4:\n{}\n".format(c))

# Step 5
d = np.random.random((10,10))
print("Step 5:\n{}\n".format(d))

# Step 6
a = a.reshape((10,10))
print("Step 6:\n{}\n".format(a))

# Step 7
print("Step 7:\n{}\n".format(a[4,5]))


# Step 8
print("Step 8:\n{}\n".format(a[4]))


# Step 9
print("Step 9:\n{}\n".format(d.sum()))

# Step 10
print("Step 10:\n{}\n".format(a.max()))
    

# Step 11
#It's the same because it's a 1 dimensional array
print("Step 11:\n{}\n".format(b.transpose()))
      

# Step 12
print("Step 12:\n{}\n".format(a + d))
    
# Step 13
# Note: Had to use multiply.  The lecture implied that * used elementwise 
# multiplication which it does not
print("Step 13:\n{}\n".format(a*d))
    
# Step 14
print("Step 14:\n{}\n".format(np.dot(a,d)))

