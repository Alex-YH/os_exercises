# lec5 SPOC思考题


NOTICE
- 有"w3l1"标记的题是助教要提交到学堂在线上的。
- 有"w3l1"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

请简要分析最优匹配，最差匹配，最先匹配，buddy systemm分配算法的优势和劣势，并尝试提出一种更有效的连续内存分配算法 (w3l1)
```
  + 采分点：说明四种算法的优点和缺点
  - 答案没有涉及如下3点；（0分）
  - 正确描述了二种分配算法的优势和劣势（1分）
  - 正确描述了四种分配算法的优势和劣势（2分）
  - 除上述两点外，进一步描述了一种更有效的分配算法（3分）
 ```
- [x]  

> 最先匹配  
> 优点：简单、在高地址空间有大块的空闲分区; 缺点：会有外部碎片、分配大块空间时较慢。  
> 最佳匹配  
> 优点：大部分分配的尺寸较小时，效果非常好；缺点：会有外部碎片、释放分区较慢、容易产生很多无用的小碎片。  
> 最差匹配  
> 优点：中等大小分配较多时，效果较好、可以避免出现太多小碎片；缺点：会有外部碎片、释放分区较慢、容易破坏大的空闲分区。  
> buddy system  
> 优点：释放内存速度非常快、仅有少量外部碎片；缺点：会有内部碎片。  
> slab分配算法也是一种较为有效的分配算法。

## 小组思考题

请参考ucore lab2代码，采用`struct pmm_manager` 根据你的`学号 mod 4`的结果值，选择四种（0:最优匹配，1:最差匹配，2:最先匹配，3:buddy systemm）分配算法中的一种或多种，在应用程序层面(可以 用python,ruby,C++，C，LISP等高语言)来实现，给出你的设思路，并给出测试用例。 (spoc)

--- 
```
class listnode:
    first = None
    def __init__(self,l,r,n):
        self.left = l
        self.right = r
        self.nextNode = None
        self.precNode = None
        self.name = n
        self.status = "available"

    def malloc(self,size,name):
        if (self.right-self.left+1 >= size):
            if self.right-self.left+1 > size:
                newNode = listnode(self.left+size,self.right,self.name)
                if self == listnode.first:
                    listnode.first = newNode

                if (self.precNode != None):
                    self.precNode.nextNode = newNode
                if (self.nextNode != None):
                    self.nextNode.precNode = newNode

                newNode.nextNode = self.nextNode
                newNode.precNode = self.precNode

                self.right = self.left+size-1
                self.status = "in use"
                self.name = name
                return self
            else:
                if self == listnode.first:
                    listnode.first = None

                if (self.precNode != None):
                    self.precNode.nextNode = self.nextNode
                if (self.nextNode != None):
                    self.nextNode.precNode = self.precNode
                
                self.status = "in use"
                self.name = name
                return self

        else:
            if self.nextNode == None:
                return None
            else:
                return self.nextNode.malloc(size,name)
    
    def release(self):
        temp = listnode.first
        self.name = "free"
        self.status = "available"
        if temp == None:
            listnode.first = self
            return

        if temp.left > self.right:
            self.nextNode = temp
            self.precNode = None
            temp.precNode = self
            listnode.first = self
        else:
            while temp.nextNode != None and temp.nextNode.right<self.left:
                temp = temp.nextNode
            
            self.nextNode = temp.nextNode
            self.precNode = temp
            temp.nextNode = self

        if self.precNode!=None and self.precNode.right+1==self.left:
            self.left = self.precNode.left

            self.precNode = self.precNode.precNode
            if (self.precNode!=None):
                self.precNode.nextNode = self
            else:
                listnode.first = self

        if self.nextNode !=None and self.nextNode.left==self.right+1:
            self.right = self.nextNode.right

            self.nextNode = self.nextNode.nextNode
            if (self.nextNode != None):
                self.nextNode.precNode = self

    def printSelf(self):
        print "Name : %s\nFrom %d to %d\nStatus: %s\n" % (self.name,self.left,self.right,self.status)
            
    def printAll(self):
        temp = self
        while temp!=None:
            temp.printSelf()
            temp = temp.nextNode

     


print "Hello, This is a program for memory allocation algorithm demonstration"
listnode.first = listnode(0,1000000,"free")

m1 = listnode.first.malloc(100,'m1')
m2 = listnode.first.malloc(200,'m2')
m3 = listnode.first.malloc(300,'m3')

listnode.first.printAll()

m2.release()

listnode.first.printAll()

m3.release()

listnode.first.printAll()

m1.release()

listnode.first.printAll()


```

用链表完成

## 扩展思考题

阅读[slab分配算法](http://en.wikipedia.org/wiki/Slab_allocation)，尝试在应用程序中实现slab分配算法，给出设计方案和测试用例。

## “连续内存分配”与视频相关的课堂练习

### 5.1 计算机体系结构和内存层次
MMU的工作机理？

- [x]  

>  http://en.wikipedia.org/wiki/Memory_management_unit

L1和L2高速缓存有什么区别？

- [x]  

>  http://superuser.com/questions/196143/where-exactly-l1-l2-and-l3-caches-located-in-computer
>  Where exactly L1, L2 and L3 Caches located in computer?

>  http://en.wikipedia.org/wiki/CPU_cache
>  CPU cache

### 5.2 地址空间和地址生成
编译、链接和加载的过程了解？

- [x]  

>  

动态链接如何使用？

- [x]  

>  


### 5.3 连续内存分配
什么是内碎片、外碎片？

- [x]  

>  

为什么最先匹配会越用越慢？

- [x]  

>  

为什么最差匹配会的外碎片少？

- [x]  

>  

在几种算法中分区释放后的合并处理如何做？

- [x]  

>  

### 5.4 碎片整理
一个处于等待状态的进程被对换到外存（对换等待状态）后，等待事件出现了。操作系统需要如何响应？

- [x]  

>  

### 5.5 伙伴系统
伙伴系统的空闲块如何组织？

- [x]  

>  

伙伴系统的内存分配流程？

- [x]  

>  

伙伴系统的内存回收流程？

- [x]  

>  

struct list_entry是如何把数据元素组织成链表的？

- [x]  

>  


