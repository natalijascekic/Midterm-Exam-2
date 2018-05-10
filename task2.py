"""
===================   TASK 2   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

#Write your script here
#silumacija bacanja kocke od korisnika uzmemo broj i ispisemo koliko je bilo jedinica dvojki itd

import random
jedinica = 0
dvojki = 0
trojki = 0
cetvorki = 0
petica = 0
sestica = 0

korisnik = input("Koliko puta zelite da bacite kockicu:")

for i in  range(int(korisnik)):
    kockica = random.randint(1, 6)
    if kockica ==1:
        jedinica +=1
    if kockica ==2:
        dvojki +=1
    if kockica ==3:
        trojki +=1
    if kockica ==4:
        cetvorki +=1
    if kockica ==5:
        petica +=1
    if kockica ==6:
        sestica +=1


print("Palo jedinica:" + str(jedinica))
print("Palo dvojki:" + str(dvojki))
print("Palo trojki:" + str(trojki))
print("Palo cetvorki:" + str(cetvorki))
print("Palo petica:" + str(petica))
print("Palo sestica:" + str(sestica))