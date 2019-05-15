# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:09:46 2019

@author: 37号菜鸡
"""

"""
链表元素不同于数组，其元素在内存中的储存顺序不一定连续，增加元素不用大幅度移动其他元素，提高储存效率
并且能储存不同类型的元素，但又需要增加空间，用于储存指针，且不能像数组一样随时提取指定序号位置的元素
"""

"""
1、实现单链表singly、循环链表、双向链表doubly，支持增删操作
"""
class node:
    def __init__(self,data,pro=None,nextn=None):
        self.data = data
        self.next = nextn
#        self.pro = pro # 双向链表用，不用时为单链表，默认值无影响
        
class linklist:    
    def __init__(self):
        head = node('head') # 方便检查0.0 改为None即可
        tail = node('tail') 
        self.head = head # 头节点
        head.next = tail
        self.tail = tail # 尾节点
        """循环/双向链表 加上下面一行"""
#        tail.next = head 
        
    def headInsert(self,node): #头插
        node.next = self.head.next
        self.head.next = node
#        node.pro = self.head
        
    def lenlist(self): #计算链表长度,首尾节点均计算在内,顺便查看链表
        x = self.head
        print(x.data)
        result = x.next
        print(result.data)
        n=2
        while result.data != 'tail':
            result = result.next
            print(result.data)
            n+=1
        return n
    
    def tailInsert(self,node): #尾插
        result = self.head
        while result.next.data != 'tail': # 判断下个节点是否为 尾节点
            result = result.next
        #当前节点下个节点为尾节点,改为下个节点为目标点(下个节点的前一个节点也是目标节点)
        node.next = result.next
        result.next = node 
        """双向链表 加上下面"""
#        node.next.pro = node
#        node.pro = result
        
    def removeList(self,index): #index>=1 删除指定位置的元素,0是头结点
        result = self.head
        if index <1:return 'index must>=1'
        if result.next.data=='tail':return 'linklist is Null'
        n=1
        while n != index:
            result = result.next
            n+=1
#        result.next.next.pro = result
        result.next = result.next.next

print('第一题·······································')
linklist1 = linklist()
linklist1.headInsert(node(2)) # 头插入2
linklist1.tailInsert(node(1)) # 尾插入1
linklist1.tailInsert(node(3)) # 尾插入3,其当前index为3
linklist1.removeList(3) # 删除index为 3 的元素
linklist1.lenlist() # 输出链表
# 输出
# head
# 2
# 1
# tail


"""
2、实现单链表反转(新建链表 或者 原链表直接遍历调换)
   这里实现第二种方法
"""
#方法一的思想：新建一个链表，对原链表元素逐个遍历，以头插的方式加入新链表
#下面实现的，第二种方法，以反转前的链表的头结点后一个节点nodex为循环退出判断节点
#假如nodex到达尾节点前，则反转完成
def reverseList(linklist):
    head = linklist.head
    last = head.next #nodex
    live = last.next #需要换位值的节点
    while last.next.data != 'tail':
        last.next = live.next
        live.next = head.next
        head.next = live
        live = last.next

print('\n第二题·······································')
linklist1.headInsert(node(3))
print('反转前:')
linklist1.lenlist()
reverseList(linklist1)
print('\n反转后:')
linklist1.lenlist()
# 输出
# head
# 3
# 2
# 1
# 0
# tail


"""
3、实现两个有序的链表合并为一个有序链表(类似插排的实现,两个链表均从小到大排序)
"""
def concatenate(llist1,llist2): #llist1不变，llist2会变(没时间就不优化了(嘿嘿,滑稽))
    """list1 插入到 list2"""
    live1 = llist1.head.next # 准备插入到另一个链表的节点
    while live1.data != 'tail':
        tempnode = node(live1.data)
        live2 = llist2.head.next
        live2_pro = llist2.head # 记录插入元素的前面元素
        while live2.data != 'tail':
            if tempnode.data <= live2.data:
                tempnode.next = live2
                live2_pro.next = tempnode
                live2_pro = tempnode
                live2 = live2.next
                break
            else:
                live2_pro = live2
                live2 = live2.next
        live1 = live1.next

print('\n第三题·······································')
linklist2 = linklist()
linklist2.tailInsert(node(0))
linklist2.tailInsert(node(2))
linklist2.tailInsert(node(5))
print('有序链表1：')
linklist1.lenlist() # 1 2 3
print('有序链表2：')
linklist2.lenlist() # 0 2 5
concatenate(linklist1,linklist2)
print('把有序链表1合并进有序链表2后的 linklist2:')
linklist2.lenlist() # head 0 1 2 2 3 5 tail


"""
4、实现求链表的中间结点(两个指针，一个指针两个两个节点地移动，另一个指针一次移动距离为一个节点)
"""
def findmid(llist):
    if llist.head.next.data=='tail':return 'llist is NULL' # 空链表处理
    fast = llist.head.next.next
    low = llist.head.next
    if fast.data == 'tail':return '链表就一个节点：',low.data # 链表只有一个元素时
    while True:
        if fast.next.data =='tail':
            print('链表内节点数为偶数,中间节点有两个为：',low.data,low.next.data)
            break
        fast = fast.next.next
        low = low.next
        if fast.data =='tail':
            print('中间节点为：', low.data);break

findmid(linklist2) # 上面的链表
# 输出 链表内节点数为偶数,中间节点有两个为： 2 2