#!/usr/bin/env python
# coding: utf-8

# ## Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[7]:


class triangle():
    def __init__(self,a,b,c):
        self.a =a
        self.b = b
        self.c = c
class area_of_triangle(triangle):
    def __init__(self,*args):
        super(area_of_triangle,self).__init__(*args)
    def area(self):
        s = (self.a+self.b+self.c)*0.5
        area  = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return(area)
a= int(input("enter the side of triangle : "))
b = int(input("enter 2nd side of triangle : "))
c = int(input("enter 3rd side of triangle : "))
obj = area_of_triangle(a,b,c)
print("the area of a triangle is : ",obj.area())


# # Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n
# 

# In[5]:


s= input("enter a string : ")
l = s.split(" ")
print(l)
n = int(input("enter length of word to filter : "))
def filter_long_words(l,n):
    l1=[]
    for i in l:
        if len(i)<=n:
            continue
        else:
            l1.append(i)
    return l1
filter_long_words(l,n)    
                


# # Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[8]:


# lenght of words in a list using lamda function in map function

s =input("enter a string : ")
# converting string to list
l = s.split(" ")
print(l)
list(map(lambda x: len(x),l))


# In[9]:


# length of words in a list using map function

j = input("input string : ")
# converting string to list
li = j.split() 
def lenlist(li):
    return len(li)
list(map(lenlist,li))


# # Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# In[9]:


v = ['a','e','i','o','u']
c = input("Input a character ")
for i in v:
    if c in v:
        print(True)
        break
    else:
        print(False)
        break

