import schedule
import time
import subprocess
import os

os.chdir(r"C:\Users\Billy\Desktop\C\Meme-Volt")

def job():
    subprocess.call('python main.py Ale 1', shell=True)

schedule.every().day.at("8:52").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)