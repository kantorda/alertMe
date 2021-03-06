alertMe

Command line utility that sends email notifications (can be received as SMS message) when a designated process terminates.

Uses the SMTP protocol via python's smtplib package.  Therefor, you need access to an external mail server.  If you don't maintain your own, many email and internet services provide public facing SMTP servers.  Look up your provider's SMTP server details, you will need a domain name and port number.  For Gmail it is 'smtp.gmail.com' at port 465.  Gmail (if not others as well) require you to change some security settings on your account; generally by allowing unverified apps from accessing your account.  This can be done from their online portal; but you may want to create a throw-away account, not connected to any account you otherwise use.

***I make no garuntees about the security of this process or any of the code in alertMe, and recommend you take your own steps to protect yourself.***  

Insert into the following line the domain name of the server and the port number:
server_ssl = smtplib.SMTP_SSL('XXX.XXX.com', INT)

Insert into the following line the email address you wish the message to be sent to:
to = ['XXX@XXX.com']

Most cellular providers allow for emails to be sent to a phone number.  You can receive your alert as an SMS (standard messaging rates) by entering the proper address in the "to" field.  Look up your mobile provider for details (for example, Verizon's is '#@vtext.com')

alertMe can be run in two modes: monitoring one process or a batch of processes.

To run alertMe on one process, call it from the command line as follows:
python3 alertMe.py ./executable [args]

If you make alertMe.py executable, you can call it as:
./alertMe.py ./executable [args]

('./' is necessary for argument parsing)

'executable' should be the name of the process you want monitored.  It must be an executable file that can be run by prepending the file name with './'.

[args] should be the space-seperated list of arguments required for your monitored process to run.  It can be of variable length or empty.

To run on multiple processes, call it from the command line as follows:
./alertMe.py inputFile outputFile

'inputFile' should be a text file containing the processes you want run and monitored.
The first line should be an integer referencing the maximum number of processes from the file you want running at a time.
Each subsequent line should contain the same data and format as calling a single process (./exec [args]).

'outputFile' should be a text file to write logs to.

Alerts will be sent when any proces fails to run or returns non-zero.  Other than that, one alert will be sent after all processes in the file terminate.

Process termination order and exit codes get written to the log file.  One process failing will not stop the others from running.

You will be prompted to enter the login credentials for the account you wish to send the email from, in the form:
XXX@XXX.com
password

This prompt will accur before alertMe begins running the process you wish to monitor so you will not need to check on it.
