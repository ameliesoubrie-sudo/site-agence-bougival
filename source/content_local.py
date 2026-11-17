def pages(g):
    cards, A = g["cards"], g["A"]
    out = []

    def ville(slug, nom, title, desc, h1, lead, body, faq):
        out.append(dict(slug=slug, kind="city", title=title, desc=desc, crumbs=[("Assurance " + nom, None)],
                        hero=dict(type="city", ghost=nom, kicker="Votre assureur près de chez vous", h1=h1, lead=lead), body=body, faq=faq))

    ville("assurance-bougival", "Bougival",
          "Assurance à Bougival (78380) | Agence Gan Assurances, quai Georges Clemenceau",
          "Votre agence d'assurance à Bougival, 23 quai Georges Clemenceau : auto, habitation, santé, épargne, professionnels. Accueil du lundi au vendredi, parking à proximité.",
          "Votre agence d'assurance à Bougival",
          "L'agence est installée sur le quai, face à la Seine. Vous pouvez passer sans rendez-vous aux heures d'ouverture, ou me demander de vous rappeler.",
          f'''<h2>Un assureur installé dans la commune</h2>
<p>Quand on habite Bougival, on peut tout à fait s'assurer en ligne ou auprès d'une plateforme. Mais le jour où une canalisation cède ou qu'un accrochage tourne mal, pouvoir pousser une porte à deux pas de chez soi et parler à quelqu'un qui connaît son dossier change beaucoup de choses. C'est ce que je propose au {A["street"]}.</p>
<h2>Ce que je regarde quand j'assure un logement à Bougival</h2>
<p>Bougival est un village à part : des maisons anciennes à flanc de coteau, des demeures de caractère, des appartements en bord de Seine. Ce cadre, qui a attiré Berthe Morisot, Monet ou Renoir, a aussi ses particularités pour un assureur.</p>
<ul>
<li><strong>La proximité de la Seine.</strong> Une partie de la commune est en zone inondable. Je vérifie avec vous ce que votre contrat prévoit pour les caves, les garages en sous-sol et les rez-de-chaussée.</li>
<li><strong>Les maisons anciennes.</strong> Murs en pierre, toitures, éléments d'époque : le coût de reconstruction à l'identique est souvent supérieur à ce que l'on imagine, et le contrat doit en tenir compte.</li>
<li><strong>Les jardins et les arbres.</strong> Tempête, chute de branches chez le voisin, mur de soutènement : des points à ne pas oublier sur un terrain en pente.</li>
</ul>
<h2>Pour les commerçants et les indépendants de Bougival</h2>
<p>Commerces du centre et des quais, restaurants en bord de Seine, artisans, professions libérales : je connais le tissu local et je me déplace volontiers dans vos locaux. La question des inondations et de la perte d'exploitation qui en découle est un sujet que j'aborde systématiquement avec les professionnels installés près du fleuve. <a href="{{R}}assurance-professionnels/">Voir les assurances professionnelles</a>.</p>
<h2>Venir à l'agence</h2>
<p>{A["street"]}, {A["zip"]} {A["city"]}. Un parking se trouve à proximité. L'agence est ouverte du lundi au vendredi, de 9h à 12h30 et de 14h à 18h30.</p>''',
          [("Faut-il prendre rendez-vous pour venir à l'agence ?", "Non, vous pouvez passer aux heures d'ouverture. Pour un bilan complet de vos contrats ou un sujet comme l'épargne ou un prêt, un rendez-vous permet de vous consacrer le temps nécessaire."),
           ("Mon logement est en zone inondable, puis-je être assuré ?", "Oui. La garantie catastrophes naturelles est incluse dans les contrats multirisques habitation et s'applique quand un arrêté reconnaît l'événement. On regarde ensemble les franchises et les biens couverts.")])

    ville("assurance-la-celle-saint-cloud", "La Celle-Saint-Cloud",
          "Assurance La Celle-Saint-Cloud | Votre agent général Gan à quelques minutes",
          "Habitants et professionnels de La Celle-Saint-Cloud : assurance auto, habitation en copropriété, santé, épargne. Votre agence Gan Assurances est à Bougival, la commune voisine.",
          "Votre assureur pour La Celle-Saint-Cloud",
          "L'agence se trouve à Bougival, la commune voisine. Beaucoup de mes clients habitent La Celle-Saint-Cloud, en résidence comme en maison.",
          '''<h2>Assurer un appartement en copropriété</h2>
<p>La Celle-Saint-Cloud compte de grandes résidences, souvent très arborées, et de nombreux propriétaires occupants. En copropriété, la question qui revient sans cesse est : qui assure quoi ?</p>
<ul>
<li><strong>L'immeuble</strong> (murs, toiture, parties communes) est assuré par le syndic, pour le compte de la copropriété.</li>
<li><strong>Votre appartement</strong>, vos aménagements et vos biens relèvent de votre contrat personnel, tout comme votre responsabilité si un dégât part de chez vous.</li>
<li><strong>Si vous louez votre bien</strong>, une assurance propriétaire non occupant prend le relais quand celle du locataire ne joue pas.</li>
</ul>
<p>Dans les immeubles des années 1960 et 1970, les dégâts des eaux liés aux canalisations sont le sinistre le plus courant. Je vérifie que la recherche de fuite et les embellissements que vous avez réalisés (cuisine, parquet, salle de bains) sont bien pris en compte. <a href="{R}assurance-habitation/">En savoir plus sur l'assurance habitation</a>.</p>
<h2>Vous prenez le train plus souvent que la voiture ?</h2>
<p>Avec les gares de la ligne vers La Défense et Paris Saint-Lazare, beaucoup d'habitants de La Celle-Saint-Cloud n'utilisent leur voiture que le soir et le week-end. Si c'est votre cas, dites-le-moi : le nombre de kilomètres parcourus et le stationnement en parking fermé comptent dans le calcul de votre assurance auto.</p>
<p>Et si vous allez à la gare en vélo ou en trottinette électrique, pensez au vol et à la responsabilité civile, qui obéissent à des règles particulières pour les engins motorisés.</p>
<h2>Retraite et transmission</h2>
<p>J'accompagne de nombreux clients de La Celle-Saint-Cloud dans la préparation de leur retraite : changement de mutuelle au moment du départ, réorganisation de l'épargne, mise à jour des clauses bénéficiaires. Des sujets qu'on traite au calme, sur rendez-vous. <a href="{R}epargne-retraite/">Voir l'épargne et la retraite</a>.</p>''',
          [("Mon syndic a une assurance, ai-je vraiment besoin de la mienne ?", "Oui. L'assurance de la copropriété ne couvre ni vos meubles, ni vos aménagements intérieurs, ni votre responsabilité personnelle. Tout copropriétaire doit d'ailleurs être assuré au moins en responsabilité civile."),
           ("Pouvez-vous vous déplacer à La Celle-Saint-Cloud ?", "Oui, sur rendez-vous, notamment pour les professionnels ou si vous avez des difficultés à vous déplacer. Sinon, l'agence de Bougival est à quelques minutes, avec un parking à proximité.")])

    ville("assurance-louveciennes", "Louveciennes",
          "Assurance Louveciennes | Maisons de caractère, auto, patrimoine | Agent Gan",
          "Assurance habitation pour maisons de caractère, auto, épargne et patrimoine à Louveciennes. Votre agent général Gan Assurances vous reçoit à Bougival, la commune voisine.",
          "Votre assureur pour Louveciennes",
          "De Bougival à Louveciennes, il n'y a que la côte à monter. J'assure des familles et des professionnels de la commune, avec une attention particulière pour les belles maisons.",
          '''<h2>Assurer une maison de caractère</h2>
<p>Louveciennes a gardé son allure de village : maisons anciennes, propriétés entourées de grands jardins, rues que Pissarro et Sisley ont peintes. Ces maisons ne s'assurent pas comme un pavillon récent.</p>
<ul>
<li><strong>La valeur de reconstruction.</strong> Pierre de taille, charpente ancienne, ferronneries, boiseries : en cas de sinistre important, reconstruire à l'identique coûte cher. Un capital sous-évalué, et c'est vous qui payez la différence.</li>
<li><strong>Les objets de valeur.</strong> Tableaux, mobilier ancien, bijoux, cave à vin : ils sont soumis à des plafonds spécifiques, et parfois à des conditions de protection (alarme, serrures). Mieux vaut les déclarer précisément.</li>
<li><strong>Le parc et les dépendances.</strong> Grands arbres, murs d'enceinte, portail, piscine, pool house, serre : tout ce qui se trouve hors de la maison doit apparaître au contrat.</li>
<li><strong>Les périodes d'absence.</strong> Beaucoup de contrats limitent la garantie vol quand le logement reste inoccupé longtemps. À vérifier si vous voyagez souvent.</li>
</ul>
<p>Je me déplace pour voir la maison avec vous. C'est le seul moyen de faire un contrat juste. <a href="{R}assurance-habitation/">En savoir plus sur l'assurance habitation</a>.</p>
<h2>Vos véhicules</h2>
<p>Voiture familiale, second véhicule, voiture de collection sortie aux beaux jours, deux-roues : je vous propose une vue d'ensemble plutôt qu'une pile de contrats séparés. Pour un véhicule de collection ou de forte valeur, la question de la valeur garantie en cas de vol ou de destruction est centrale, et elle se fixe à la souscription. <a href="{R}assurance-auto-moto/">Voir l'assurance auto et moto</a>.</p>
<h2>Épargne et patrimoine</h2>
<p>Assurance vie, préparation de la retraite, transmission : ces sujets demandent du temps et de la confidentialité. Je vous reçois sur rendez-vous à l'agence, ou je viens chez vous.</p>''',
          [("Faut-il une expertise pour assurer des objets de valeur ?", "Pour les pièces importantes, une facture ou une estimation récente est vivement conseillée. Elle fixe la valeur avant tout sinistre et évite les discussions le moment venu."),
           ("Ma maison est partiellement classée ou située en secteur protégé, cela change-t-il quelque chose ?", "Oui, car les travaux de remise en état peuvent être soumis à des contraintes particulières et coûter plus cher. Il faut le signaler pour que le capital garanti en tienne compte.")])

    ville("assurance-croissy-sur-seine", "Croissy-sur-Seine",
          "Assurance Croissy-sur-Seine | Familles, maisons, prêt immobilier | Agent Gan",
          "Assurance habitation, auto, santé, scolaire et prêt immobilier pour les familles de Croissy-sur-Seine. Votre agence Gan Assurances est juste de l'autre côté du pont, à Bougival.",
          "Votre assureur pour Croissy-sur-Seine",
          "Il suffit de traverser le pont : l'agence est sur le quai de Bougival, juste en face. J'assure de nombreuses familles installées dans la boucle de la Seine.",
          '''<h2>Les assurances d'une famille, sans doublon</h2>
<p>Croissy-sur-Seine attire les familles pour ses maisons avec jardin, ses écoles et sa vie de quartier. Qui dit famille dit beaucoup de contrats, et rarement le temps de les relire. Voici ce que je passe en revue avec vous :</p>
<ul>
<li><strong>La maison</strong> : capital mobilier à jour, véranda, abri de jardin, piscine, trampoline et autres équipements extérieurs.</li>
<li><strong>Les enfants</strong> : responsabilité civile, activités sportives, trajets, assurance scolaire. Souvent, la moitié est déjà dans votre contrat habitation, et l'autre manque.</li>
<li><strong>Les vélos</strong>, classiques ou électriques : très utilisés à Croissy, et très convoités. Le vol hors du domicile n'est presque jamais inclus d'office.</li>
<li><strong>La santé</strong> : orthodontie, lunettes, pédiatre. Autant de postes à bien couvrir quand on a des enfants. <a href="{R}mutuelle-sante-prevoyance/">Voir la santé et la prévoyance</a>.</li>
<li><strong>Les accidents de la vie</strong> : une chute, une brûlure, un accident de jardinage, sans tiers responsable.</li>
</ul>
<h2>Vous achetez à Croissy ?</h2>
<p>L'achat d'une maison est le moment où l'assurance du prêt se décide, souvent dans la précipitation. Vous n'êtes pas tenu d'accepter celle de la banque. Sur un emprunt long, l'écart peut être significatif. Et si votre prêt est déjà en cours, vous pouvez changer d'assurance à tout moment. Je fais l'étude pour vous. <a href="{R}assurance-emprunteur/">En savoir plus sur l'assurance emprunteur</a>.</p>
<h2>Vivre dans une boucle de la Seine</h2>
<p>Croissy est bordée par le fleuve sur une grande partie de son territoire. Comme à Bougival, certains quartiers sont concernés par le risque d'inondation. Sous-sols aménagés, chaudière ou pompe à chaleur installée en bas, véhicule garé en sous-sol : ce sont les points que je vérifie dans votre contrat.</p>
<h2>Familles venues de l'étranger</h2>
<p>Croissy accueille de nombreuses familles internationales. Si vous arrivez en France, je vous explique simplement ce qui est obligatoire, comment faire reconnaître votre historique de conduite et quels justificatifs un propriétaire peut vous demander.</p>''',
          [("L'assurance scolaire est-elle obligatoire ?", "Elle ne l'est pas pour les activités obligatoires de l'école, mais elle est exigée pour les sorties facultatives, la cantine ou l'étude dans la plupart des établissements. Vérifiez d'abord ce que couvre déjà votre contrat habitation."),
           ("Mon vélo électrique est-il couvert par mon assurance habitation ?", "Souvent seulement au domicile, et avec un plafond. Pour le vol dans la rue ou la casse, une option ou un contrat dédié est nécessaire. Un vélo à assistance limitée à 25 km/h ne demande pas d'assurance spécifique pour la responsabilité, contrairement aux modèles plus rapides.")])

    ville("assurance-rueil-malmaison", "Rueil-Malmaison",
          "Assurance Rueil-Malmaison | Particuliers, indépendants, entreprises | Agent Gan",
          "Assurances pour les particuliers, indépendants, professions libérales et entreprises de Rueil-Malmaison. Votre agent général Gan Assurances est à Bougival, à la sortie de Rueil.",
          "Votre assureur pour Rueil-Malmaison",
          "L'agence est à Bougival, dans le prolongement de Rueil en suivant la Seine. Un interlocuteur de proximité, pour votre vie privée comme pour votre activité.",
          '''<h2>Indépendants et entreprises de Rueil</h2>
<p>Rueil-Malmaison est une ville d'entreprises : des sièges de grands groupes, mais aussi une multitude de consultants, de professions libérales, de commerçants du centre-ville et de TPE. Si vous en faites partie, voici les sujets sur lesquels je peux vous aider :</p>
<ul>
<li><strong>Consultants et indépendants</strong> : responsabilité civile professionnelle, protection juridique, cyber-risques, et prévoyance pour maintenir vos revenus en cas d'arrêt. <a href="{R}assurance-professions-liberales/">Voir les professions libérales</a>.</li>
<li><strong>Commerçants et restaurateurs</strong> : multirisque du local, stock, perte d'exploitation. <a href="{R}assurance-artisans-commercants/">Voir les artisans et commerçants</a>.</li>
<li><strong>Dirigeants</strong> : bilan de protection sociale, retraite, assurance homme-clé. <a href="{R}protection-dirigeant/">Voir la protection du dirigeant</a>.</li>
<li><strong>Employeurs</strong> : mutuelle et prévoyance des salariés, véhicules de société. <a href="{R}sante-collective-flotte/">Voir la santé collective et la flotte</a>.</li>
</ul>
<p>Je me déplace dans vos bureaux, à Rueil-sur-Seine comme en centre-ville.</p>
<h2>Cadres et salariés : complétez ce que prévoit votre employeur</h2>
<p>Si vous êtes salarié d'un grand groupe, vous avez une mutuelle et une prévoyance d'entreprise. C'est une bonne base, mais elle s'arrête souvent là où vos besoins commencent : dépassements d'honoraires, maintien de votre niveau de vie en cas d'invalidité, protection du conjoint. Je vous aide à lire vos garanties collectives et à ne compléter que ce qui manque.</p>
<p>C'est aussi vrai pour l'épargne : épargne salariale, plan d'épargne retraite d'entreprise, assurance vie personnelle. Une vue d'ensemble permet de savoir où vous en êtes. <a href="{R}epargne-retraite/">Voir l'épargne et la retraite</a>.</p>
<h2>Votre logement à Rueil</h2>
<p>Appartement dans une résidence récente, maison du côté de Buzenval ou des coteaux, investissement locatif : les besoins ne sont pas les mêmes. Pour un bien mis en location, l'assurance propriétaire non occupant et la garantie des loyers impayés sont deux sujets distincts, que je vous explique clairement. <a href="{R}assurance-habitation/">Voir l'assurance habitation</a>.</p>''',
          [("Vous êtes dans les Yvelines, pouvez-vous m'assurer dans les Hauts-de-Seine ?", "Bien sûr. Un agent général peut assurer des clients où qu'ils habitent. La proximité compte surtout pour le service : Bougival touche Rueil-Malmaison, et l'agence est à quelques minutes."),
           ("Proposez-vous des rendez-vous en dehors des heures de bureau ?", "L'agence est ouverte du lundi au vendredi jusqu'à 18h30. Pour un rendez-vous à un autre moment ou par téléphone, appelez-moi : on trouve généralement une solution.")])

    # ---------------------------------------------------------------- CONSEILS
    ARTS = [
        ("conseils/changer-assurance-auto", "Changer d'assurance auto : comment faire sans se tromper", "Résiliation, délais, pièges à éviter : la marche à suivre, étape par étape."),
        ("conseils/degat-des-eaux-bons-reflexes", "Dégât des eaux : les bons réflexes dans les premières heures", "Ce qu'il faut faire tout de suite, et ce qu'il vaut mieux éviter."),
        ("conseils/assurances-obligatoires-artisan-commercant", "Artisan, commerçant : quelles assurances sont vraiment obligatoires ?", "Le point sur ce que la loi impose, et sur ce qui protège réellement votre activité."),
    ]
    out.append(dict(slug="conseils", title="Conseils assurance | Le blog de l'agence Gan Assurances de Bougival",
                    desc="Des réponses claires aux questions que vous vous posez sur vos assurances : auto, habitation, sinistres, assurances professionnelles. Par Willy Guillaume, agent général.",
                    crumbs=[("Conseils", None)],
                    hero=dict(type="plain", kicker="Conseils", h1="L'assurance expliquée simplement",
                              lead="Les questions que mes clients me posent au comptoir, et les réponses que je leur donne."),
                    body=f'<section class="sec tight"><div class="wrap">{cards(ARTS, "Lire l\'article")}</div></section>' + g["cta_band"]()))

    def art(i, title, desc, lead, body):
        slug, h1, _ = ARTS[i]
        out.append(dict(slug=slug, kind="article", date="2026-11-17", title=title, desc=desc,
                        crumbs=[("Conseils", "conseils"), (h1, None)],
                        hero=dict(type="plain", kicker="Conseils · par Willy Guillaume", h1=h1, lead=lead), body=body))

    art(0, "Changer d'assurance auto : la marche à suivre | Agence Gan Bougival",
        "Comment résilier et changer d'assurance auto : délais, démarches, documents à fournir et erreurs à éviter. Les explications de votre agent général à Bougival.",
        "Votre contrat a augmenté, ou vous avez simplement envie de comparer ? Changer d'assurance auto est devenu simple. Voici comment s'y prendre.",
        '''<h2>Quand pouvez-vous résilier ?</h2>
<p>La règle est simple : dès que votre contrat a un an, vous pouvez le résilier à tout moment, sans frais et sans avoir à vous justifier. La résiliation prend effet un mois après la demande, et l'assureur vous rembourse la part de cotisation déjà payée pour la période restante.</p>
<p>Avant un an, la résiliation reste possible dans certains cas : vente du véhicule, déménagement ou changement de situation qui modifie le risque, ou augmentation du tarif non prévue au contrat.</p>
<h2>Les étapes, dans l'ordre</h2>
<ol>
<li><strong>Demandez votre relevé d'information</strong> à votre assureur actuel. Il indique votre bonus et vos sinistres des dernières années. L'assureur doit vous le fournir sous quinze jours.</li>
<li><strong>Comparez à garanties égales.</strong> Même formule, mêmes franchises, mêmes options. Sinon, vous comparez des prix qui ne veulent rien dire.</li>
<li><strong>Souscrivez le nouveau contrat.</strong> C'est le nouvel assureur qui se charge de résilier l'ancien. Vous n'avez aucun courrier à envoyer.</li>
<li><strong>Vérifiez les dates.</strong> Le nouveau contrat doit démarrer le jour exact où l'ancien s'arrête.</li>
</ol>
<h2>Les trois erreurs que je vois le plus souvent</h2>
<ul>
<li><strong>Résilier soi-même avant d'avoir un nouveau contrat.</strong> Rouler sans assurance, même un seul jour, est un délit. Et en cas d'accident, les conséquences financières peuvent vous suivre toute une vie.</li>
<li><strong>Ne regarder que le prix.</strong> Une franchise doublée, un véhicule de remplacement supprimé, une protection du conducteur plafonnée : l'économie peut disparaître au premier sinistre.</li>
<li><strong>Oublier de déclarer un conducteur.</strong> Si votre enfant prend régulièrement le volant, il doit figurer au contrat.</li>
</ul>
<h2>Besoin d'un coup de main ?</h2>
<p>Passez à l'agence avec votre carte grise, votre permis et votre relevé d'information. Je compare avec vous, et si vous changez, je m'occupe de la résiliation. <a href="{R}assurance-auto-moto/">Voir l'assurance auto et moto</a>.</p>''')

    art(1, "Dégât des eaux : que faire dans les premières heures ? | Agence Gan Bougival",
        "Fuite, infiltration, inondation chez vous : les gestes à faire tout de suite, le constat amiable, le délai de déclaration et les erreurs à éviter.",
        "Une tache au plafond, de l'eau qui coule le long d'un mur : le dégât des eaux est le sinistre le plus fréquent dans un logement. Les premières heures comptent.",
        '''<h2>Tout de suite : limiter les dégâts</h2>
<ol>
<li><strong>Coupez l'eau</strong> au robinet d'arrêt du logement, ou demandez au gardien ou au syndic de couper la colonne si la fuite vient d'ailleurs.</li>
<li><strong>Coupez l'électricité</strong> dans les pièces touchées si l'eau s'approche des prises ou du tableau.</li>
<li><strong>Mettez vos affaires à l'abri</strong> et épongez ce que vous pouvez.</li>
<li><strong>Prévenez les voisins</strong> concernés, le syndic si vous êtes en copropriété, et votre propriétaire si vous êtes locataire.</li>
</ol>
<h2>Ensuite : garder des preuves</h2>
<p>Prenez des photos et des vidéos avant de nettoyer : l'origine de la fuite si elle est visible, les murs, les sols, les meubles et les objets abîmés. Ne jetez rien, même ce qui semble irrécupérable : l'expert peut demander à le voir. Rassemblez les factures des biens endommagés si vous les avez.</p>
<h2>Déclarer le sinistre</h2>
<p>Vous avez cinq jours ouvrés pour déclarer le dégât des eaux à votre assureur. Si un voisin est concerné, remplissez ensemble un constat amiable dégât des eaux : il décrit les circonstances et permet aux assureurs de régler le dossier plus vite. Chacun en envoie un exemplaire à son propre assureur.</p>
<p>Peu importe qui est responsable : c'est toujours votre assureur que vous contactez en premier pour vos propres dommages.</p>
<h2>Ce qu'il vaut mieux éviter</h2>
<ul>
<li><strong>Lancer les travaux de remise en état</strong> avant l'accord de l'assureur ou le passage de l'expert. Seules les réparations d'urgence pour stopper la fuite sont à faire tout de suite. Gardez la facture.</li>
<li><strong>Repeindre trop vite.</strong> Un mur doit sécher complètement, ce qui peut prendre plusieurs semaines.</li>
<li><strong>Laisser traîner une petite fuite.</strong> Un sinistre dû à un défaut d'entretien connu peut être moins bien indemnisé.</li>
</ul>
<h2>Vous êtes client de l'agence ?</h2>
<p>Appelez-moi dès que la situation est sous contrôle. Je vous dis quoi faire, je vous aide à remplir le constat et je suis le dossier jusqu'au règlement. <a href="{R}assurance-habitation/">Voir l'assurance habitation</a>.</p>''')

    art(2, "Artisan, commerçant : les assurances obligatoires | Agence Gan Bougival",
        "Décennale, responsabilité civile, véhicules, mutuelle des salariés : quelles assurances sont obligatoires quand on est artisan ou commerçant, et lesquelles sont vraiment utiles ?",
        "Quand on se lance, on a mille choses à penser, et l'assurance arrive rarement en tête de liste. Voici ce qui est obligatoire, et ce qui ne l'est pas mais peut sauver votre entreprise.",
        '''<h2>Ce que la loi impose</h2>
<ul>
<li><strong>La garantie décennale</strong>, si vous exercez un métier du bâtiment. Elle doit être souscrite avant l'ouverture du chantier, et ses références doivent figurer sur vos devis et vos factures.</li>
<li><strong>L'assurance de vos véhicules</strong>, au minimum en responsabilité civile, avec un usage professionnel déclaré.</li>
<li><strong>La responsabilité civile professionnelle</strong>, pour les professions réglementées.</li>
<li><strong>La complémentaire santé de vos salariés</strong>, dès la première embauche, financée au moins pour moitié par l'employeur.</li>
</ul>
<h2>Ce que votre bail ou vos clients exigent</h2>
<p>Certaines assurances ne sont pas imposées par la loi, mais le deviennent par contrat. Votre bail commercial prévoit presque toujours l'obligation d'assurer le local, attestation à l'appui. Et de plus en plus de donneurs d'ordre demandent une attestation de responsabilité civile avant de vous confier un marché.</p>
<h2>Ce qui n'est pas obligatoire, mais que je recommande toujours</h2>
<ul>
<li><strong>La responsabilité civile professionnelle</strong>, même quand rien ne vous y oblige. Un client qui glisse dans votre boutique, un chantier qui abîme le parquet du voisin : sans assurance, c'est votre entreprise qui paie, et parfois vous personnellement.</li>
<li><strong>La multirisque professionnelle</strong>, pour vos locaux, votre matériel et votre stock.</li>
<li><strong>La perte d'exploitation</strong>, qui compense votre chiffre d'affaires pendant une fermeture forcée. C'est elle qui permet de rouvrir.</li>
<li><strong>La prévoyance du dirigeant.</strong> Si vous êtes arrêté trois mois, qui fait tourner l'entreprise, et de quoi vivez-vous ?</li>
<li><strong>La protection juridique</strong>, pour les impayés et les litiges.</li>
</ul>
<h2>Par quoi commencer quand le budget est serré ?</h2>
<p>Je conseille de procéder dans cet ordre : d'abord ce qui est obligatoire, ensuite la responsabilité civile et le local, puis la perte d'exploitation et votre prévoyance. On peut démarrer avec des garanties simples et les renforcer quand l'activité se développe. L'important est de ne pas laisser de trou sur les risques qui peuvent tout arrêter.</p>
<p>Vous vous installez à Bougival ou dans les environs ? Venez me voir avec votre projet : on fait le point ensemble. <a href="{R}assurance-artisans-commercants/">Voir les assurances des artisans et commerçants</a>.</p>''')

    return out
