#=== Mein To-do-Manager ===

#--1. Aufgabe hinzufügen --
#--2. Aufgaben anzeigen" --
#--3. Aufgabe löschen --
#--4. Programm beenden --
#--Bitte wähle eine Option:--

aufgaben = [] # AUfgabenliste

# Aufgabe zu einer Liste hinzufügen
def hinzufügen():
    abfrage = True
    while abfrage == True:
        print("Welche Aufgabe möchtest du hinzufügen?")
        print("Gebe 'Fertig' ein, um zum Menü zurückzukehren")
        eingabe = input("Aufgabe: ")

        if eingabe == "Fertig": #--Austieg aus der schleife
            print("Danke!")
            abfrage = False
            print("-" * 15)
        else:
            aufgaben.append(eingabe)
            print("Aufgabe wurde hinzugefügt!")
            print("-" * 15)

def anzeigen():
    for a in aufgaben:
        print(a)

    print("-" * 15)

# Aufgabe aus Liste löschen
def löschen():
    abfrage = True
    while abfrage == True:

        print("Welche Aufgabe möchtest du löschen?")
        print(" Gebe 'Fertig' ein, um zum Menü zurückzukehren")
        eingabe = input("Aufgabe löschen: : ")

        if eingabe == "Fertig":
            print("Danke!")
            abfrage = False
            print("-" * 15)
        elif eingabe not in aufgaben:
            print("Aufgabe nicht vorhanden. Bitte überprüfe deine Eingabe!")
            print("-" * 15)
        else:
            aufgaben.remove(eingabe)
            print("Aufgabe wurde gelöscht!")
            print("-" * 15)

# main-funktion
def main():
    main = True
    while main == True:
        option = ["1. Aufgabe hinzufügen", "2. Aufgaben anzeigen", "3. Aufgabe löschen", "4. Programm beenden"]
        for o in option:
            print(o)

        print("-"*15)

        wählen = input("Bitte wähle eine Option: ")

        if wählen == "1":
            hinzufügen()
        elif wählen == "2":
            anzeigen()
        elif wählen == "3":
            löschen()
        elif wählen == "4": #--Austieg aus der schleife
            main = False
            print("Die liste wird geschlossen. Bis bald!")
        else:
            print("Keine gültige eingabe. Bitte versuche es erneut!")

print("-" * 15)

#Programm starten
if __name__ == "__main__":
    main()

