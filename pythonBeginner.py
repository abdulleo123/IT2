from math import *
from calendar import * 


#Oppgaver

# 11

# Få verdien av radius fra brukeren
'''
rad = float(input("Skriv inn radianen til sirkelen: "))

# Beregn omkretsen og arealet
omkrets = 2 * pi * rad
areal = pi * rad**2

# Skriv ut resultatene
print("Omkretsen til sirkelen:", omkrets)
print("Arealet til sirkelen:", areal)
'''

# 13

'''
idag = month(2005, 2)
print(idag)
'''


'''
text = "Harry Potter, created by J.K. Rowling, is a beloved fantasy series featuring a young wizard's adventures at Hogwarts School of Witchcraft and Wizardry. With themes of friendship, bravery, and the battle against dark forces, it has captivated readers and led to a successful film franchise, becoming a cultural phenomenon."
antallTegn = len(text)
print(text.upper())
'''


# 16


'''
text = "Hallo!"
lengde = len(text)
sisteTegn = text[5]
print(lengde)
print(sisteTegn)
'''

# 17

'''
text = "HALLO!"
nyttOrd = text.lower()
print(nyttOrd)
'''

# 18

'''
data = "Datamaskiner er ubrukelige. De kan bare gi oss svar."
print(data)
nySettning = data.replace("Datamaskiner er ubrukelige. De kan bare gi oss svar.", "Datamaskiner kan gi oss svar.")
print(nySettning)
'''

# 19

'''
fornavn = "Abdul"
etternavn = "Al kadri"
telefonnummer = "87128738"

nummer = float(telefonnummer)
navn = fornavn.lower()
etterNa = etternavn.lower()

text = f"{navn} {etterNa} har telefonnummer {nummer}"
print(text)
'''

# Kalkulator


'''
tall1 = input("Skriv et tall: ")
tall1 = float(tall1) 

tall2 = input("Skriv et tall: ")
tall2 = float(tall2) 

sum = tall1 + tall2

print("Summen av tallene er", sum)
'''


'''
tekst1 = "Monty"
tekst2 = "Python"
tekst3 = tekst1.upper()
tekst4 = tekst2.lower()
tekst5 = tekst3[:4]
tekst6 = tekst4[4:]
tekst7 = tekst5 + tekst6

print(tekst7)
'''



#Blandede oppgaver
#Oppgave 3


'''
maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"

maanedsnummer = int(input("Skriv in et månedsnummer, for eksempel 2 (Februar): "))

if maanedsnummer == 1:
    print(maaneder[:3])
elif maanedsnummer == 2:
    print(maaneder[3:6])
elif maanedsnummer == 3:
    print(maaneder[6:9])
elif maanedsnummer == 4:
    print(maaneder[9:12])
elif maanedsnummer == 5:
    print(maaneder[12:15])
elif maanedsnummer == 6:
    print(maaneder[15:18])
elif maanedsnummer == 7:
    print(maaneder[18:21])
elif maanedsnummer == 8:
    print(maaneder[21:24])
elif maanedsnummer == 9:
    print(maaneder[24:27])
'''

#Kapittel 1B
#Oppgave 4

'''
tall1 = int(input("Tast in det første tallet: "))
tall2 = int(input("Tast in det andre tallet: "))
tall3 = int(input("Tast in det tredje tallet: "))

if tall1 == tall2 == tall3:
    print("Alle tallene er like")
'''

'''
tall = int(input("Tast in ett tall: "))

if tall%2 == 0:
    print("Tallet er ett partall")
else:
    print("Tallet er ett oddetall")
'''


'''
except ValueError:
    print("Skriv ett tall: ")
'''

'''
for i in range(1, 31):
    print(i)
'''


'''
for i in range(1, 101, 2):
    print(i)
'''


'''
for i in range(1, 11):
    print(i * 5)
'''


'''
for i in range(1, 10, 2):
    print(i)
'''
