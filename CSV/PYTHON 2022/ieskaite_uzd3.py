#1--7

class Ballite():
    def __init__(self, ēdiens, dekorācijas, dāvanas):
        self.ediens = ēdiens
        self.dekoracijas = dekorācijas
        self.davanas = dāvanas

    def ēdiens(self):
        print(f"ēdiens ir {self.ediens}")

    def dekorācijas(self):
        print(f"dekorācijas ir {self.dekoracijas}")

    def dāvanas(self):
        print(f"vēlamās dāvanas ir {self.davanas}")

dzD = Ballite(dekorācijas=["Baloni","Virtene","Salvetes"], dāvanas=["Grāmata","Krājkase","Termokrūze"], ēdiens=["Kartupeļi","Gurķi","Burkāni","Kūka","Sula"])

dzD.ēdiens()
dzD.dāvanas()
dzD.dekorācijas()
