class Produit:
    def __init__(self, id, nom, quantite, description, prix):
        self.id = id
        self.nom = nom
        self.quantite = quantite
        self.description = description
        self.prix = prix

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "quantite": self.quantite,
            "description": self.description,
            "prix": self.prix
        }