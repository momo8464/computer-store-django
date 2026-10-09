from django.contrib import admin
from .models import Categorie, Produit, Message, Commande, LigneCommande

admin.site.register(Categorie)
admin.site.register(Produit)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email", "date_envoi")


class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 0
    can_delete = False
    readonly_fields = ("produit", "nom_produit", "prix_unitaire", "quantite")

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ("id", "prenom", "nom", "telephone", "total", "statut", "date_commande")
    list_filter = ("statut",)
    list_editable = ("statut",)
    readonly_fields = ("total", "date_commande")
    inlines = [LigneCommandeInline]