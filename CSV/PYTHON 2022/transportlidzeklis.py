class Transportlidzekils():
    def __init__(self,modelis,krasa,motoraTilpums,atrumkarba):
        self.modelis = modelis
        self.krasa = krasa
        self.motoraTilpums =motoraTilpums
        self.atrumkarba = atrumkarba

    def dati(self):
        print(f"modelis: {self.modelis}")
        print(f"krasa: {self.krasa}")
        print(f"motora tilpums: {self.motoraTilpums}")
        print(f"atrumkarba: {self.atrumkarba}")

auto = Transportlidzekils("otlander","melna","10","manuāla")
auto.dati() 