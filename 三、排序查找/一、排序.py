# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
【排序】```````````````````````````````````````````````````````````````````````
排序的稳定性：相同值的节点相对位置是否会发生改变
稳定：如果a原本在b前面,而a=b,排序之后a仍然在b的前面
不稳定：如果a原本在b的前面,而a=b，排序之后a可能会出现在b的后面、

python赋值 = 类的实例化; 定义的变量为 指针变量
数值、字符、布尔型直接传递值的内存地址,列表元组字典等均为复合型,传递指针的内存地址,指向所有值的内存地址(浅拷贝的例子)
对于python而言,python的一切变量都是对象,变量的存储,采用了引用语义的方式,存储的只是一个变量的值所在的内存地址,而不是这个变量的只本身.
引用语义：
在python中,变量保存的是对象(值)的引用,我们称为引用语义.采用这种方式,变量所需的存储空间大小一致,因为变量只是保存了一个引用,也被称为对象语义和指针语义.
值语义：
有些语言采用的不是这种方式,它们把变量的值直接保存在变量的存储区里,这种方式被我们称为值语义,例如C语言,采用这种存储方式,每一个变量在内存中所占的空间就要根据变量实际的大小而定,无法固定下来.

python列表切片时间、空间复杂度"等于"切片长度
空间复杂度(新增的空间)：
1、在外面的定义的变量,只在栈中声明了一次
2、在里面的定义的变量,循环多少次就在栈中声明了多少次
3、在内存或说资源节省方面,肯定是在外面定义较好,是摧荐的写法
   但是如果循环数不大,其实也者体现出来的差别也不大
4、形参的空间会在调用该算法的算法中考虑,只需最初的实参的空间
"""

"""
1_1   直接插入排序(稳定,有有序组,每次非全局有序)
将无序区的元素逐渐插入有序区,一般有序区元素起始个数为1
每次插入后 有序组长度+1,无序组长度-1,向左/有序组比较移动;插入排序是稳定的,不会改变相同元素的相对顺序
时间复杂度(比较次数 和 移动次数之和,最坏O(n^2),最好O(n-1))
空间复杂度(tmep一个,O(1))
"""
def insertSort(alist): # 从小到大排序
    blist = alist.copy()
    for i in range(1,len(blist)): # 无序组    
        j = i-1
        if blist[i] < blist[j]:
            temp = blist[i]
            # 从有序组末尾逐个比较换位
            while j >= 0 and temp < blist[j]: # 一直比有序组小就一直换位,最坏情况移动全部元素
                blist[j+1] = blist[j]
                j-=1
            blist[j+1] = temp # 遇到小于等于插入的元素则停止
            
    return blist
#alist = [1,6,2,5,3,4,2]
#blist = insertSort(alist)
    

"""
1_2   折半/二分插排(稳定,有有序组,每次非全局有序)
(使用二分查找待排序元素(无序组的元素)在 有序组 里应在的位置,不用从头比较
为稳定算法,相同元素相对位置不变)
折半排序移动元素次数 跟 直接排序一样,但减少了 比较次数(仍是O(n^2))
空间复杂度(O(1))
"""
def BinInsertSort(alist):
    blist = alist.copy()
    for i in range(1,len(blist)): # 无序组    
        """二分查找某元素的位置 或 插入的元素应该放的位置"""
        low,high = 0,i-1 # high = i-1 限制在无序组
        mid = int((low+high)/2)
        while True:
            if blist[mid] > blist[i]:high = mid-1
            else:low = mid+1 
            mid = int((low+high)/2)
            
            """无序组元素插入有序组,两种情况"""
            if blist[mid] == blist[i]: # 已经存在相同元素一个或多个
                temp = blist[i]
                j = i-1
                while j>=0 and temp < blist[j]:
                    blist[j+1] = blist[j]
                    j-=1
                blist[j+1] = temp
                print(blist)
                break
            
            if high<low: # 插入新的元素
                temp = blist[i]
                del blist[i]
                blist.insert(max(low,mid,high),temp)
                print(blist)
                break
    return blist

#BinInsertSort([1,6,2,5,3,4,2])
    

"""
2_   希尔排序(不稳定,有每组自己的有序组,每次非全局有序)
(0123 增量d至少为len/2=2,0-2,1-3,每组中相邻两个元素相距d(类似步长)=2个位置,
保证全部元素能被比较,每次循环每个组各自进行插排,循环后增量/2,最后变成增量为1的插排)
时间复杂度：O(n^3/2)
空间复杂度：O(1)
"""
def shellSort(alist):
    blist = alist.copy()
    d = len(blist)//2
    while d > 0 : # 增量向下取整,最后为1,1//2 = 0
        i = d # 以第一个元素为有序组开始插排
        while i < len(blist): # 遍历元素,(向左)插排(有序组数量逐渐增加,跟增量有关)
            j = i - d
            temp = blist[i]
            while j>=0 and temp <= blist[j]: # 不能保证稳定/相同元素位置不变
                blist[j+d] = blist[j]
                j -= d
            blist[j+d] = temp
            print(blist)
            i += 1
        d //= 2
    return blist

#shellSort([1,6,2,5,3,4,2])
    

"""
3_1   冒泡排序(稳定,无序组,每次全局有序)
通过无序区(原数组)中相邻元素间比较进行位置变换
产生有序区(全局有序,排序方法1和2的有序区不一定全局)
冒泡: n-1层,每层n次,优化后,比较次数少了,移动次数较插排多,平均O(n^2),接近最坏情况O(n^2)
空间复杂度(O(1))
"""
def BubbleSort(alist):
    blist = alist.copy()
    for i in range(len(blist)-1): # 长为5,最多循环4次出结果
        change = False
        for j in range(len(blist)-1):
            if blist[j] > blist[j+1]:
                blist[j],blist[j+1] = blist[j+1],blist[j]
                change = True
        if change == False:break # 优化设置,不更新则退出
        print(blist)
    return blist

#BubbleSort([1,9,9,5,3,4,2])
    

"""
3_2   快速排序(不稳定,左右"冒泡"——比较移动;无有序组;每次基准全局有序)
由冒泡排序改进,取一个基准,比其小丢左边,大的丢右边,基准归位,左右再分别取基准(递归)
时间复杂度：递归树: log2n层,每层n次比较,即复杂度为O(nlog2n);
空间复杂度：每次递归产生mid,且在未释放时进入下次递归,消耗栈空间等于树高logn
           最坏的情况是O(n)(初始是逆序的情况)所以平均空间复杂度是O(log(n))
"""
# 原始版(从小到大排列)
def partition(alist,head,tail): # 进行比较分区
    i,j = head,tail
    temp = alist[head] # 取第一个元素作为基准,容易出现左边1右边n-1
    while i < j:
        while i < j and alist[j] >= temp: # 左边为基准,指针右边先开始,不然右边小的换不到前面
            j -= 1
        alist[i] = alist[j]
        while i < j and alist[i] <= temp:
            i += 1
        alist[j] = alist[i]
        alist[i] = temp
    return i
    
def quickSort(alist,head,tail): # 总函数,递归分区
    if head<tail:
        # 一次递归增加1的空间复杂度,程序未结束则累计,总复杂度等于递归次数
        mid = partition(alist,head,tail) 
        
        quickSort(alist,head,mid-1) # 左边
        quickSort(alist,mid+1,tail) # 右边
    return alist

#alist = [4,2,4,1,3,4]
#quickSort(alist,0,len(alist)-1)


"""
4_1   选择排序(不稳定,有有序组,每次全局有序)(递归方法——全排列)
每次无序组里选择最小的丢到有序组后面(和有序组后第一个无序元素互换位置)
类似冒泡,O(n^2)
空间复杂度(O(1))
"""
def selectSort(alist):
    blist = alist.copy()
    i = 0
    while i <= len(blist)-2:
        minindex = i
        for j in range(i,len(blist)):    
            if blist[j] < blist[minindex]:
                minindex = j
        print(blist,minindex)

        blist[i],blist[minindex] = blist[minindex],blist[i]
        i+=1
    return blist

#selectSort([4,2,1,4,3,0,6,7])
    

"""
4_2   堆排序(不稳定,“有序组”全局有序)
大顶堆,堆顶最大,求出堆顶后丢最后,最终是小顶堆
构造初始堆：从下往上,保证每个父节点i>子节点j/j+1
调整堆：从上往下,初始堆构建完之后,换元素可能打乱该节点往下的堆,
        只从该节点往下看,看一条线路(子树),节省比较的时间
时间复杂度：O(nlogn)
构建堆的时间不超过4n
调整时间：几乎每层(每三个点)2次比较,循环len次共Σlogi(i∈(len,2)层, 总次数2Σlogi<2nlogn
空间复杂度：O(1)
"""
def sift(alist,now,high): # 建堆：大顶堆,最终从小到大排序
    i = now
    j = 2*i + 1
    while j <= high: # 构建大顶堆,从now往下 “调整” 树
        # 当前结点的子节点比较,决定谁是父节点进入下次循环
        if j+1 <= high and alist[j] < alist[j+1]: 
            j += 1 # 往右边走
        # 上面j没变则往左走
        if alist[i] < alist[j]: # 当前结点与子节点比较 或 与比较结果比较
            alist[i],alist[j] = alist[j],alist[i]
            # 往结点变动了的子树路线往下调整
            i = j # 接到当前结点的下一个结点(子节点变父节点)
            j = 2*i + 1 # 接到当前结点的下一个结点的叶子结点(左边的,免得溢出)
        else:break # 没变动,即当前父节点和子节点间满足堆属性退出循环
        
def HeapSort(alist):
    high = len(alist) - 1
    # 从下往上 “构造” 初始堆
    i = (high-1)//2
    while i >= 0:
        sift(alist,i,high)
        i -= 1
    print(alist)
    
    # 选择根节点换元素位置并从上往下调整树
    while high > 0:
        alist[0],alist[high] = alist[high],alist[0] # 根节点换到最后面
        high -= 1 # 每次一个元素归位,待排序长度-1
        sift(alist,0,high)
        print(alist)
        
#alist = [9,2,4,8,2,1,4]
#HeapSort(alist)


"""
5_   归并排序(稳定;多次将两个或两个以上的有序表合成(逐个插入到)一个新的有序表)
只有两个有序表的合成即 二路 归并排序
时间复杂度：每层c*n * 递归层数logn = O(nlogn)
空间复杂度：O(n)(来自最终return Merge和实参alist)
"""
def Merge(alist1,alist2): # 排序合并 每层时间空间复杂度O(n)
    i,j = 0,0
    high1,high2 = len(alist1),len(alist2)
    new = [None]*(high1+high2)
    n=0
    while i<high1 and j<high2:
        if alist1[i] < alist2[j]:
            new[n] = alist1[i]
            i+=1;n+=1
        else:
            new[n] = alist2[j]
            j+=1;n+=1
    if i==high1:new[n:] = alist2[j:]
    else:new[n:] = alist1[i:]
    return new

def MergeSort(alist): # 时间复杂度O(logn)
    if len(alist) < 2:return alist
    left = MergeSort(alist[:len(alist)//2]) # 传参为内存地址
    # 空间O(1),时间赋值+切片=O(n)
    right = MergeSort(alist[len(alist)//2:])
    return Merge(left,right)

#alist = [4,2,4,8,1,4]
#blist = MergeSort(alist)

"""下面的排序方法均将时间转化到空间上,数字范围小优势大"""
"""
桶排序(分治,按第一位数放入桶,每个桶插排)
计数排序(个位数,有一点'桶排序'/'hash'表思想,先n次找出最大最小,
        建立一个max-min+1大的新数组,假如有[1,2,3,2],计数[0,1,2,1])
计数排序,基数排序就像是桶排序的一个特例

6_   基数排序(稳定,十位百位等,类似上面)
按照个位十位百位等依次放入对应位置,最后输出
时间复杂度O(d(n+r)),空间复杂度O(r) # 新增r个列表(指针,所以跟链表相同)
"""
def RadixSort(alist):
    # 位数
    maxbit = len(str(max(alist)))
    # hash表长度 多加1预留给0(9+1和+2)
    maxlen = 10
    if maxbit==1:maxlen = max(alist)-min(alist)+2 #+1+1
    for bit in range(1,maxbit+1):
        # "hash"表
        temp = [[] for i in range(maxlen)] # 多个index 0满足index
        print(temp)
        # 遍历列表
        for num in alist:
            if len(str(num))<bit: # 位数少于最大位
                temp[0].append(num)
            else:
                temp[int(str(num)[-bit])].append(num)
        
        alist=[]
        for i in temp:alist.extend(i)
    return alist

#a = RadixSort([45,23,52,1,1,142])
#b = RadixSort([5,4,3,2,1])
