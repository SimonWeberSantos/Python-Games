# Wortfinder - Ein Spieler gibt ein Wort ein - der nächste Spieler muss ein Wort eingeben, 
# bei dem der erste und letzte Buchstabe des vorherigen Wortes drin vorkommt. Das Wort darf noch nicht benutzt worden sein.

import time

#Liste der bereits verwendeten Wörter
benutzteWorte = []

# Starteingabe des Spiels
print('Bitte ein Wort IN KLEINBUCHSTABEN eingeben:')
wortvorgabe = input()
benutzteWorte.append(wortvorgabe)

# Herausfiltern des ersten Buchstabens
def filternA():
    listA = []
    for i in wortvorgabe:
        listA.append(i)
    a = (listA[0])
    return a

# Herausfiltern des letzten Buchstabens
def filternZ():
    listZ = []
    for i in wortvorgabe:
        listZ.append(i)
    listZ.reverse()
    z = (listZ[0])
    return z

# Eingabe und Check, ob das Wort richtig war und noch nicht benutzt wurde
wiederholung = 'ja'
wortfinder = True
while wiederholung in ['Ja', 'ja', 'J', 'j', 'JA', 'jA']:
    while wortfinder == True:
        neuesWort = []
        print()
        print('Bitte neues Wort IN KLEINBUCHSTABEN eingeben:')
        eingabe = input()
        for i in eingabe:
            neuesWort.append(i)
        anfangsbuchstabe = filternA()
        schlussbuchstabe = filternZ()
        if anfangsbuchstabe in neuesWort and schlussbuchstabe in neuesWort and eingabe not in benutzteWorte:
            print('Sehr gut gemacht - weiter gehts.')
            time.sleep(1)
            benutzteWorte.append(eingabe)
            wortvorgabe = eingabe
        elif eingabe in benutzteWorte:
            print('Bereits benutztes Wort eingegeben - GAME OVER')
            time.sleep(1)
            wortfinder = False        
        else:
            print('Falsches Wort eingegeben - GAME OVER')
            time.sleep(1)
            wortfinder = False
    
    #Schleife 'Spiel nochmals spielen'
    print('Nochmals spielen? (Ja / Nein)')
    antwort = input()
    if antwort not in ['Ja', 'ja', 'J', 'j', 'JA', 'jA']:
        break
    else:
        benutzteWorte.clear()
        wortfinder = True
        print('Bitte ein Wort IN KLEINBUCHSTABEN eingeben:')
        wortvorgabe = input()
        benutzteWorte.append(wortvorgabe)

input('Danke fürs Mitspielen!')