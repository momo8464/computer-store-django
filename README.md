# 💻 COMPUTER STORE

Bienvenue sur **Computer Store**, un site web moderne de présentation de matériel informatique.

Le projet a été conçu avec une approche orientée **UI/UX**, afin de proposer une interface claire, moderne, responsive et agréable à utiliser.

Computer Store présente une sélection d'ordinateurs adaptés aux **études, au travail, aux projets professionnels et au divertissement**.

---

## 📌 Présentation du projet

**Computer Store** est un site web de présentation de produits informatiques.

Le site permet aux utilisateurs de découvrir différents ordinateurs et de naviguer facilement entre plusieurs sections grâce à une interface simple et structurée.

Le projet contient notamment :

* 🏠 Une section d'accueil moderne avec un **Hero**
* ℹ️ Une section **À propos**
* ⚡ Une section présentant les **avantages de Computer Store**
* 💻 Une section de présentation des **produits**
* 🏷️ Des cartes produits avec prix et badges
* 📩 Un formulaire de contact
* 📞 Des informations de contact
* 🦶 Un footer complet avec navigation et coordonnées

---

# 🎯 Objectifs du projet

Ce projet a été réalisé afin de mettre en pratique différentes compétences en développement web.

Les principaux objectifs sont :

* Créer une interface moderne et professionnelle
* Améliorer l'expérience utilisateur
* Organiser correctement une page HTML
* Utiliser des balises HTML sémantiques
* Créer une mise en page responsive
* Utiliser Flexbox et CSS Grid
* Améliorer l'accessibilité du site
* Organiser proprement le code HTML et CSS
* Préparer le projet pour une évolution future avec JavaScript

L'objectif principal est de créer un site :

> **Simple, moderne, responsive et agréable à utiliser.**

---

# 🛠️ Technologies utilisées

| Technologie   | Utilisation                           |
| ------------- | ------------------------------------- |
| HTML5         | Structure du site                     |
| CSS3          | Design et mise en page                |
| Flexbox       | Alignement des éléments               |
| CSS Grid      | Organisation des produits et sections |
| Media Queries | Adaptation aux différents écrans      |
| Variables CSS | Gestion des couleurs                  |
| Git           | Gestion des versions                  |
| GitHub        | Hébergement du code                   |
| GitHub Pages  | Mise en ligne du site                 |

---

# 🧱 Structure du site

Le site est organisé autour de plusieurs sections principales.

```text
HEADER
│
├── Logo
│
└── Navigation
    ├── Accueil
    ├── À propos
    ├── Produits
    └── Contact


MAIN
│
├── 🏠 Accueil / Hero
│
├── ℹ️ À propos
│
├── ⚡ Nos avantages
│
├── 💻 Nos produits
│
└── 📩 Contact


FOOTER
│
├── Présentation de Computer Store
│
├── Navigation
│
├── Informations de contact
│
└── Copyright
```

---

# 🏠 Section Accueil

La page commence par une section **Hero** moderne.

Elle contient :

* un badge de présentation ;
* un titre principal ;
* une description ;
* un bouton vers les produits ;
* un bouton pour découvrir davantage le site ;
* une image représentant un ordinateur.

Exemple :

```text
💻 Votre partenaire informatique

La technologie adaptée
à vos besoins.

[ Découvrir nos produits ]  [ En savoir plus ]
```

Cette section permet à l'utilisateur de comprendre rapidement l'objectif du site dès son arrivée.

---

# ℹ️ Section À propos

La section **À propos** présente Computer Store et son objectif.

Elle explique que le site propose du matériel informatique destiné :

* aux étudiants ;
* aux professionnels ;
* aux passionnés de technologie ;
* aux utilisateurs recherchant du matériel adapté à leurs besoins.

La section contient également un lien permettant d'accéder directement aux produits.

---

# ⚡ Pourquoi choisir Computer Store ?

Une nouvelle section présente les principaux avantages de Computer Store.

Elle met en avant trois éléments :

### ⚡ Performance

Des ordinateurs adaptés aux tâches quotidiennes et aux besoins plus exigeants.

### ✓ Qualité

Une sélection de matériel pensée pour proposer une expérience fiable et agréable.

### 💬 Accompagnement

Une aide permettant aux utilisateurs de mieux choisir le matériel correspondant à leurs besoins.

Cette section améliore l'expérience utilisateur en présentant clairement les points forts du site.

---

# 💻 Section Produits

La section Produits présente différents ordinateurs sous forme de **cartes modernes**.

Chaque carte peut contenir :

* une image ;
* un badge, par exemple **Nouveau** ;
* le nom du produit ;
* une description ;
* le prix ;
* un bouton d'action.

Exemple :

