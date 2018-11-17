# Threading example using 'thread' library
import thread
import time

# Worker Function
def printTime(threadName, delay):
    while(1):
        time.sleep(delay)
        print "%s : %s" % (threadName, time.ctime(time.time()))


# Instance new Thread objects
thread.start_new_thread(printTime, ("Thread-1", 4, ))
thread.start_new_thread(printTime, ("Thread-2", 2, ))

# To keep alive the execution of the process
while(1):
    pass
