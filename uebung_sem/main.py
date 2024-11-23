artikel = [['schuhe', 100, 20], ['iphone', 1000, 10], ['ipad', 800, 5], ['airpods', 300, 15], ['kugelschreiber', 2, 20]]

discount = 0

def discount():
    for item in artikel:
        if item[2]>=5:
            discount = 0.05
            return discount
        elif item[2] >= 10:
            discount = 0.10
            return discount

discount()









#Pro Artikel gibt es einen 5% igen Rabatt ab 5 Stück des gleichen Artikels, bzw. 10%
#Rabatt ab 10 Stück eines Artikels – der Rabatt wird individuell für jeden Artikel
#berechnet.