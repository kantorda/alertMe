#!/usr/bin/python3
import os, sys, smtplib, concurrent.futures
from email.mime.text import MIMEText

data = {"account": None, "password": None}
cmds = []

def sendNotification(msgBody):
    try:
        #connect to SMTP server
        serverSSL = smtplib.SMTP_SSL('XXX.XXX.com', INT)
        serverSSL.ehlo()
        
        #format msg
        to = ['XXX@XXX.com']
        subject = 'alertMe'
        emailText = """\
        From: {}
        To: {}
        Subject: {}

        {}
        """.format(data["account"], ", ".join(to), subject, msgBody)

        #send msg
        serverSSL.login(data["account"], data["password"])
        serverSSL.sendmail(data["account"], to, emailText)
        serverSSL.close()

    except:
        print('notification failed to send')

def singlePWatcher():
    cmd = ""
    for arg in sys.argv[1:]:
        cmd += arg + " "
    exitCode = os.system(cmd)
    msgBody = "process terminated with exit code {}".format(exitCode)
    sendNotification(msgBody)

def runCMD(info):
    return os.system(info[1])

def multiPWatcher():
    inputFileName = sys.argv[1]
    file = open(inputFileName, 'r')
    maxThreads = int(file.readline().rstrip())
    count = 0
    for line in file:
        cmds.append([count, line.rstrip()])
        count += 1
    file.close()
    #initiate thread pool with cmds
    logFileName = sys.argv[2]
    logFile = open(logFileName, 'w')
    with concurrent.futures.ThreadPoolExecutor(max_workers=maxThreads) as executor:
        futuresToRun = {executor.submit(runCMD, info): info for info in cmds}
        for future in concurrent.futures.as_completed(futuresToRun):
            callData = futuresToRun[future]
            try:
                exitCode = future.result()
            except Exception as exc:
                msgBody = "Process {} has generated an exception: {}".format(callData[0], exec)
                logFile.write(msgBody + '\n')
                sendNotification(msgBody)
            else:
                msgBody = "Process {} has terminated with exit code: {}".format(callData[0], exitCode)
                logFile.write(msgBody + '\n')
                if exitCode != 0:
                    sendNotification(msgBody)
    msgBody = "All processes have terminated"
    logFile.write(msgBody)
    logFile.close()
    sendNotification(msgBody)

if __name__ == "__main__":
    data["account"] = input("account: ")
    data["password"] = input("password: ")
    token = sys.argv[1][:2]
    if token == "./":
        singlePWatcher()
    else:
        multiPWatcher()