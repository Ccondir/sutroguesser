import random
import time

right = 0
right1 = 1
right2 = 2
right3 = 3
right4 = 4
right5 = 5

print("wlecome to stoneguesser")
time.sleep(2)
print("uděláno Peetou a mnou")

time.sleep(3)
a = input("začínáme? (ano/ne): ")
if a == "ne":
    print("k")
    time.sleep(9999999999999)
elif a == "ano":
    print("ok")
    time.sleep(5)
elif a == "SPbSB":
    print("")
    print("")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░    ░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░        ░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░        ░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░        ░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░            ░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ░░            ░░      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ░░                ░░      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ████████████████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ████████    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ████  ████  ████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ████  ████  ████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ██    ████████    ██  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░        ░░░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                    ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓            ▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ▓▓░░  ▓▓▓▓  ░░▓▓  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓    ▓▓▓▓    ▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ▓▓░░  ▓▓▓▓  ░░▓▓  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓    ▓▓▓▓    ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓░░  ▓▓▓▓  ░░▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    time.sleep(2)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("tento projekt vám byl přinesen naším sponzorem, skupinou Squid Bay, SB(SquidBay) je: ")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    time.sleep(2)
    print("-> Aktivní komunita, která je schopná udělat skvělé zážitky, obráťit špatný den v dobrý,")
    time.sleep(2)
    print("-> Je komunita plná přátelských lidí (a Milkeše), co spolu hrají různé počítačové hry")
    time.sleep(2)
    print("-> SB je i vzdělávací platforma pro lidi kteří se chystají naučit nové dovednosti např.")
    time.sleep(2)
    print("   -> Motion grafika od Skrafiho, programování od Ccondira a goda, hacking s Perchantem")
    time.sleep(2)
    print("-> A spoustu dalších věcí najdete nás na discordu https://discord.gg/UWfGJ4q4Yq")
    time.sleep(2)
    print("-> Máme i semi-funkční ekonomiku ve formě Aquamarinů")
    time.sleep(2)
    print("-> Přiďte a řekněte ahoj těšíme se.")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    time.sleep(5)
    print("")
    print("")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░    ░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░        ░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░        ░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░        ░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░            ░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ░░            ░░      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ░░                ░░      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ████████████████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ████████    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ████  ████  ████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ████  ████  ████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ██    ████████    ██  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░        ░░░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                    ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓            ▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ▓▓░░  ▓▓▓▓  ░░▓▓  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓    ▓▓▓▓    ▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ▓▓░░  ▓▓▓▓  ░░▓▓  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓    ▓▓▓▓    ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓░░  ▓▓▓▓  ░░▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    time.sleep(5)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("")
    time.sleep(1)


stons = ["zlato", "grafit", "diamand", "síra", "flourid",
         "halit", "galenit", "antimonit", "pyrit", "chalkopyrit"]
rndgston = random.choice(stons)
if rndgston == "zlato":
    c = input(
        'je to měkký kov, ktrý je nažloutlý a nachází se v "žilách". Kamenem je: ')
    time.sleep(5)
    if c == "zlato":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif c != "zlato":
        print("špatně 0/5")
elif rndgston == "grfit":
    d = input(
        "měkký, odolný, voďiví, nekov ze kterého se dělá tuha do tužek. Kámen je: ")
    time.sleep(5)
    if d == "grafit":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif d != "grafit":
        print("špatně 0/5")
elif rndgston == "diamant":
    e = input("nejtvrdší nerost, vzníká velkým tlakem. Kámen je: ")
    if e == "diamnd":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif e != "diamand":
        print("špatně 0/5")
elif rndgston == "síra":
    f = input("křehká, zakalená, s krystaly, užívá se na výrobu sirek. Kámen je: ")
    if f == "síra":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif f != "síra":
        print("špatně 0/5")
elif rndgston == "flourid":
    g = input("používá se ve sklenářství, mnoho barev. Kámen je: ")
    if g == "flourid":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif g != "flourid":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston == "halit":
    h = input("bezbarvý halóógenit, jinim jménem sůl kamenná. Kamen je: ")
    if h == "halit":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif h != "halit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston == "galenit":
    i = input("hlavní ruda olova, kovová barva. Kámen je: ")
    if i == "galenit":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif i != "galenit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston == "antimonit":
    j = input("šedý/černý využití v pyrotechnice. Kámen je: ")
    if j == "antimonit":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif j != "antimonit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston == "pyrit":
    k = input("kovová barva, jinim jménem kočičí zlato. Kámen je: ")
    if k == "pyrit":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif k != "pyrit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston == "chalkopyrit":
    l = input("ruda mědi, žlutší než pyrit. Kámen je: ")
    if l == "chalkopyrit":
        print("správně " + str(right1) + "/5")
        time.sleep(3)
    elif l != "chalkopyrit":
        print("špatně 0/5")
        time.sleep(5)
