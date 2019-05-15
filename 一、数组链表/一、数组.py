# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:41:44 2019

@author: Ace
"""

"""
一、动态数组
"""
#数组里的元素类型相同,数组按元素顺序存储到一块地址连续的内存单元;每个元素占用n个存储单元;
#动态数组是指在定义时没有明确定义大小的数组
#能随时对数组进行扩容或缩容;只储存必要的元素,减少储存空间
class array():
    def __init__(self):
        self.data = [] #定义一个空数组
        
    def extend(self,x):  #元组或列表里的值一个一个传入
        if type(x) in [list,tuple]:
            new = [0]*(len(self.data)+len(x))
            for i in range(len(self.data)):
                new[i] = self.data[i]
            for i in range(len(x)):
                new[len(self.data)+i] = int(x[i])
        else:
            new = [0]*(len(self.data)+1)
            for i in range(len(self.data)):
                new[i] = self.data[i]
            new[len(self.data)] = int(x)
        self.data = new
    
    def pop(self): #删除最后面的值
        print('remove:',self.data[-1])
        self.data = self.data[:-1]
    
a = array() # 定义一个空数组 []
a.extend(1.0)
a.extend((2,3))
a.extend([4,5])
print(a.data) # [1, 2, 3, 4, 5]

a.pop() # remove: 5
print(a.data) # [1, 2, 3, 4]



"""
二、大小固定的有序数组，支持动态增删改操作
"""
#有序数组里元素按一定顺序排列
class fixedArray():
    def __init__(self):
        self.data = [None]*5 #定义一个固定长度为5的数组
        
    def add(self,x): #增加新元素
        if type(x) not in [float,int]:return 'type error'
        if self.data[4] != None:return 'index out of range'
        new = self.data.copy()
        for i in range(5):
            if new[i] == None:
                new[i] = int(x)
                break
            if (new[i] != None) and (new[i] > x):
                new[i] = int(x)
                for j in range(i+1,5):
                    new[j] = self.data[j-1]
                break
        self.data = new
    
    def replace(self,index,x): #更改数组中某个位置的元素
        if index>=5:return 'index out of range'
        data = self.data[:index]+self.data[index+1:]
        for i in range(4):
            if data[i]== None or data[i]>x:
                self.data[:i]= data[:i]
                self.data[i]=x
                self.data[i+1:] = data[i:]
                
                break
    
    def remove(self,index): #删除数组中某个位置的元素
        self.data= self.data[:index]+[None]+self.data[index+1:]
        
b = fixedArray() # [None, None, None, None, None]
b.add(1) # [1, None, None, None, None]
b.add(2.0) # [1, 2, None, None, None]
b.replace(0,3) # [2, 3, None, None, None]
b.remove(0) # [None, 3, None, None, None]
print(b.data)



"""
实现两个有序数组合并为一个有序数组
"""
def concatenate(a,b): #从b里每个元素逐个加进a里,同时进行排序
    length = len(a+b)
    for i in b:
        n=-1
        for j in a:
            n+=1
            if i<a[n]:
                a = a[:n]+[i]+a[n:]
                break
            if n==length-2:a+=[i]

    if len(a)==3:a +=b
    return a
print(concatenate([1,3,5],[2,4,6])) # [1, 2, 3, 4, 5, 6]



