from win10toast import ToastNotifier
import requests
import bananopy.banano as ban
from PIL import Image
import time
import json
from dotenv import load_dotenv
import os
load_dotenv()

toaster = ToastNotifier()

account_to_view = os.getenv("ADDRESS")

monkey = requests.get(f"https://monkey.banano.cc/api/v1/monkey/{account_to_view}?format=png&size=512")
filename = r"monkey.png"
img = Image.open(filename)
img.save("monkey.ico")


def checkbalance(address):
    response = requests.get(f"https://api-beta.banano.cc:443/?action=account_info&account={address}")
    todos = json.loads(response.text)
    bal = todos['balance']
    return bal 

def messageBalance(total):
    toaster.show_toast("Banano Account",f"You have received a new transaction, your new balance is now {total} ", icon_path= "monkey.ico")

balance1= ban.ban_from_raw(checkbalance(account_to_view))

while True:
    time.sleep(10)
    balance2 = ban.ban_from_raw(checkbalance(account_to_view))
    if balance2 > balance1:
        balance1 = balance2
        messageBalance(round(balance2, 2))
        print("LOG")
    print("No log")
    if balance2 == 0:
        balance1 = 0