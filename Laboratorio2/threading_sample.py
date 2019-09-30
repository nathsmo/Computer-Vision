from threading import Thread
import time

i = 0
running = True



def thread1():
	""" Print i, modified by thread 2
	"""
	global i, running

	while running:
		print('Executing code. i = {0}\r'.format(i), end = '')
	return None

def thread2():
	""" Modify 1
	"""
	global i, running


	while running:
		i +=1
		time.sleep(1)
	return None

# create threads and assign functions
t1 = Thread(target=thread1, args=())
t2 = Thread(target=thread2, args=())

#starts execution of threads
t1.start()
t2.start()

# do additional work and signal threads to stop
time.sleep(10)
running = False

# add to ensure that threads terminate properly
t1.join()
t2.join()