# Python program to illustrate the concept
# of threading
import threading
import os
import random
import time

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    random_int = random.randint(3, 10)
    print(f'pause for {random_int} seconds\n')
    time.sleep(random_int)
    print("ID of process running task 1: {}\n".format(os.getpid()))

def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    random_int = random.randint(3, 10)
    print(f'pause for {random_int} seconds\n')
    time.sleep(random_int)
    print("ID of process running task 2: {}\n".format(os.getpid()))

def task3():
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))
    random_int = random.randint(3, 10)
    print(f'pause for {random_int} seconds\n')
    time.sleep(random_int)
    print("ID of process running task 3: {}\n".format(os.getpid()))

if __name__ == "__main__":

	# print ID of current process
	print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
	print("Main thread name: {}\n".format(threading.current_thread().name))

	# creating threads
	thread1 = threading.Thread(target=task1, name='thread1')
	thread2 = threading.Thread(target=task2, name='thread2')
	thread3 = threading.Thread(target=task3, name='thread3')

	# starting threads
	thread1.start()
	thread2.start()
	thread3.start()

	# wait until all threads finish
	thread1.join()
	thread2.join()
	thread3.join()
