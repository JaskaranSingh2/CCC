numA = int(input("How many antennas? \n"))
numE = int(input("How many eyes? \n"))

while True:
    if numA >= 3 and numE <= 4:
        print("TroyMartian")
    if numA <= 6 and numE >= 3:
        print("VladSaturnian")
    if numA <= 2 and numE <= 3:
        print("GraemeMercurian")
    exit()
