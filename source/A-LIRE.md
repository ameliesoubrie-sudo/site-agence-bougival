# Site de l'agence Gan Assurances Bougival Morisot

Site 100 % statique : 26 pages publiques, aucune base de données.
Couleurs : bleu #1f5fb0, jaune #f2a81d, noir #15181d (variables en haut de static/css/style.css).

## Publication (GitHub Pages)

Le dossier `docs/` est le site publié. Réglage à faire une seule fois sur GitHub :
Settings > Pages > Source : "Deploy from a branch" > Branch : `main`, dossier `/docs` > Save.

Adresse du site : https://www.assurance-bougival.fr/ (fichier CNAME dans static/)

Le reste (build.py, content_*.py, static/) sert à régénérer `docs/` avec `python3 build.py`.

## Réglages (en haut de build.py, bloc CONFIG)

1. `preview` : True tant que le site est en validation (Google ne l'indexe pas). À passer à False le jour de la mise en ligne publique.
2. `site_url` : à remplacer par le vrai nom de domaine le jour de la mise en ligne.
3. `form_email` : l'adresse qui reçoit les demandes du formulaire (service formsubmit.co, sans clé). À la toute première demande envoyée, FormSubmit adresse un email d'activation à cette adresse : il faut cliquer sur le lien une fois, sinon rien n'arrive.
4. `has_agence` : passer à True après avoir déposé `agence-bougival.jpg` (horizontal, 1200 x 900 px environ) dans `static/images/`.

## Modifier un texte

Tous les textes sont dans `content_main.py` (accueil, agence, avis, contact, pages légales),
`content_products.py` (9 pages produits) et `content_local.py` (5 pages villes, 3 articles).
Après modification : `python3 build.py`.

## À compléter ou valider par Willy

Les encadrés jaunes visibles sur le site signalent ce qui manque. Ils sont à supprimer une fois traités.

- Page L'agence : son parcours, l'année d'installation, l'équipe (prénoms, rôles, photos)
- Mentions légales : forme juridique, SIRET, email, capital et RCS de Gan Assurances, hébergeur (le texte indique Vercel, à remplacer par GitHub si le site reste sur GitHub Pages)
- Confidentialité : durée de conservation des données
- Avis : reprise éventuelle de vrais avis Google, avec l'accord des clients
- Toutes les pages produits : vérifier que chaque garantie citée correspond bien à ce que l'agence propose
- Engagements commerciaux écrits dans les textes : "bilan gratuit et sans engagement", déplacements chez le client, rendez-vous à domicile
- Note Google (4,9/5, 13 avis au 17/11/2026) : à mettre à jour de temps en temps
- Accord de la compagnie sur l'usage de la marque et des couleurs

## Le jour de la mise en ligne publique

- Brancher le nom de domaine (Settings > Pages > Custom domain)
- `preview` à False, `site_url` au vrai domaine, puis `python3 build.py`
- Déclarer le site dans Google Search Console et y envoyer `sitemap.xml`
- Faire pointer la fiche Google de l'agence vers le nouveau site
