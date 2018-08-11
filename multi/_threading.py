import threading


class myThread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id

    def run(self):
        print(self.threadID)


thread1 = myThread(1)
thread2 = myThread(2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("finished")
