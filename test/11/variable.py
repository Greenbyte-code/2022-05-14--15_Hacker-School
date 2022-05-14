"""Test/Einfürung Vab"""

#Vab als str
v1 = "Ein Text"
print(v1)

#Vab als int
zahl1 = 7
zahl2 = 8

summe = zahl1 + zahl2

text = "Die Summe ist: {}"
print(text.format(summe))

#Vab als bool

bool_1 = True
bool_2 = False

bool_3 = (2 < 1)
bool_3_text = f"Die aussage 2 < 1 ist {bool_3}"

print(bool_3_text)