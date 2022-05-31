#Kopf oder Zahl

#Einführungstext
print("Die Münze wird 1000x geworfen und wir werden herausfinden ob Kopf oder Zahl mehr "
      "Landungen hat. Wir wiederholen das Ganze 5x um sicher zu stellen, dass es sich um "
      "Zufälle handelt. Wer gewinnt: Kopf oder Zahl? Rate mit!")

#Importe
import random
import time

#Variablen
kopf = 0
zahl = 0
wuerfe = 0
wiederholungen = 0

#Schleife
while wiederholungen <5:
    print("Los geht's...")
    time.sleep(1)
    for wuerfe in range(1001):
        zufall = random.randint(1,2)
        
        if wuerfe == 500:
            if kopf > zahl:
                print("Wir sind in der Hälfte und Kopf steht mit", kopf, "Landungen in Führung")
                input()
            elif kopf == zahl:
                print("Wir sind in der Hälfte. Es ist ein Kopf an Kopf Rennen - oder in diesem Fall ein Kopf an Zahl Rennen. Es steht nämlich unentschieden!")
                input()
            else:
                print("Wir sind in der Hälfte und Zahl steht mit", zahl, "Landungen in Führung")
                input()

        elif zufall == 1:
            kopf = kopf + 1
        elif zufall == 2:
            zahl = zahl + 1

    wiederholungen = wiederholungen + 1
    time.sleep(0.5)

    #Ausgabe
    print("Von 1000 Würfen gab es folgende Verteilung:")
    print("Kopf =", kopf)
    print("Zahl =", zahl)
    
    if kopf > zahl:
        print("Kopf hat mit", kopf, "Landungen gewonnen")
    elif kopf == zahl:
        print("Ein astreines Unentschieden!")
    else:
        print("Zahl hat mit", zahl, "Landungen gewonnen")
        
    input()
    print()
    
    kopf = 0
    zahl = 0

#Schlusstext
input("Das war interessant - Danke fürs Mitmachen")
