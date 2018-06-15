#!/usr/bin/python

import os,thread,time,threading

root_dir = "/home/ubuntu/aria2-data"
target_dir = "/home/ubuntu/upload"

cache_files=[]
class MyThread1(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        while 1:
            time.sleep(2)
            self.find_file(root_dir)

    def find_file(self,root_dir):
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file not in cache_files:
                    cache_files.append(file)

class MyThread2(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        while 1:
            time.sleep(2)
            self.deal_file()

    def deal_file(self):
        while True:
            for file in cache_files:
                if not file.endswith(".aria2"):
                    if file + ".aria2" not in cache_files:
                        self.move(file)

    def move(self,file):
        print("move and upload file,and the delete the local file:" + file)
        command = 'mv ' + root_dir + '/' + file + ' ' + target_dir + ' && onedrive ' + target_dir + '/' + file + ' && rm  -rf ' + target_dir + '/' + file
        os.system(command)
        cache_files.remove(file)

if __name__ == "__main__":
    try:
        thread1 = MyThread1(1, "Thread-1", 1)
        thread2 = MyThread2(2, "Thread-2", 2)
        thread1.start()
        thread2.start()
    except:
        print "Error: unable to start thread"

    while 1:
        time.sleep(5)
