from urllib import request
from bs4 import BeautifulSoup
import requests
import smtplib
import email.message


URL = ""

headers = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h1', class_ = 'name').get_text()

price = soup.find('strong', class_ = 'sale-price').get_text().strip()

num_price = price[3:8]
num_price = num_price.replace('.', '')
num_price = float(num_price)

def send_email():
    email_content = """ """
    msg = email.message.Message()
    msg['Subject'] = 'Preço baixou'

    msg['From'] = ''
    msg['To'] = ''
    password = ''
    msg.add_header('Contet-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

if (num_price < 5000):
    send_email()