#!/usr/bin/python3
import os, sys, smtplib
from email.mime.text import MIMEText

def send_notification(return_code, userData):
    try:
        #connect to google server
        server_ssl = smtplib.SMTP_SSL('XXX.XXX.com', INT)
        server_ssl.ehlo()
        
        #format msg
        to = ['XXX@XXX.com']
        subject = 'alertMe'
        body = "process ended with return code {}".format(return_code)

        email_text = """\
        From: {}
        To: {}
        Subject: {}

        {}
        """.format(userData['account'], ", ".join(to), subject, body)

        #send msg
        server_ssl.login(userData['account'], userData['password'])
        server_ssl.sendmail(userData['account'], to, email_text)
        server_ssl.close()

    except:
        print('notification email failed to send')

def watcher(cmd, userData):
    for arg in sys.argv[1:]:
        cmd += arg + " "
    return_code = os.system(cmd)
    send_notification(return_code, userData)

if __name__ == "__main__":
    userData = {"account": None, "password": None}
    userData["account"] = input("account: ")
    userData["password"] = input("password: ")
    file_extension = sys.argv[1][-3:]
    if file_extension == ".py":
        watcher("python3 ", userData)
    else:
        watcher("./", userData)
