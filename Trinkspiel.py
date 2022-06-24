# Trinkspiel

import getpass

print('''Zwei Spieler trinken aus der selben Flasche, welche 1 Liter umfasst.
Es können abwechslungsweise verschieden grosse Schlücke genommen werden.
Das Ziel ist es möglichst genau bei "Null" (Ende der Flasche) anzukommen.
Das Spiel geht über sechs Runden und Sieger ist, wer am Ende am meitsen Punkte
auf seinem Konto hat. Folgendermassen werden die Punkte aufs Konto geschrieben:
Genau bei Null angekommen = 4 Punkte und die Gegnerin erhält + 1 Punkt
Unter Null = - 1 Punkt und die Gegnerin erhält + 1 Punkt
''')

kontoSpieler1 = 0
kontoSpieler2 = 0

#Input Name der Spieler
print('Spieler 1 - Bitte Namen eingeben:')
name1 = input()
print()
print('Spieler 2 - bitte Namen eingeben:')
name2 = input()

print()

#Funktion Spieler 1 - Trinkmenge
def trinkmengeSpieler1():
    trinkmengen = [0.1, 0.2, 0.5] # Drei mögliche Trinkmengen
    print()
    print(name1 +', wie viel möchtest du trinken? (Auswahl 1, 2 oder 3 eingeben)')
    for i in range(1, 4):
        print(str(i) + ':', trinkmengen[i-1], 'Liter')
    # Eingabe Spieler 1 + Check ob korrekt
    eingabe = int(4)
    while eingabe != 1 or eingabe != 2 or eingabe != 3:
        try:
            eingabe = int(getpass.getpass("Verdeckte Eingabe: "))
        except:
            print('Bitte eine Zahl zwischen 1 und 3 eingeben:')
            continue
        if eingabe == 1:
            return 0.1
        elif eingabe == 2:
            return 0.2
        elif eingabe == 3:
            return 0.5
        else:
            print('Bitte eine Zahl zwischen 1 und 3 eingeben.')
            continue

#Funktion Spieler 2 - Trinkmenge
def trinkmengeSpieler2():
    trinkmengen = [0.1, 0.2, 0.5] # Drei mögliche Trinkmengen
    print()
    print(name2 +', wie viel möchtest du trinken? (Auswahl 1, 2 oder 3 eingeben)')
    for i in range(1, 4):
        print(str(i) + ':', trinkmengen[i-1], 'Liter')
    # Eingabe Spieler 1 + Check ob korrekt
    eingabe = int(4)
    while eingabe != 1 or eingabe != 2 or eingabe != 3:
        try:
            eingabe = int(getpass.getpass("Verdeckte Eingabe: "))
        except:
            print('Bitte eine Zahl zwischen 1 und 3 eingeben:')
            continue
        if eingabe == 1:
            return 0.1
        elif eingabe == 2:
            return 0.2
        elif eingabe == 3:
            return 0.5
        else:
            print('Bitte eine Zahl zwischen 1 und 3 eingeben.')
            continue

history = [] #Hier werden die getrunkenen Mengen zum Nachvollziehen einer Runde abgespeichert

