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




