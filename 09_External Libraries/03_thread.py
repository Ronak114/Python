# threading is a module in Python that allows for concurrent execution of code. It enables you to run multiple threads (smaller units of a process) simultaneously, which can be useful for I/O-bound tasks or when you want to perform background operations without blocking the main program flow.

import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2) # Simulate some work
    print(f"Thread {num}: Finishing")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Wait for all threads to finish
    
print("All threads completed.")