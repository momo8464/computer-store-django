# Computer Store

Boutique en ligne de matériel informatique, réalisée avec **Django** dans le cadre de mon apprentissage du développement web.

Le site est parti d'une page HTML/CSS statique, que j'ai rendue dynamique : les produits viennent d'une base de données, les visiteurs peuvent remplir un panier et passer commande, et tout se gère depuis l'interface d'administration de Django.

## Fonctionnalités

- Catalogue de produits géré depuis l'administration (catégories, prix, images, badges)
- Filtre des produits par catégorie
- Page de détail pour chaque produit
- Panier basé sur les sessions, avec compteur dans le menu
- Validation de commande (nom, téléphone, adresse de livraison) avec page de confirmation
- Suivi des commandes dans l'administration (statuts : en attente, confirmée, livrée, annulée)
- Formulaire de contact : les messages sont enregistrés en base de données
- Design responsive (ordinateur, tablette, téléphone)

## Technologies

- Python 3
- Django 6.1
- SQLite (base de données de développement)
- HTML5 et CSS3
- Pillow (gestion des images)

## Installation

Prérequis : Python 3 et Git installés.

```bash
git clone https://github.com/momo8464/computer-store-django.git
cd computer-store-django

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / Mac

pip install -r requirements.txt

python manage.py migrate
python -X utf8 manage.py loaddata demo
python manage.py createsuperuser
python manage.py runserver
```

Le site est alors disponible sur http://127.0.0.1:8000 et l'administration sur http://127.0.0.1:8000/admin.

La commande `loaddata demo` charge 4 catégories et 6 produits de démonstration, avec leurs images. D'autres produits peuvent être ajoutés depuis l'administration.

## Structure du projet

```
Computer store/
├── config/              # Configuration du projet Django
├── boutique/            # Application principale
│   ├── models.py        # Categorie, Produit, Message, Commande, LigneCommande
│   ├── views.py         # Accueil, détail, panier, commande
│   ├── forms.py         # Formulaires de contact et de commande
│   ├── urls.py          # Adresses du site
│   ├── admin.py         # Configuration de l'administration
│   ├── templates/       # Pages HTML (base.html et pages enfants)
│   └── static/          # CSS et images du site
├── manage.py
└── requirements.txt
```

## Ce que ce projet m'a appris

- Le modèle MVT de Django (modèles, vues, templates) et les migrations
- L'administration de Django et la personnalisation de ses écrans
- L'héritage de templates et les formulaires avec validation
- Les sessions (panier) et la protection CSRF
- Git et GitHub pour versionner et publier un projet

## Auteur

Koné Mohamed, étudiant en BTS Informatique Développeur d'Applications (IDA) à l'ETIC.