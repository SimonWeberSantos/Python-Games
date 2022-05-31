#Container verladen

#Importe
import time
import random
random.seed()

#Funktionen
def gameOver():
    print("Du Süsswassermatrose hast das Schiff überfüllt (",containerAktuell,"Container) - Es sinkt!!!")
    print("GAME OVER") 

def schiffUeberladen():
    if containerAktuell > 24:
        gameOver()
        gameIsOver = 1
        return gameIsOver

#Auszeichnung
auszeichnung = ["ADMIRAL", "KAPITÄN", "VERLADESPEZIALIST:IN", "LOGISTIKCHEF:IN", 
                "MATROSE ERSTEN GRADES", "MÖCHTEGERNKRANFÜHRER:IN", "HOBBYMATHEMATIKER",
                "ZAHLENANALPHABET:IN", "BETRUNKENER PIRAT", "AKTUELL ARBEITSLOS"]

#Variablen
wiederholung = "Ja"

#Schleife über alles falls das Spiel wiederholt werden soll
while wiederholung in ["Ja", "JA", "ja", "j", "J"]:
    gameIsOver = False
    while gameIsOver == False:
        #Einführungstext
        print("Es ist ein neuer Auftrag reingekommen...")
        time.sleep(2)

        print("""Wir müssen ein Containerschiff so komplett wie nur möglich verladen.
Es hat Platz für 24 Container. Das Schiff kommt mit bereits 1-4 Containern
bei 'Station A' an. Hier bei 'Station A' haben wir Zugriff und können das Schiff
zusätzlich mit beliebig vielen Containern beladen. Bei 'Station B' wird
das Schiff automatisch mit 1-10 Containern aufgestockt. Die ungefähre Menge
wird uns mitgeteilt. Danach fährt es zur 'Station C' wo wir wieder Zugriff haben
und entweder Container be- oder entladen können. Zum Schluss fährt das Schiff zur
'Station D' wo es wieder mit 1-4 Containern automatisch beladen wird.
Wenn alles klar ist, bitte Enter drücken""")
        input()
        
        print("Pass auf, dass du das Schiff nicht überlädst!!!")
        print()
        time.sleep(3)



        # --- Station A ---

        #Zufällige Anzahl Container bereits vorgeladen
        vorgeladen = random.randint(1,4)
        
        #Anzeige wie viele Container vorgeladen sind
        print("Das Schiff fährt bei 'Station A' ein...")
        time.sleep(2)
        if vorgeladen < 3:
            print("...Es hat bereits einen oder zwei Container geladen.")
            time.sleep(2)
        else:
            print("...Es hat bereits drei oder vier Container geladen.")
            time.sleep(2)
        print("Wie viele Container möchtst du dazuladen?")

        #Schleife Eingabe
        containerA = False
        while containerA == False:
            try:
                containerA = int(input())
            except:
                print("Bitte gib eine ganze Zahl ein:")
                containerA = False
                
        #Ausrechnung akutelle Anzahl Container auf dem Schiff
        containerAktuell = containerA + vorgeladen

        #Check, dass Schiff nicht überladen ist.
        gameIsOver = schiffUeberladen()
        if gameIsOver == 1:
            break



        # --- Station B ---

        #Zufällige Anzahl Container welche geladen werden
        containerB = random.randint(1,10)

        #Anzeige wie viele Container geladen wurden
        time.sleep(1)
        print("Das Schiff fährt bei 'Station B' ein...")
        time.sleep(1)
        if containerB < 6:
            print("...Es hat zwischen 1 - 5 Container geladen.")
            time.sleep(1)
        else:
            print("...Es hat zwischen 6 - 10 Container geladen.")
            time.sleep(1)
        #Ausrechnung akutelle Anzahl Container auf dem Schiff
        containerAktuell = containerB + containerAktuell

        #Check, dass Schiff nicht überladen ist.
        gameIsOver = schiffUeberladen()
        if gameIsOver == 1:
            break



        # --- Station C ---

        #Zufällige Anzahl Container die bei Station D geladen werden
        containerD = random.randint(1,4)
        
        #Anzeige wie viele Container geladen werden
        print()
        print()
        time.sleep(3)
        print("Das Schiff ist nun bei 'Station C' angekommen.")
        time.sleep(1)
        print("Hier kannst du entweder Container aufladen oder abladen...")
        time.sleep(1)
        print()
        if containerD < 3:
            print("...Bedenke aber, dass bei 'Station D' ein oder zwei Container noch dazugeladen werden!")
            time.sleep(1)
        else:
            print("...Bedenke aber, dass bei 'Station D' zwei oder drei Container noch dazugeladen werden!")
            time.sleep(1)
        print("Wähle:")
        print("1 = Container aufladen")
        print("2 = Container abladen")

        #Eingabe Entscheid ob Auf- oder Abladen
        entscheid = 0
        while entscheid < 1 or entscheid > 2:
            try:
                entscheid = int(input())
                if entscheid < 1 or entscheid > 2:
                    print("Bitte gib eine 1 oder 2 ein:")
            except:
                print("Bitte gib eine 1 oder 2 ein:")
                
                
        #Eingabe wie viele Container aufgeladen werden sollen       
        if entscheid == 1:
            print("Wie viele Container möchtest du dazu laden?")
            containerAufladenC = False
            while containerAufladenC == False:
                try:
                    containerAufladenC = int(input())
                except:
                    print("Bitte gib eine ganze Zahl ein:")
                    containerAufladenC = False
        #Ausrechnung akutelle Anzahl Container auf dem Schiff
            containerAktuell = containerAktuell + containerAufladenC

        #Eingabe wie viele Container abgeladen werden sollen
        else:
            print("Wie viele Container möchtest du gerne abladen?")
            containerAbladenC = False
            while containerAbladenC == False:
                try:
                    containerAbladenC = int(input())
                except:
                    print("Bitte gib eine ganze Zahl:")
                    containerAbladenC = False
        #Ausrechnung akutelle Anzahl Container auf dem Schiff
            containerAktuell = containerAktuell - containerAbladenC

        #Check, dass Schiff nicht überladen ist.
        gameIsOver= schiffUeberladen()
        if gameIsOver == 1:
            break



        # --- Station D ----

        containerAktuell = containerAktuell + containerD

        #Check, dass Schiff nicht überladen ist.
        gameIsOver = schiffUeberladen()
        if gameIsOver == 1:
            break

        #Auszeichnung
        time.sleep(1)
        print("Du hast", containerAktuell,"Container geladen und folgenden Status erreicht:")
        if containerAktuell == 24:
            print()
            print("---", auszeichnung[0],"---")
            print()
        elif containerAktuell == 23:
            print()
            print("---", auszeichnung[1],"---")
            print()
        elif containerAktuell == 22:
            print()
            print("---", auszeichnung[2],"---")
            print()
        elif containerAktuell == 21:
            print()
            print("---", auszeichnung[3],"---")
            print()
        elif containerAktuell == 20:
            print()
            print("---", auszeichnung[4],"---")
            print()
        elif containerAktuell == 19:
            print()
            print("---", auszeichnung[5],"---")
            print()
        elif containerAktuell == 18:
            print()
            print("---", auszeichnung[6],"---")
            print()
        elif containerAktuell == 17:
            print()
            print("---", auszeichnung[7],"---")
            print()
        elif containerAktuell == 16:
            print()
            print("---", auszeichnung[8],"---")
            print()
        elif containerAktuell < 16:
            print()
            print("---", auszeichnung[9],"---")
            print()
        time.sleep(3)

    #Wiederholung abfragen
    print("Willst du nochmals spielen? (Ja / Nein)")
    wiederholung = input()

    if wiederholung not in ["Ja", "JA", "ja", "j", "J"]:
        break
    else:
        continue

input("Danke fürs Mitspielen")