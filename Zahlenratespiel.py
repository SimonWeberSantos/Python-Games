#Zahlenratespiel

#Import
import random
import time

#Variablen
versuche = 0
print('Wie heisst du?')
name = input()
zahl = random.randint(1,20)

#Einstieg
print('Ok ' + name + ', ich denke mir eine Zahl zwischen 1 und 20 aus und du musst erraten welche.')
time.sleep(3)
print('Du hast 6 Versuche dazu - viel Spass')
time.sleep(2)

#Schleife
for versuche in range(6):
    print('Bitte gib eine Zahl zwischen 1 und 20 ein:')
    eingabe = int(input())

    if eingabe > zahl:
        print('Du hast zu hoch geraten..')
        time.sleep(1)

    elif eingabe < zahl:
        print('Du hast zu tief geraten..')
        time.sleep(1)

    else:
        break

versuche = versuche + 1

if eingabe == zahl:
    print('Bingo ' + name + '!! Du hast es insgesamt ' + str(versuche) + 'x versucht.')

else:
    print('Du Pfeiffe!! Meine ausgedachte Zahl wäre ' + str(zahl) + ' gewesen...')

input('Danke fürs Mitspielen')