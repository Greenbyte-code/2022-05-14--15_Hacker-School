"""Aufgabe 1 Input"""

in_Name = input("Wie lautet dein Name: ")
in_Alter = input("Und wie alt bist du: ")

text = "Hallo {}, ich heiße Jan und bin {} Jahre {} als du"

in_Alter = int(in_Alter)

if in_Alter > 12:
  Jahredrüber = in_Alter - 12
  text = "Hallo " + in_Name + ", ich heiße Jan und bin " + str(Jahredrüber) + " Jahre jünger als du"
elif in_Alter < 12:
  Jahredrunter = 12 - in_Alter
  text = "Hallo " + in_Name + ", ich heiße Jan und bin " + str(Jahredrunter) + " Jahre älter als du"
elif in_Alter == 12:
  text = "Hallo " + in_Name + ", ich heiße Jan und bin Jahre auch 12"
else:
  text = "Kp was los ist"

print(text)