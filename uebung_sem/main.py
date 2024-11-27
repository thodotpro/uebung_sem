artikel = [['schuhe', 100, 20], ['iphone', 1000, 10], ['ipad', 800, 5], ['airpods', 300, 15], ['kugelschreiber', 2, 20]]

#rabatt funktion

def discount():
    for item in artikel:
        if item[2] >= 5:
            discount = 0.05
            return discount
        elif item[2] >= 10:
            discount = 0.10
            return discount

discount()

# steuer funktion
def steuer():
    for i in artikel:
        print(i)

rabatt()
steuer()

def summe():
