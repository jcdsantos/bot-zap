import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['codPais + codArea + numCelular']

while len(contatos) >= 1:

    pywhatkit.sendwhatmsg(contatos[0],'Oi',datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep[60]
    keyboard.press_and_release(atalho para fecha a aba)