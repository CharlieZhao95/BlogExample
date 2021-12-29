# @Time    : 2021/12/26 22:43 
# @Author  : CharlieZhao
# @File    : test_multiprocessing.py
# @Software: PyCharm

""" To avoid performance deficiency caused by GIL, multiprocessing is a better way to perform concurrent tasks than
threading. This module is used to test performance between multiprocessing and threading.
"""

from multiprocessing import Process
from threading import Thread
import time

def _print_number(info):
    res = 0
    for i in range(100_000_000):
        res = res + i
    print(info + " task over, result = {}".format(res))


def show_execution_time(start_time, end_time):
    print("The execution time is {} s".format(end_time - start_time))


def execute_multiprocessing_task():
    """
    log the execution time of multiprocessing task.
    :return: void
    """
    print(" multiprocessing task start ")
    p1 = Process(target=_print_number, args=("Process 1",))
    p2 = Process(target=_print_number, args=("Process 2",))

    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()

    show_execution_time(start, end)
    print(" multiprocessing task end ")


def execute_threading_task():
    print(" threading task start ")
    t1 = Thread(target=_print_number, args=("Thread 1",))
    t2 = Thread(target=_print_number, args=("Thread 2",))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()

    show_execution_time(start, end)
    print(" threading task end ")


if __name__ == "__main__":
    execute_multiprocessing_task()
    execute_threading_task()
    pass
