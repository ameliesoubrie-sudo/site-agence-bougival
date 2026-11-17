#!/usr/bin/env python3
"""Generateur du site statique. Lancer : python3 build.py  -> dossier docs/ (publie par GitHub Pages)"""
import json, shutil, html, datetime
from pathlib import Path

# ------------------------------------------------------------------ A REGLER
CONFIG = {
    "site_url": "https://ameliesoubrie-sudo.github.io/site-agence-bougival",   # sans / final ; a remplacer par le vrai domaine
    "preview": True,         # True = site en validation, non indexe par Google. Passer a False a la mise en ligne publique
    "form_key": "CLE_WEB3FORMS_A_COLLER_ICI",      # cle publique web3forms.com
    "has_portrait": True,   # True quand static/images/willy-guillaume.jpg existe
    "has_agence": False,     # True quand static/images/agence-bougival.jpg existe
}
# ---------------------------------------------------------------------------

A = {
    "name": "Gan Assurances Bougival Morisot",
    "agent": "Willy Guillaume",
    "street": "23 quai Georges Clemenceau",
    "zip": "78380", "city": "Bougival",
    "tel": "01 30 78 14 10", "tel_link": "+33130781410",
    "orias": "07015028",
    "maps": "https://www.google.com/maps/search/?api=1&query=Gan+Assurances+Bougival+Morisot+23+Quai+Georges+Clemenceau+78380+Bougival",
    "client": "https://www.gan.fr/",
}

ROOT = Path(__file__).parent
DIST = ROOT / "docs"

PART = [
    ("assurance-auto-moto", "Auto et deux-roues", "Voiture, moto, scooter, trottinette : la bonne formule pour votre usage réel."),
    ("assurance-habitation", "Habitation", "Locataire, propriétaire ou bailleur : votre logement et vos biens bien couverts."),
    ("mutuelle-sante-prevoyance", "Santé et prévoyance", "Une complémentaire santé adaptée, et vos proches protégés en cas de coup dur."),
    ("epargne-retraite", "Épargne et retraite", "Assurance vie, plan d'épargne retraite : faire travailler votre argent, à votre rythme."),
    ("assurance-emprunteur", "Assurance emprunteur", "Assurer votre prêt immobilier, ou changer d'assurance en cours de prêt."),
]
PRO = [
    ("assurance-artisans-commercants", "Artisans et commerçants", "Local, stock, matériel, responsabilité : votre activité protégée au quotidien."),
    ("assurance-professions-liberales", "Professions libérales", "Responsabilité civile professionnelle, cabinet, cyber-risques."),
    ("protection-dirigeant", "Protection du dirigeant", "Prévoyance, retraite, perte d'emploi : ce que votre statut ne couvre pas."),
    ("sante-collective-flotte", "Santé collective et flotte auto", "Mutuelle d'entreprise, prévoyance des salariés, véhicules de la société."),
]
VILLES = [
    ("assurance-bougival", "Bougival"),
    ("assurance-la-celle-saint-cloud", "La Celle-Saint-Cloud"),
    ("assurance-louveciennes", "Louveciennes"),
    ("assurance-croissy-sur-seine", "Croissy-sur-Seine"),
    ("assurance-rueil-malmaison", "Rueil-Malmaison"),
]

def e(s): return html.escape(s, quote=True)

