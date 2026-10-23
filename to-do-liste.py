#=== Mein To-do-Manager ===

#--1. Aufgabe hinzufügen --
#--2. Aufgaben anzeigen --
#--3. Aufgabe löschen --
#--4. Programm beenden --
#--Bitte wähle eine Option:--

aufgaben = [] # Aufgabenliste

# --Aufgabe zu einer Liste hinzufügen
def hinzufügen():
    abfrage = True
    while abfrage == True:
        print("Welche Aufgabe möchtest du hinzufügen?")
        print(" -Gebe 'Fertig' ein, um zum Menü zurückzukehren-")
        eingabe = input("Aufgabe: ").capitalize()

        if eingabe == "Fertig": # --Ausstieg aus der schleife
            print("Danke!")
            abfrage = False
            print("-" * 15)
        elif eingabe == "": # -- Verhindert leere Eingaben
            print("Bitte Aufgabe hinzufügen")
            print("-" * 15)
        elif eingabe in aufgaben: # --Überschreibt doppelte Aufgabe
            print("Aufgabe bereits vorhanden")
            print("-" * 15)
        else:
            aufgaben.append(eingabe)
            print("Aufgabe wurde hinzugefügt!")
            print("-" * 15)

# --Aufgabenliste anzeigen lassen
def anzeigen():
    print("-" * 15)
    print("To-Do:")

    if aufgaben == []:
        print("Noch keine Aufgabe hinzugefügt")

    for a in aufgaben:
        print(a)

    print("-" * 15)

# --Aufgabe aus Liste löschen
def löschen():
    abfrage = True
    while abfrage == True:

        print("Welche Aufgabe möchtest du löschen?")
        print(" -Gebe 'Fertig' ein, um zum Menü zurückzukehren-")
        eingabe = input("Aufgabe löschen: ").capitalize()

        if eingabe == "Fertig": # --Ausstieg aus der Schleife
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

# --main-funktion
def main():
    programm_läuft = True
    print("Hallo!")
    print("-" * 15)

    while programm_läuft == True:
        option = ["1. Aufgabe hinzufügen", "2. Aufgaben anzeigen", "3. Aufgabe löschen", "4. Programm beenden"]
        print("Was möchtest du tun?")
        for o in option:
            print(o)

        print("-"*15)

        wählen = input("Bitte wähle eine Option: ")

        if wählen == "1": # --Hinzufügen
            hinzufügen()
        elif wählen == "2": # --Anzeigen
            anzeigen()
        elif wählen == "3": # --Löschen
            löschen()
        elif wählen == "4": #--Ausstieg aus der schleife
            programm_läuft = False
            print("Die liste wird geschlossen. Bis bald!")
        else:
            print("Keine gültige eingabe. Bitte versuche es erneut!")
            print("-" * 15)

print("-" * 15)

# --Programm starten
if __name__ == "__main__":
    main()

