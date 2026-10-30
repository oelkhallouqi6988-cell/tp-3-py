
# Classe principale
class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print("Titre :", self.titre)
        print("Annee :", self.annee)



class Livre(Document):
    def __init__(self, titre, annee, auteur):
        Document.__init__(self, titre, annee)
        self.auteur = auteur

    def afficher(self):
        print("Type : Livre")
        print("Titre :", self.titre)
        print("Auteur :", self.auteur)
        print("Annee :", self.annee)



class Magazine(Document):
    def __init__(self, titre, annee, numero):
        Document.__init__(self, titre, annee)
        self.numero = numero

    def afficher(self):
        print("Type : Magazine")
        print("Titre :", self.titre)
        print("Numero :", self.numero)
        print("Annee :", self.annee)


livre1 = Livre("L'etranger", 1942, "Albert Camus")
magazine1 = Magazine("National Geographic", 2024, 125)
livre2 = Livre("Les Miserables", 1862, "Victor Hugo")


documents = [livre1, magazine1, livre2]


print(" Bibliotheque ")

for doc in documents:
    doc.afficher()
    print("---")