def _i(body):
    return ('<svg class="ico" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="#16264f" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + body + '</svg>')
Y = 'fill="#f5b921"'
ICONS = {
    "assurance-auto-moto": _i(f'<path d="M7 28l3.5-9.5A4 4 0 0 1 14.3 16h19.4a4 4 0 0 1 3.8 2.5L41 28v9H7z"/><path d="M7 28h34"/><circle cx="15" cy="37" r="4.5" {Y}/><circle cx="33" cy="37" r="4.5" {Y}/>'),
    "assurance-habitation": _i(f'<path d="M6 23L24 8l18 15"/><path d="M11 20v20h26V20"/><rect x="20" y="28" width="8" height="12" {Y}/>'),
    "mutuelle-sante-prevoyance": _i(f'<path d="M24 5l15 5v12c0 10-6 17-15 21-9-4-15-11-15-21V10z"/><path d="M21.5 16h5v5.5H32v5h-5.5V32h-5v-5.5H16v-5h5.5z" {Y}/>'),
    "epargne-retraite": _i(f'<path d="M6 41h36"/><rect x="9" y="29" width="7" height="12"/><rect x="20.5" y="22" width="7" height="19"/><rect x="32" y="13" width="7" height="28" {Y}/><path d="M9 19l9-6 7 3 9-9"/>'),
    "assurance-emprunteur": _i(f'<circle cx="15" cy="24" r="8"/><circle cx="15" cy="24" r="2.8" {Y}/><path d="M23 24h19M36 24v7M42 24v5"/>'),
    "assurance-artisans-commercants": _i(f'<path d="M8 18l3-9h26l3 9"/><path d="M8 18a4 4 0 0 0 8 0 4 4 0 0 0 8 0 4 4 0 0 0 8 0 4 4 0 0 0 8 0"/><path d="M11 23v17h26V23"/><rect x="26" y="29" width="7" height="11" {Y}/><rect x="15" y="29" width="7" height="6"/>'),
    "assurance-professions-liberales": _i(f'<rect x="6" y="16" width="36" height="24" rx="3"/><path d="M17 16v-4a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v4"/><path d="M6 27h36"/><rect x="21" y="24" width="6" height="6" {Y}/>'),
    "protection-dirigeant": _i(f'<circle cx="24" cy="15" r="7.5" {Y}/><path d="M9 41c0-8.5 6.5-14 15-14s15 5.5 15 14z"/>'),
    "sante-collective-flotte": _i(f'<circle cx="15" cy="17" r="5.5"/><circle cx="33" cy="17" r="5.5" {Y}/><path d="M5 39c0-6.5 4.5-11 10-11s10 4.5 10 11"/><path d="M23 39c0-6.5 4.5-11 10-11s10 4.5 10 11"/>'),
    "pin": _i(f'<path d="M24 43s14-12.5 14-24a14 14 0 0 0-28 0c0 11.5 14 24 14 24z"/><circle cx="24" cy="19" r="5" {Y}/>'),
    "chat": _i(f'<path d="M7 9h34v23H23l-9 8v-8H7z"/><path d="M15 17h18M15 24h11" stroke="#f5b921"/>'),
    "doc": _i(f'<path d="M12 5h17l8 8v30H12z"/><path d="M29 5v8h8"/><path d="M18 28l5 5 8-10" stroke="#f5b921" stroke-width="3"/>'),
    "phone": _i(f'<rect x="14" y="4" width="20" height="40" rx="4"/><circle cx="24" cy="37" r="2.2" {Y}/><path d="M20 10h8"/>'),
    "shield": _i(f'<path d="M24 5l15 5v12c0 10-6 17-15 21-9-4-15-11-15-21V10z"/><path d="M17 24l5 5 9-10" stroke="#f5b921" stroke-width="3"/>'),
}
ICONS["person"] = ICONS["protection-dirigeant"]
ICONS["duo"] = ICONS["sante-collective-flotte"]
def icon(k): return f'<span class="blob">{ICONS[k]}</span>' if k in ICONS else ""

def tiles(items):
    return '<div class="tiles">' + "".join(f'<a class="tile" href="{{R}}{s}/">{icon(s)}<span>{e(n)}</span></a>' for s, n, *_ in items) + "</div>"


def url(slug):
    return CONFIG["site_url"] + "/" + (slug + "/" if slug else "")

def base_schema():
    return {
        "@context": "https://schema.org", "@type": "InsuranceAgency",
        "@id": CONFIG["site_url"] + "/#agence",
        "name": A["name"] + " - " + A["agent"],
        "url": CONFIG["site_url"] + "/",
        "telephone": A["tel_link"],
        "address": {"@type": "PostalAddress", "streetAddress": A["street"], "postalCode": A["zip"],
                    "addressLocality": A["city"], "addressCountry": "FR"},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": o, "closes": c}
            for o, c in (("09:00", "12:30"), ("14:00", "18:30"))],
        "areaServed": [v[1] for v in VILLES] + ["Marly-le-Roi", "Le Port-Marly", "Chatou"],
        "founder": {"@type": "Person", "name": A["agent"], "jobTitle": "Agent général d'assurance"},
    }

