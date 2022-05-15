"""Apfelladen"""

from time import sleep
import os

"""
Wir haben eine Bestimmte Anzahl Äapfel im Lager.
der Kunde Soll so lange kaufen können bis das Lager leer ist / oder seinen Bestllung zu groß ist
"""

#https://www.delftstack.com/de/howto/python/python-clear-console/
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def porf_Clear(se):
  sleep(se)
  clearConsole()
  
Apfel = 150

while True:
  print(f"Wir haben akuell {Apfel} Äpfel im lager.")

  anzahl = int(input("Wie viele Äpfel möchtest du haben: "))
  print(f"Du möchtest also {anzahl} Äpfel kaufen")

  if Apfel <= 0:
    break
  elif anzahl > Apfel:
    print("So viele habe ich leider nicht")
    porf_Clear(2)
  elif anzahl == 42:
    print("Natürlich bekommst du " + "42"*42 + " Äpfel")
    anzahl -= 42
    porf_Clear(2)
  else:
    Apfel -= anzahl
    print(f"Natürlich bekommst du {anzahl} Äpfel, wir haben noch {Apfel} im Lager")
    porf_Clear(2)