import sys
import Core
import os


# Gebruik deze functie om het ingegeven nummer omtezetten in de juiste extensie.
class Numcheck:
    def picture(number):
        # Lijst met ondersteunde extensies maar 0 geen waarden geven.
        extensies = [None, "jpeg", "png", "jpg", "gif", "heic", "webp", "bmp", "tiff", "ico"]
        return extensies[number] # type: ignore

    def video(number):
        extensies = [None, "mp4", "m4v", "ogv", "webm", "gif", "avi", "mp3", "wmv", "mov", "ts"]
        return extensies[number] # type: ignore

    def audio(number):
        extensies = [None, "mp3", "m4a", "ogg", "wav", "m4p", "raw", "webm", "wmv", "cda"]
        return extensies[number] # type: ignore


def getfilenames():
    print("How do you wanna select files?")
    print("""
+---------------------------------------------------------------------+
| 1) Take all files in the current folder                             |
+---------------------------------------------------------------------+
| 2) I will give the filenames myself                                 |
+---------------------------------------------------------------------+
    """)
    # Vragen welke selectie methoden ze willen gebruiken.
    while True:
        val = input("Enter: exit to quit | Number:").strip()
        if val.isnumeric():
            keuze_bestandsmethode = int(val)
            if 3 > keuze_bestandsmethode > 0:
                break
            else:
                print("That's not a valid option number.")
        elif val == "exit":
            exit()
        else:
            print("Whoops that's not a number!")
            

    if keuze_bestandsmethode == 1:
        # Alle bestanden toevoegen aan de lijst van de map waar script nu instaat.
        lijst_bestanden = os.listdir(os.getcwd())
        return lijst_bestanden
    elif keuze_bestandsmethode == 2:
        print("Enter a relative path to this exe file.")
        print("Alternatively, you can enter the full path like C:/Users/test/Images/1.png")
        while True:
            # Lijst maken
            lijst_bestanden = []
            # Gebruiker laten toevoegen
            lijst_bestanden += [input("Name/path?:")]
            nog = input("Do you have another file to convert Y/N?:")
            if nog == "N" or "n":
                break
            else:
                continue
        return lijst_bestanden


# Printing ASCII graphics.
# Greetings

print(r"""
 __    __            __         ______                                                      __     
|  \  |  \          |  \       /      \                                                    |  \    
| $$  | $$ _______   \$$      |  $$$$$$\  ______   _______  __     __   ______    ______  _| $$_   
| $$  | $$|       \ |  \      | $$   \$$ /      \ |       \|  \   /  \ /      \  /      \|   $$ \  
| $$  | $$| $$$$$$$\| $$      | $$      |  $$$$$$\| $$$$$$$\\$$\ /  $$|  $$$$$$\|  $$$$$$ $$$$$$  
| $$  | $$| $$  | $$| $$      | $$   __ | $$  | $$| $$  | $$ \$$\  $$ | $$    $$| $$   \$$ | $$ __ 
| $$__/ $$| $$  | $$| $$      | $$__/  \| $$__/ $$| $$  | $$  \$$ $$  | $$$$$$$$| $$       | $$|  
 \$$    $$| $$  | $$| $$       \$$    $$ \$$    $$| $$  | $$   \$$$    \$$     \| $$        \$$  $$
  \$$$$$$  \$$   \$$ \$$        \$$$$$$   \$$$$$$  \$$   \$$    \$      \$$$$$$$ \$$         \$$$$ 

+-+-+-+-+-+-+-+-+-+-+- +-+ +-+-+-+-+-+-+-+-+-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|K|o|b|e|M|o|t|m|a|n|s |&| |Z|a|n|d|e|r|C|e|u|n|e|n| |&| |t|h|e|b|l|a|c|k|s|w|i|t|c|h|
+-+-+-+-+-+-+-+-+-+-+- +-+ +-+-+-+-+-+-+-+-+-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Look at https://github.com/ZanderCeunen/file-converter for more information.
""")

print("""What file type to you want to convert?
+----------+----------+-----------+
| 1 Video  |  2 Audio |  3 Foto's |
+----------+----------+-----------+""")
# Welke converter moet worden gebruikt.
while True:
    val = input("Enter: exit to quit | Number:").strip()
    if val.isnumeric():
        soort_bestand = int(val)

        if 5 > soort_bestand > 0:
            break
        else:
            print("That's not a valid file type number. Please try again.")

    elif val == "exit":
        exit()
    
    else:
        print("Whoops that's not a number!")