def crumbs_html(crumbs):
    if not crumbs: return ""
    parts = ['<a href="{R}">Accueil</a>']
    for label, slug in crumbs:
        parts.append(f'<a href="{{R}}{slug}/">{e(label)}</a>' if slug else f'<span aria-current="page">{e(label)}</span>')
    return '<nav class="crumbs" aria-label="Fil d\'Ariane">' + " / ".join(parts) + "</nav>"

def crumbs_schema(crumbs, slug):
    items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": url("")}]
    for i, (label, s) in enumerate(crumbs, 2):
        items.append({"@type": "ListItem", "position": i, "name": label, "item": url(s if s else slug)})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

WAVES = '<svg class="waves" viewBox="0 0 1200 46" preserveAspectRatio="none" aria-hidden="true"><path d="M0 22c100-22 200 22 300 0s200-22 300 0 200 22 300 0 200-22 300 0v24H0z" fill="#f6f7f9"/></svg>'

SCENE = '''<svg viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<circle cx="285" cy="118" r="44" fill="#fff3d0"/>
<path d="M0 172c60-34 120-30 180-8s150 20 220-18v30H0z" fill="#5b8fd0"/>
<path d="M0 176h400v20H0z" fill="#3f77c2"/>
<g fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="3" stroke-linecap="round">
<path d="M30 240c22-10 44 10 66 0s44-10 66 0"/><path d="M210 290c22-10 44 10 66 0s44-10 66 0"/>
<path d="M60 350c22-10 44 10 66 0s44-10 66 0"/><path d="M230 410c22-10 44 10 66 0s44-10 66 0"/>
<path d="M40 455c22-10 44 10 66 0"/></g>
<path d="M118 196l34-26h52l30 26z" fill="#15181d"/><path d="M178 170V120l34 44z" fill="#fffdf8"/></svg>'''

