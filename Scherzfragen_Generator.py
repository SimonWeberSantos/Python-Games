#Scherzfragen_Generator

#Import
import time

#Variable
wiederholung = 1

#Schleife mit Scherzfragen
while wiederholung <11:
    print("Möchtest du eine Scherzfrage hören? Bitte mit Ja/Nein beantworten")
    antwort = input()
    if antwort in ["Ja", "JA", "jA", "ja", "Yes", "Ok", "ok", "OK", "jawohl"]:
        if wiederholung == 1:
            print("Wie heisst die Farbe welche für das Färben von Fussbällen verwendet wird?")
            input()
            print('"Ballack"')
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 2:
            print("Was machen Mathematiker im Garten?")
            input()
            print("Wurzeln ziehen")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 3:
            print("Warum können Bienen so gut rechnen?")
            input()
            print("Weil sie sich den ganzen Tag mit Summen beschäftigen.")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 4:
            print("Wenn ein Yogalehrer seine Beine senkrecht nach oben streckt und dabei furzt, welche Yoga Figur stellt er dar?")
            input()
            print("Die Duftkerze!")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 5:
            print("Welcher Wein wird an den Hängen eines Vulkanes angebaut?")
            input()
            print("Der Glühwein")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 6:
            print("Was macht Robin Hood mit gestohlenen Deo-Rollern?")
            input()
            print("Er verteilt sie unter den Armen.")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 7:
            print("Warum erhalten Polizisten in Zukunft eine große Schere für Ihre Polizeiausrüstung?")
            input()
            print("Damit sie den Bösewichten den Weg abschneiden können.")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 8:
            print("Was ist grün und tut im Gesicht weh?")
            input()
            print("Ein Billardtisch")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 9:
            print("Was ist ein Cowboy, dem das Pferd weggerannt ist?")
            input()
            print("Ein Sattelschlepper!")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1
        elif wiederholung == 10:
            print("Letzte Scherzfrage: Einige Monate haben 30 Tage andere haben 31 Tage. Doch wie viel Monate haben 28 Tage?")
            input()
            print("Alle")
            print()
            time.sleep(2)
            wiederholung = wiederholung + 1

    else:
       break 

print("Besten Dank fürs Mitlachen")
input()