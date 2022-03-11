# import the multiprocessing,random and time modules
import multiprocessing
import random
import time
# create a worker function which takes a name as argument and prints hello name
# It returns nothing. Inside, it prints out the name of the worker, then use 
# time.sleep() to simulate doing some long-running process. Finally, it will
# print out that it has finished.
def worker(name):
    print(f'Hello {name}')
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f'{name} worker finished in {worker_time} seconds')
if __name__ == '__main__':
    # creating an empty list to hold processes
    processes = []
    # create 3 worker processes by using multiprocessing.Process()
    for i in range(3):
        # Tell Process the target function to use and the arguments to pass
        process = multiprocessing.Process(target=worker, args=(f'computer_{i}',))
        processes.append(process)
        #For each process, you call its start() method to start the process.
        process.start()
    # Finally, loop over list of processes and call its join() method, 
    # which tells Python to wait for the process to terminate.
    for proc in processes:
        proc.join()