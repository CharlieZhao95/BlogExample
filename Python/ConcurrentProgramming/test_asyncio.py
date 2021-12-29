# @Time    : 2021/12/29 22:41 
# @Author  : CharlieZhao
# @File    : test_asyncio.py 
# @Software: PyCharm

"""async task example"""

import threading
import asyncio
import time


def show_execution_time(start_time, end_time):
    print("The execution time is {} s".format(end_time - start_time))


async def _async_print_number(info):
    res = 0
    for i in range(100_000_000):
        res = res + i
        # 增加一条线程打印语句
        print(info, " res={} in {}".format(res, threading.currentThread()))
        await asyncio.sleep(1)  # 1s switch task
    print(info + " task over, result = {}".format(res))


def execute_async_task():
    loop = asyncio.get_event_loop()
    tasks = [_async_print_number("async task 1:"), _async_print_number("async task 2:")]
    print(" async task start ")

    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()

    show_execution_time(start, end)
    print(" async task end ")


if __name__ == "__main__":
    execute_async_task()
