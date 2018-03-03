#!/usr/bin/python3
import os, sys, smtplib, concurrent.futures, shutil, psutil
from email.mime.text import MIMEText

def sendNotification(msgBody):
    # print statement for dev
    # will need to prompt user for credentials
    print("alert: {}".format(msgBody))

def getPath():
    execPath = ""
    try:
        execPath = shutil.which(sys.argv[1])
    except:
        print("invalid number of arguments")
    if execPath is None:
        execPath = os.getcwd() + "/" + sys.argv[1]
    return execPath

def runCmd(execPath):
    argList = [execPath]
    for arg in sys.argv[2:]:
        argList.append(arg)
    try:
        process = psutil.Popen(argList)
    except:
        print(sys.exc_info())
        return None
    return process

if __name__ == "__main__":
    execPath = getPath()
    process = runCmd(execPath)
    if process is not None:
        process.wait()
        sendNotification("process with pid {} has terminated".format(process.pid))
