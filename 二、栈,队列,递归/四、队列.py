# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:49:41 2019

@author: 37号菜鸡学习数据结构的苦逼日子
"""

"""
队列 先进先出 进出在同一边(从左到右填充,左边开始出队)
用数组实现一个顺序队列(sequential queue)
"""
class squeue():
    def __init__(self):
        self.front = -1 # 队头
        self.rear = -1 # 队尾
        self.maxsize = 5 # 定义最大容量
        self.data = [None]*self.maxsize #定义一个空数组
        
    def push(self,x):  #入队 左到右
        if self.rear +1 > self.maxsize-1:return 'squeue is full'
        self.rear += 1
        self.data[self.rear] = x
    
    def pop(self): #出队 左到右
        if self.front +1 > self.maxsize-1:
            return 'squeue is Null' # 队空 无法继续出队
        self.front += 1
        print('顺序队列 出队元素:',self.data[self.front])
        self.data[self.front]=None

sq = squeue()
for i in range(5):sq.push(i) # [0, 1, 2, 3, 4]
print(sq.data)
sq.pop()
sq.push(5) # 'squeue is full'
print(sq.data,'\n') # [None, 1, 2, 3, 4]


"""
用链表实现一个链式队列
"""
class node:
    def __init__(self,data,pro=None,nextn=None):
        self.data = data
        self.next = nextn
        
class lqueue:    
    def __init__(self):
        head = node('head') # 方便检查0.0 改为None即可
        self.head = head # 链队结点
        head.next = None # 链队结点
        self.front = -1 # 队头指针
        self.rear = -1 # 队尾指针
        self.maxsize = 5 # 定义最大容量
            
    def push(self,x): # 入栈(尾插)
        if self.rear +1 > self.maxsize-1:return 'squeue is full'
        nodex = node(x)
        result = self.head
        n = -1
        while n < self.rear: # 判断下节点是否为 尾节点
            result = result.next
            n +=1
        nodex.next = result.next
        result.next = nodex # 新的尾节点nodex
        self.rear += 1
        
    def pop(self): # 出栈(头结点/链队结点后的队首节点开始)
        if self.front ==self.rear:return 'stack is null'
        print('链式队列 出栈元素',self.head.next.data)
        self.head.next = self.head.next.next
        self.front += 1
        
    def lenqueue(self): #计算链队长度,首尾节点均计算在内,顺便查看链队
        result = self.head
        print(result.data)
        n=0
        while n < self.rear-self.front:
            result = result.next
            print(result.data)
            n+=1

lq = lqueue()
for i in range(5):lq.push(i) # head 0 1 2 3 4
lq.lenqueue()
lq.pop() # head 1 2 3 4
lq.lenqueue()
lq.push(5) # 'squeue is full'
print('\n')

"""
实现一个循环队列(Circular Queue这里用数组实现了下)
无论用 数组或者链表 实现的 连续存储结构或非连续存储结构 的队列中,都会出现一种 "假性溢出"
的情况, 即即使队尾指针到达队头指针,但在一个队尾指针后面仍有 maxsize-1 的空间,循环队列
便是解决此问题,将一般队列首尾相连
"""
class cqueue:
    def __init__(self):
        self.front = 0 # 队头
        self.rear = 0 # 队尾
        self.maxsize = 5 # 定义最大容量(包括了front,元素只能装4个)
        self.data = [None]*self.maxsize #定义一个空数组
        
    def push(self,x):  #入队 左到右
        if self.rear -self.front == 4 or self.rear -self.front==-1:
            return 'cqueue is full'
        self.rear += 1
        self.rear %= 5
        self.data[self.rear] = x
    
    def pop(self): #出队 左到右
        if self.front == self.rear:
            return 'cqueue is Null' # 队空 无法继续出队
        self.front += 1
        self.front %= 5
        print('循环队列 出队元素:',self.data[self.front])
        self.data[self.front] = None
        
cq = cqueue()
for i in range(5):cq.push(i) # [None, 0, 1, 2, 3] None为front指针位置
cq.pop()
cq.push(4)
print(cq.data)