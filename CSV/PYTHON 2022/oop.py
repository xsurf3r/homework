#class - definē klasi

class  Auto():
    def __init__(self,modelis,krasa):
        self.modelis = modelis
        self.krasa = krasa

bmw = Auto(modelis = "x5" , krasa = "sarkana")

print(bmw.modelis)

class Auto():
    def __init__(self,modelis,krasa):
        self.modelis = modelis
        self.krasa = krasa

    def dati(self):
        print(f"modelis ir {self.modelis}, krāsa - {self.krasa}")

    def krasas_maina(self , jaunakrasa):
        print(f"Iepriekšējā auto krāsa - {self.krasa}")
        print(f"Jaunā auto krāsa - {jaunakrasa}")

audi = Auto(modelis="Q6",krasa="zila")

audi.dati()
audi.krasas_maina("melna")