rndgston1 = random.choice(stons)
if rndgston1 == "zlato":
    c = input(
        'je to měkký kov, ktrý je nažloutlý a nachází se v "žilách". Kamenem je: ')
    time.sleep(5)
    if c == "zlato":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif c != "zlato":
        print("špatně 0/5")
elif rndgston1 == "grfit":
    d = input(
        "měkký, odolný, voďiví, nekov ze kterého se dělá tuha do tužek. Kámen je: ")
    time.sleep(5)
    if d == "grafit":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif d != "grafit":
        print("špatně 0/5")
elif rndgston1 == "diamant":
    e = input("nejtvrdší nerost, vzníká velkým tlakem. Kámen je: ")
    if e == "diamnd":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif e != "diamand":
        print("špatně 0/5")
elif rndgston1 == "síra":
    f = input("křehká, zakalená, s krystaly, užívá se na výrobu sirek. Kámen je: ")
    if f == "síra":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif f != "síra":
        print("špatně 0/5")
elif rndgston1 == "flourid":
    g = input("používá se ve sklenářství, mnoho barev. Kámen je: ")
    if g == "flouri":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif g != "flourit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston1 == "halit":
    h = input("bezbarvý halóógenit, jinim jménem sůl kamenná. Kamen je: ")
    if h == "halit":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif h != "halit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston1 == "galenit":
    i = input("hlavní ruda olova, kovová barva. Kámen je: ")
    if i == "galenit":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif i != "galenit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston1 == "antimonit":
    j = input("šedý/černý využití v pyrotechnice. Kámen je: ")
    if j == "antimonit":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif j != "antimonit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston1 == "pyrit":
    k = input("kovová barva, jinim jménem kočičí zlato. Kámen je: ")
    if k == "pyrit":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif k != "pyrit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston1 == "chalkopyrit":
    l = input("ruda mědi, žlutší než pyrit. Kámen je: ")
    if l == "chalkopyrit":
        print("správně " + str(right2) + "/5")
        time.sleep(3)
    elif l != "chalkopyrit":
        print("špatně 0/5")
        time.sleep(5)
rndgston2 = random.choice(stons)
if rndgston2 == "zlato":
    c = input(
        'je to měkký kov, ktrý je nažloutlý a nachází se v "žilách". Kamenem je: ')
    time.sleep(5)
    if c == "zlato":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif c != "zlato":
        print("špatně 0/5")
elif rndgston2 == "grfit":
    d = input(
        "měkký, odolný, voďiví, nekov ze kterého se dělá tuha do tužek. Kámen je: ")
    time.sleep(5)
    if d == "grafit":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif d != "grafit":
        print("špatně 0/5")
elif rndgston2 == "diamant":
    e = input("nejtvrdší nerost, vzníká velkým tlakem. Kámen je: ")
    if e == "diamnd":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif e != "diamand":
        print("špatně 0/5")
elif rndgston2 == "síra":
    f = input("křehká, zakalená, s krystaly, užívá se na výrobu sirek. Kámen je: ")
    if f == "síra":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif f != "síra":
        print("špatně 0/5")
elif rndgston2 == "flourid":
    g = input("používá se ve sklenářství, mnoho barev. Kámen je: ")
    if g == "flouri":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif g != "flourit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston2 == "halit":
    h = input("bezbarvý halóógenit, jinim jménem sůl kamenná. Kamen je: ")
    if h == "halit":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif h != "halit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston2 == "galenit":
    i = input("hlavní ruda olova, kovová barva. Kámen je: ")
    if i == "galenit":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif i != "galenit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston2 == "antimonit":
    j = input("šedý/černý využití v pyrotechnice. Kámen je: ")
    if j == "antimonit":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif j != "antimonit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston2 == "pyrit":
    k = input("kovová barva, jinim jménem kočičí zlato. Kámen je: ")
    if k == "pyrit":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif k != "pyrit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston2 == "chalkopyrit":
    l = input("ruda mědi, žlutší než pyrit. Kámen je: ")
    if l == "chalkopyrit":
        print("správně " + str(right3) + "/5")
        time.sleep(3)
    elif l != "chalkopyrit":
        print("špatně 0/5")
        time.sleep(5)
