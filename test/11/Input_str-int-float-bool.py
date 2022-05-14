"""Wandeld Input um"""
#Nich Fertig

vab1 = input("Deine erste zahl: ")
vab2 = input("</> : ")
vab3 = input("Deine zweite Zahl: ")
end_bool = False

if vab2 != "<" or ">":
  print("Bitte </> eingeben")

try:
  vab1 = float(vab1)
  vab3 = float(vab3)
  if vab2 == "<":
    if vab1 < vab3:
      end_bool = True
  if vab2 == ""
    