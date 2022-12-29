#The greatest number
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

import random
 
rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(3,9))
print(rand_list)