rndgston3 = random.choice(stons)
if rndgston3 == "zlato":
    c = input(
        'je to měkký kov, ktrý je nažloutlý a nachází se v "žilách". Kamenem je: ')
    time.sleep(5)
    if c == "zlato":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif c != "zlato":
        print("špatně 0/5")
elif rndgston3 == "grfit":
    d = input(
        "měkký, odolný, voďiví, nekov ze kterého se dělá tuha do tužek. Kámen je: ")
    time.sleep(5)
    if d == "grafit":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif d != "grafit":
        print("špatně 0/5")
elif rndgston3 == "diamant":
    e = input("nejtvrdší nerost, vzníká velkým tlakem. Kámen je: ")
    if e == "diamnd":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif e != "diamand":
        print("špatně 0/5")
elif rndgston3 == "síra":
    f = input("křehká, zakalená, s krystaly, užívá se na výrobu sirek. Kámen je: ")
    if f == "síra":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif f != "síra":
        print("špatně 0/5")
elif rndgston3 == "flourid":
    g = input("používá se ve sklenářství, mnoho barev. Kámen je: ")
    if g == "flouri":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif g != "flourit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston3 == "halit":
    h = input("bezbarvý halóógenit, jinim jménem sůl kamenná. Kamen je: ")
    if h == "halit":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif h != "halit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston3 == "galenit":
    i = input("hlavní ruda olova, kovová barva. Kámen je: ")
    if i == "galenit":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif i != "galenit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston3 == "antimonit":
    j = input("šedý/černý využití v pyrotechnice. Kámen je: ")
    if j == "antimonit":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif j != "antimonit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston3 == "pyrit":
    k = input("kovová barva, jinim jménem kočičí zlato. Kámen je: ")
    if k == "pyrit":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif k != "pyrit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston3 == "chalkopyrit":
    l = input("ruda mědi, žlutší než pyrit. Kámen je: ")
    if l == "chalkopyrit":
        print("správně " + str(right4) + "/5")
        time.sleep(3)
    elif l != "chalkopyrit":
        print("špatně 0/5")
        time.sleep(5)
rndgston4 = random.choice(stons)
if rndgston4 == "zlato":
    c = input(
        'je to měkký kov, ktrý je nažloutlý a nachází se v "žilách". Kamenem je: ')
    time.sleep(5)
    if c == "zlato":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif c != "zlato":
        print("špatně 0/5")
elif rndgston4 == "grfit":
    d = input(
        "měkký, odolný, voďiví, nekov ze kterého se dělá tuha do tužek. Kámen je: ")
    time.sleep(5)
    if d == "grafit":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif d != "grafit":
        print("špatně 0/5")
elif rndgston4 == "diamant":
    e = input("nejtvrdší nerost, vzníká velkým tlakem. Kámen je: ")
    if e == "diamnd":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif e != "diamand":
        print("špatně 0/5")
elif rndgston4 == "síra":
    f = input("křehká, zakalená, s krystaly, užívá se na výrobu sirek. Kámen je: ")
    if f == "síra":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif f != "síra":
        print("špatně 0/5")
elif rndgston4 == "flourid":
    g = input("používá se ve sklenářství, mnoho barev. Kámen je: ")
    if g == "flouri":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif g != "flourit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston4 == "halit":
    h = input("bezbarvý halóógenit, jinim jménem sůl kamenná. Kamen je: ")
    if h == "halit":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif h != "halit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston4 == "galenit":
    i = input("hlavní ruda olova, kovová barva. Kámen je: ")
    if i == "galenit":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif i != "galenit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston4 == "antimonit":
    j = input("šedý/černý využití v pyrotechnice. Kámen je: ")
    if j == "antimonit":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif j != "antimonit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston4 == "pyrit":
    k = input("kovová barva, jinim jménem kočičí zlato. Kámen je: ")
    if k == "pyrit":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif k != "pyrit":
        print("špatně 0/5")
        time.sleep(5)
elif rndgston4 == "chalkopyrit":
    l = input("ruda mědi, žlutší než pyrit. Kámen je: ")
    if l == "chalkopyrit":
        print("správně " + str(right5) + "/5")
        time.sleep(3)
    elif l != "chalkopyrit":
        print("špatně 0/5")
        time.sleep(5)

print("gratuluji za dokončení. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!")
time.sleep(60)
