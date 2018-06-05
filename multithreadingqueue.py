import multiprocessing as mp
import queue
import numpy as np
import time
import random

def main():
    trainbatch_q = mp.Queue(10)

    batchperq = 50  
    event = mp.Event()

    tl1 = mp.Process(target=proc, args=( trainbatch_q, 20, batchperq, event))
    print("Got here")
    tl1.start()
    time.sleep(3)
    event.set()
    tl1.join()
    print("Never printed..")    

def proc(batch_q, batch_size, batchperentry, the_event):
    print("enter")
    nrow = 100000
    i0 = 0
    to_q = []
    while i0 < nrow:
        rowend = min(i0 + batch_size,nrow)
        somerows = random.randint(0,5,(rowend-i0,2))
        to_q.append(somerows.tolist())  
        if len(to_q) == batchperentry:
            print("adding..", i0, len(to_q))
            while not the_event.is_set():
                try: 
                    batch_q.put(to_q, block=False)
                    to_q = []
                    break
                except queue.Full:
                    time.sleep(1)
        i0 += batch_size                    
    print("proc finishes")
    return

if __name__ == "__main__":
    main()