#Schleife für sechs Runden
runden = 1
while runden < 7:
    #Schleife für ungerade Runden (Spieler 1 fängt hier jeweils an)
    while runden == 1 or runden == 3 or runden == 5:
        bestandFlasche = round(1.0, 1)
        print()
        print('Runde', runden, '-', name1, 'fängt an.')
        #Schleife Geheimeingabe der beiden Spieler abwechslungsweise und Check, ob der Flanschenbestand unter oder bei Null ist
        while bestandFlasche > 0.0:
            a = trinkmengeSpieler1()
            history.append(a)
            bestandFlasche = round(bestandFlasche, 1) - round(a, 1)
            round(bestandFlasche, 1)
            if bestandFlasche == 0.0:
                print()
                print('Super gemacht,', name1, '- du bist genau bei Null gelandet!')
                kontoSpieler1 = kontoSpieler1 + 4
                kontoSpieler2 = kontoSpieler2 + 1
                break
            elif bestandFlasche < 0.0:
                print()
                print('Du bist unter Null und verlierst einen Punkt.')
                kontoSpieler1 = kontoSpieler1 - 1
                kontoSpieler2 = kontoSpieler2 + 1
                break
            b = trinkmengeSpieler2()
            history.append(b)
            bestandFlasche = round(bestandFlasche, 1) - round(b, 1)
            round(bestandFlasche, 1)
            if bestandFlasche == 0.0:
                print()
                print('Super gemacht,', name2, '- du bist genau bei Null gelandet!')
                kontoSpieler2 = kontoSpieler2 + 4
                kontoSpieler1 = kontoSpieler1 + 1
            elif bestandFlasche < 0.0:
                print()
                print('Du bist unter Null und verlierst einen Punkt.')
                kontoSpieler2 = kontoSpieler2 - 1
                kontoSpieler1 = kontoSpieler1 + 1
        print()
        print('Ablauf Runde', runden)
        for i in range(len(history)):
            print(str(i+1)+':', round(history[i], 1))
        print()
        print('Zwischenstand Runde', runden)
        print(name1+':', kontoSpieler1)  
        print(name2+':', kontoSpieler2)
        history.clear()
        runden = runden + 1
    
    #Schleife für gerade Runden (Spieler 2 fängt hier jeweils an)
    while runden == 2 or runden == 4 or runden == 6:
        bestandFlasche = round(1.0, 1)
        print()
        print('Runde', runden, '-', name2, 'fängt an.')
        while bestandFlasche > 0.0:
            a = trinkmengeSpieler2()
            history.append(a)
            bestandFlasche = round(bestandFlasche, 1) - round(a, 1)
            round(bestandFlasche, 1)
            if bestandFlasche == 0.0:
                print()
                print('Super gemacht,', name2, '- du bist genau bei Null gelandet!')
                kontoSpieler2 = kontoSpieler2 + 4
                kontoSpieler1 = kontoSpieler1 + 1
                break
            elif bestandFlasche < 0.0:
                print()
                print('Du bist unter Null und verlierst einen Punkt.')
                kontoSpieler2 = kontoSpieler2 - 1
                kontoSpieler1 = kontoSpieler1 + 1
                break
            b = trinkmengeSpieler1()
            history.append(b)
            bestandFlasche = round(bestandFlasche, 1) - round(b, 1)
            round(bestandFlasche, 1)
            if bestandFlasche == 0.0:
                print()
                print('Super gemacht,', name1, '- du bist genau bei Null gelandet!')
                kontoSpieler1 = kontoSpieler1 + 4
                kontoSpieler2 = kontoSpieler2 + 1
            elif bestandFlasche < 0.0:
                print()
                print('Du bist unter Null und verlierst einen Punkt.')
                kontoSpieler1 = kontoSpieler1 - 1
                kontoSpieler2 = kontoSpieler2 + 1
        print()
        print('Ablauf Runde', runden)
        for i in range(len(history)):
            print(str(i+1)+':', round(history[i], 1))
        print()
        print('Zwischenstand Runde', runden)
        print(name1+':', kontoSpieler1)  
        print(name2+':', kontoSpieler2)
        history.clear()
        runden = runden + 1

#Ausgabe wer gewonnen hat
print()
if kontoSpieler1 > kontoSpieler2:
    print(name1, 'hat gewonnen.')
elif kontoSpieler1 == kontoSpieler2:
    print('Ein astreines Unentschieden!')
else:
    print(name2, 'hat gewonnen.')

#Ausgabe Punkte-Endstand
print()
print('Endstand')
print(name1+':', kontoSpieler1)  
print(name2+':', kontoSpieler2)

input('Danke fürs Mitspielen!')