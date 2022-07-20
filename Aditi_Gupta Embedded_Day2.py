#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


sys.version


# In[3]:


import os
os


# In[4]:


import os
os


# In[5]:


a = "Hello, World!"
for i in a:
    print(i)


# In[6]:


a[:4]


# In[7]:


a[:-4]


# In[8]:


a[1:4]


# In[9]:


a[: : -1]


# In[10]:


a[1::-1]


# In[11]:


f = float("3")
print(type(f))


# In[15]:


txt ="Hello, welcome to my world."
x = txt.endswith(".")
print(x)


# In[17]:


(/StUnpacking, a, tuple)
fruits =("Apple","cherry" , "banana")
(green, yellow, blue) = fruits
print(green)
print(yellow)
print(blue)


# In[22]:


str = "Hello"
str


# In[23]:


list = [1,2,3,4,5,6,7,8,9,10]
list1 = [x for x in list if x%2 ==0]
print(list1)


# In[24]:


a = 250
b = 100
print("A") if a>b  else print("B")


# In[25]:


def FuncDemo():
    print("hello")


# In[33]:


a = [1,2,2,4,5,5]
list =[]
for i in a:
    if i not in list:
        list.append(i)
        print(list)
    


# In[1]:


#linear regression
import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
	n = np.size(x)
	m_x = np.mean(x)
	m_y = np.mean(y)

	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def plot_regression_line(x, y, b):
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = "g")
	plt.xlabel('x')
	plt.ylabel('y')


def main():
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
	b = estimate_coef(x, y)
	print("Estimated coefficients:\nb_0 = {} 		\nb_1 = {}".format(b[0], b[1]))
	plot_regression_line(x, y, b)

if __name__ == "__main__":
	main()


# In[4]:


#selection sort
import sys
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
	A[i], A[min_idx] = A[min_idx], A[i]
print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")


# In[ ]:




