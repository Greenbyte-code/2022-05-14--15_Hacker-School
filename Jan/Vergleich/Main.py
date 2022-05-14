"""Vergleich Von STR, INT, FLOAT"""

inp = input("Eingabe ")

if "." in inp:
  try:
    inp = float(inp)
    print("hi")