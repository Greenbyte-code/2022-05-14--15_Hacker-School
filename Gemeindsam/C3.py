import random 
zufall=random.randint(1,50)
richtig = False

print("Wilkommen im Zahlenratenspiel (1-50)")
versuche = int(input("Wie vielen Versuchen willst du? "))

while versuche > 0:
  guess=int(input("Was ist dein Tipp? "))
  if guess < zufall:
    print("Die Zahl ist größer")
  elif guess > zufall:
    print("Die Zahl ist kleiner")
  else: 
    print("Dein Tipp ist richtig!")
    print("Du hast " + str(versuche) + " Versuche gebraucht um die die Zahl " + str(zufall) + " zu erraten!")
    richtig = True
    break
  versuche=versuche - 1
    
if richtig == False:
  print("Du hast leider nicht geschafft die Zahl " + str(zufall) + " zu erraten ")
