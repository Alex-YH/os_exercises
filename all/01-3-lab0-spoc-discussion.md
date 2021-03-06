# lab0 SPOC思考题

## 个人思考题

---

能否读懂ucore中的AT&T格式的X86-32汇编语言？请列出你不理解的汇编语言。

>  http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
>
>  这些汇编语言在之前的学习中都有接触过，故都知道含义。

虽然学过计算机原理和x86汇编（根据THU-CS的课程设置），但对ucore中涉及的哪些硬件设计或功能细节不够了解？

>  我对ucore的引导过程，如何将操作系统引导如内存的过程不是特别熟悉，希望在之后的学习过程中能有进一步的了解。


哪些困难（请分优先级）会阻碍你自主完成lab实验？

> 1、对硬件资源调用的不理解。
> 2、对操作系统机制的不熟悉。
> 3、操作系统引导过程的不了解。

如何把一个在gdb中或执行过程中出现的物理/线性地址与你写的代码源码位置对应起来？

> gdb的调试功能可以在可执行文件中记录其在源文件中的位置，通过这种方法可以将其对应起来。  

了解函数调用栈对lab实验有何帮助？

> 函数调用栈可以帮助我们进行调试，可以非常清晰的发现问题所在。

你希望从lab中学到什么知识？

> 我希望能知道操作系统组织各种数据的文件系统的实现方法、进程调度的算法以及内存管理的机制。

---

## 小组讨论题

---

搭建好实验环境，请描述碰到的困难和解决的过程。

> 根据学堂在线上的视频，我们很顺利的完成了实验环境的搭建工作。

熟悉基本的git命令行操作命令，从github上的[ucore git repo](http://www.github.com/chyyuu/ucore_lab)下载ucore lab实验

> 已经通过git clone http://www.github.com/chyyuu/ucore_lab 命令将源代码下载到本地。

尝试用qemu+gdb（or ECLIPSE-CDT）调试lab1

> 已经尝试用ECLIPSE-CDT对lab1进行调试，初步了解了调试的方法。

对于如下的代码段，请说明”：“后面的数字是什么含义
```
/* Gate descriptors for interrupts and traps */
struct gatedesc {
    unsigned gd_off_15_0 : 16;        // low 16 bits of offset in segment
    unsigned gd_ss : 16;            // segment selector
    unsigned gd_args : 5;            // # args, 0 for interrupt/trap gates
    unsigned gd_rsv1 : 3;            // reserved(should be zero I guess)
    unsigned gd_type : 4;            // type(STS_{TG,IG32,TG32})
    unsigned gd_s : 1;                // must be 0 (system)
    unsigned gd_dpl : 2;            // descriptor(meaning new) privilege level
    unsigned gd_p : 1;                // Present
    unsigned gd_off_31_16 : 16;        // high bits of offset in segment
};
```

> 后面的数字是位域，表示的是该成员变量所占位数。

对于如下的代码段，
```
#define SETGATE(gate, istrap, sel, off, dpl) {            \
    (gate).gd_off_15_0 = (uint32_t)(off) & 0xffff;        \
    (gate).gd_ss = (sel);                                \
    (gate).gd_args = 0;                                    \
    (gate).gd_rsv1 = 0;                                    \
    (gate).gd_type = (istrap) ? STS_TG32 : STS_IG32;    \
    (gate).gd_s = 0;                                    \
    (gate).gd_dpl = (dpl);                                \
    (gate).gd_p = 1;                                    \
    (gate).gd_off_31_16 = (uint32_t)(off) >> 16;        \
}
```
如果在其他代码段中有如下语句，
```
unsigned intr;
intr=8;
SETGATE(intr, 0,1,2,3);
```
请问执行上述指令后， intr的值是多少？

> intr的值为65538.

请分析 [list.h](https://github.com/chyyuu/ucore_lab/blob/master/labcodes/lab2/libs/list.h)内容中大致的含义，并能include这个文件，利用其结构和功能编写一个数据结构链表操作的小C程序

> #include "list.h"
> 
> int main(){  
>   list_entry* l = (list_entry)malloc(sizeof(list_entry));  
>   list_init(l);  
>   return 0;  
> }

---

## 开放思考题

---

是否愿意挑战大实验（大实验内容来源于你的想法或老师列好的题目，需要与老师协商确定，需完成基本lab，但可不参加闭卷考试），如果有，可直接给老师email或课后面谈。

> 如果基本实验完成的较为顺利的话，希望挑战大实验。

---
