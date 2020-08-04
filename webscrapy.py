#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script looks for an item in an url when the price will de less than a limit
Usage:
Start a bot in Telegram, pass an url and a price limit and wait til bot send a notification to yousource venv/bin/activate
"""

# Importo las funciones utilizadas (Confirmar que son necesarias)
import requests 
# , sys, urllib2, hashlib, os, ssl
#bfrom urlparse import urlparse
from bs4 import BeautifulSoup

# Importo las funciones utilizadas para Telegram
# import logging
# from telegram import ReplyKeyboardMarkup
# from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
#                           ConversationHandler)

# Importo la configuración del fichero
from config.auth import *

def main():
    myUrl = requests.get(url)

    soup = BeautifulSoup(myUrl.content, 'html.parser')

    print(soup.prettify())

if __name__ == "__main__":
	main()