if soort_bestand == 1:
    # Als foto geef de ondersteunde extensies
    print("""
+-------+--------+--------+--------+
| 1 mp4 | 4 webm | 7 mp3  | 10 ts |
| 2 m4v | 5 gif  | 8 wmv  |       |
| 3 ogv | 6 avi  | 9 mov  |       |
+-------+--------+--------+--------+""")
    while True:  # Zet nummer om in extensie voor de input bestanden.
        val = input("Enter: exit to quit | Which extension has the input file? Number:").strip()
        if val.isnumeric():
            gekozen_input_formaat_nummer = int(val)
            if 10 > gekozen_input_formaat_nummer > 0:
                break
            else:
                print("This is not a valid extension number. Please try again.")
        elif val == "exit":
            exit()
        else:
            print("Whoops that's not a number!")
    gekozen_input_formaat_extensie = Numcheck.video(gekozen_input_formaat_nummer) # type: ignore

    while True:
        val = input("Enter: exit to quit | To which extension do you want to convert the file(s)? Number?:").strip()
        if val.isnumeric():
            gekozen_output_formaat_nummer = int(val)
            if 10 > gekozen_output_formaat_nummer > 0:
                break
            else:
                print("This is not a valid extension number. Please try again.")
        elif val == "exit":
            exit()
        else:
            print("Whoops that's not a number!")
    # Zet het nummer om in een extensie.
    gekozen_output_formaat_extensie = Numcheck.video(gekozen_output_formaat_nummer) # type: ignore
    # Vraag de lijst met bestanden op.
    bestanden = getfilenames()
    # Voor elk bestand in de lijst bijhorende Core converter uitvoeren.
    for filename in bestanden: # type: ignore
        Core.video_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)
elif soort_bestand == 2:
    # Als foto geef de ondersteunde extensies
    print("""
+-------+-------+--------+
| 1 mp3 | 4 wav | 7 webm |
| 2 m4a | 5 m4p | 8 msv  |
| 3 ogg | 6 raw | 9 cda  |
+-------+-------+--------+
""")
    while True:  # Zet nummer om in extensie voor de input bestanden.
        val = input("Enter: exit to quit | Which extension has the input file? Number:")
        if val.isnumeric():
            gekozen_input_formaat_nummer = int(val)
            if 10 > gekozen_input_formaat_nummer > 0:
                break
            else:
                print("This is not a valid extension number. Please try again.")
        elif val == "exit":
            exit()
        else:
            print("Whoops that's not a number!")
    gekozen_input_formaat_extensie = Numcheck.audio(gekozen_input_formaat_nummer) # type: ignore

    while True:
        val = input("Enter: exit to quit | Wich extension needs the output file? Number?:")
        if val.isnumeric():
            gekozen_output_formaat_nummer = int(val)
            if 10 > gekozen_output_formaat_nummer > 0:
                break
            else:
                print("This is not a valid extension number. Please try again.")
        elif val == "exit":
            exit()
        else:
            print("Whoops that's not a number")
    # Zet het nummer om in een extensie.
    gekozen_output_formaat_extensie = Numcheck.audio(gekozen_output_formaat_nummer) # type: ignore
    # Vraag de lijst met bestanden op.
    bestanden = getfilenames()
    # Voor elk bestand in de lijst bijhorende Core converter uitvoeren.
    for filename in bestanden: # type: ignore
        Core.audio_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)
elif soort_bestand == 3:
    # Als foto geef de ondersteunde extensies
    print("""
+--------+--------+--------+
| 1 jpeg | 4 gif  | 7 bmp  |
| 2 png  | 5 heic | 8 tiff |
| 3 jpg  | 6 webp | 9 ico  |
+--------+--------+--------+
""")
    while True:  # Zet nummer om in extensie voor de input bestanden.
        val = input("Enter: exit to quit | Which extension has the input file? Number:")
        if val.isnumeric():
            gekozen_input_formaat_nummer = int(val)
            if 10 > gekozen_input_formaat_nummer > 0:
                break
            else:
                print("This is not a valid extension number. Please try again.")
        elif val == "exit":
            exit()
        else:
            print("Whoops that's not a number!")
    gekozen_input_formaat_extensie = Numcheck.picture(gekozen_input_formaat_nummer) # type: ignore

    while True:
        val = input("Enter: exit to quit | Wich extension needs the output file? Number?:")
        if val.isnumeric():
            gekozen_output_formaat_nummer = int(val)
            if 10 > gekozen_output_formaat_nummer > 0:
                break
            else:
                print("This is not a valid extension number. Please try again.")
        elif val == "exit":
            exit()
        else:
            print("Whoops that's not a number!")
    # Zet het nummer om in een extensie.
    gekozen_output_formaat_extensie = Numcheck.picture(gekozen_output_formaat_nummer) # type: ignore
    # Vraag de lijst met bestanden op.
    bestanden = getfilenames()
    # Voor elk bestand in de lijst bijhorende Core converter uitvoeren.
    for filename in bestanden: # type: ignore
        Core.foto_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)