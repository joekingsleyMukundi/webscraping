import requests
import pandas as ps
from bs4 import BeautifulSoup


def stock():
    page = requests.get('https://finance.yahoo.com/quote/CL=F?p=CL=F')
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(id='quote-header-info')
    name = content.find(class_='D(ib) Fz(18px)').get_text()
    price_index = content.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').get_text()
    crude_oil = [name,price_index]
    return crude_oil



while True:
  print(stock())
