#!/usr/bin/env python
# coding: utf-8

# # Assignment_04-02-2023

# ## 1. Creat a python program to sort the given list of tuples based on intiger value using a lamda function.
# ### [('sachin Tendulkar',34357),('Rucky Pointing',27483),('Jack Kallis',25534),('Virat Kohil',24936)]

# In[1]:


#def list(list_of_tuples):
    #return list_of_tuples

list_of_tuples =[('Sachin Tendulkar',34357),('Rucky Pointing',27483),('Jack Kallis',25534),('Virat Kohil',24936)]

list_of_tuples.sort(key= lambda x : x[1])
print(list_of_tuples)


# ## 2. Write a python program to fine the squred root of all the numbers in the given list of integers using map and lambda functions.
# 
# ### [1,2,3,4,5,6,7,8,9,10]

# In[2]:


## Squred root of the given list in using map function.
def sq(x):
    return x**2
list1=[1,2,3,4,5,6,7,8,9,10]
square_root =list(map(sq,list1))
print("list of square root",square_root)


# In[3]:


## Squred root of the given list in using lambda function.
numbers=[1,2,3,4,5,6,7,8,9,10]
square_root=list(map(lambda m: m**2 ,numbers))
print("list of square root",square_root)


# ## 3. write a python program to convert the given list of integers into a tuples of strings. Use map and Lambda function.
# 
# ### Given String :[ 1,2,3,4,5,6,7,8,9,10]
# 

# In[4]:


## Ans:-
L1=[1,2,3,4,5,6,7,8,9,10]
tuple(map(lambda x: str(x),L1))


# ## 4. Write a python program using reduce function to compute the product of a list containing number from 1 to 25.

# In[5]:


## Ans:-
from functools import reduce

numbers = [i for i in range(1,26)]
product= reduce(lambda x,y:x*y,numbers)
print("The product of the number from 1 to 25:- ",product)


# In[6]:


nums = [i for i in range(1,26)]
reduce(lambda x,y : x*y,nums)


# ## 5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.
# 
# ### [2,3,6,9,27,60,90,120,55,46]

# In[7]:


#Ans:-
def is_dividible_by_2_and_3 (num):
    return num % 2==0 and num % 3 == 0
L1=[2,3,6,27,60,90,120,55,46]
list(filter(is_dividible_by_2_and_3,L1))


# ## 6. write a python program to find palindromes in the given list of strings using lambda and filter function.
# 
# ### ['python','php','aba','radar','level']

# In[8]:


def is_palindrome(word):
    return word == word[::-1]

words = ['python', 'php', 'aba', 'radar', 'level']
result = list(filter(is_palindrome, words))

print("The palindromes in the list are:", result)


# In[9]:


words = ['python', 'php', 'aba', 'radar', 'level']
list(filter(lambda x : x==x[::1],words))

