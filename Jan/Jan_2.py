year_heute = 2022
name = input("Wie ist dein Name: str: ")
geja = int(input("Wann bist du geboren: INT: "))

#Rehnung
alter = year_heute - geja

if alter < 18:
  text2 = "Und bist relativ jung"
elif alter > 18:
  text2 = f"{name}: Wann gehe ich in Rente?"

text = f"Du bist {alter} Jahre alt."

print(text)
print(text2)