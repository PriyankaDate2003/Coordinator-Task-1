#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import math
import random

class cross_entropy_loss:
    def loss(n):
        n=100
        y1=np.random.randint(2, size=n)
        y2=np.random.random(size=n)
        sum = 0.00
        for i in range(n):
            o=y1[i]*math.log2(y2[i])+(1-y1[i])*math.log2(1-y2[i])
            sum=sum+o
        sum = -0.01*sum
        print(sum)
        
obj=cross_entropy_loss()
obj.loss()


# In[ ]:




