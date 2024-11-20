äpple = 7
päron = 13

def input_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print("Felaktig inmatning, skriv ett heltal.")

print("Hur många äpplen och päron sålde Axel och petra?")

axel = input_int("Axel har sålt: ")
petra = input_int("Petra har sålt: ")
axel_inkomst = axel * äpple
petra_inkomst = petra * päron

if axel_inkomst > petra_inkomst:
    print(f"Axel har tjänat mest med {axel_inkomst}kr.")
elif petra_inkomst > axel_inkomst:
    print(f"Petra har tjänat mest med {petra_inkomst}kr.")
else:
    print(f"Både har tjänat lika mycket med {axel_inkomst}kr.")