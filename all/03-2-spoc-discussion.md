# lec6 SPOC思考题


NOTICE
- 有"w3l2"标记的题是助教要提交到学堂在线上的。
- 有"w3l2"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

（1） (w3l2) 请简要分析64bit CPU体系结构下的分页机制是如何实现的
```
  + 采分点：说明64bit CPU架构的分页机制的大致特点和页表执行过程
  - 答案没有涉及如下3点；（0分）
  - 正确描述了64bit CPU支持的物理内存大小限制（1分）
  - 正确描述了64bit CPU下的多级页表的级数和多级页表的结构或反置页表的结构（2分）
  - 除上述两点外，进一步描述了在多级页表或反置页表下的虚拟地址-->物理地址的映射过程（3分）
 ```
- [x]  

>  64bit的CPU，它的地址个数最大为2^64个，即最大支持的物理内存大小为16EiB
>  使用四级页表，多级页表结构，有多级页表，逐层查找得到物理地址
>  多级页表的映射过程：虚拟地址->
>  					先在第一级页表查找，得到第一级页表号
>  					再在第二级页表中查找，得到第二级页表号
>  					...
>  					在第四级页表中查找，得到物理页表号，加上offset，得到物理地址
>  反置页表的映射过程：页表号和进程ID进行Hash，得到的值进行查找，得到物理页号

## 小组思考题
---

（1）(spoc) 某系统使用请求分页存储管理，若页在内存中，满足一个内存请求需要150ns。若缺页率是10%，为使有效访问时间达到0.5us,求不在内存的页面的平均访问时间。请给出计算步骤。 

- [x]  

> 500=0.9\*150+0.1\*x
> 设不在内存的页面的平均访问时间为x
> 则500 = 0.9\*150+0.1\*x
> x = 3650

（2）(spoc) 有一台假想的计算机，页大小（page size）为32 Bytes，支持32KB的虚拟地址空间（virtual address space）,有4KB的物理内存空间（physical memory），采用二级页表，一个页目录项（page directory entry ，PDE）大小为1 Byte,一个页表项（page-table entries
PTEs）大小为1 Byte，1个页目录表大小为32 Bytes，1个页表大小为32 Bytes。页目录基址寄存器（page directory base register，PDBR）保存了页目录表的物理地址（按页对齐）。

PTE格式（8 bit） :
```
  VALID | PFN6 ... PFN0
```
PDE格式（8 bit） :
```
  VALID | PT6 ... PT0
```
其
```
VALID==1表示，表示映射存在；VALID==0表示，表示映射不存在。
PFN6..0:页帧号
PT6..0:页表的物理基址>>5
```
在[物理内存模拟数据文件](./03-2-spoc-testdata.md)中，给出了4KB物理内存空间的值，请回答下列虚地址是否有合法对应的物理内存，请给出对应的pde index, pde contents, pte index, pte contents。
```
Virtual Address 6c74
Virtual Address 6b22
Virtual Address 03df
Virtual Address 69dc
Virtual Address 317a
Virtual Address 4546
Virtual Address 2c03
Virtual Address 7fd7
Virtual Address 390e
Virtual Address 748b
```

###answer
```
Virtual Address 6c74:
  --> pde index:0x1b  pde contents: (valid 1, pfn 0x20)
    --> pte index:0x3 pte contents: (valid 1, pfn 0x61)
      --> Translates to Physical Adress 0xc34 --> Value: 6

Virtual Address 6b22:
  --> pde index:0x1a  pde contents: (valid 1, pfn 0x52)
    --> pte index:0x19 pte contents: (valid 1, pfn 0x47)
      --> Translates to Physical Adress 0x8e2 --> Value: 26

Virtual Address 3df:
  --> pde index:0x0  pde contents: (valid 1, pfn 0x5a)
    --> pte index:0x1e pte contents: (valid 1, pfn 0x5)
      --> Translates to Physical Adress 0xbf --> Value: 15

Virtual Address 69dc:
  --> pde index:0x1a  pde contents: (valid 1, pfn 0x52)
    --> pte index:0xe pte contents: (valid 0, pfn 0x7f)
      --> Fault (page table entry not vaild)

Virtual Address 317a:
  --> pde index:0xc  pde contents: (valid 1, pfn 0x18)
    --> pte index:0xb pte contents: (valid 1, pfn 0x35)
      --> Translates to Physical Adress 0x6ba --> Value: 30

Virtual Address 4546:
  --> pde index:0x11  pde contents: (valid 1, pfn 0x21)
    --> pte index:0xa pte contents: (valid 0, pfn 0x7f)
      --> Fault (page table entry not vaild)

Virtual Address 2c03:
  --> pde index:0xb  pde contents: (valid 1, pfn 0x44)
    --> pte index:0x0 pte contents: (valid 1, pfn 0x57)
      --> Translates to Physical Adress 0xae3 --> Value: 22

Virtual Address 7fd7:
  --> pde index:0x1f  pde contents: (valid 1, pfn 0x12)
    --> pte index:0x1e pte contents: (valid 0, pfn 0x7f)
      --> Fault (page table entry not vaild)

Virtual Address 390e:
  --> pde index:0xe  pde contents: (valid 0, pfn 0x7f)
    --> Fault (page directory entry not valid)

Virtual Address 748b:
  --> pde index:0x1d  pde contents: (valid 1, pfn 0x0)
    --> pte index:0x4 pte contents: (valid 0, pfn 0x7f)
      --> Fault (page table entry not vaild)
```

