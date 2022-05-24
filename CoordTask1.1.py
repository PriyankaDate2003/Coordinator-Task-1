#!/usr/bin/env python
# coding: utf-8

# In[1]:


def twosum(arr,target_sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>target_sum):
            right=right-1
        elif(arr[left]+arr[right]<target_sum):
            left=left+1
        elif(arr[left]+arr[right]==target_sum):
                print("values of pair are [",arr.index(arr[left]),",",arr.index(arr[right]),"]","[",arr.index(arr[right]),",",arr.index(arr[left]),"]")
                right=right-1
                left=left+1
arr=[10,20,10,40,50,60,70]
target_sum=50
twosum(arr,target_sum)


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




