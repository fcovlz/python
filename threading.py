# Threading using new 'threading' library from Python 2.4
import threading
import thread
import time


class myThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.exit_flag = 0
        
    def run(self):
        print "\nStarting " + self.name
        self.print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

    def print_time(self, thread_name, delay, counter):
        while 1:
            if self.exitFlag:
                thread_name.exit()
            time.sleep(delay)
            print "\n%s: %s" % (thread_name, time.ctime(time.time()))
            counter -= 1


def thread_print_time(thread_name, delay):
    while True:
        time.sleep(delay)
        print "%s : %s" % (thread_name, time.ctime(time.time()))


if __name__ == "__main__":
    # Threading example 1
    thread1 = myThread(1, "Thread-1", 1)
    thread1.daemon = True
    thread2 = myThread(2, "Thread-2", 2)
    thread2.daemon = True
    thread1.start()
    thread2.start()

    # Threading example 2
    thread3 = threading.Thread(target=thread_print_time("Thread-3", 3))
    thread.start()

    # Thread example
    # Instance new Thread objects
    thread.start_new_thread(thread_print_time(), ("Thread-4", 4,))
    thread.start_new_thread(thread_print_time(), ("Thread-5", 2,))