def hero(p):
    h = p["hero"]; t = h["type"]
    cr = crumbs_html(p.get("crumbs"))
    kicker = f'<span class="kicker">{h["kicker"]}</span>' if (h.get("kicker") and t == "home") else ""
    lead = f'<p class="lead">{h["lead"]}</p>' if h.get("lead") else ""
    call = f'<a class="btn btn-main" href="{{R}}contact/">Être rappelé</a><a class="btn btn-ghost" href="tel:{A["tel_link"]}">{A["tel"]}</a>'
    if t == "home":
        img = '<img src="{R}images/willy-guillaume.jpg" alt="Willy Guillaume, agent général Gan Assurances à Bougival" width="800" height="1000" fetchpriority="high">' if CONFIG["has_portrait"] else SCENE
        return f'''<section class="hero-home on-dark"><div class="wrap grid"><div>{kicker}<h1>{h["h1"]}</h1>{lead}<div class="btn-row">{call}</div>
<ul class="checks"><li>Devis gratuit</li><li>Un seul interlocuteur</li><li>Suivi de vos sinistres à l'agence</li></ul></div>
<div class="scene-wrap"><div class="scene">{img}</div>
<span class="chip2"><svg viewBox="0 0 48 48" width="20" height="20" fill="none" stroke="#16264f" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M24 43s14-12.5 14-24a14 14 0 0 0-28 0c0 11.5 14 24 14 24z"/><circle cx="24" cy="19" r="4.5" fill="#f5b921"/></svg>Sur le quai, à Bougival</span>
<a class="badge" href="{{R}}avis-clients/" style="text-decoration:none"><span class="stars" aria-hidden="true">★★★★★</span><b>4,9/5</b><small>13 avis clients sur Google</small></a></div></div>
<div class="strip"><div class="wrap">
<div>{icon("person")}<p><b>Un interlocuteur unique</b><span>Vous savez à qui vous parlez, du devis au sinistre.</span></p></div>
<div>{icon("pin")}<p><b>À deux pas de chez vous</b><span>Sur le quai, à Bougival, avec un parking tout près.</span></p></div>
<div>{icon("duo")}<p><b>Particuliers et pros</b><span>Vie privée et activité, au même endroit.</span></p></div>
<div>{icon("shield")}<p><b>La solidité d'un grand groupe</b><span>Gan Assurances, groupe Groupama.</span></p></div>
</div></div></section>'''
    if t == "dark":
        pills = "".join(f'<a href="{{R}}{s}/">{e(n)}</a>' for s, n, _ in h["pills"])
        return f'''<section class="hero-dark on-dark"><div class="wrap grid"><div>{cr}{kicker}<h1>{h["h1"]}</h1>{lead}<div class="btn-row">{call}</div></div>
<div class="pills">{pills}</div></div></section>'''
    if t == "product":
        return f'''<section class="hero-product"><div class="wrap grid"><div>{cr}{icon(p["slug"])}<h1>{h["h1"]}</h1>{lead}</div>
<aside class="quick"><h2>Un devis, une question ?</h2><a class="tel" href="tel:{A["tel_link"]}">{A["tel"]}</a>
<p>Du lundi au vendredi, 9h-12h30 et 14h-18h30. En agence, par téléphone ou sur rendez-vous.</p>
<a class="btn btn-main" href="{{R}}contact/">Demander à être rappelé</a></aside></div></section>'''
    if t == "city":
        return f'''<section class="hero-city on-dark"><div class="wrap">{cr}{kicker}<h1>{h["h1"]}</h1>{lead}<div class="btn-row">{call}</div></div></section>'''
    return f'''<section class="hero-plain"><div class="wrap">{cr}{kicker}<h1>{h["h1"]}</h1>{lead}</div></section>'''

def faq_html(faq):
    if not faq: return ""
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    return f'<section class="sec alt"><div class="wrap"><div class="sec-head"><h2>Questions fréquentes</h2></div><div class="faq prose">{items}</div></div></section>'

def faq_schema(faq):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faq]}

def cta_band(title="Parlons de votre situation", text="Dix minutes au téléphone ou un passage à l'agence suffisent souvent pour y voir clair."):
    return f'''<section class="sec"><div class="wrap"><div class="cta-band"><div><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn btn-main" href="{{R}}contact/">Être rappelé</a><a class="btn btn-ghost" href="tel:{A["tel_link"]}">{A["tel"]}</a></div></div></div></section>'''

def cards(items, more="En savoir plus"):
    return '<div class="cards">' + "".join(
        f'<a class="card" href="{{R}}{s}/">{icon(s)}<h3>{e(n)}</h3><p>{e(d)}</p><span class="more">{more}</span></a>' for s, n, d in items) + "</div>"

def side(p):
    fam = PART if p.get("family") == "part" else PRO
    links = "".join(f'<li><a href="{{R}}{s}/">{e(n)}</a></li>' for s, n, _ in fam if s != p["slug"])
    title = "Pour les particuliers" if fam is PART else "Pour les professionnels"
    return f'''<aside class="side"><div class="box"><h2>{title}</h2><ul>{links}</ul></div>
<div class="box"><h2>L'agence</h2><p style="margin:0;font-size:.95rem">{A["street"]}<br>{A["zip"]} {A["city"]}<br>Parking à proximité<br><a href="tel:{A["tel_link"]}"><strong>{A["tel"]}</strong></a></p></div></aside>'''

