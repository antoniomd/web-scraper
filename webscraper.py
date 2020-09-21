# -*- coding: utf-8 -*-

"""
rpi-monitor.py

The script gets CPU temperature, use and frequency.

Then these parameters can be viewed in the Terminal.

Usage:
Clone the repository.

Run rpi-monitor.py in your RPi. Maybe, you must install psutil.
"""

# Importo las librerias
import subprocess, psutil, requests

# Importo la configuración del fichero
from config.auth import *


# Envía un mensaje a través de Telegram
def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + userTelegramID + '&parse_mode=Markdown&text=' + bot_message
    requests.post(send_text)

def main():
    # Obtengo la Tª de la CPU
    tempFile = open('/sys/class/thermal/thermal_zone0/temp', 'r')
    cpuTemp = float(tempFile.read())/1000
    tempFile.close()

    # Obtengo el % de uso de la CPU
    cpuUse = psutil.cpu_percent(interval=1, percpu=False)
    
    # Obtengo la frecuencia de la CPU
    freqFile = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq', 'r')
    cpuFreq = float(freqFile.read())/1000
    freqFile.close()
    
    # Muestra en el Terminal la información
    print('Temperatura CPU => ' + str(int(cpuTemp)) + ' ºC')
    print('Uso de la CPU => ' + str(cpuUse) + ' %')
    print('Frecuencia CPU => ' + str(cpuFreq) + ' Hz')

    # Gestión alarmas de temperatura
    if cpuTemp >= 80 and cpuTemp < 85:
        message = 'La temperatura de la CPU de nuestra Raspberry ha alcanzado los 80ºC'
        if warningTemp is False:
            telegram_bot_sendtext(message)
            warningTemp = True
    elif cpuTemp >= 85:
        message = 'La temperatura de la CPU de nuestra Raspberry ha alcanzado los 85ºC'
        if tripTemp is False:
            telegram_bot_sendtext(message)
            tripTemp = True
    else:
        warningTemp = tripTemp = False



if __name__ == "__main__":
	main()
