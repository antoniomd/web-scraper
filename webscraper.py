#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script looks for an item in an url when the price will de less than a limit
Usage:
Start a bot in Telegram, pass an url and a price limit and wait til bot send a notification to yousource venv/bin/activate
"""

# Importo las funciones utilizadas
import requests 
from bs4 import BeautifulSoup

# Importo la configuración del fichero
from config.auth import *

def telegram_bot_sendtext(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    print(send_text)

    requests.post(send_text)

def main():
    myUrl = requests.get(url)
    soup = BeautifulSoup(myUrl.content, 'html.parser')

    priceContent = soup.find("meta",  property="product:price:amount")
    price = float(priceContent["content"])

    if price < priceLimit:
        message = 'El precio del articulo es ' + str(price) + ' y es menor que el precio límite indicado de ' + str(priceLimit)
        telegram_bot_sendtext(message)
    
    else:
        message = 'El precio del articulo es mayor que el precio límite indicado'
        telegram_bot_sendtext(message)

if __name__ == "__main__":
	main()