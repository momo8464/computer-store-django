from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "catégories"

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.PositiveIntegerField(help_text="Prix en FCFA")
    image = models.ImageField(upload_to="produits/")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits")
    badge = models.CharField(max_length=30, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Message(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_envoi"]

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.date_envoi:%d/%m/%Y}"

class Commande(models.Model):
    STATUTS = [
        ("en_attente", "En attente"),
        ("confirmee", "Confirmée"),
        ("livree", "Livrée"),
        ("annulee", "Annulée"),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=30)
    adresse = models.TextField(help_text="Adresse ou lieu de livraison")
    total = models.PositiveIntegerField()
    statut = models.CharField(max_length=20, choices=STATUTS, default="en_attente")
    date_commande = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_commande"]

    def __str__(self):
        return f"Commande n°{self.id} - {self.prenom} {self.nom}"


class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name="lignes")
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True, blank=True)
    nom_produit = models.CharField(max_length=150)
    prix_unitaire = models.PositiveIntegerField()
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} × {self.nom_produit}"