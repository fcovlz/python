# Threading using new 'threading' library from Python 2.4
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print "\nStarting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while 1:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "\n%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

if __name__ == "__main__":
    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread1.daemon = True
    thread2 = myThread(2, "Thread-2", 2)
    thread2.daemon = True
    
    # Start new Threads
    thread1.start()
    thread2.start()

    # print "\nExiting Main Thread"

      
    # while(1):
        # print "~"
        # time.sleep(1)