```text
┌────────────────────────────┐
│         NOUVEAU            │
│                            │
│       🖥️ IMAGE PRODUIT      │
│                            │
├────────────────────────────┤
│ Ordinateur portable        │
│                            │
│ Description du produit...  │
│                            │
│ 250 000 FCFA               │
│                            │
│      [ Acheter → ]         │
└────────────────────────────┘
```

Les produits sont organisés à l'aide de **CSS Grid** afin de s'adapter automatiquement aux différentes tailles d'écran.

---

# 🎨 Design et approche UI/UX

Le nouveau design du site a été pensé pour être :

* ✨ moderne ;
* 💻 professionnel ;
* 📱 responsive ;
* 🎯 facile à comprendre ;
* 🧭 simple à naviguer ;
* 👀 agréable visuellement.

L'interface utilise notamment :

* des espaces réguliers entre les éléments ;
* des cartes avec coins arrondis ;
* des boutons visuellement distincts ;
* des effets au survol ;
* une hiérarchie claire entre les titres et les textes ;
* des sections bien séparées ;
* des couleurs cohérentes.

L'objectif est d'améliorer à la fois l'apparence du site et l'expérience de l'utilisateur.

---

# 🎨 Identité visuelle

Le site utilise principalement une identité visuelle basée sur des couleurs modernes.

Les variables CSS permettent de centraliser la gestion des couleurs.

Exemple :

```css
:root {
    --orange-principal: #F5A900;
    --vert: #007900;
    --blanc: #FFFFFF;
    --noir: #222222;
    --gris: #F3F3F3;
}
```

### 🟠 Orange

Utilisé pour mettre en avant certains éléments importants de l'interface et renforcer l'identité visuelle du site.

### 🟢 Vert

Utilisé principalement pour les actions importantes, certains boutons et éléments interactifs.

### ⚪ Blanc

Permet de garder une interface claire, propre et facile à lire.

### ⚫ Noir et gris

Utilisés pour les textes, les descriptions et la création d'une bonne hiérarchie visuelle.

---

# 📩 Section Contact

La section Contact permet à l'utilisateur d'envoyer un message.

Le formulaire contient notamment :

* Nom
* Prénom
* Adresse e-mail
* Numéro de téléphone
* Message

Les champs utilisent des balises `label` afin d'améliorer l'accessibilité.

Exemple :

```html
<label for="mail">
    Adresse e-mail
</label>

<input
    type="email"
    id="mail"
    name="mail"
    placeholder="exemple@email.com"
    autocomplete="email"
    required
>
```

Le formulaire propose également deux boutons :

* **Envoyer le message**
* **Effacer**

⚠️ Pour le moment, le formulaire est uniquement présent côté front-end. Les informations ne sont pas encore envoyées vers un serveur.

---

# 🦶 Footer

Le footer a été amélioré afin de fournir davantage d'informations.

Il contient :

### Computer Store

Une courte présentation du site.

### Navigation

Des liens vers les différentes sections :

* Accueil
* À propos
* Produits
* Contact

### Contact

Les informations permettant de contacter Computer Store :

* 📧 Adresse e-mail
* 📞 Numéro de téléphone

Le bas du footer contient également les informations de copyright.

---

# ♿ Accessibilité

Plusieurs bonnes pratiques d'accessibilité sont utilisées dans le projet.

Notamment :

* utilisation de balises HTML sémantiques ;
* utilisation de `alt` pour les images ;
* utilisation de `label` pour les champs du formulaire ;
* utilisation de `aria-label` lorsque nécessaire ;
* utilisation de `aria-hidden="true"` pour certains éléments décoratifs ;
* champs obligatoires avec `required` ;
* utilisation de `autocomplete` pour améliorer le remplissage du formulaire.

Exemple :

```html
<a
    href="#accueil"
    class="logo"
    aria-label="Retour à l'accueil"
>
```

L'attribut `aria-label` permet notamment aux technologies d'assistance de mieux comprendre la fonction du lien.

---

# 📱 Responsive Design

Le site est conçu pour fonctionner sur plusieurs tailles d'écran.

## 🖥️ Ordinateur

Sur les grands écrans :

* les sections utilisent plusieurs colonnes ;
* les produits sont organisés en grille ;
* les éléments sont disposés horizontalement lorsque cela améliore la lisibilité.

## 📱 Tablette

Sur tablette :

* certaines grilles passent à moins de colonnes ;
* les espacements sont adaptés ;
* la navigation reste accessible.

## 📱 Téléphone

Sur téléphone :

* les sections passent progressivement sur une seule colonne ;
* les boutons restent faciles à utiliser ;
* les images s'adaptent à la largeur de l'écran ;
* le contenu reste lisible.

Cette adaptation est réalisée grâce aux **Media Queries CSS**.

---

# 📁 Structure du projet

