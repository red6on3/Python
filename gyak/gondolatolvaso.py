import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

slow_print("Látok a gondolataidban!")

szam = False
igaz_e = False

while not szam:
    gondolj = int(input("Gondolj egy számra 1-10 között: "))
    if gondolj < 1 or gondolj > 10:
        print("Érvénytelen adat. 1-10 között.")
    else:
        szam = True

slow_print("Gondolatok olvasása...")
time.sleep(1)
slow_print("Memória szkennelése...")
time.sleep(1)
slow_print("Lehetőségek számolása...")
time.sleep(1)
slow_print("Gondolatok dekódolása...")
time.sleep(1)

while not igaz_e:
 biztos_e = input(f"Biztos, hogy belemászak az agyadba (veszélyes)? (I/N): ").upper()
 if biztos_e == "I":
    igaz_e = True
    slow_print("5G elhelyezése...")
    time.sleep(1)
    slow_print("Nanobotok aktiválása...")
    time.sleep(1)
    slow_print("Covid ellenszer áramoltatása...")
    time.sleep(1)
    slow_print(f"A szám, amire gondoltál: {gondolj}")
 elif biztos_e == "N":
    print("Ha nem, akkor nem.")
    igaz_e = True
 else:
   print("Ilyen könnyen nem úszod meg, (I,N).")