import os
import requests
from json import loads
import random
import time

logo = '''
\033[38;5;5m▒███████▒ ▒█████   ██▀███   ▒█████  
\033[38;5;13m▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒
\033[38;5;212m░ ▒ ▄▀▒░ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒
\033[38;5;218m  ▄▀▒   ░▒██   ██░▒██▀▀█▄  ▒██   ██░
\033[38;5;219m▒███████▒░ ████▓▒░░██▓ ▒██▒░ ████▓▒░
\033[38;5;213m░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
\033[38;5;218m░░▒ ▒ ░ ▒  ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ 
░ ░ ░ ░ ░░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒  
\033[38;5;219m  ░ ░        ░ ░     ░         ░ ░  
░                                   '''
class image_scraper:
  def __init__(self, channel_id):
    self.token = "token here" #ToKeN HeRe!!!
    self.headers = {
      "Authorization": f"{self.token}"
    }
    self.channel_id = channel_id
  def scraper(self):
     self.r = requests.get(f"https://discord.com/api/v8/channels/{self.channel_id}/messages", headers=self.headers)
     jsonnn = loads(self.r.text)
     self.lst = []
     with open("name.txt","a", errors="ignore") as a:  
       for i in jsonnn:
         if i['author']['username'] not in self.lst:
            self.user = i['author']['username']
            a.write(self.user)
            a.write('\n')
            self.lst.append(self.user)
            print(f'\033[38;5;77m[+] successfully scraped username from {self.user}')

           
print(logo)
chan = str(input('enter channle id >> '))
run = image_scraper(chan)
run.scraper()
