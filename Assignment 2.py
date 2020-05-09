#!/usr/bin/env python
# coding: utf-8

# In[7]:


#assigning elements to different lists
list1=[1,2,3,4]
list2=[]
for i in range(len(list1)):
    list2.append(list1[i])

      


# In[8]:


#accessing elements from a tuple
tuple = ("virat","mahendra","rohit")
for x in tuple:
    print(x)


# In[ ]:


#deleting different dictionary elements
dict = {"brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print("elements of dictionary :"+ str(dict))
print("For deleting mango, put 0")
print("For deleting mango, put 1")
print("For deleting mango, put 2")
x = int(input("Put your option : "))
if x==0:
    dict.pop("brand")
    print(dict)
elif x==1:
    dict.pop("model")
    print(dict)
elif x==2:
    dict.pop("year")
    print(dict)
else:
    print("your option is incorrect")
    print("try again")


# In[ ]:





# In[ ]:




