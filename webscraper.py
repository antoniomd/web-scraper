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
    
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + userTelegramID + '&parse_mode=Markdown&text=' + bot_message

    print(send_text)

    requests.post(send_text)

def main():

    for item,details in allItems.items():
        myItem = item
        # myLimit = details.get('priceMax',0)
        # myUrl = details.get('url',0)

        # print('Item: ' + myItem)
        # print('Price Limit: ' + str(myLimit))
        # print('URL: ' + str(myUrl))

        myUrl = requests.get(details.get('url',0))
        soup = BeautifulSoup(myUrl.content, 'html.parser')

        priceContent = soup.find("meta",  property="product:price:amount")
        price = float(priceContent["content"])

        if price < details.get('priceMax',0):
            # message = 'El precio del articulo ' + item + 'es ' + str(price) + ' y es menor que el precio límite indicado de ' + str(priceLimit)
            telegram_bot_sendtext('El precio del articulo ' + item + ' es ' + str(price) + ' y es menor que el precio límite indicado de ' + str(details.get('priceMax',0)))
    
        else:
            # message = 'El precio del articulo ' + item + 'es mayor que el precio límite indicado'
            telegram_bot_sendtext('El precio del articulo ' + item + ' es mayor que el precio límite indicado de ' + str(details.get('priceMax',0))')
        

        

if __name__ == "__main__":
	main()