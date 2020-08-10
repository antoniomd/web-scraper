#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script sends a notification when an item in cheaper than price maximum
Usage:
Pass an item, url and a price max in auth.py and wait til bot sends a notification to you
A Telegram bot and Telegram user ID is required
"""

# Importo las funciones utilizadas
import requests 
from bs4 import BeautifulSoup


# Importo la configuración del fichero
from config.auth import *


# Extrae el precio de la URL del articulo
def getPrice(url):
        myUrl = requests.get(url)
        soup = BeautifulSoup(myUrl.content, 'html.parser')

        # Encuentra el precio del producto que tiene la propiedad product:price:amount
        priceContent = soup.find("meta",  property="product:price:amount")
        if priceContent:
            price = float(priceContent["content"])
        # Si no encuentra ningún precio indica con None que no lo ha encontrado
        else:
            price = None
        return price


# Envía un mensaje a través de Telegram
def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + userTelegramID + '&parse_mode=Markdown&text=' + bot_message
    requests.post(send_text)


def main():
    # Recorro con un for los articulos
    for item,details in allItems.items():
        # item indica el nombre del artículo que estamos buscando
        priceMax = details.get('priceMax',0)    # priceMax indica el precio máximo que estamos dispuesto a pagar
        url = details.get('url',0)              # url indica la url del articulo

        price = getPrice(url)                   # Se llama a la función getPrice donde extraigo el precio de la página

        # Si no encuentro el precio en la url envío una notificación para indicarlo
        if price == None:
            message = 'No se encuentra el precio en la url indicada'
            telegram_bot_sendtext(message)

        # Si el precio es inferior al precio máximo lo notifico
        elif price < priceMax:
            message = 'El precio del articulo ' + item + ' es ' + str(price) + ' y es menor que el precio límite indicado de ' + str(priceMax)
            telegram_bot_sendtext(message)


if __name__ == "__main__":
	main()