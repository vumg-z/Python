#! /usr/bin/python3
# an insecure password locker program 

PASSWORDS = {'email': 'password',
            'twitter': 'password',
             'reddit': 'password'}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python pw.py  [account] - copy acount password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for account " + account + " copied to clipboard.")
else:
    print("There is no account name " + account)
    