#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script looks for an item in an url when the price will de less than a limit
Usage:
Start a bot in Telegram, pass an url and a price limit and wait til bot send you a message
"""
# Importo las funciones utilizadas
import random, logging

# Importo las funciones utilizadas (Confirmar que son necesarias)
import  sys, urllib2, hashlib, os, ssl, requests
from urlparse import urlparse
from bs4 import BeautifulSoup

# Importo las funciones utilizadas para Telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Importo la configuración del fichero
from config.auth import *

def main():
    

if __name__ == "__main__":
	main()