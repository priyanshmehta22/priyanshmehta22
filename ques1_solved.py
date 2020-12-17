#!/usr/bin/env python
# coding: utf-8

# In[124]:


list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
z=['h','i','j']
a=(list1[2])
print(a)
b=a[1]
b.insert(3,z)
print(list1)

