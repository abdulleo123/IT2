import random
#Øving 1: Variabler, input og output

#1.1
'''
# The problem here is that there is a space in between the name
Et tall = 123

# The problem here is that the name starts with a number
3variabelen = 3

Variabel1 = "teksten skal hit"

detførstetallet = "1"

# The problem here is that the name doesnt start with a letter, but an invalid sign
#%AvTallet = 15

SummenAvRegnestykketEr = 16
'''


'''
Et_tall = 123


var3 = 3

Variabel1 = "teksten skal hit"

detførstetallet = "1"

AvTallet = 15

SummenAvRegnestykketEr = 16
'''



#1.2

'''
# Definer variablene
første_tall = 5
andre_tall = 10
resultat = 50

# Lag teksten ved å kombinere variablene
tekst = f"{første_tall} ganger {andre_tall} er {resultat}"

# Skriv teksten til konsollen
print(tekst)
'''

#1.3

'''
fornavn = input("Tast in navnet ditt: ")
etternavn = input("Tast in etternnet ditt: ")
domene = input("Tast in domene ditt: ")

epost = f"{fornavn}.{etternavn}@{domene}"

print(epost)
'''

#1.4

# A)
#REgnestykket blir ikke printet ut fordi når vi bruker " " så blir det til text, altså "4 + 6" blir printet ut
#print("4 + 6")

# B)

# Det blir printet ut to forskjellige tall, og det er fordi når vi skriver int(total), så blir det printet ut kun heltall
'''
a = 3.4 
b = 20.5 
total = a * b 
print(total) 
print(int(total))
'''

# 1.5

# A)

# husnr må skrives på denne måten: husnr = '432' og det samme med oppgang = 'b'
'''
gate = 'Kongens gate' 
husnr = '432' 
oppgang = 'b' 

# B)
address1 = f"Adressen er {gate} {husnr}{oppgang}"
address2 = f"Gaten er {gate}, husnummeret er {husnr}, oppgang {oppgang}"
print(address1)
print(address2)
'''


# 1.6
'''
matDrikke = 850
studentRabatt = 25
tips = 10

discountedPrice = matDrikke - (matDrikke * studentRabatt) / 100
discountedPrice += (discountedPrice * tips) / 100

total = discountedPrice
'''

# Øving 2: if-else, løkker og funksjoner

# 2.1
'''
hemmeligTall = random.randint(1, 100)  # Hent et tilfeldig tall

gjettet = 0  # Initier variabelen for gjettet tall
antGjett = 0  # Initier counter for antall forsøk

while gjettet != hemmeligTall:
    gjettet = int(input('Gjett det hemmelige tallet (1-100): '))  # Ta inn et gjett fra bruker
    antGjett += 1  # Øk antall forsøk med 1 for hver runde

    if gjettet > hemmeligTall:
        print("Tallet som ble gjettet var for høyt")
    elif gjettet < hemmeligTall:
        print("Tallet som ble gjettet var for lavt")
    else:
        print('Du gjettet riktig! Det hemmelige tallet var', hemmeligTall, '. Du brukte', antGjett, 'forsøk.')
'''


# 2.2
'''
tall1 = int(input("Skriv et tall mellom 40-50 eller mellom 70-90: "))
tall2 = int(input("Skriv et tall mellom 40-50 eller mellom 70-90: "))

if (40 <= tall1 <= 50 or 70 <= tall1 <= 90) and (40 <= tall2 <= 50 or 70 <= tall2 <= 90):
    print("Begge tallene er innenfor gyldig intervall.")
else:
    print("Minst ett av tallene er utenfor gyldig intervall.")
'''

