def panier_compteur(request):
    contenu_panier = request.session.get("panier", {})
    return {"panier_compteur": sum(contenu_panier.values())}