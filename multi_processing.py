"""
Python Multiprocessing:
Run Code in Parallel Using the Multiprocessing Module

-> CPU bound tasks like download images from online and then resize them


"""

import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()


# def do_something():
#     print(f'Sleeping {1} second(s)...')
#     time.sleep(1)
#     return f'Done Sleeping...{1}'
#
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()

# processes = list()
#
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something)
#     p.start()
#     processes.append(p)
#
# for process in processes:
#     process.join()


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')