from datetime import datetime

# 1D Lister


# Oppgave 1
'''
verdensdeler = ["Europa", "Asia", "Afrika", "Nord-Amerika", "Sør-Amerika", "Oseania", "Antarktis"]
print(verdensdeler[0])
print(verdensdeler[3])
print(verdensdeler[-1])
'''

# Oppgave 2
'''
heltall = list(range(0, 51))
print(heltall)
'''

# Oppgave 3
'''
oddetall = list(range(1, 100, 2))
print(oddetall)
'''


# Oppgave 4
'''
kvadrattallene = [x ** 2 for x in range(1, 21)]
print(kvadrattallene)
'''


# Oppgave 5
'''
kvadrattallene = [x ** 3 for x in range(1, 15)]
print(kvadrattallene)
'''

# Oppgave 6
'''
maxKvadrattallene = sum(kvadrattallene)
print(maxKvadrattallene)
'''


# Oppgave 7
'''
tegneseriefigurer = []

tegneseriefigurer.append("Donald Duck")
tegneseriefigurer.append("Obleix")
tegneseriefigurer.append("Pondus")

tegneseriefigurer.insert(3, "Asterix")

tegneseriefigurer[3] = "Asterix"

if "Asterix" in tegneseriefigurer:
  print("Asterix er registrert")

print(tegneseriefigurer)

liste = []

for i in range(1, 21):
    liste.append(i)

liste = [x for x in liste if x % 2 != 0]

print(liste)
'''



# Oppgave 8
'''
tall = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]

ny_liste = [x for x in tall if x != 3]

tall = ny_liste

print(tall)
'''


# Oppgave 9
# a)
'''
a = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

a.reverse()

print(a)
'''

# Oppgave 16
'''
tall = [0, 2, 4, 6, 8, 10, 12, 14]

storst = tall[0]

for x in tall:
  if x > storst:
    storst = x

print(storst)

# Find and print the maximum and minimum values in the tall list
print(max(tall))
print(min(tall))
'''


# Ordbøker

#Oppgave 1 
'''
person = {"firstName":"Abdul", "lastName":"Al Kadri", "age":18}

print(f"Personens fornavn er {person['firstName']}. {person['firstName']} er {person['age']} år gammel")
'''

# Oppgave 2


'''

dagens_ukedag = datetime.now().strftime('%A')

# Opprett en tom ordbok med dagens ukedag som navn
værdata1 = {
    dagens_ukedag: {},
    "maksimumstemperatur":16,
    "minimumstemperatur":11,
    "nedbørsmengde":"1.4mm",
    "gjennomsnittlige vindstyrke": "4m/s"
    
    }

for key, value in værdata1.items():
    print(f"{key}: {value}")
'''


# Oppgave 3


'''
vaerdata = {
  "lat":59.97,"lon":10.78,"timezone":"Europe/Oslo","timezone_offset":7200,"daily": [
    { 
      "dt":1649329200,
      "sunrise":1649305463,
      "sunset":1649355199,
      "moonrise":1649311440,
      "moonset":1649295060,
      "moon_phase":0.19,
      "temp":{"day":277.51,"min":271.29,"max":277.51,"night":271.8,"eve":273.29,"morn":271.79},
      "feels_like":{"day":273.59,"night":265.92,"eve":268.02,"morn":269.78},
      "pressure":956,
      "humidity":46,
      "dew_point":267.62,
      "wind_speed":6.13,
      "wind_deg":19,
      "wind_gust":13.63,
      "weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"}],
      "clouds":100,"pop":0.89,"snow":1.65,"uvi":1.57
    },
    {
      "dt":1649415600,
      "sunrise":1649391683,
      "sunset":1649441745,
      "moonrise":1649400060,
      "moonset":1649385480,
      "moon_phase":0.22,
      "temp":{"day":274.79,"min":270.59,"max":275.91,"night":271.85,"eve":274.38,"morn":270.83},
      "feels_like":{"day":269.76,"night":268.08,"eve":270.43,"morn":264.98},
      "pressure":978,
      "humidity":47,
      "dew_point":264.4,
      "wind_speed":6.47,
      "wind_deg":17,
      "wind_gust":13.84,
      "weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"}],
      "clouds":100,"pop":0.93,"snow":3.25,"uvi":1.52
    }
    
  ]
}

# print(vaerdata)

for dag in vaerdata["daily"]:
  dato = dag["dt"]
  temperatur = dag["temp"]["day"]
  print(f"Varsel for {dato}. Temperatur: {temperatur}.")

'''
