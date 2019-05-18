# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:55:42 2019

@author: Ace
"""
"""
编程实现斐波那契数列求值 f(n)=f(n-1)+f(n-2)
"""
def func1(flist,n): #长度为n的菲波那切数列
    flist.append(flist[-2]+flist[-1])
    while len(flist) < n:
        func1(flist,n)
    
    return flist

func1([0,1],10) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


"""
编程实现求阶乘 n!
"""
def func2(n): # n 的阶乘
    if n==1:return 1
    return n*func2(n-1)

func2(4) # 24


"""
编程实现一组数据集合的全排列
"""  
COUNT=0  
def perm(n,begin,end):  
    global COUNT  
    if begin>=end:  
        print(n)  
        COUNT +=1  
    else:  
        i=begin      
        for num in range(begin,end):  # 从begin 到 den 的元素轮流换 begin位置的元素
            n[num],n[i]=n[i],n[num]  
            perm(n,begin+1,end)  # index0换index0，然后1-3换1，2-3换2(第一个元素后面的值)
            n[num],n[i]=n[i],n[num]  #换回原始状态，下个循环index1换index0(第一个元素的值)

n=[1,2,3,4]  
perm(n,0,len(n))  
print(COUNT)
