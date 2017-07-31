#usr/bin/python

APK_PATH = '/home/lee/APKs'  # Download Path
#apk_path = '/home/lee/git/kernel-taskforce/apks'
GPLAY_PATH = '/home/lee/git/gplaycli/gplaycli' # Location of Gplaycli.py

import gevent.monkey
import gevent.queue
gevent.monkey.patch_all()

from os.path import isfile, join
from os import listdir 
from time import sleep
import os
import subprocess
import urllib 
import csv



queue = gevent.queue.Queue()

def cleanfolder():
    command = 'cd %s; find . -type d -empty -delete' % APK_PATH
    subprocess.Popen(command, shell=True).wait()

def download_helper():
    while not queue.empty():
        n = queue.get()
        FOLDER = APK_PATH + '/' + n + '.apk/'
        if not n:
            break
        if os.path.exists(FOLDER):
            print 'skipping..', n
            continue
        else:
            command = 'gplaycli -f %s -d %s' % (FOLDER, n)
            subprocess.Popen(command, shell=True).wait()
            #upload_command = 'sshpass -p %s scp -r %s austin@skjellum2.cse.eng.auburn.edu:/home/austin/MaliciousAPKs' % (PASS, FOLDER)
            #subprocess.Popen(upload_command, shell=True).wait()

def download(names, workercount=10):
    for idx, n in enumerate(names):
        if idx > 500:
            queue.put(n)

    workers = [
        gevent.spawn(download_helper)
        for _ in xrange(workercount)
    ]
    gevent.joinall(workers)

def main():
    # Grabs all App IDs from Sqlite DB
    print 'Reading from Remaining.csv'
    names = []
    input = open('Remaining.csv', 'rb')
    for row in csv.reader(input):
        name = row[0]
        names.append(row[0])
    print 'Removing Empty Directories'
    cleanfolder()
    print 'Starting Downloads'
    download(names)
    cleanfolder()

if __name__ == '__main__':
    main()
