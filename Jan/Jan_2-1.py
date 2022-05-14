""""""
import time, os

header = "--------Rechner--------"
header2 = "-----------------------"

Operatoren = ["+", "-", "*", "/"]
Rechnungen =[]

zahl1 = None
operator = None
zahl2 = None
ergebnis = None

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def _QUIT(Grund, sec):
  print(Grund + "\n" f"Quit in {sec} sec")
  time.sleep(sec)
  quit()

def UI():
  global zahl1, operator, zahl2
  print(Rechnungen)
  print(header)
  zahl1 = input("1. Zahl -}   float: ")
  operator = input("Operator: [+, -, *, /]: ")
  zahl2 = input("2. Zahl -}     float: " )
  print(header2)


def überprüfen():
  global zahl1,  zahl2
  if operator not in Operatoren:
    _QUIT("Bitte geben einen gültigen Operator ein.", 3)
  try:
    zahl1 = float(zahl1)
    zahl2 = float(zahl2)
  except:
    _QUIT("Bitte geben eine gültige Zahl ein.", 3)


def rechen():
  global ergebnis
  überprüfen()
  if operator == '+':
    ergebnis = zahl1 + zahl2
  elif operator == '-':
    ergebnis = zahl1 - zahl2
  elif operator == '*':
    ergebnis = zahl1 * zahl2
  elif operator == '/':
    ergebnis = zahl1 / zahl2
  else:
    _QUIT("Irgend ein Fehler ist aufgerteten", 3)

def ERGBNIS():
  global Rechnungen
  text = f"{zahl1} {operator} {zahl2} = {ergebnis}"
  Rechnungen.append(text)
  text +=  "\n" + header2
  print(text)
while True:
  UI()
  rechen()
  ERGBNIS()