以上答案由以下程序生成：
```
#include<stdio.h>

unsigned int memory[128][32];

void convert(unsigned int virAdd){
    printf("Virtual Address %x:\n",virAdd);

    unsigned int mask1 = 0x7c00;//0111 1100 0000 0000
    unsigned int pdeIndex = (virAdd & mask1) >> 10;
    printf("  --> pde index:0x%x",pdeIndex);
    unsigned int GDBR = 0x220;
    unsigned int temp = memory[GDBR >> 5][pdeIndex];
    unsigned int valid = temp >> 7;
    unsigned int pfn = temp&0x7f;
    printf("  pde contents: (valid %d, pfn 0x%x)\n",valid,pfn);
    
    if (valid == 0) {
        printf("    --> Fault (page directory entry not valid)\n\n");
        return;
    }

    unsigned int mask2 = 0x03e0;//0000 0011 1110 0000
    unsigned int pteIndex = (virAdd & mask2) >> 5;
    printf("    --> pte index:0x%x",pteIndex);
    temp = memory[pfn][pteIndex];
    valid = temp >> 7;
    pfn = temp&0x7f;
    printf(" pte contents: (valid %d, pfn 0x%x)\n",valid,pfn);

    if (valid == 0){
        printf("      --> Fault (page table entry not vaild)\n\n");
        return;
    }
    
    unsigned int mask3 = 0x1f;
    unsigned int offset = virAdd & mask3;
    printf("      --> Translates to Physical Adress 0x%x --> Value: %d\n\n",(pfn<<5)+offset,memory[pfn][offset]);
}


int main(){
    freopen("in.txt","r",stdin);
    for (int i=0;i<128;i++){
        char temp[8];
        scanf("%s",temp);
        //printf("%s",temp);
        scanf("%s",temp);
        //printf("%s\n",temp);
        for (int j=0;j<32;j++){
            scanf("%x",&memory[i][j]);
            //printf("%x ",memory[i][j]);
        }
        //printf("\n");
    }

    while (1){
        unsigned int virAdd;
        scanf("%x",&virAdd);
        if (virAdd > 0xffff) break;
        convert(virAdd);
    }
    
}

```

比如答案可以如下表示：
```
Virtual Address 7570:
  --> pde index:0x1d  pde contents:(valid 1, pfn 0x33)
    --> pte index:0xb  pte contents:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
      
Virtual Address 21e1:
  --> pde index:0x8  pde contents:(valid 0, pfn 0x7f)
      --> Fault (page directory entry not valid)

Virtual Address 7268:
  --> pde index:0x1c  pde contents:(valid 1, pfn 0x5e)
    --> pte index:0x13  pte contents:(valid 1, pfn 0x65)
      --> Translates to Physical Address 0xca8 --> Value: 16
```



（3）请基于你对原理课二级页表的理解，并参考Lab2建页表的过程，设计一个应用程序（可基于python, ruby, C, C++，LISP等）可模拟实现(2)题中描述的抽象OS，可正确完成二级页表转换。


（4）假设你有一台支持[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)的机器，请问你如何设计操作系统支持这种类型计算机？请给出设计方案。

 (5)[X86的页面结构](http://os.cs.tsinghua.edu.cn/oscourse/OS2015/lecture06#head-1f58ea81c046bd27b196ea2c366d0a2063b304ab)
--- 

## 扩展思考题

阅读64bit IBM Powerpc CPU架构是如何实现[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)，给出分析报告。

--- 
