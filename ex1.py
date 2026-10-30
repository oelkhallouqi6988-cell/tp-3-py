
class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def salaire_total(self):
        return self.salaire_base

    def __str__(self):
        return self.nom + " gagne " + str(self.salaire_total()) + " €"


class Manager(Employe):
    def __init__(self, nom, salaire_base, prime):
        Employe.__init__(self, nom, salaire_base)
        self.prime = prime

    def salaire_total(self):
        resultat = self.salaire_base + self.prime
        return resultat


class Developpeur(Employe):
    def __init__(self, nom, salaire_base, technologie):
        Employe.__init__(self, nom, salaire_base)
        self.technologie = technologie

    def salaire_total(self):
        if self.technologie == "Python":
            return self.salaire_base + 500
        elif self.technologie == "Java":
            return self.salaire_base + 400
        else:
            return self.salaire_base + 300


e1 = Employe("Ahmed", 2100)
e2 = Manager("Sara", 2800, 700)
e3 = Developpeur("Omar", 2300, "Java")

employes = [e1, e2, e3]

for e in employes:
    print(e)
