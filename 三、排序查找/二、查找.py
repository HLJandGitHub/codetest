# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:53:46 2019

@author: Ace
"""
"""
编程实现 O(n) 时间复杂度内找到一组数据的第 K 大元素```````````````````````````````
"hash"表,桶/计数/基数排序
基数排序
前面有k-1个数则为第k大数,平均情况下时间复杂度O(n)
"""


"""
【二分查找】
1、实现一个有序数组的二分查找算法(类似list.index),要求表中元素有序
2、实现模糊二分查找算法（比如大于等于给定值的第一个元素）
# max(low,mid,high)对应的元素
"""
def index(alist,x): # 若存在输出index,若不在输出应在位置,可以直接insert结果不用再排序
    low,high = 0,len(alist)-1
    mid = int((low+high)/2)
    while True:
        if alist[mid] > x:high = mid-1
        else:low = mid+1 
        mid = int((low+high)/2)
        if alist[mid] == x: # 已经存在的元素以及相同元素
            print('元素已在数组中,index=:',mid,'相同元素插入index=',mid+1)
            alist.insert(mid+1,x)
            break
        # 插入新的元素
        if high<low:
            print('没有目标元素,模糊查找结果为：',alist[max(low,mid,high)])
            alist.insert(max(low,mid,high),x)
            break
alist = [1,2,3,3,4,5]
index(alist,3.5)
    
