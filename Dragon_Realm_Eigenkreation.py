#Dragon_Realm_Eigenkreation

#import
import time
import random
random.seed()

#Variable
antwort = "Ja"

#Schleife
while antwort in ["Ja", "ja", "jA", "JA", "Jaa", "jaa", "Jja", "jja", "JJa", "j", "J"]:
    print("Du befindest dich in einem Land voller Drachen. \n"
          "Vor dir befinden sich zwei Höhlen. In der einen lauert ein hungriger Drachen, \n"
          "welcher dich Fressen will - in der anderen sitzt ein dir freundlich gesinnter Drachen, \n"
          "welcher seinen Schatz mit dir teilen will. In welche Höhle willst du gehen? (1 oder 2)")
    try:
        auswahl = int(input())
    except:
        print("Bitte gib eine ganze Zahl (1 oder 2) ein")
        time.sleep(3)
        print()
        continue

    #random Variable
    a = random.randint(1,2)

    if auswahl == a:
        print("Glückwunsch! Du hast dich für die Höhle des freundlichen Drachens entschieden und wirst ein reicher Mensch!")

    else:
        print("Du dringst in die Höhle ein. Es ist dunkel und riecht verfault. Da plötzlich \n"
              "stürzt sich ein Drache über dich und verschlingt dich in einem Bissen - Game Over")

    print()
    time.sleep(5)
    print("Nochmals spielen? (Ja oder Nein)")
    antwort = input()
    print()

input("Danke fürs Mitspielen")