def main_html(p):
    k = p.get("kind", "plain")
    body = p["body"]
    if k == "product":
        return (f'<section class="sec"><div class="wrap layout"><div class="prose">{body}</div>{side(p)}</div></section>'
                + faq_html(p.get("faq")) + cta_band())
    if k == "city":
        return (f'<section class="sec"><div class="wrap"><div class="prose">{body}</div></div></section>'
                f'<section class="sec alt"><div class="wrap"><div class="sec-head"><h2>Ce que je peux assurer pour vous</h2></div>{cards(PART[:3] + PRO[:2] + [PART[4]])}</div></section>'
                + faq_html(p.get("faq")) + cta_band())
    if k == "article":
        return f'<section class="sec tight"><div class="wrap"><div class="prose">{body}</div></div></section>' + cta_band("Une question sur votre contrat ?", "Je regarde avec vous ce que prévoit réellement votre contrat.")
    return body

def nav(p):
    cur = lambda s: ' aria-current="page"' if p["slug"] == s else ""
    sub = lambda fam: "".join(f'<li><a href="{{R}}{s}/"{cur(s)}>{e(n)}</a></li>' for s, n, _ in fam)
    return f'''<nav class="nav" id="nav" aria-label="Menu principal"><ul>
<li><a href="{{R}}assurance-particuliers/"{cur("assurance-particuliers")}>Particuliers</a><ul class="sub">{sub(PART)}</ul></li>
<li><a href="{{R}}assurance-professionnels/"{cur("assurance-professionnels")}>Professionnels</a><ul class="sub">{sub(PRO)}</ul></li>
<li><a href="{{R}}agence/"{cur("agence")}>L'agence</a></li>
<li><a href="{{R}}avis-clients/"{cur("avis-clients")}>Avis</a></li>
<li><a href="{{R}}conseils/"{cur("conseils")}>Conseils</a></li>
<li><a class="cta" href="{{R}}contact/">Contact et rendez-vous</a></li></ul></nav>'''

def footer():
    li = lambda fam: "".join(f'<li><a href="{{R}}{s}/">{e(n)}</a></li>' for s, n, *_ in fam)
    villes = "".join(f'<li><a href="{{R}}{s}/">Assurance {e(n)}</a></li>' for s, n in VILLES)
    return f'''<footer class="foot"><div class="wrap"><div class="grid">
<div><a class="brand" href="{{R}}"><b>{A["agent"]}</b><span>Agent général Gan Assurances</span></a>
<p style="margin-top:1.2em">{A["street"]}<br>{A["zip"]} {A["city"]}<br><a href="tel:{A["tel_link"]}">{A["tel"]}</a></p>
<p>Lundi au vendredi<br>9h-12h30 et 14h-18h30</p></div>
<div><h2>Particuliers</h2><ul>{li(PART)}</ul></div>
<div><h2>Professionnels</h2><ul>{li(PRO)}</ul><h2 style="margin-top:1.6em">L'agence</h2><ul><li><a href="{{R}}agence/">Qui sommes-nous</a></li><li><a href="{{R}}avis-clients/">Avis clients</a></li><li><a href="{{R}}conseils/">Conseils</a></li><li><a href="{{R}}contact/">Contact</a></li></ul></div>
<div><h2>Près de chez vous</h2><ul>{villes}</ul><h2 style="margin-top:1.6em">Déjà client</h2><ul><li><a href="{A["client"]}" rel="noopener">Espace client Gan</a></li></ul></div>
</div><div class="legal">{A["agent"]}, agent général d'assurance Gan Assurances, immatriculé à l'ORIAS sous le n° {A["orias"]} (<a href="https://www.orias.fr" rel="noopener">orias.fr</a>).
Site de l'agence {A["name"]}. <a href="{{R}}mentions-legales/">Mentions légales</a> · <a href="{{R}}confidentialite/">Confidentialité</a></div></div></footer>
<div class="callbar"><a href="tel:{A["tel_link"]}">Appeler</a><a href="{{R}}contact/">Être rappelé</a></div>'''

