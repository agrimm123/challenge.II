import time
import openai
import configparser
from datetime import datetime
import os

# Funktion zum Erstellen einer neuen Chat-Datei
def create_chat_file():
    now = datetime.now()
    datei_name = now.strftime("%d%m%y-%H%M.txt")
    ordner = "chats"
    datei_pfad = os.path.join(ordner, datei_name)
    return datei_pfad

# Funktion zum Schreiben in die Chat-Datei
def write_ticket(datei_pfad, text):
    with open(datei_pfad, 'a') as datei:
        datei.write(text + "\n")


# Chatbot Funktion (Entwicklung in bot.py)
def bot():
    # Lade API-Schlüssel
    config = configparser.ConfigParser()
    config.read('config.ini')
    openai.api_key = config['DEFAULT']['API_KEY']

    # Erstelle eine neue Chat-Datei
    chat_file_path = create_chat_file()

    # Openai Integration
    def ask_openai(question):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": question},
            ]
        )
        return response.choices[0].message['content']

    # Funktion um eigene Frage an OpenAI zu stellen
    def openai_pr(inp):
        answer = ask_openai(
            "Ich habe eine Firma namens Bugland und die baut Reinigungsroboter und einen Gartenroboter. "
            "Du sollst so tun als wärst du der Supportchat von dem Unternehmen und Tipps geben. "
            "Sag bitte nicht, dass der Support kontaktiert werden soll oder das du bei weiteren " 
            "Fragen helfen kannst. Auch bitte nicht sagen, dass detailierte Informationen "
            "helfen. Also einfach nur die Antwort auf folgende Frage geben und bitte die einzelnen "
            "Punkte mit Gedankenstrichen klar trennen: " + inp
        )
        write_ticket(chat_file_path, f"Frage: {inp}")
        write_ticket(chat_file_path, f"Antwort: {answer}")
        print()
        print("Antwort:")
        print(answer)

    # Zusammenstellung der vorgegebenen Probleme und Lösungen
    def qs_1(problem_choice):
        i = 0
        while i < 4:
            i+=1
            if i == 1:
                print()
                print("Was für ein Problem hast du?")
                print("")
                print("Bitte wähle aus folgenden aus:")
                print("1. Konfiguration")
                print("2. Defekt")
                print("3. Fehlermeldung")
                print("4. Fehlverhalten des Roboters")
                print("5. Sonstiges")
            elif i == 2 or i == 3:
                print()
                print("Hast du ein weiteres Problem? Wenn ja, bitte wähle aus folgenden aus:")
                print("")
                print("Bitte wähle aus folgenden aus:")
                print("1. Konfiguration")
                print("2. Defekt")
                print("3. Fehlermeldung")
                print("4. Fehlverhalten des Roboters")
                print("5. Sonstiges")
            else:
                print("")
                print("Tut mir leid, ich denke ich kann dir bei deinem Problem nicht weiterhelfen. Bitte kontaktiere den Support unter folgender Telefonnummer oder E-Mail.")
                print("Telefonnummer: 0123456789")
                print("E-Mail: supp.bt@bugland.de")
                time.sleep(5)
                break
            
            print("Bitte gib die Nummer deines Problemes an: ")
            problem_choice = input()
            write_ticket(chat_file_path, f"Problemwahl: {problem_choice}")
            while not (problem_choice == "1" or problem_choice == "2" or problem_choice == "3" or problem_choice == "4" or problem_choice == "5"
                       or problem_choice == "1." or problem_choice == "2." or problem_choice == "3." or problem_choice == "4." or problem_choice == "5." 
                       or problem_choice.lower() == "konfiguration" or problem_choice.lower() == "defekt" or problem_choice.lower() == "fehlermeldung" 
                       or problem_choice.lower() == "fehlverhalten des roboters" or problem_choice.lower() == "sonstiges"
                       or problem_choice.lower() == "exit" ):
                print()
                print("Ungültige Eingabe. Überprüfe auch auf Rechtschreibung!")
                print()
                print("Bitte gib die Nummer deines Problemes an: ")
                problem_choice = input()
                write_ticket(chat_file_path, f"Problemwahl (ungültig): {problem_choice}")

            if problem_choice == "1" or problem_choice == "1." or problem_choice.lower() == "konfiguration":
                openai_pr("Mein Roboter hat ein Konfigurationsproblem. Was soll ich nun machen?")
            elif problem_choice == "2" or problem_choice == "2." or problem_choice.lower() == "defekt":
                openai_pr("Ich glaub mein Roboter ist defekt. Was soll ich nun machen?")
            elif problem_choice == "3" or problem_choice == "3." or problem_choice.lower() == "fehlermeldung":
                openai_pr("Ich habe einen Roboter und er zeigt eine Fehlermeldung an. Was soll ich nun machen?")
            elif problem_choice == "4" or problem_choice == "4." or problem_choice.lower() == "fehlverhalten des roboters":
                openai_pr("Der Roboter funktioniert nicht so wie er soll. Was soll ich nun machen?")
                print("Alternativ kontaktiere den Support unter folgender Telefonnummer oder E-Mail.")
                print("Telefonnummer: 0123456789")
                print("E-Mail: supp.bt@bugland.de")
                time.sleep(5)
            elif problem_choice == "5" or problem_choice == "5." or problem_choice.lower() == "sonstiges":
                print()
                print("Bitte schildere dein Problem: ")
                problem_choice = input()
                openai_pr(problem_choice)
                write_ticket(chat_file_path, f"Sonstiges Problem: {problem_choice}")
            elif problem_choice.lower() == "exit":
                break
            else:
                print("Ungültige Eingabe")
            time.sleep(5)
   
    # Chatstart 
    print("Um welches BUGLAND Produkt handelt es sich?")
    print()
    print("Bitte wähle aus folgenden aus:")
    print("1. CleanBug")
    print("2. WindowFly")
    print("3. GardenBeetle")
    pr_1 = input()

    write_ticket(chat_file_path, f"Produktwahl: {pr_1}")

    # Wenn ungültige Eingabe, dann erneut fragen
    while not (pr_1.lower() == "cleanbug" or pr_1.lower() == "windowfly" or pr_1.lower() == "gardenbeetle"
               or pr_1 == "1" or pr_1 == "2" or pr_1 == "3"
               or pr_1 == "1." or pr_1 == "2." or pr_1 == "3."
               or pr_1.lower() == "exit"):
        print()
        print("Ungültige Eingabe, bitte achte auf Rechtschreibung! Alternativ zum Abbrechen 'Exit' eingeben")
        print()
        print("Bitte gib dein Produkt ein: ")
        pr_1 = input()
        write_ticket(chat_file_path, f"Produktwahl (ungültig): {pr_1}")

    # Chat findet solange statt, bis Nutzer 'exit' eingibt
    while pr_1.lower() != "exit":

        if pr_1.lower() == "cleanbug" or pr_1 == "1" or pr_1 == "1.":
            qs_1(pr_1)
            break  
        elif pr_1.lower() == "windowfly" or pr_1 == "2" or pr_1 == "2.":
            qs_1(pr_1)
            break    
        elif pr_1.lower() == "gardenbeetle" or pr_1 == "3" or pr_1 == "3.":
            qs_1(pr_1)
            break    
        else:
            print("Bitte gib deine Eingabe ein:")
            pr_1 = input()
            write_ticket(chat_file_path, f"Frage: {pr_1}")

    # Chat beenden - wird immer ausgegeben wenn 'Exit' eingegeben wird
    print()
    print("Ich hoffe ich konnte weiterhelfen.")    
    print("Vielen Dank für die Nutzung unseres Chats!")
    write_ticket(chat_file_path, "Chat beendet.")

