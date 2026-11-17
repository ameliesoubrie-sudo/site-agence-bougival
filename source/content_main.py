def pages(g):
    PART, PRO, ENT, VILLES, cards, cta_band, A, CONFIG, tiles, icon = (g[k] for k in ("PART", "PRO", "ENT", "VILLES", "cards", "cta_band", "A", "CONFIG", "tiles", "icon"))
    def aud(cls, ico, title, text, fam, slug, btn):
        links = "".join(f'<li><a href="{{R}}{s}/">{n}</a></li>' for s, n, _ in fam)
        return f'<article class="aud {cls}">{icon(ico)}<h3>{title}</h3><p>{text}</p><ul>{links}</ul><a class="btn" href="{{R}}{slug}/">{btn}</a></article>'

    ARTICLES = [
        ("conseils/changer-assurance-auto", "Changer d'assurance auto : comment faire sans se tromper", "Résiliation, délais, pièges à éviter : la marche à suivre, étape par étape."),
        ("conseils/degat-des-eaux-bons-reflexes", "Dégât des eaux : les bons réflexes dans les premières heures", "Ce qu'il faut faire tout de suite, et ce qu'il vaut mieux éviter."),
        ("conseils/assurances-obligatoires-artisan-commercant", "Artisan, commerçant : quelles assurances sont vraiment obligatoires ?", "Le point sur ce que la loi impose, et sur ce qui protège réellement votre activité."),
    ]
    villes_links = " ".join(f'<a class="btn btn-ghost" href="{{R}}{s}/">{n}</a>' for s, n in VILLES)
    rating = '''<div class="rating"><div class="num">4,9<small style="font-size:1.6rem">/5</small></div>
<div><div class="stars" aria-hidden="true">★★★★★</div><p style="margin:.3em 0 0"><strong>13 avis clients sur Google.</strong><br>Ce qui revient le plus : la disponibilité, la réactivité et la qualité des conseils.</p></div>
<div class="btn-row" style="margin:0 0 0 auto"><a class="btn btn-ink" href="{MAPS}" rel="noopener">Lire les avis sur Google</a></div></div>'''

    home = f'''
<section class="sec"><div class="wrap">
<div class="sec-head center"><h2><span class="lt">Trois publics,</span> une même exigence</h2><p>Dites-moi qui vous êtes, je vous montre ce que je peux faire pour vous.</p></div>
<div class="auds">
{aud("a1", "house", "Particuliers", "Votre voiture, votre logement, votre santé, votre épargne et vos projets.", PART, "assurance-particuliers", "Je suis un particulier")}
{aud("a2", "case", "Professionnels", "Artisans, commerçants, professions libérales : vous êtes à votre compte.", PRO, "assurance-professionnels", "Je suis indépendant")}
{aud("a3", "building", "Entreprises", "Vous dirigez une société et vous avez des salariés à protéger et à fidéliser.", ENT, "assurance-entreprises", "Je dirige une entreprise")}
</div></div></section>

<section class="sec alt"><div class="wrap split">
<div><h2><span class="lt">Depuis 2005,</span> le même interlocuteur pour toutes vos assurances</h2>
<p>Je suis Willy Guillaume, agent général Gan Assurances à Bougival. Depuis 2005, j'accompagne des particuliers, des professionnels et des dirigeants d'entreprise. Mon métier tient en une phrase : faire en sorte que vous soyez bien couvert le jour où vous en avez besoin, et que vous ne payiez pas pour des garanties qui ne vous servent à rien.</p>
<p>Ici, pas de plateforme téléphonique ni de numéro de dossier à rappeler dix fois. Vous poussez la porte de l'agence, vous m'appelez ou vous prenez rendez-vous. Mon équipe et moi connaissons votre dossier, et c'est nous qui le suivons, y compris quand un sinistre arrive.</p>
<div class="btn-row"><a class="btn btn-ink" href="{{R}}agence/">Découvrir l'agence</a></div></div>
<ul class="rows">
<li>{icon("chat")}<div><b>On fait le point ensemble</b>Vous m'expliquez votre situation, vos contrats actuels, ce qui vous inquiète. Sans jargon.</div></li>
<li>{icon("doc")}<div><b>Je vous propose une solution claire</b>Ce qui est couvert, ce qui ne l'est pas, et combien ça coûte. Vous décidez tranquillement.</div></li>
<li>{icon("phone")}<div><b>Je reste votre interlocuteur</b>Un changement de véhicule, un déménagement, un sinistre : vous savez qui appeler.</div></li>
</ul></div></section>

<section class="sec"><div class="wrap"><div class="sec-head"><h2><span class="lt">Ce sont mes clients</span> qui en parlent le mieux</h2></div>{rating}</div></section>

<section class="sec alt"><div class="wrap split"><div><h2><span class="lt">Une agence pour</span> Bougival et les communes voisines</h2>
<p>L'agence se trouve au {A["street"]}, sur les bords de Seine, avec un parking à proximité. J'accompagne des familles, des indépendants et des entreprises de Bougival et de tout le secteur.</p></div>
<div class="btn-row" style="margin:0">{villes_links}</div></div></section>

<section class="sec"><div class="wrap"><div class="sec-head"><h2><span class="lt">Des réponses simples</span> aux questions qu'on se pose vraiment</h2></div>
{cards(ARTICLES, "Lire l'article")}</div></section>
{cta_band("Un devis, un doute sur un contrat ?", "Laissez-moi vos coordonnées, je vous rappelle. Ou passez nous voir à l'agence.")}'''

    part = f'''
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Vos assurances, contrat par contrat</h2>
<p>Chaque situation est différente : un jeune conducteur n'a pas les mêmes besoins qu'une famille propriétaire de sa maison, ni qu'un couple qui prépare sa retraite. Choisissez le sujet qui vous concerne, ou appelez-moi pour un point complet.</p></div>
{cards(PART)}</div></section>
<section class="sec alt"><div class="wrap split"><div class="prose"><h2>Faire le tri dans ses contrats, ça vaut le coup</h2>
<p>Avec les années, on empile les contrats : l'assurance de la voiture prise chez le concessionnaire, l'habitation souscrite à la banque avec le prêt, la mutuelle de l'ancien employeur. Résultat, on paie parfois deux fois la même garantie, et il reste des trous que personne n'a regardés.</p>
<p>Je vous propose un bilan gratuit et sans engagement de vos contrats. On les passe en revue ensemble, je vous dis franchement ce qui est bien, ce qui fait doublon et ce qui manque. Si vos contrats actuels sont bons, je vous le dis aussi.</p>
<ul><li>Vos garanties correspondent-elles encore à votre vie d'aujourd'hui ?</li><li>Vos franchises sont-elles adaptées à votre budget ?</li><li>Vos proches sont-ils protégés s'il vous arrive quelque chose ?</li></ul></div>
<div class="prose"><h2>Les moments où il faut m'appeler</h2>
<ul><li>Vous achetez une voiture, une moto ou un vélo électrique</li><li>Vous déménagez, vous achetez ou vous mettez un bien en location</li><li>Un enfant arrive, ou quitte la maison pour ses études</li><li>Vous changez de travail, ou vous vous mettez à votre compte</li><li>Vous signez un prêt immobilier</li><li>La retraite approche</li></ul>
<p>Ce sont des étapes où les contrats doivent bouger avec vous. Un coup de fil suffit souvent.</p></div></div></section>
{cta_band("Un bilan de vos contrats ?", "C'est gratuit, sans engagement, et ça prend moins d'une heure.")}'''

    pro = f'''
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Des solutions selon votre métier</h2>
<p>Un boulanger, un architecte et un kinésithérapeute n'ont ni les mêmes risques ni les mêmes obligations. Je commence toujours par comprendre comment vous travaillez avant de parler de contrat.</p></div>
{cards(PRO)}</div></section>
<section class="sec alt"><div class="wrap split"><div class="prose"><h2>Les risques auxquels on pense trop tard</h2>
<p>La plupart des professionnels que je rencontre sont assurés pour leur local et leur responsabilité civile. C'est la base. Mais ce qui met vraiment une entreprise en difficulté, c'est rarement le sinistre lui-même : c'est ce qui se passe après.</p>
<ul><li><strong>L'arrêt d'activité</strong> après un incendie ou un dégât des eaux, pendant que les charges continuent de tomber</li>
<li><strong>L'arrêt de travail du dirigeant</strong>, quand tout repose sur une seule personne</li>
<li><strong>Le piratage informatique</strong> ou la perte de données clients</li>
<li><strong>Le litige</strong> avec un client, un fournisseur ou un salarié</li></ul>
<p>Ce sont ces points que je regarde en priorité avec vous.</p></div>
<div class="prose"><h2>Ma façon de travailler avec les pros</h2>
<ul><li>Je me déplace dans vos locaux si vous le souhaitez, pour voir votre activité telle qu'elle est</li><li>Je vous remets une proposition lisible, garantie par garantie</li><li>Je revois vos contrats quand votre activité évolue : embauche, nouveau local, nouveau matériel</li><li>En cas de sinistre, vous m'appelez directement</li></ul>
<p>Et comme j'assure aussi les particuliers, on peut traiter au même endroit votre activité et votre vie privée. Vous avez des salariés ? Consultez aussi les <a href="{{R}}assurance-entreprises/">solutions pour les entreprises</a>.</p></div></div></section>
{cta_band("Un audit de vos assurances professionnelles ?", "Je passe vos contrats en revue et je vous dis où vous en êtes. Sans engagement.")}'''

    ent = f'''
<section class="sec"><div class="wrap"><div class="sec-head"><h2><span class="lt">Tous les sujets de l'entreprise,</span> un seul interlocuteur</h2>
<p>Une entreprise s'assure sur trois plans : ses biens et sa responsabilité, ses salariés, et son dirigeant. Je les traite ensemble, parce qu'ils sont liés.</p></div>
{cards(ENT)}</div></section>
<section class="sec alt"><div class="wrap split"><div class="prose"><h2>Vos salariés : des obligations, et un levier</h2>
<p>Mutuelle d'entreprise, prévoyance, retraite, épargne salariale : une partie est imposée par la loi ou par votre convention collective, l'autre est un choix. Bien construit, l'ensemble devient un argument pour recruter et garder vos équipes, avec un coût maîtrisé grâce à un cadre social et fiscal favorable.</p>
<ul>
<li><a href="{{R}}mutuelle-entreprise/"><strong>Santé collective</strong></a> : obligatoire dès le premier salarié.</li>
<li><a href="{{R}}prevoyance-collective/"><strong>Prévoyance collective</strong></a> : arrêt de travail, invalidité, décès.</li>
<li><a href="{{R}}epargne-salariale/"><strong>Épargne salariale</strong></a> : intéressement, participation, plan d'épargne.</li>
<li><a href="{{R}}retraite-entreprise/"><strong>Retraite collective</strong></a> : un complément de revenu pour vos salariés et pour vous.</li>
</ul>
<p>Je vérifie la conformité de vos contrats actuels et je vous accompagne dans la mise en place.</p></div>
<div class="prose"><h2>Vous, le dirigeant</h2>
<p>Le chef d'entreprise est souvent le moins bien protégé de sa société. Pas d'assurance chômage, une couverture en cas d'arrêt de travail qui dépend de votre statut, une retraite à construire vous-même.</p>
<ul>
<li><strong>Garantie chômage du dirigeant</strong>, en cas de perte de votre mandat.</li>
<li><strong>Prévoyance</strong> et assurance homme-clé.</li>
<li><strong>Retraite et patrimoine</strong> : optimisation, structuration, transmission.</li>
</ul>
<p>C'est mon domaine de spécialité : je vous propose un bilan complet, que nous revoyons chaque année.</p>
<div class="btn-row"><a class="btn btn-ink" href="{{R}}protection-dirigeant/">Protection du dirigeant</a></div></div></div></section>
{cta_band("Un audit des assurances de votre entreprise ?", "Je passe vos contrats en revue, dans vos locaux, et je vous remets un point clair.")}'''

    photo = '<div class="photo"><img src="{R}images/agence-bougival.jpg" alt="L\'agence Gan Assurances de Bougival, quai Georges Clemenceau" loading="lazy" width="1200" height="900"></div>' if CONFIG["has_agence"] else ""
    agence = f'''
<section class="sec tight"><div class="wrap layout"><div class="prose">
{photo}
<h2>Qui suis-je ?</h2>
<figure class="portrait"><img src="{{R}}images/willy-guillaume.jpg" alt="Willy Guillaume, agent général Gan Assurances à Bougival" width="800" height="1000" loading="lazy"><figcaption>Willy Guillaume<span>Agent général depuis 2005</span></figcaption></figure>
<p>Je m'appelle Willy Guillaume. Agent général Gan Assurances, installé à Bougival, j'accompagne depuis 2005 les particuliers, les professionnels et les dirigeants d'entreprise dans la protection de leur activité, de leurs proches et de leur patrimoine.</p>
<p>Mon métier consiste à rendre les sujets d'assurance clairs, compréhensibles et adaptés à chaque situation. Mon engagement tient en trois points : un suivi dans le temps, une vraie disponibilité et des solutions construites sur mesure.</p>
<p>Être agent général, c'est être un chef d'entreprise indépendant qui représente une compagnie auprès de ses clients. Vous avez la relation directe d'un professionnel de proximité, et derrière, la solidité du groupe.</p>
<h2>Ce qui fonde mon expertise</h2>
<ul>
<li><strong>Plus de 20 ans d'expérience de terrain</strong>, au contact des familles et des entreprises du secteur.</li>
<li><strong>Une connaissance fine des enjeux des dirigeants</strong> : statut, protection sociale, retraite, transmission.</li>
<li><strong>Un accompagnement global</strong>, qui traite ensemble le professionnel et le personnel.</li>
<li><strong>La solidité du groupe Gan Assurances.</strong></li>
</ul>
<h2>Ce que je propose</h2>
<h3>Assurance de personnes</h3>
<ul><li><a href="{{R}}prevoyance/">Prévoyance</a></li><li><a href="{{R}}mutuelle-sante/">Complémentaire santé</a></li><li><a href="{{R}}preparer-retraite/">Retraite</a></li><li><a href="{{R}}epargne-salariale/">Épargne salariale</a></li><li><a href="{{R}}protection-dirigeant/">Protection chômage du dirigeant</a></li><li><a href="{{R}}assurance-emprunteur/">Assurance emprunteur</a></li></ul>
<h3>Assurance de biens et de responsabilité</h3>
<ul><li><a href="{{R}}multirisque-entreprise/">Multirisque professionnelle</a></li><li>Responsabilité civile</li><li>Assurance des locaux et des équipements</li><li><a href="{{R}}flotte-automobile-garages/">Flotte automobile et garages</a></li><li>Protection juridique</li><li><a href="{{R}}assurance-auto-moto/">Auto</a> et <a href="{{R}}assurance-habitation/">habitation</a> des particuliers</li></ul>
<h3>Entreprises et gestion de patrimoine</h3>
<ul><li><a href="{{R}}protection-dirigeant/">Protection du chef d'entreprise</a></li><li><a href="{{R}}preparer-retraite/">Optimisation de la retraite</a></li><li><a href="{{R}}epargne-assurance-vie/">Structuration patrimoniale et transmission</a></li></ul>
<h2>L'équipe</h2>
<p>Je ne travaille pas seul. À l'agence, mon équipe vous accueille, répond à vos questions et suit vos dossiers au quotidien.</p>
<div class="todo">À compléter : prénom, rôle et photo de chaque membre de l'équipe.</div>
<h2>Ce à quoi je m'engage</h2>
<ul>
<li><strong>Vous dire les choses clairement.</strong> Ce qui est couvert, ce qui ne l'est pas, ce que ça coûte. Un contrat d'assurance n'a d'intérêt que si vous savez ce qu'il contient.</li>
<li><strong>Vous conseiller selon votre situation.</strong> Je préfère un contrat bien ajusté à un contrat qui en fait trop ou pas assez.</li>
<li><strong>Être joignable.</strong> En agence, par téléphone ou sur rendez-vous. Vous parlez à quelqu'un qui connaît votre dossier.</li>
<li><strong>Être là quand ça compte.</strong> C'est le jour du sinistre que l'on juge un assureur. Je vous accompagne dans les démarches, du premier appel jusqu'au règlement.</li>
</ul>
<h2>Une agence ancrée à Bougival</h2>
<p>L'agence est installée au {A["street"]}, face à la Seine. Bougival, c'est le village des impressionnistes, des maisons de caractère et des commerces de proximité. C'est aussi un territoire avec ses particularités, la proximité du fleuve par exemple, que je connais bien et dont je tiens compte quand j'assure une maison ou un local.</p>
<p>J'accompagne des clients à Bougival, La Celle-Saint-Cloud, Louveciennes, Croissy-sur-Seine, Chatou, Le Vésinet, Rueil-Malmaison et dans les communes alentour.</p>
</div>
<aside class="side"><div class="box"><h2>Nous trouver</h2><p style="font-size:.95rem">{A["street"]}<br>{A["zip"]} {A["city"]}<br>Parking à proximité</p>
<table class="hours" style="font-size:.92rem"><tr><td>Lundi au vendredi</td><td>9h-12h30<br>14h-18h30</td></tr><tr><td>Samedi, dimanche</td><td>Fermé</td></tr></table>
<p style="margin:1em 0 0"><a class="btn btn-main" href="{{R}}contact/" style="width:100%;justify-content:center">Prendre rendez-vous</a></p></div>
<div class="box"><h2>En quelques mots</h2><ul><li><a href="{{R}}avis-clients/">4,9/5 sur Google</a></li><li><a href="{{R}}assurance-particuliers/">Assurances des particuliers</a></li><li><a href="{{R}}assurance-professionnels/">Assurances des professionnels</a></li></ul></div></aside>
</div></section>{cta_band("Envie d'en parler de vive voix ?", "Passez à l'agence ou laissez-moi vos coordonnées.")}'''

    avis = f'''
<section class="sec tight"><div class="wrap">{rating}</div></section>
<section class="sec"><div class="wrap split"><div class="prose"><h2>Pourquoi je vous renvoie vers Google</h2>
<p>Les avis affichés sur Google sont déposés directement par mes clients. Je ne les choisis pas et je ne les modifie pas. C'est pour cela que je préfère vous inviter à les lire là où ils ont été écrits, plutôt que d'en sélectionner quelques-uns ici.</p>
<p>Vous y verrez ce que mes clients retiennent : quelqu'un de disponible, qui rappelle, qui explique et qui s'occupe du dossier jusqu'au bout.</p>
<div class="todo">Option : avec l'accord écrit des clients concernés, on peut reprendre ici 3 ou 4 avis Google mot pour mot, avec le prénom et la date.</div></div>
<div class="prose"><h2>Vous êtes client de l'agence ?</h2>
<p>Votre avis compte, pour moi et pour les personnes qui cherchent un assureur dans le secteur. Deux minutes suffisent pour raconter comment s'est passé votre devis, votre rendez-vous ou la gestion de votre sinistre.</p>
<div class="btn-row"><a class="btn btn-main" href="{{MAPS}}" rel="noopener">Laisser un avis sur Google</a></div>
<p style="margin-top:1.4em">Et si quelque chose ne s'est pas passé comme vous l'attendiez, dites-le-moi directement : <a href="tel:{A["tel_link"]}">{A["tel"]}</a>. Je préfère le savoir et corriger.</p></div></div></section>
{cta_band()}'''

    contact = f'''
<section class="sec tight"><div class="wrap split" style="align-items:start">
<form class="form" action="https://api.web3forms.com/submit" method="POST">
<input type="hidden" name="access_key" value="{{FORM_KEY}}">
<input type="hidden" name="subject" value="Nouvelle demande depuis le site de l'agence">
<input type="hidden" name="from_name" value="Site agence Bougival">
<input type="hidden" name="redirect" value="{{SITE}}/merci/">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="two"><label>Nom et prénom<input name="nom" required autocomplete="name"></label>
<label>Téléphone<input name="telephone" type="tel" required autocomplete="tel" inputmode="tel"></label></div>
<label>Email<input name="email" type="email" autocomplete="email"></label>
<div class="two"><label>Vous êtes<select name="profil"><option>Un particulier</option><option>Un professionnel</option></select></label>
<label>Votre demande concerne<select name="sujet"><option>Auto, moto</option><option>Habitation</option><option>Santé, prévoyance</option><option>Épargne, retraite</option><option>Prêt immobilier</option><option>Assurance professionnelle</option><option>Un sinistre</option><option>Autre</option></select></label></div>
<label>Quand puis-je vous rappeler ?<select name="creneau"><option>Peu importe</option><option>Le matin</option><option>Entre 12h et 14h</option><option>L'après-midi</option><option>En fin de journée</option></select></label>
<label>Votre message (facultatif)<textarea name="message" rows="4"></textarea></label>
<label class="check"><input type="checkbox" required><span>J'accepte que mes coordonnées soient utilisées pour répondre à ma demande. Elles ne sont ni revendues ni conservées au-delà du nécessaire. <a href="{{R}}confidentialite/">En savoir plus</a></span></label>
<button class="btn btn-main" type="submit">Envoyer ma demande</button>
</form>
<div><h2>L'agence</h2>
<dl class="info"><dt>Adresse</dt><dd>{A["street"]}<br>{A["zip"]} {A["city"]}<br>Parking à proximité</dd>
<dt>Téléphone</dt><dd><a href="tel:{A["tel_link"]}" style="font-family:var(--serif);font-size:1.5rem;text-decoration:none">{A["tel"]}</a></dd>
<dt>Email</dt><dd><a href="mailto:{A["email"]}">{A["email"]}</a></dd>
<dt>Horaires</dt><dd><table class="hours"><tr><td>Lundi au vendredi</td><td>9h-12h30 et 14h-18h30</td></tr><tr><td>Samedi et dimanche</td><td>Fermé</td></tr></table></dd></dl>
<div class="btn-row"><a class="btn btn-ink" href="{{MAPS}}" rel="noopener">Voir l'itinéraire</a></div>
<div class="note" style="margin-top:2em"><p><strong>Vous avez un sinistre ?</strong></p><p>Mettez-vous en sécurité, prenez des photos, puis appelez l'agence aux heures d'ouverture. En dehors de ces horaires, les numéros d'assistance figurent sur votre contrat et dans votre <a href="{A["client"]}" rel="noopener">espace client Gan</a>.</p></div>
</div></div></section>'''

    merci = f'''<section class="sec tight"><div class="wrap prose"><p>Votre demande est bien partie. Je vous rappelle dès que possible, aux heures d'ouverture de l'agence.</p>
<p>Si c'est urgent, appelez directement le <a href="tel:{A["tel_link"]}"><strong>{A["tel"]}</strong></a>.</p><div class="btn-row"><a class="btn btn-ink" href="{{R}}">Retour à l'accueil</a></div></div></section>'''

    mentions = f'''<section class="sec tight"><div class="wrap prose">
<div class="todo">Page à faire valider par Willy et par sa compagnie avant mise en ligne : les informations légales ci-dessous doivent reprendre exactement celles de ses documents officiels.</div>
<h2>Éditeur du site</h2>
<p>{A["agent"]}, agent général d'assurance exclusif Gan Assurances.<br>{A["street"]}, {A["zip"]} {A["city"]}<br>Téléphone : {A["tel"]}<br>Email : {A["email"]}</p>
<div class="todo">À compléter : forme juridique, numéro SIRET, directeur de la publication.</div>
<h2>Immatriculation</h2>
<p>Immatriculé au registre des intermédiaires en assurance (ORIAS) sous le numéro {A["orias"]}. Cette immatriculation peut être vérifiée sur <a href="https://www.orias.fr" rel="noopener">www.orias.fr</a>.</p>
<p>Activité exercée sous le contrôle de l'Autorité de Contrôle Prudentiel et de Résolution (ACPR), 4 place de Budapest, CS 92459, 75436 Paris Cedex 09.</p>
<h2>Compagnie représentée</h2>
<p>Gan Assurances, société anonyme régie par le Code des assurances, 8-10 rue d'Astorg, 75008 Paris.</p>
<div class="todo">À compléter : capital social et numéro RCS de Gan Assurances, tels qu'ils figurent sur les documents de la compagnie.</div>
<h2>Réclamations et médiation</h2>
<p>En cas de désaccord, parlez-m'en d'abord : la plupart des difficultés se règlent directement à l'agence. Si la réponse ne vous satisfait pas, vous pouvez adresser une réclamation écrite selon les modalités indiquées dans votre contrat.</p>
<p>En dernier recours, vous pouvez saisir gratuitement La Médiation de l'Assurance : TSA 50110, 75441 Paris Cedex 09, ou sur <a href="https://www.mediation-assurance.org" rel="noopener">www.mediation-assurance.org</a>.</p>
<h2>Hébergement</h2>
<p>Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, États-Unis.</p>
<h2>Contenu du site</h2>
<p>Les informations publiées sur ce site sont générales. Elles ne constituent ni un conseil personnalisé ni une offre contractuelle. Seules les conditions générales et particulières du contrat souscrit font foi : garanties, exclusions, plafonds et franchises.</p>
<p>Les textes et la mise en page de ce site ne peuvent pas être reproduits sans autorisation. Gan Assurances est une marque de sa société titulaire.</p>
</div></section>'''

    confid = f'''<section class="sec tight"><div class="wrap prose">
<h2>Les données que vous me confiez</h2>
<p>Quand vous remplissez le formulaire de contact, vous me transmettez votre nom, votre numéro de téléphone, éventuellement votre email et le contenu de votre message. Ces informations me servent uniquement à vous répondre et à préparer votre demande de devis ou de rendez-vous.</p>
<p>Elles me sont transmises par email, par l'intermédiaire d'un service d'envoi de formulaires (Web3Forms). Le site lui-même ne les enregistre dans aucune base de données.</p>
<h2>Combien de temps sont-elles conservées ?</h2>
<p>Si votre demande n'aboutit pas à un contrat, vos coordonnées sont conservées trois ans au maximum après notre dernier échange. Si vous devenez client, elles sont traitées dans le cadre de votre contrat, selon la politique de protection des données de Gan Assurances.</p>
<div class="todo">À faire valider : durée de conservation et référence à la politique de données de la compagnie.</div>
<h2>Vos droits</h2>
<p>Vous pouvez à tout moment demander à consulter, corriger ou supprimer vos données, ou vous opposer à leur utilisation. Il suffit de m'en faire la demande à l'agence, par courrier ou par téléphone au {A["tel"]}. Vous pouvez aussi saisir la CNIL (<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p>Si vous ne souhaitez pas être démarché par téléphone, vous pouvez vous inscrire gratuitement sur la liste d'opposition Bloctel.</p>
<h2>Cookies</h2>
<p>Ce site ne dépose aucun cookie publicitaire ni aucun outil de suivi. Les polices de caractères sont hébergées directement sur le site : aucune donnée n'est envoyée à un service tiers quand vous naviguez.</p>
</div></section>'''

    P = lambda **k: k
    return [
        P(slug="", title="Assurance à Bougival (78) | Willy Guillaume, agent général Gan Assurances",
          desc="Votre agence d'assurance à Bougival : auto, habitation, santé, épargne, assurances professionnelles. Un interlocuteur unique, noté 4,9/5 sur Google. 01 30 78 14 10.",
          hero=dict(type="home", kicker="Gan Assurances Bougival Morisot", h1="À Bougival, votre assureur a <span class=\"hl\">un visage</span>",
                    lead="Auto, habitation, santé, épargne, activité professionnelle : je vous conseille, je vous assure et je reste votre interlocuteur le jour où vous avez besoin de moi."), body=home),
        P(slug="assurance-particuliers", title="Assurances pour les particuliers à Bougival | Gan Assurances",
          desc="Auto, habitation, santé, prévoyance, épargne, retraite, prêt immobilier : toutes vos assurances de particulier à l'agence Gan de Bougival, avec un conseiller dédié.",
          crumbs=[("Particuliers", None)],
          hero=dict(type="dark", kicker="Particuliers", h1="Vos assurances au même endroit, avec quelqu'un qui vous connaît",
                    lead="Votre voiture, votre logement, votre santé, votre épargne : je vous aide à choisir des contrats qui correspondent à votre vie, et je les fais évoluer avec vous.", pills=PART), body=part),
        P(slug="assurance-professionnels", title="Assurance des indépendants à Bougival | Artisans, commerçants, libéraux",
          desc="Artisans, commerçants, professions libérales : responsabilité civile professionnelle, multirisque, santé, prévoyance et retraite des indépendants avec votre agent Gan à Bougival.",
          crumbs=[("Professionnels", None)],
          hero=dict(type="dark", kicker="Professionnels", h1="Votre activité mérite un assureur qui la comprend",
                    lead="Artisans, commerçants, professions libérales : vous êtes à votre compte. Je commence par comprendre votre métier, puis je construis une protection qui tient la route.", pills=PRO), body=pro),
        P(slug="assurance-entreprises", title="Assurance des entreprises à Bougival | Salariés, dirigeant, flotte, multirisque",
          desc="Mutuelle et prévoyance des salariés, épargne salariale, retraite, garantie chômage du dirigeant, multirisque et flotte automobile : votre agent général Gan à Bougival, depuis 2005.",
          crumbs=[("Entreprises", None)],
          hero=dict(type="dark", kicker="Entreprises", h1="Protéger votre entreprise, vos salariés et vous-même",
                    lead="Dirigeants de TPE et de PME : depuis plus de vingt ans, j'accompagne des chefs d'entreprise sur leurs assurances, leur protection sociale et celle de leurs équipes.", pills=ENT), body=ent),
        P(slug="agence", title="L'agence Gan Assurances de Bougival | Willy Guillaume et son équipe",
          desc="Willy Guillaume, agent général Gan Assurances depuis 2005, et son équipe vous accueillent à Bougival. Particuliers, professionnels, dirigeants et gestion de patrimoine.",
          crumbs=[("L'agence", None)],
          hero=dict(type="plain", kicker="L'agence", h1="Une agence à taille humaine, sur les bords de Seine",
                    lead="Derrière vos contrats, il y a des personnes. Voici qui nous sommes et comment nous travaillons."), body=agence),
        P(slug="avis-clients", title="Avis clients | Gan Assurances Bougival, noté 4,9/5 sur Google",
          desc="L'agence Gan Assurances de Bougival est notée 4,9/5 sur Google par ses clients. Lisez leurs avis, ou partagez votre propre expérience.",
          crumbs=[("Avis clients", None)],
          hero=dict(type="plain", kicker="Avis clients", h1="La parole est à mes clients",
                    lead="Le meilleur moyen de savoir comment je travaille, c'est de lire ce qu'en disent celles et ceux que j'assure."), body=avis),
        P(slug="contact", title="Contact et rendez-vous | Agence Gan Assurances Bougival",
          desc="Contactez l'agence Gan Assurances de Bougival : 01 30 78 14 10, 23 quai Georges Clemenceau. Demande de rappel, devis et rendez-vous du lundi au vendredi.",
          crumbs=[("Contact", None)],
          hero=dict(type="plain", kicker="Contact et rendez-vous", h1="Laissez-moi vos coordonnées, je vous rappelle",
                    lead="Un devis, une question sur un contrat, un rendez-vous à l'agence : dites-moi en deux mots ce qui vous amène."), body=contact),
        P(slug="merci", noindex=True, title="Merci | Agence Gan Assurances Bougival", desc="Votre demande a bien été envoyée.",
          hero=dict(type="plain", h1="Merci, c'est bien reçu"), body=merci),
        P(slug="mentions-legales", title="Mentions légales | Agence Gan Assurances Bougival", desc="Mentions légales du site de l'agence Gan Assurances de Bougival : éditeur, immatriculation ORIAS, médiation, hébergement.",
          crumbs=[("Mentions légales", None)], hero=dict(type="plain", h1="Mentions légales"), body=mentions),
        P(slug="confidentialite", title="Confidentialité et données personnelles | Agence Gan Assurances Bougival", desc="Comment l'agence Gan Assurances de Bougival utilise et protège les données que vous lui confiez.",
          crumbs=[("Confidentialité", None)], hero=dict(type="plain", h1="Confidentialité et données personnelles"), body=confid),
        P(slug="404", noindex=True, title="Page introuvable | Agence Gan Assurances Bougival", desc="Cette page n'existe pas ou plus.",
          hero=dict(type="plain", h1="Cette page a pris le large", lead="L'adresse est peut-être erronée, ou la page a été déplacée."),
          body='<section class="sec tight"><div class="wrap"><div class="btn-row"><a class="btn btn-ink" href="{R}">Retour à l\'accueil</a><a class="btn btn-ghost" href="{R}contact/">Contacter l\'agence</a></div></div></section>'),
    ]