# 2.3
'''
def calculate_ticket_price(route, age):
    if route == 1:
        standard_price = 150
    elif route == 2:
        standard_price = 250
    elif route == 3:
        standard_price = 50
    else:
        print("Ugyldig reiserute valgt.")
        return

    if age <= 2:
        discount = 1.0  # Gratis
    elif age <= 16:
        discount = 0.5  # -50 %
    elif age <= 65:
        discount = 1.0  # Ingen rabatt (standard pris)
    else:
        discount = 0.3  # -70 %

    final_price = standard_price * discount
    return final_price

route = int(input("Velg reiserute:\n1 = By-Sjø\n2 = Sjø-Fjell\n3 = Fjell-By\n"))
age = int(input("Skriv inn alder: "))

ticket_price = calculate_ticket_price(route, age)

if ticket_price is not None:
    print("Standard pris:", ticket_price * 1.0)  # Skriver ut standard pris
    if ticket_price < 1.0:
        print("Gratis")
    else:
        print("Rabatt:", (1 - ticket_price) * 100, "%")
        print("Sluttpris:", ticket_price)
'''

# 2.4
'''
antPar = 0  # Initierer antall partall-counter
forsok = 0  # Initierer counter for antall forsøk
ny = 'J'    # Initierer kontrollstruktur for ny input

while ny == 'J':
    tall = int(input('Skriv et tall mellom 1-1000: '))  # Ta inn et tall fra bruker
    forsok += 1  # Øker antall forsøk med 1 for hver innskriving

    # Finn ut om tallet er et oddetall eller et partall
    if tall % 2 == 0:
        erPartall = True
        antPar += 1  # Øker counter for antall partall med 1
    else:
        erPartall = False

    # Skriv en setning til bruker med beskjed om tallet var et partall eller et oddetall
    if erPartall:
        print('Tallet', tall, 'er et partall.')
    else:
        print('Tallet', tall, 'er et oddetall.')

    ny = str(input('Vil du skrive inn et nytt tall? (J/N): '))  # Sjekker om programmet skal avsluttes eller startes på nytt

print('Du skrev inn', forsok, 'tall, og', antPar, 'av dem var partall.')  # Beskjed til bruker om antall forsøk og antall partall
'''

# 2.5

'''
ai_score = 0
user_score = 0
winning_score = 10

while ai_score < winning_score and user_score < winning_score:
    ai = random.randint(1, 3)
    bruker = input("stein('st'), saks('sa') eller papir('p'): ")

    if (ai == 1 and bruker == "sa") or (ai == 2 and bruker == "p") or (ai == 3 and bruker == "st"):
        ai_score += 1
        print("AI vinner!")
    elif (ai == 1 and bruker == "p") or (ai == 2 and bruker == "st") or (ai == 3 and bruker == "sa"):
        user_score += 1
        print("Du vinner!")
    elif ai == 1 and bruker == "st":
        print("Uavgjort: Begge valgte stein")
    elif ai == 2 and bruker == "sa":
        print("Uavgjort: Begge valgte saks")
    elif ai == 3 and bruker == "p":
        print("Uavgjort: Begge valgte papir")
    else:
        print("Ugyldig valg. Prøv igjen.")

print("Spillet er over!")
print("AI-score:", ai_score)
print("Din score:", user_score)
'''


# Øving 3: Mer om løkker
# 3.1

'''
tall = 0
while tall != 10:
    tall += 1
    print(tall)
'''

# 3.2

'''
ord = "programmering"

for i in range(len(ord)):
    if ord[i] == 'e':
        break
    print(ord[i])
'''
    
# 3.3

'''
navn = ["Kari", "Arne", "Hanne", "Julie", "Maria", "Christine"]
for i in range(len(navn)):
    if navn[i] != "Maria":
        print("Ikke Maria")
    else:
        print(navn[i])
'''



# 3.4

'''
ord = "fiskeboller"
for i in range(len(ord)):
    if ord[i] == 'b':
        break
    print(ord[i])
'''

# 3.5


'''
bruker_input = input("Vennligst skriv inn eit spørsmål: ")

if '?' in bruker_input:
    print("Eg har godteke spørsmålet ditt!")
else:
    print("Det ser ikkje ut til at du stilte eit spørsmål.")
'''

# 3.6