# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:55:40 2019

@author: 37号菜鸡学习数据结构的苦逼日子
"""
"""
用数组实现一个顺序栈(sequential stack)
"""
class sstack():
    def __init__(self):
        self.data = [] #定义一个空数组
        self.top = -1 # 定义栈顶指针
        self.maxsize = 10 # 定义最大容量
        
    def push(self,x):  #入栈
        if self.top +1 > self.maxsize-1:return '栈满溢出'
        new = [0]*(len(self.data)+1)
        for i in range(len(self.data)):
            new[i] = self.data[i]
        new[len(self.data)] = int(x)
        self.data = new
        self.top +=1
    
    def pop(self): #出栈
        self.top -= 1
        if self.top <-1:self.top = -1;return 'sstack is Null' # 栈空 无法继续出栈
        print('顺序栈 出栈元素:',self.data[-1])
        self.data = self.data[:-1]
   
stack = sstack()     
for i in range(10):
    stack.push(i)
stack.data # 输出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('当前栈顶指针：',stack.top) # 输出 9
print(stack.push(1)) # 输出 '栈满溢出'
for i in range(10):
    stack.pop() #全部元素出栈并输出显示
print('当前栈顶指针：',stack.top)
print(stack.pop(),'\n') # 输出 'sstack is Null'


"""
用链表实现一个链式栈
"""
class node:
    def __init__(self,data,pro=None,nextn=None):
        self.data = data
        self.next = nextn
        
class linkstack:    
    def __init__(self):
        head = node('head') # 方便检查0.0 改为None即可
        self.head = head # 栈底
        head.next = None # 栈底
        self.maxsize = 10 # 最大节点数
        self.top = -1 # 栈顶指针
            
    def push(self,x): # 入栈(尾插,队列头插)
        if self.top == self.maxsize-1:return 'stack is full'
        nodex = node(x)
        result = self.head
        n = -1
        while n < self.top: # 判断是否到栈顶
            result = result.next
            n+=1
        nodex.next = result.next
        result.next = nodex 
        self.top += 1
        
    def pop(self): # 出栈
        if self.top ==-1:return 'stack is null'
        result = self.head
        n=-1
        while n <= self.top-2:
            result = result.next
            n+=1
#        print('链式栈 出栈元素',result.next.data)
        outer = result.next.data
        result.next = None
        self.top -= 1
        return outer
        
    def lenstack(self): #计算链表长度,首尾节点均计算在内,顺便查看链表
        result = self.head
        print(result.data)
        n=-1
        while n != self.top:
            result = result.next
            print(result.data)
            n+=1
        
stack2 = linkstack()
for i in range(10):
    stack2.push(i)
stack2.lenstack() # head 9 8 7 6 5 4 3 2 1 0
print('当前栈顶指针：',stack2.top) # 输出 9
print(stack2.push(1)) # 输出 '栈满溢出'
for i in range(10):
    stack2.pop() #全部元素出栈并输出显示
print('当前栈顶指针：',stack2.top)
print(stack2.pop(),'\n') # 输出 'sstack is Null'


"""
编程模拟实现一个浏览器的前进、后退功能(设置两个栈,一个出栈另一个则入栈)
"""
def Surf():
    forward = linkstack()
    backward = linkstack()
    x = 1
    print('这里是head首页,输入forward x,前往x: ')
    while x:
        x = input()
        y = x.split(' ')
        if y[0]=='forward' and len(y)>1:
            forward.push(y[1])
            print('当前网页为{}'.format(y[1]));continue
        if y[0]=='forward' and len(y)==1 and backward.top >-1:
            forward.push(backward.pop())
            result = forward.head
            n=-1
            while n != forward.top:
                result = result.next
                n+=1
            print('当前网页为{}'.format(result.data));continue
        if y[0]=='backward' and forward.top >-1:
            backward.push(forward.pop())
            result = forward.head
            n=-1
            while n != forward.top:
                result = result.next
                n+=1
            print('当前网页为{}'.format(result.data));continue
        else:print('请重新输入');continue

# 事例
#Surf()
#这里是head首页,输入forward x,前往x: 
#
#forward 4399
#当前网页为4399
#
#backward
#当前网页为head
#
#forward
#当前网页为4399
#
#forward
#请重新输入