def render(p):
    depth = p["slug"].count("/") + 1 if p["slug"] else 0
    R = "../" * depth if depth else "./"
    schemas = [base_schema()]
    if p.get("crumbs"): schemas.append(crumbs_schema(p["crumbs"], p["slug"]))
    if p.get("faq"): schemas.append(faq_schema(p["faq"]))
    if p.get("kind") == "article":
        schemas.append({"@context": "https://schema.org", "@type": "Article", "headline": p["hero"]["h1"],
                        "author": {"@type": "Person", "name": A["agent"]}, "datePublished": p["date"],
                        "mainEntityOfPage": url(p["slug"]), "publisher": {"@id": CONFIG["site_url"] + "/#agence"}})
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex, nofollow">' if (p.get("noindex") or CONFIG["preview"]) else ""
    out = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
<link rel="canonical" href="{url(p["slug"])}">{robots}
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{e(p["title"])}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:url" content="{url(p["slug"])}">
<meta name="theme-color" content="#16264f">
<link rel="preload" href="{{R}}fonts/archivo-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{{R}}fonts/source-sans-3-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{{R}}css/style.css">
<link rel="icon" href="{{R}}favicon.svg" type="image/svg+xml">
{ld}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="top"><div class="wrap"><span id="open-status">Lundi au vendredi, 9h-12h30 et 14h-18h30</span><span><span class="hide-s">{A["street"]}, {A["city"]} · </span><a href="tel:{A["tel_link"]}">{A["tel"]}</a></span></div></div>
<header class="head"><div class="wrap"><a class="brand" href="{{R}}"><b>{A["agent"]}</b><span>Agent général Gan Assurances · Bougival</span></a>
<button class="burger" aria-expanded="false" aria-controls="nav">Menu</button>{nav(p)}</div></header>
<main id="contenu">
{hero(p)}
{main_html(p)}
</main>
{footer()}
<script src="{{R}}js/site.js" defer></script>
</body>
</html>
'''
    return out.replace("{R}", R).replace("{TEL}", A["tel"]).replace("{TEL_LINK}", A["tel_link"]).replace("{FORM_KEY}", CONFIG["form_key"]).replace("{SITE}", CONFIG["site_url"]).replace("{MAPS}", A["maps"])

def build():
    from content_main import pages as p1
    from content_products import pages as p2
    from content_local import pages as p3
    pages = p1(globals()) + p2(globals()) + p3(globals())
    if DIST.exists(): shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST)
    today = datetime.date.today().isoformat()
    sm = []
    for p in pages:
        d = DIST / p["slug"] if p["slug"] else DIST
        d.mkdir(parents=True, exist_ok=True)
        if p["slug"] == "404":
            (DIST / "404.html").write_text(render(p).replace('href="../', 'href="' + CONFIG["site_url"] + '/').replace('src="../', 'src="' + CONFIG["site_url"] + '/'), encoding="utf-8"); d.rmdir(); continue
        (d / "index.html").write_text(render(p), encoding="utf-8")
        if not p.get("noindex"):
            sm.append(f"<url><loc>{url(p['slug'])}</loc><lastmod>{today}</lastmod></url>")
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(sm) + "\n</urlset>\n", encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {CONFIG['site_url']}/sitemap.xml\n", encoding="utf-8")
    (DIST / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#16264f"/><path d="M12 40c7-6 13 6 20 0s13-6 20 0" fill="none" stroke="#1f5fb0" stroke-width="5" stroke-linecap="round"/><path d="M22 30l6-6h10l6 6z" fill="#fff"/><path d="M33 24V12l8 10z" fill="#f2a81d"/></svg>', encoding="utf-8")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    print(len(pages), "pages")

if __name__ == "__main__":
    build()
