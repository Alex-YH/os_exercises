6. 设有一个可以装A、B两种物品的仓库，其容量无限大，但要求仓库中A、B两种物品的数量满足下述不等式： -M≤A物品数量-B物品数量≤N 其中M和N为正整数。试用信号量和PV操作描述A、B两种物品的入库过程。  
```
Semaphore方法:
#coding = utf-8

import threading
import time
import random

N = 5  #producer number
M = 20  #buffer size
num_a = 0
num_b = 0
class A(threading.Thread):
	def __init__(self, threadName, isa, isb, imutex):
		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = random.randrange(1,6)
		self.sa = isa
		self.sb = isb
		self.mutex = imutex

	def run(self) :
		global num_a, num_b
		while True:
			self.sa.acquire()
			self.mutex.acquire()
			num_a += 1
			print "A:%d, B:%d" %(num_a, num_b)
			self.mutex.release()
			self.sb.release()
			time.sleep(self.sleepTime)

class B(threading.Thread):
	def __init__(self, threadName, isa, isb, imutex):
		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = random.randrange(1,6)
		self.sa = isa
		self.sb = isb
		self.mutex = imutex

	def run(self):
		global num_a, num_b
		while True:
			self.sb.acquire()
			self.mutex.acquire()
			num_b += 1
			print "A:%d, B:%d" %(num_a, num_b)
			self.mutex.release()
			self.sa.release()
			time.sleep(self.sleepTime)


sa = threading.Semaphore(N)
sb = threading.Semaphore(M)
mutex = threading.Semaphore(1)

a = A("A", sa, sb, mutex)
b = B("B", sa, sb, mutex)
b.start()
a.start()





	Monitor：首先用1个变量表示A与B的差值，然后判断A-B是否满足-M&lt;=A-B&lt;=N。在达到右临界值时就开始等待条件变量，在B往仓库里面加的时候就发送signal。
	```
