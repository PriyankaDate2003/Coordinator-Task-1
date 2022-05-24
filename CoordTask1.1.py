#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[20]:


class pair:
    def __init__(self, arr, sum):
        self.arr=arr
        self.sum=sum

    def ans(self):
        dict={}
        c=1
        for x in range(len(self.arr)-1):
            for y in range(len(self.arr)-1):
                if(self.arr[x]+self.arr[y]==sum):
                    value='['+str(x)+','+str(y)+']'
                    dict.update({c:value})
                    c=c+1
        print(dict)

obj=pair([10,20,10,40,50,60,70],50)
obj.ans()


# In[ ]:




