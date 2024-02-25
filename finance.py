import math
import json

class Compte:

    depenses = {}

    def __init__(self, charges, loisirs, investissement, dons, epargne, imprevus):
        self.charges = charges
        self.loisirs = loisirs
        self.investissement = investissement
        self.dons = dons
        self.epargne = epargne
        self.imprevus = imprevus
        self.total = charges + loisirs + investissement + dons + epargne + imprevus

    def update_total(self):
        self.total = self.charges + self.loisirs + self.epargne + self.dons + self.imprevus + self.investissement
    

    def sommesi(self, type, prix, desc):
        if type == "charges":
            self.charges -= prix
            self.depenses['Charges'] += desc,prix;
        elif type == "loisirs":
            self.loisirs -= prix
        elif type == "investissement":
            self.investissement -= prix
        elif type == "dons":
            self.dons -= prix
        elif type == "epargne":
            self.epargne -= prix
        elif type == "imprevus":
            self.imprevus -= prix
        else:
            return "Invalid type"
        self.update_total()

    def to_string(self):
        return json.dumps(self.__dict__)
        



compte1 = Compte(100, 50, 200, 30, 80, 10)
compte1.sommesi("charges", 50, "Some description")
print(compte1.to_string())
print(compte1.depenses)