# rot orange grün
# --> Nur für zwei Spieler geeignet
# --> Muss im Terminal oder bei VSC ausgeführt werden, damit es korrekt funktioniert

# Import "Input-Verdecker'
import getpass

# Spieler 1 gibt eine dreistellige Geheimzahl ein(funktioniert NICHT bei Idle!!!)
userInput = getpass.getpass(
    'Spieler 1 - Bitte eine dreistellige Geheimzahl eingeben: ')
zahl = str(userInput)
userZahl = [str(i) for i in zahl]

# Erklärung
print()
print('Spieler 2 - du musst die dreistellige Geheimzahl in max. 10 Versuchen erraten.')
print('"Rot" bedeutet: Falsche Zahl')
print('"Orange" bedeutet: Richtige Zahl, aber am falschen Ort')
print('"Grün" bedeutet: Richtige Zahl am richtigen Ort')
print()

# Schleife "Check Eingabe Spieler 2"
wiederholungen = 0
while wiederholungen < 10:

    eingabe1 = 'orange'
    eingabe2 = 'orange'
    eingabe3 = 'orange'

    # Eingabe Spieler 2
    print('Zahl eingeben')
    versuch = str(input())
    eingabe = [str(i) for i in versuch]

    # Check erste Zahl
    if eingabe[0] == userZahl[0]:
        print('grün')
        eingabe1 = 'grün'
    if eingabe1 != 'grün':
        if eingabe[0] == userZahl[1] or eingabe[0] == userZahl[2]:
            print('orange')
    if eingabe[0] not in userZahl:
        print('rot')

    # Check zweite Zahl
    if eingabe[1] == userZahl[1]:
        print('grün')
        eingabe2 = 'grün'
    if eingabe2 != 'grün':
        if eingabe[1] == userZahl[0] or eingabe[1] == userZahl[2]:
            print('orange')
    if eingabe[1] not in userZahl:
        print('rot')

    # Check dritte Zahl
    if eingabe[2] == userZahl[2]:
        print('grün')
        eingabe3 = 'grün'
    if eingabe3 != 'grün':
        if eingabe[2] == userZahl[0] or eingabe[2] == userZahl[1]:
            print('orange')
    if eingabe[2] not in userZahl:
        print('rot')
    wiederholungen += 1
    print()

    # Check ob alle Zahlen am richtigen Ort
    if eingabe[0] == userZahl[0] and eingabe[1] == userZahl[1] and eingabe[2] == userZahl[2]:
        break

# Ausgabe Spielende
if eingabe[0] == userZahl[0] and eingabe[1] == userZahl[1] and eingabe[2] == userZahl[2]:
    print('Bravo!!! Du hast die Geheimzahl in',
          wiederholungen, 'Versuchen herausgefunden!')
else:
    print('GAME OVER! Die zehn Versuche sind um - du konntest die Geheimzahl nicht knacken..')

print()
input('Danke fürs Mitspielen')