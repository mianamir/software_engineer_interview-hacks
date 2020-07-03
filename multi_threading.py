"""
Python Threading:
Run Code Concurrently Using the Threading Module

-> Running tasks Concurrently to speed up the program
-> CPU and IO bounds tasks are handled by multi_threading
-> IO bounds tasks: network operations like scraping multi sites,
    reading / writing files from file system
-> IO bounds tasks are a lot of waiting for Input / Output operations
-> If tasks are a lot of CPU using than multi_threading is not suitable
->

"""
import concurrent.futures
import threading
import time

start = time.perf_counter()


def do_somthing(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f'Done sleeping.. {seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_somthing, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executor.map(do_somthing, secs)
    for res in results:
        print(res)


# manual way to create threads

# do_somthing()
# do_somthing()
# do_somthing()

# t1 = threading.Thread(target=do_somthing)
# t2 = threading.Thread(target=do_somthing)
# t3 = threading.Thread(target=do_somthing)
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()



# threads = list()
#
# for _ in range(10):
#     t = threading.Thread(target=do_somthing ,args=[1.6])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds(s)')