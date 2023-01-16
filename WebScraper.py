from bs4 import BeautifulSoup
import requests
import csv
from time import gmtime, strftime
import datetime
import time 
import pandas as pd
import smtplib

#Enter URL of Item looking to buy
url = "https://www.newegg.com/samsung-1tb-980-pro/p/N82E16820147790"
#Enter target price
target = 300.0

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
thought = "Too Exspensive"
Float = float(strong.string)
if Float < target:
    thought = "Cheap enough to buy"

print (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print(strong.string + " " + thought + "  ")


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('elhesh02@gmail.com','PASSWORD place holder')
    
    subject = "Price Drop"
    body = "The price has dropped! buy at" + url
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'elhesh02@gmail.com',
        msg
     
    )

while True:
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    if Float < target:
        print("BUY")
       # send_mail()

    time.sleep(10)
