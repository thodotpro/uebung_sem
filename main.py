# Artikel: Schuh, Koffer, Handy, Torte, Bleistift
bestellung = [["Schuh", 50, 10], ["Koffer", 200, 5], ["Handy", 600, 7], ["Torte", 60, 3], ["Bleistift", 3, 20]]

#verschachtelte liste

summe = 0
for idx in range(len(bestellung)):
#    summe = 0
#    for idx2 in range(len(bestellung[idx])):
    artikel = bestellung[idx][0]
    preis = bestellung[idx][1]
    anzahl = bestellung[idx][2]
    artikel_first = str(artikel[0])
    if artikel_first > "K":
       # print("Steuer 20")
        steuer = 1.20
    else:
        #print("Steuer 10")
        steuer = 1.10

    if anzahl >= 10:
        #print("Rabatt 10")
        rabatt = 0.90
    elif anzahl >= 5:
        #print("Rabatt 5")
        rabatt = 0.95
    else:
        #print("Rabatt 0")
        rabatt = 1

    summe = int(((preis * anzahl) * rabatt) * steuer) + summe
print(summe)













# print(bestellung[0:5:3])

# artikel = [sublist[:1] for sublist in bestellung]

#print("artikel")
#print(artikel)

# anzahl = [sublist[2:] for sublist in bestellung]
#print("anzahl")
#print(anzahl)

#slicedbestellung = bestellung[1::2]
#print("slicedbestellung")


#print(bestellung)
# print(artikel)

#Rabatt
# 5 gleiche Artikel = 5% Rabatt
# 10 gleiche Artikel = 10% Rabatt

# for idx1 in range(len(bestellung)):
  #  print("Element " + str(idx1) + " äußere Liste")
   # print(bestellung[idx1])

