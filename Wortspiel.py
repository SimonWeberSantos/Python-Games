#Wortspiel - Spieler 1 gibt das Wort ein. Das Programm vertauscht die Buchstaben und der Spieler 2 muss das Wort herausfinden

# Importe
import getpass
import time

# Spieler 1 gibt ein Geheimwort ein(funktioniert NICHT bei Idle!!!)
eingabe = getpass.getpass('Spieler*in 1 - Bitte ein Wort mit max. 10 Buchstaben eingeben:')

wort = []

for i in eingabe:
    wort.append(i)

print()
print('Spieler*in 2 - Entwirre folgendes Wort in maximum drei Versuchen')

if len(wort) == 3:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    print(b, c, a)

if len(wort) == 4:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    print(b, c, d, a)

if len(wort) == 5:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    e = wort[4]
    print(d, b, e, a, c)

if len(wort) == 6:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    e = wort[4]
    f = wort[5]
    print(b, d, f, a, c, e)

if len(wort) == 7:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    e = wort[4]
    f = wort[5]
    g = wort[6]
    print(g, d, a, c, f, b, e)

if len(wort) == 8:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    e = wort[4]
    f = wort[5]
    g = wort[6]
    h = wort[7]
    print(e, h, a, b, g, d, c, f)

if len(wort) == 9:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    e = wort[4]
    f = wort[5]
    g = wort[6]
    h = wort[7]
    i = wort[8]
    print(b, i, d, a, h, f, c, g, e)

if len(wort) == 10:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    e = wort[4]
    f = wort[5]
    g = wort[6]
    h = wort[7]
    i = wort[8]
    j = wort[9]
    print(b, i, d, j, a, h, f, c, g, e)

if len(wort) == 11:
    a = wort[0]
    b = wort[1]
    c = wort[2]
    d = wort[3]
    e = wort[4]
    f = wort[5]
    g = wort[6]
    h = wort[7]
    i = wort[8]
    j = wort[9]
    k = wort[10]
    print(k, b, i, d, j, a, h, f, c, g, e)

print('Korrektes Wort:')
versuch = 1

while versuch < 4:
    loesung = input()
    print()
    if loesung == eingabe:
        print('Bravo, du hast das Wort entwirrt!')
        time.sleep(1)
        print('Benötigte Versuche:', versuch)
        time.sleep(1)
        break
    else:
        print('Das war nichts!')
        time.sleep(1)
        if versuch < 3:
            print('Probier es nochmals:')
            versuch += 1
        else:
            print('Du hast deine Versuche aufgebraucht und konntest das Wort nicht entwirren - GAME OVER')
            time.sleep(1)
            break

input('Danke fürs Mitspielen!')