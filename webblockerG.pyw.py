# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:14:03 2021

@author: USER
"""
from datetime import datetime as dt
import time 
hosts_temp=r"C:\Users\USER\Desktop\discrete\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=[ "www.konga.com" ,"www.opay.com","www.jumia.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for websites in website_list):
                    file.write(line)
            file.truncate()
            
        print("what life is suppose to be ,fun hours")
    time.sleep(5)