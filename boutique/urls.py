from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("produit/<int:pk>/", views.detail_produit, name="detail_produit"),
    path("panier/", views.panier, name="panier"),
    path("panier/ajouter/<int:pk>/", views.ajouter_au_panier, name="ajouter_au_panier"),
    path("panier/retirer/<int:pk>/", views.retirer_du_panier, name="retirer_du_panier"),
    path("commander/", views.commander, name="commander"),
    path("commande/<int:pk>/confirmation/", views.confirmation_commande, name="confirmation_commande"),
]