'''
Gebe Begrüßung aus
Pausiere
Frag nach der Art des Kunden (Privat oder Geschäftlich)
Warte auf Eingabe

Wenn Privatkunde oder Geschäftskunde oder Verlassen eingegeben wird, wird der Code weitergeführt, wenn nicht mache folgendes:
    Gebe aus, dass die Eingabe ungültig ist und frage erneut nach der Art des Kunden
    Warte auf Eingabe

Wenn Privatkunde eingegeben wird
    Gebe "Vielen Dank!" aus
    Rufe die Funktion bot() auf
Wenn Geschäftskunde eingegeben wird
    Gebe "Vielen Dank für deine Eingabe!" aus
    Pausiere
    Gebe "Du hast als Geschäftskunde einen persönlichen Ansprechpartner." aus
    Gebe "Natürlich kannst du auch den Chatbot verwenden." aus
    Frage ob der Geschäftskunde den Chatbot dennoch verwenden möchte und warte auf Eingabe

        Wenn Ja oder Nein oder Verlassen eingegeben wird, wird der Code weitergeführt, wenn nicht mache folgendes:
            Gebe aus, dass die Eingabe ungültig ist und frage erneut nach
            Warte auf Eingabe

        Wenn Ja eingegeben wird
            Gebe "Vielen Dank!" aus
            Rufe die Funktion bot() auf
        Sonst
            Gebe "Vielen Dank für die Nutzung unseres Chats!" aus

Sonst
    Gebe "Vielen Dank für die Nutzung unseres Chats!" aus
'''

# Hauptprogramm
# Begrüße Nutzer und frage ob Privatkunde oder Geschäftskunde
print("Herzlich Willkommen beim BUGLAND Supportchatbot!")
time.sleep(0.75)
print()
print("Bist du ein Privatkunde oder ein Geschäftskunde?")
print("Bitte gib 'Privat' oder 'Gewerbe' ein: ")
kd_typ = input()

# Wenn nur wenn Privatkunde oder Geschäftskunde eingegeben wird, wird weitergefragt, alternativ verlassen oder nachfragen
while not (kd_typ.lower() == "privat" or kd_typ.lower() == "gewerbe" or kd_typ.lower() == "exit"):
    print()
    print("Ungültige Eingabe, bitte achte auf Rechtschreibung!")
    print()
    print("Bitte gib 'Privat' oder 'Gewerbe' ein: ")
    kd_typ = input()

# Wenn gültige Antwort gegeben wurde
if kd_typ.lower() == "privat":
        print()
        print("Vielen Dank!")
        bot() # Chatbot wird aufgerufen
elif kd_typ.lower() == "gewerbe":
        print()
        print("Vielen Dank für deine Eingabe!")
        time.sleep(1)
        print("Du hast als Geschäftskunde einen persönlichen Ansprechpartner.")
        print()
        print("Natürlich kannst du auch den Chatbot verwenden.")
        print("Möchtest du dennoch den Chatbot verwenden? (Ja/Nein/Exit)")
        kd_gk = input()

    # Solange keine gültige Antwort gegeben wird, wird nachgefragt
        while not (kd_gk.lower() == "ja" or kd_gk.lower() == "nein" or kd_gk.lower() == "exit"):
            print()
            print("Ungültige Eingabe, bitte achte auf Rechtschreibung!")
            print()
            print("Bitte gib 'Ja', 'Nein' oder 'Exit' ein: ")
            kd_gk = input()

    # Gültiger Wert wurde eingegeben
        if kd_gk.lower() == "ja":
            print()
            print("Vielen Dank!")
            bot() # Chatbot wird aufgerufen
        else:
            print()
            print("Vielen Dank für die Nutzung unseres Chats!")

else:
    print()
    print("Vielen Dank für die Nutzung unseres Chats!")