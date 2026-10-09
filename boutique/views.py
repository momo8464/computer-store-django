from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommandeForm, MessageForm
from .models import Categorie, Commande, LigneCommande, Produit


def accueil(request):
    if request.method == "POST":
        formulaire = MessageForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
            messages.success(request, "Votre message a bien été envoyé. Merci !")
            return redirect("/#contact")
    else:
        formulaire = MessageForm()

    categories = Categorie.objects.all()
    categorie_active = request.GET.get("categorie", "")

    produits = Produit.objects.filter(disponible=True)
    if categorie_active.isdigit():
        produits = produits.filter(categorie_id=categorie_active)

    return render(request, "boutique/index.html", {
        "produits": produits,
        "categories": categories,
        "categorie_active": categorie_active,
        "formulaire": formulaire,
    })


def detail_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk, disponible=True)
    return render(request, "boutique/detail.html", {"produit": produit})


def construire_lignes(request):
    contenu_panier = request.session.get("panier", {})
    produits = Produit.objects.filter(id__in=contenu_panier.keys(), disponible=True)

    lignes = []
    total = 0
    for produit in produits:
        quantite = contenu_panier[str(produit.id)]
        sous_total = produit.prix * quantite
        total += sous_total
        lignes.append({
            "produit": produit,
            "quantite": quantite,
            "sous_total": sous_total,
        })

    return lignes, total


@require_POST
def ajouter_au_panier(request, pk):
    produit = get_object_or_404(Produit, pk=pk, disponible=True)
    contenu_panier = request.session.get("panier", {})
    cle = str(produit.id)
    contenu_panier[cle] = contenu_panier.get(cle, 0) + 1
    request.session["panier"] = contenu_panier
    return redirect("panier")


@require_POST
def retirer_du_panier(request, pk):
    contenu_panier = request.session.get("panier", {})
    contenu_panier.pop(str(pk), None)
    request.session["panier"] = contenu_panier
    return redirect("panier")


def panier(request):
    lignes, total = construire_lignes(request)
    return render(request, "boutique/panier.html", {
        "lignes": lignes,
        "total": total,
    })


def commander(request):
    lignes, total = construire_lignes(request)
    if not lignes:
        return redirect("panier")

    if request.method == "POST":
        formulaire = CommandeForm(request.POST)
        if formulaire.is_valid():
            with transaction.atomic():
                commande = formulaire.save(commit=False)
                commande.total = total
                commande.save()
                for ligne in lignes:
                    LigneCommande.objects.create(
                        commande=commande,
                        produit=ligne["produit"],
                        nom_produit=ligne["produit"].nom,
                        prix_unitaire=ligne["produit"].prix,
                        quantite=ligne["quantite"],
                    )
            request.session["panier"] = {}
            request.session["derniere_commande"] = commande.id
            return redirect("confirmation_commande", pk=commande.id)
    else:
        formulaire = CommandeForm()

    return render(request, "boutique/commande.html", {
        "lignes": lignes,
        "total": total,
        "formulaire": formulaire,
    })


def confirmation_commande(request, pk):
    if request.session.get("derniere_commande") != pk:
        return redirect("accueil")
    commande = get_object_or_404(Commande, pk=pk)
    return render(request, "boutique/confirmation.html", {"commande": commande})