```text
Computer-Store/
│
├── index.html
│
├── css/
│   └── main.css
│
├── img/
│   ├── logo computeur store.png
│   ├── pc.png
│   ├── ordinateur.png
│   ├── OIP.webp
│   ├── Desktop-Computer-PNG-Free-Download.png
│   ├── 61qN9d08hgL._AC_SL1500_.jpg
│   └── 61rrbeZa4WL._AC_.jpg
│
└── README.md
```

---

# 🧩 Fonctionnalités actuelles

Le site propose actuellement :

* ✅ Navigation entre les différentes sections
* ✅ Défilement fluide
* ✅ Section Hero moderne
* ✅ Présentation de Computer Store
* ✅ Section avantages
* ✅ Présentation des produits
* ✅ Cartes produits
* ✅ Badges sur certains produits
* ✅ Boutons d'action
* ✅ Formulaire de contact
* ✅ Bouton d'envoi
* ✅ Bouton de réinitialisation
* ✅ Liens e-mail et téléphone
* ✅ Design responsive
* ✅ Effets au survol
* ✅ Utilisation de bonnes pratiques d'accessibilité
* ✅ Structure HTML sémantique
* ✅ Mise en ligne possible avec GitHub Pages

---

# ⚠️ Fonctionnalités à développer

Le projet est actuellement principalement un projet **Front-End**.

Certaines fonctionnalités pourraient être ajoutées dans le futur.

Par exemple :

* 🛒 Panier d'achat
* 💳 Système de paiement
* 🔐 Authentification des utilisateurs
* 📦 Gestion des commandes
* 🗄️ Base de données
* 📩 Traitement réel du formulaire
* 🔎 Recherche de produits
* 🏷️ Système de catégories
* ❤️ Liste de favoris
* 🌙 Mode sombre
* ⚡ Ajout de JavaScript
* 🔧 Ajout d'un backend

---

# 🚀 Évolution possible du projet

Le projet peut progressivement évoluer vers une véritable plateforme de vente en ligne.

```text
HTML + CSS
      ↓
Site vitrine
      ↓
Présentation des produits
      ↓
JavaScript
      ↓
Interactivité
      ↓
Panier
      ↓
Backend
      ↓
Base de données
      ↓
Gestion des utilisateurs
      ↓
Commandes
      ↓
Paiement
```

---

# 🔧 Installation en local

## 1. Cloner le projet

```bash
git clone URL_DU_REPOSITORY
```

## 2. Entrer dans le dossier

```bash
cd Computer-Store
```

## 3. Ouvrir le projet

Ouvrez le fichier :

```text
index.html
```

Vous pouvez l'ouvrir avec un navigateur comme :

* Google Chrome
* Microsoft Edge
* Mozilla Firefox

Vous pouvez également utiliser **Visual Studio Code** avec une extension permettant de lancer le projet localement.

---

# 🌐 Mise en ligne avec GitHub Pages

Le projet peut être publié gratuitement avec GitHub Pages.

Les étapes principales sont :

1. Créer un dépôt GitHub.
2. Ajouter le fichier `index.html`.
3. Ajouter les dossiers `css` et `img`.
4. Ajouter le fichier `README.md`.
5. Envoyer les fichiers sur GitHub.
6. Ouvrir les paramètres du dépôt.
7. Aller dans la section **Pages**.
8. Sélectionner la branche principale.
9. Sélectionner le dossier contenant le fichier `index.html`.
10. Enregistrer.

GitHub Pages génère ensuite une version accessible en ligne du site.

---

# 📚 Compétences mises en pratique

## HTML5

Le projet permet de travailler avec :

* la structure d'une page web ;
* les balises sémantiques ;
* les sections ;
* les liens ;
* les images ;
* les formulaires ;
* les attributs `id` et `class` ;
* les attributs `alt` ;
* les attributs `aria-label`.

## CSS3

Le projet permet également de pratiquer :

* les sélecteurs CSS ;
* les variables CSS ;
* les couleurs ;
* les marges ;
* le `padding` ;
* Flexbox ;
* CSS Grid ;
* le Responsive Design ;
* les Media Queries ;
* les transitions ;
* les effets au survol ;
* les bordures arrondies ;
* les ombres ;
* l'organisation d'une interface moderne.

---

# 👨‍💻 Auteur

**Koné Mohamed**

Développeur Web Front-End en formation.

Ce projet a été réalisé dans le cadre de mon apprentissage du développement web afin de mettre en pratique mes connaissances en :

* HTML5
* CSS3
* Responsive Design
* UI/UX
* Accessibilité web
* Organisation d'un projet web

---

# 📄 Licence

Ce projet est réalisé dans un objectif d'apprentissage et de démonstration.

Vous pouvez consulter le code et vous en inspirer pour vos propres projets.

---

# ⭐ Conclusion

**Computer Store** est un projet qui évolue progressivement.

Il représente une étape dans mon apprentissage du développement web et pourra être amélioré avec de nouvelles technologies et fonctionnalités.

> **Computer Store — La technologie adaptée à vos besoins.** 💻🚀
