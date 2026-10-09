from django import forms
from .models import Message, Commande


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["nom", "prenom", "email", "telephone", "contenu"]
        widgets = {
            "nom": forms.TextInput(attrs={
                "placeholder": "Votre nom",
                "autocomplete": "family-name",
            }),
            "prenom": forms.TextInput(attrs={
                "placeholder": "Votre prénom",
                "autocomplete": "given-name",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "exemple@email.com",
                "autocomplete": "email",
            }),
            "telephone": forms.TextInput(attrs={
                "placeholder": "+225 05 84 64 34 99",
                "autocomplete": "tel",
            }),
            "contenu": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Écrivez votre message...",
            }),
        }


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ["nom", "prenom", "telephone", "adresse"]
        widgets = {
            "nom": forms.TextInput(attrs={
                "placeholder": "Votre nom",
                "autocomplete": "family-name",
            }),
            "prenom": forms.TextInput(attrs={
                "placeholder": "Votre prénom",
                "autocomplete": "given-name",
            }),
            "telephone": forms.TextInput(attrs={
                "placeholder": "+225 05 84 64 34 99",
                "autocomplete": "tel",
            }),
            "adresse": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Commune, quartier, repère pour la livraison...",
            }),
        }