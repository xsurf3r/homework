class Rekins():
    def __init__(self,klients,veltijums,izmers,materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = float(materials)

        sad_izm = self.izmers.split(",")
        print(sad_izm)
        

    def izdrukat(self):
        print("Klients:",self.klients)
        print("Veltījums:",self.veltijums)
        print("Izmērs:", self.izmers)
        print("Materiāls:",self.materials)

    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = (len(self.veltijums)) * 1.2 + (self.izmers[0]/100 * self.izmers[1]/100 * self.izmers[2]/100)/ 3 * self.materials
        PVN_summa = (produkta_cena + darba_samaksa)*PVN/100 
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        return rekina_summa

klients = input("ievadi vārdu: ")
veltijums = input("ievadi veltijumu: ")
izmers = input("ievdi izmēru (platums, garums, augstums): ")
materials = input("ievadi materiāla cenu EUR/m2: ")

pirmais = Rekins(klients,veltijums,izmers,materials)
pirmais.izdrukat()