#Geografiespiel mit einem Dictionary

hauptstadt = {'Italien':'Rom', 'Spanien':'Madrid',
              'Portugal':'Lissabon', 'der Schweiz':'Bern'}
hs = hauptstadt.items()

for land, stadt in hs:
    eingabe = input('Bitte die Hauptstadt von ' + land + ' eingeben: ')
    if eingabe == stadt:
        print('Richtig')
    else:
        print('Falsch - richtig wäre:', stadt)

input('Danke fürs Mitspielen')