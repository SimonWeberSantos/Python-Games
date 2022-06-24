#Würfelspiel

print('Wie viele Versuche braucht es um alle Zahlen von 1 bis 6 zu würfeln?')
input('Drücke auf Enter, um zu starten.')

import random
random.seed()

versuch = 0
gewürfelt = []

while "1" not in gewürfelt or "2" not in gewürfelt or "3" not in gewürfelt \
      or "4" not in gewürfelt or "5" not in gewürfelt or "6" not in gewürfelt:
    a = random.randint(1, 6)
    a = str(a)
    if a not in gewürfelt:
        gewürfelt.append(a)
        versuch = versuch + 1
    else:
        versuch = versuch + 1

gewürfelt.sort()
print()
print('Anzahl gewürfelt:', versuch)
print()
input('Danke fürs Mitspielen!')
