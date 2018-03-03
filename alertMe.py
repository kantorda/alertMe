#!/usr/bin/python3
import os, sys, smtplib, concurrent.futures
from email.mime.text import MIMEText

def sendNotification(msgBody):
    # print statement for dev
    # will need to prompt user for credentials
    print("alert: {}".format(msgBody))

if __name__ == "__main__":
    sendNotification("hello world")