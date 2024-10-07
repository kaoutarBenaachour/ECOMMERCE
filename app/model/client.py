from datetime import date

class Client:
    def _init_(self, id, nom, prenom, mail, password, numTele):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.password = password
        self.numTele = numTele
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "mail": self.mail,
            "numTele": self.numTele,
        }