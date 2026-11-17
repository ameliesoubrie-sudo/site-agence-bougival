def pages(g):
    out = []
    def add(slug, family, title, desc, kicker, h1, lead, body, faq):
        parent = {"part": ("Particuliers", "assurance-particuliers"), "pro": ("Professionnels", "assurance-professionnels"), "ent": ("Entreprises", "assurance-entreprises")}[family]
        out.append(dict(slug=slug, family=family, kind="product", title=title, desc=desc,
                        crumbs=[parent, (kicker, None)],
                        hero=dict(type="product", kicker=kicker, h1=h1, lead=lead), body=body, faq=faq))

    # ------------------------------------------------------------ AUTO
    add("assurance-auto-moto", "part",
        "Assurance auto et moto à Bougival | Devis avec votre agent Gan",
        "Assurance auto, moto, scooter et trottinette électrique à Bougival. Tiers, intermédiaire ou tous risques : un devis adapté à votre usage, avec un conseiller qui suit votre dossier.",
        "Auto et deux-roues", "Assurance auto et moto à Bougival",
        "Vous roulez tous les jours pour aller travailler, ou seulement le week-end ? Votre voiture est neuve, ou elle a quinze ans ? La bonne assurance n'est pas la même. On la choisit ensemble.",
        '''<h2>Quelle formule pour quel véhicule ?</h2>
<p>La seule assurance obligatoire, c'est la responsabilité civile : elle indemnise les dommages que vous causez aux autres. Tout le reste est un choix, et ce choix dépend surtout de la valeur de votre véhicule et de ce que vous pourriez payer de votre poche en cas de coup dur.</p>
<ul>
<li><strong>Au tiers</strong> : le minimum légal. Adapté à un véhicule ancien, de faible valeur. Vos propres dégâts ne sont pas couverts si vous êtes responsable.</li>
<li><strong>Intermédiaire</strong> : le tiers, plus des garanties comme le vol, l'incendie, le bris de glace ou les événements climatiques. Un bon compromis pour une voiture de quelques années.</li>
<li><strong>Tous risques</strong> : vos dommages sont couverts même si vous êtes responsable, ou si le responsable n'est pas identifié. À privilégier pour un véhicule récent, en leasing ou acheté à crédit.</li>
</ul>
<div class="note"><p><strong>Mon conseil :</strong> regardez la franchise autant que le prix. Un contrat moins cher avec une franchise élevée peut coûter plus au premier accrochage.</p></div>
<h2>Les garanties qui font la différence au quotidien</h2>
<ul>
<li><strong>La protection du conducteur.</strong> Si vous êtes blessé dans un accident dont vous êtes responsable, la responsabilité civile ne vous indemnise pas. C'est la garantie que je vérifie en premier.</li>
<li><strong>L'assistance 0 km.</strong> Une panne devant chez vous un lundi matin est un cas très courant, et toutes les assistances ne la couvrent pas.</li>
<li><strong>Le véhicule de remplacement</strong>, si vous ne pouvez pas vous passer de voiture.</li>
<li><strong>La valeur de remboursement</strong> en cas de vol ou de destruction : valeur à neuf, valeur d'achat ou valeur à dire d'expert, l'écart peut être important.</li>
</ul>
<h2>Moto, scooter, trottinette électrique</h2>
<p>Les deux-roues ont leurs propres besoins : l'équipement du pilote (casque, gants, blouson), le vol, souvent plus fréquent qu'en voiture, et surtout la protection corporelle du conducteur, beaucoup plus exposé.</p>
<p>À savoir : les trottinettes électriques, gyroroues et autres engins motorisés doivent eux aussi être assurés en responsabilité civile, comme un véhicule. Votre assurance habitation ne suffit pas.</p>
<h2>Jeune conducteur, malus, conduite occasionnelle</h2>
<p>Un premier contrat, un retour à l'assurance après quelques années sans véhicule, un bonus à reconstruire : ce sont des situations où le conseil compte vraiment. Conduite accompagnée, véhicule choisi, conducteur secondaire sur la voiture des parents : il existe plusieurs façons de faire baisser la note sans rogner sur l'essentiel. Si vous roulez peu, parlez-m'en aussi : il existe des formules adaptées aux petits rouleurs.</p>
<h2>Et en cas d'accident ?</h2>
<p>Remplissez un constat amiable sur place, prenez des photos, puis appelez l'agence. Vous avez cinq jours ouvrés pour déclarer un accident, et deux jours ouvrés en cas de vol. Je vous guide pour la suite : expertise, garage, véhicule de prêt.</p>''',
        [("Puis-je changer d'assurance auto quand je veux ?", "Oui, dès que votre contrat a plus d'un an. Vous pouvez alors le résilier à tout moment, sans frais ni justificatif. C'est le nouvel assureur qui se charge des démarches auprès de l'ancien, pour qu'il n'y ait aucun jour sans assurance. Je m'en occupe pour vous."),
         ("La carte verte existe-t-elle encore ?", "Non. Depuis le 1er avril 2024, il n'y a plus de carte verte ni de vignette à coller sur le pare-brise. Votre assureur vous remet un mémo du véhicule assuré, et les forces de l'ordre vérifient l'assurance dans un fichier national."),
         ("Quels documents faut-il pour un devis ?", "La carte grise du véhicule, votre permis de conduire et votre relevé d'information, que votre assureur actuel doit vous fournir sur simple demande. Avec ces trois documents, je peux vous faire une proposition précise."),
         ("Assurez-vous les véhicules électriques et hybrides ?", "Oui. Je regarde en particulier la couverture de la batterie, du câble de recharge et de la borne installée à domicile, ainsi que l'assistance en cas de panne d'énergie.")])

    # ------------------------------------------------------------ HABITATION
    add("assurance-habitation", "part",
        "Assurance habitation à Bougival | Maison, appartement, propriétaire bailleur",
        "Assurance habitation à Bougival et dans les Yvelines : locataire, propriétaire occupant, copropriétaire ou bailleur. Dégât des eaux, vol, incendie, responsabilité civile.",
        "Habitation", "Assurance habitation à Bougival",
        "Un appartement en copropriété, une maison avec jardin, un bien que vous louez : votre contrat doit ressembler à votre logement, pas à un formulaire.",
        '''<h2>Locataire, propriétaire, bailleur : qui doit assurer quoi ?</h2>
<ul>
<li><strong>Locataire</strong> : l'assurance est obligatoire, au minimum pour les risques locatifs (incendie, dégât des eaux, explosion). Votre propriétaire peut vous demander une attestation chaque année.</li>
<li><strong>Copropriétaire</strong> : vous devez être assuré au moins en responsabilité civile, que vous occupiez le logement ou non.</li>
<li><strong>Propriétaire d'une maison</strong> : la loi ne vous oblige à rien, mais ne pas s'assurer serait prendre un risque considérable sur ce qui est souvent le projet d'une vie.</li>
<li><strong>Propriétaire bailleur</strong> : l'assurance propriétaire non occupant couvre votre bien quand il est loué ou vide, y compris quand l'assurance du locataire ne joue pas.</li>
</ul>
<h2>Ce que couvre une multirisque habitation</h2>
<p>Le socle est à peu près le même partout : incendie, dégât des eaux, vol, bris de glace, événements climatiques, catastrophes naturelles, et la responsabilité civile de toute la famille. Les différences se jouent dans les détails.</p>
<ul>
<li><strong>Le capital mobilier.</strong> C'est la valeur de tout ce que contient votre logement. On le sous-estime presque toujours : faites le tour des pièces, vous serez surpris.</li>
<li><strong>Le mode de remboursement.</strong> En valeur d'usage, un canapé de huit ans ne vaut presque plus rien. En valeur à neuf, il est remplacé.</li>
<li><strong>Les objets de valeur</strong> : bijoux, tableaux, instruments de musique. Ils ont souvent un plafond à part.</li>
<li><strong>Les dépendances et l'extérieur</strong> : garage, cave, abri de jardin, clôture, piscine, panneaux solaires.</li>
</ul>
<div class="note"><p><strong>Bon à savoir :</strong> gardez vos factures et prenez des photos de vos biens de valeur. Le jour d'un sinistre, c'est ce qui permet d'être indemnisé vite et bien.</p></div>
<h2>Habiter près de la Seine</h2>
<p>À Bougival et dans les communes voisines, certains logements se trouvent en zone inondable. Les inondations sont prises en charge au titre de la garantie catastrophes naturelles, quand un arrêté ministériel reconnaît l'événement. Je vérifie avec vous ce que prévoit votre contrat pour les caves, les sous-sols et les rez-de-chaussée, qui sont les premiers touchés.</p>
<h2>Les options utiles, et celles dont on peut se passer</h2>
<p>Toutes les options ne se valent pas. Selon votre situation, certaines sont vraiment pertinentes : la garantie des appareils électriques contre la surtension, la protection juridique en cas de litige avec un artisan ou un voisin, l'assurance scolaire incluse pour les enfants, le vol des vélos hors du domicile. D'autres font doublon avec votre carte bancaire ou un autre contrat. Je vous aide à faire le tri.</p>
<h2>Résidence secondaire, logement étudiant, colocation</h2>
<p>Une maison de vacances inoccupée une partie de l'année, le studio d'un enfant parti faire ses études, une colocation : chaque cas a ses règles, notamment sur le vol pendant les périodes d'absence. Parlez-m'en, il existe des solutions simples.</p>''',
        [("Combien de temps ai-je pour déclarer un sinistre ?", "Cinq jours ouvrés pour un dégât des eaux ou un incendie, deux jours ouvrés pour un vol, après dépôt de plainte. Pour une catastrophe naturelle, vous disposez de trente jours après la publication de l'arrêté au Journal officiel. Dans le doute, appelez l'agence tout de suite."),
         ("Puis-je résilier mon assurance habitation à tout moment ?", "Oui, après la première année de contrat, sans frais ni pénalité. Si vous êtes locataire, c'est votre nouvel assureur qui effectue la résiliation, pour que vous restiez couvert sans interruption."),
         ("Mon assurance habitation couvre-t-elle mes enfants à l'école ?", "La responsabilité civile de votre contrat couvre les dommages que vos enfants causent aux autres. En revanche, s'ils se blessent seuls, il faut une garantie individuelle accident, souvent proposée en option ou dans une assurance scolaire."),
         ("Je mets mon logement en location saisonnière, suis-je couvert ?", "Pas automatiquement. La location de courte durée, même occasionnelle, doit être déclarée à votre assureur. Selon le contrat, une extension ou un contrat spécifique est nécessaire.")])

    # ------------------------------------------------------------ SANTE
    add("mutuelle-sante-prevoyance", "part",
        "Mutuelle santé et prévoyance à Bougival | Complémentaire santé sur mesure",
        "Complémentaire santé, prévoyance, garantie des accidents de la vie : comparez vos garanties avec votre agent Gan à Bougival. Familles, seniors, indépendants.",
        "Santé et prévoyance", "Mutuelle santé et prévoyance à Bougival",
        "Une bonne complémentaire santé rembourse bien ce dont vous avez réellement besoin. La prévoyance, elle, protège vos revenus et vos proches. Deux sujets qu'on regarde ensemble.",
        '''<h2>Choisir sa complémentaire santé sans se perdre dans les tableaux</h2>
<p>Les tableaux de garanties sont difficiles à lire : des pourcentages, des forfaits, des plafonds. Pour s'y retrouver, je pars toujours de vos dépenses réelles. Portez-vous des lunettes ? Avez-vous des soins dentaires prévus ? Consultez-vous des spécialistes qui pratiquent des dépassements d'honoraires ? Vos enfants auront-ils besoin d'orthodontie ?</p>
<p>À partir de là, on renforce les postes qui comptent pour vous, et on ne surpaie pas ceux dont vous ne vous servez pas.</p>
<ul>
<li><strong>Hospitalisation</strong> : c'est le poste à ne jamais négliger, dépassements d'honoraires et chambre particulière compris.</li>
<li><strong>Optique, dentaire, audition</strong> : avec le dispositif 100 % Santé, certains équipements sont intégralement remboursés. Pour le reste, tout dépend du niveau de votre contrat.</li>
<li><strong>Médecines complémentaires</strong> : ostéopathie, psychologue, diététicien, selon les formules.</li>
</ul>
<h2>Une mutuelle selon votre situation</h2>
<ul>
<li><strong>Familles</strong> : orthodontie, lunettes des enfants, pédiatre. Les besoins sont concentrés sur quelques postes, autant bien les couvrir.</li>
<li><strong>Jeunes actifs</strong> : une formule simple, centrée sur l'hospitalisation et les soins courants, suffit souvent.</li>
<li><strong>Retraités</strong> : à la fin de la mutuelle d'entreprise, la cotisation et les besoins changent. C'est le bon moment pour comparer.</li>
<li><strong>Indépendants</strong> : vos cotisations santé et prévoyance peuvent, sous conditions, être déduites de votre revenu professionnel.</li>
</ul>
<h2>La prévoyance, la grande oubliée</h2>
<p>On assure sa voiture et sa maison, mais rarement ce qui les finance : ses revenus. Que se passe-t-il si un arrêt de travail se prolonge, si une invalidité vous empêche de reprendre votre métier, ou si vous disparaissez ?</p>
<p>La prévoyance répond à ces questions avec trois types de garanties : des indemnités journalières en cas d'arrêt de travail, une rente en cas d'invalidité, un capital ou une rente pour vos proches en cas de décès. Les salariés sont en partie couverts par leur employeur. Les indépendants, beaucoup moins.</p>
<h2>La garantie des accidents de la vie</h2>
<p>Une chute dans l'escalier, un accident de bricolage, une brûlure en cuisine : ces accidents du quotidien, sans tiers responsable, ne sont couverts ni par votre assurance habitation ni par votre assurance auto. La garantie des accidents de la vie indemnise les conséquences d'un accident grave de la vie privée : préjudices, perte de revenus, aménagement du logement. Elle peut couvrir toute la famille.</p>
<div class="note"><p><strong>Pour gagner du temps :</strong> apportez votre tableau de garanties actuel et vos derniers décomptes de remboursement. En vingt minutes, on voit si votre contrat vous correspond.</p></div>''',
        [("Puis-je changer de mutuelle en cours d'année ?", "Oui. Après un an de contrat, vous pouvez résilier votre complémentaire santé à tout moment, sans frais. Le nouvel assureur peut s'occuper de la résiliation à votre place."),
         ("Qu'est-ce que le 100 % Santé ?", "C'est un ensemble de lunettes, de prothèses dentaires et d'aides auditives intégralement remboursées par l'Assurance maladie et votre complémentaire, si elle est dite responsable. Vous restez libre de choisir un équipement hors de ce panier, avec un reste à charge."),
         ("Y a-t-il un délai d'attente avant d'être remboursé ?", "Cela dépend des contrats et des garanties. Certains prévoient un délai de quelques mois sur des postes comme le dentaire ou l'optique. Je vous l'indique clairement avant toute souscription."),
         ("Je suis salarié avec une mutuelle d'entreprise, ai-je besoin d'autre chose ?", "Parfois oui. La mutuelle d'entreprise offre un socle qui peut être insuffisant sur certains postes : une surcomplémentaire peut alors le compléter. Et côté prévoyance, il est utile de vérifier ce que prévoit réellement votre employeur.")])

    # ------------------------------------------------------------ EPARGNE
    add("epargne-retraite", "part",
        "Assurance vie, épargne et retraite à Bougival | Conseil personnalisé",
        "Assurance vie, plan d'épargne retraite (PER), transmission : faites le point sur votre épargne avec votre agent général Gan à Bougival.",
        "Épargne et retraite", "Épargne, assurance vie et retraite à Bougival",
        "Mettre de l'argent de côté, préparer sa retraite, protéger ses proches : avant de parler de produits, on parle de vos projets et du temps que vous avez devant vous.",
        '''<h2>D'abord vos objectifs, ensuite les placements</h2>
<p>Il n'y a pas de bon placement dans l'absolu. Il y a un placement adapté à un projet, à une durée et à un tempérament. C'est pour cela que je commence toujours par trois questions simples :</p>
<ul>
<li><strong>À quoi servira cet argent ?</strong> Une réserve de sécurité, les études des enfants, un complément de revenu à la retraite, une transmission.</li>
<li><strong>Dans combien de temps en aurez-vous besoin ?</strong> Deux ans, dix ans, vingt ans : la réponse change tout.</li>
<li><strong>Quel risque êtes-vous prêt à accepter ?</strong> Certains supports garantissent le capital, d'autres peuvent rapporter plus, mais aussi baisser.</li>
</ul>
<h2>L'assurance vie, le couteau suisse de l'épargne</h2>
<p>L'assurance vie reste le placement préféré des Français, pour de bonnes raisons. Votre argent n'est pas bloqué : vous pouvez effectuer des retraits quand vous le souhaitez. Vous versez à votre rythme, librement ou tous les mois. Et vous choisissez la répartition entre deux familles de supports :</p>
<ul>
<li><strong>Le fonds en euros</strong>, dont le capital est garanti par l'assureur.</li>
<li><strong>Les unités de compte</strong>, investies sur les marchés financiers ou l'immobilier. Elles offrent un potentiel de rendement plus élevé sur le long terme, mais présentent un risque de perte en capital.</li>
</ul>
<p>Après huit ans, la fiscalité des retraits devient plus légère, avec un abattement annuel sur les gains. L'assurance vie est aussi un outil de transmission : vous désignez librement vos bénéficiaires, dans un cadre fiscal spécifique.</p>
<h2>Le plan d'épargne retraite (PER)</h2>
<p>Le PER est conçu pour une chose : vous constituer un complément de revenu pour la retraite. Son principal atout est fiscal : les sommes que vous versez peuvent être déduites de votre revenu imposable, dans la limite d'un plafond. Plus vous êtes imposé, plus l'avantage est important.</p>
<p>En contrepartie, l'épargne est bloquée jusqu'à la retraite, sauf dans quelques cas prévus par la loi, comme l'achat de votre résidence principale ou certains accidents de la vie. À la sortie, vous choisissez entre un capital, une rente, ou un mélange des deux.</p>
<div class="note"><p><strong>Mon conseil :</strong> assurance vie et PER ne s'opposent pas, ils se complètent. L'un garde votre argent disponible, l'autre allège vos impôts aujourd'hui. La bonne répartition dépend de votre situation.</p></div>
<h2>Gestion de patrimoine : structurer et transmettre</h2>
<p>J'accompagne depuis plus de vingt ans des dirigeants et des familles dans l'organisation de leur patrimoine. Au-delà du choix d'un placement, il s'agit de répondre à des questions de fond : comment répartir ce que vous possédez entre le professionnel et le privé, comment préparer des revenus pour la retraite, comment protéger votre conjoint, comment transmettre à vos enfants dans de bonnes conditions.</p>
<p>Je travaille en lien avec votre notaire et votre expert-comptable, pour que chaque décision soit cohérente avec l'ensemble.</p>
<h2>Protéger ses proches et préparer la transmission</h2>
<p>La rédaction de la clause bénéficiaire d'un contrat d'assurance vie est un point que l'on néglige trop souvent. Une clause mal rédigée ou jamais mise à jour après un mariage, une naissance ou une séparation peut avoir des conséquences que personne ne souhaitait. Je relis la vôtre avec vous.</p>
<p style="font-size:.9rem;color:var(--mute)">Les informations de cette page sont générales et ne constituent pas un conseil en investissement personnalisé. Les règles fiscales dépendent de votre situation et peuvent évoluer. Une recommandation ne peut vous être faite qu'après un échange sur votre situation, vos objectifs et votre connaissance des placements.</p>''',
        [("À partir de quel montant peut-on ouvrir une assurance vie ?", "Les montants d'ouverture sont accessibles, et vous pouvez ensuite mettre en place des versements réguliers adaptés à votre budget. L'important est de commencer tôt : c'est la durée qui fait le résultat."),
         ("Mon argent est-il bloqué pendant huit ans sur une assurance vie ?", "Non, c'est une idée reçue. Vous pouvez retirer tout ou partie de votre épargne à tout moment. Les huit ans correspondent seulement à la date à partir de laquelle la fiscalité des retraits devient plus favorable."),
         ("Le PER est-il intéressant si je paie peu d'impôts ?", "L'avantage fiscal à l'entrée est proportionnel à votre taux d'imposition. Si vous êtes peu ou pas imposé, l'assurance vie est souvent plus adaptée. C'est précisément le genre de calcul que je fais avec vous."),
         ("J'ai déjà des contrats ailleurs, pouvez-vous y jeter un oeil ?", "Bien sûr. Apportez vos derniers relevés : je regarde les frais, la répartition des supports et la clause bénéficiaire, et je vous dis ce que j'en pense.")])

    # ------------------------------------------------------------ EMPRUNTEUR
    add("assurance-emprunteur", "part",
        "Assurance emprunteur à Bougival | Assurer ou changer l'assurance de son prêt",
        "Assurance de prêt immobilier : délégation d'assurance, changement en cours de prêt, garanties décès, invalidité, arrêt de travail. Étude gratuite à l'agence Gan de Bougival.",
        "Assurance emprunteur", "Assurance de prêt immobilier à Bougival",
        "Sur la durée d'un crédit, l'assurance pèse lourd dans le coût total. Vous avez le droit de la choisir, et même d'en changer en cours de route. Encore faut-il comparer les bonnes choses.",
        '''<h2>À quoi sert l'assurance emprunteur ?</h2>
<p>Elle rembourse tout ou partie de votre prêt à votre place si vous ne pouvez plus le faire. Aucune loi ne l'impose, mais dans les faits, aucune banque ne prête sans elle. Elle protège la banque, bien sûr, mais surtout votre famille, qui ne se retrouve pas avec un crédit sur les bras.</p>
<p>Les garanties s'empilent selon votre projet et votre situation :</p>
<ul>
<li><strong>Décès et perte totale et irréversible d'autonomie</strong> : le socle, toujours exigé.</li>
<li><strong>Invalidité permanente</strong>, totale ou partielle.</li>
<li><strong>Incapacité temporaire de travail</strong> : l'assurance prend en charge vos mensualités pendant un arrêt de travail, après un délai de franchise.</li>
<li><strong>Perte d'emploi</strong> : une option, à étudier au cas par cas.</li>
</ul>
<h2>Vous n'êtes pas obligé de prendre l'assurance de la banque</h2>
<p>Quand vous signez un prêt, la banque vous propose son propre contrat, le même pour tous ses clients. Vous avez le droit de lui préférer un contrat extérieur, à une condition : qu'il présente des garanties au moins équivalentes. C'est ce qu'on appelle la délégation d'assurance. La banque ne peut ni refuser un contrat équivalent, ni modifier le taux de votre crédit en échange.</p>
<p>Un contrat individuel tient compte de votre âge, de votre profession et de votre état de santé. Pour beaucoup d'emprunteurs, l'économie sur la durée du prêt est réelle. Je vous le chiffre précisément avant toute décision.</p>
<h2>Changer d'assurance en cours de prêt</h2>
<p>Depuis 2022, vous pouvez changer d'assurance emprunteur à tout moment, sans frais et sans attendre la date anniversaire. La démarche est simple :</p>
<ol>
<li>Vous m'apportez votre offre de prêt et votre tableau d'amortissement.</li>
<li>Je compare vos garanties actuelles et je vous fais une proposition équivalente.</li>
<li>Si elle vous convient, je transmets le dossier à votre banque, qui dispose de dix jours ouvrés pour répondre.</li>
<li>L'ancien contrat s'arrête quand le nouveau commence. Vous n'êtes jamais sans couverture.</li>
</ol>
<div class="note"><p><strong>À retenir :</strong> ne comparez pas seulement le prix. La définition de l'invalidité, les exclusions liées au dos ou aux affections psychiques, la prise en charge forfaitaire ou indemnitaire des mensualités : c'est là que les contrats se distinguent vraiment.</p></div>
<h2>Santé : ce que la loi a changé</h2>
<p>Pour les prêts dont la part assurée ne dépasse pas 200 000 euros par personne et qui se terminent avant vos 60 ans, il n'y a plus de questionnaire médical. Et le droit à l'oubli permet, cinq ans après la fin d'un traitement pour un cancer ou une hépatite C, de ne plus avoir à le déclarer. Si vous avez ou avez eu un problème de santé, venez m'en parler en toute confidentialité : il existe presque toujours une solution.</p>''',
        [("Combien peut-on économiser en changeant d'assurance de prêt ?", "Tout dépend de votre âge, de votre profession, du capital restant dû et de la durée restante. L'écart peut être important, surtout en début de prêt. La seule façon de le savoir est de faire une étude, qui est gratuite et sans engagement."),
         ("Ma banque peut-elle refuser mon changement d'assurance ?", "Seulement si le nouveau contrat ne présente pas des garanties équivalentes à celles qu'elle exige. Dans ce cas, elle doit motiver son refus par écrit. C'est pourquoi je construis la proposition à partir des critères de votre banque."),
         ("Nous empruntons à deux, comment répartir l'assurance ?", "C'est ce qu'on appelle la quotité. Chacun peut être assuré à 50 %, à 100 %, ou selon une répartition qui reflète vos revenus. Assurer chacun à 100 % est plus protecteur : en cas de décès de l'un, le prêt est entièrement remboursé."),
         ("Faut-il assurer un prêt pour un investissement locatif ?", "Oui, la banque exige en général au moins les garanties décès et invalidité. Comme les loyers participent au remboursement, les garanties d'arrêt de travail sont parfois allégées.")])

    # ------------------------------------------------------------ ARTISANS COMMERCANTS
    add("assurance-artisans-commercants", "pro",
        "Assurance artisans et commerçants à Bougival | Multirisque professionnelle",
        "Multirisque professionnelle, responsabilité civile, décennale, perte d'exploitation : votre agent général Gan à Bougival assure les artisans, commerçants et restaurateurs.",
        "Artisans et commerçants", "Assurance des artisans et commerçants à Bougival",
        "Votre boutique, votre atelier, votre restaurant, votre camionnette : c'est votre outil de travail et souvent votre patrimoine. Je vous aide à le protéger sans payer pour l'inutile.",
        '''<h2>La multirisque professionnelle, la base de votre protection</h2>
<p>Elle réunit dans un seul contrat l'essentiel de ce dont une petite entreprise a besoin :</p>
<ul>
<li><strong>Vos locaux</strong>, que vous soyez propriétaire ou locataire : incendie, dégât des eaux, vol, vandalisme, bris de vitrine, événements climatiques.</li>
<li><strong>Votre contenu</strong> : matériel, outillage, mobilier, stock et marchandises.</li>
<li><strong>Votre responsabilité civile</strong> : les dommages causés à un client, un fournisseur ou un passant dans le cadre de votre activité.</li>
</ul>
<p>Ensuite, on ajuste selon votre métier. Un boulanger a besoin d'une garantie sur ses fours et sur les marchandises en chambre froide. Un fleuriste, sur sa vitrine et ses livraisons. Un coiffeur, sur les dommages causés à un client.</p>
<h2>La perte d'exploitation, la garantie qui sauve les entreprises</h2>
<p>Après un incendie ou un gros dégât des eaux, l'assurance paie les réparations. Mais pendant les semaines ou les mois de fermeture, le loyer, les salaires et les charges continuent, sans aucune recette en face. C'est cette période qui fait tomber des entreprises pourtant bien assurées pour leurs murs.</p>
<p>La garantie perte d'exploitation compense la baisse de votre chiffre d'affaires et prend en charge vos frais fixes le temps que l'activité reparte. C'est la première chose que je vérifie dans un contrat de commerçant.</p>
<h2>Artisans du bâtiment : la décennale</h2>
<p>Si vous intervenez sur la construction ou la rénovation, l'assurance de responsabilité décennale est obligatoire, et vous devez pouvoir en justifier avant l'ouverture de chaque chantier. Elle couvre pendant dix ans les dommages qui compromettent la solidité de l'ouvrage ou le rendent impropre à son usage.</p>
<p>L'attestation doit correspondre exactement aux activités que vous exercez. Un plombier qui pose aussi du carrelage sans l'avoir déclaré n'est pas couvert pour ce travail. On reprend ensemble la liste de vos activités réelles.</p>
<h2>Restaurants, métiers de bouche, commerces alimentaires</h2>
<p>Intoxication alimentaire, panne de chambre froide, dégât sur la terrasse, bris de machine : les risques sont nombreux et très spécifiques. Je regarde aussi votre extraction, vos installations de cuisson et vos obligations vis-à-vis du bailleur.</p>
<h2>Véhicules, outillage transporté, protection juridique</h2>
<ul>
<li><strong>Le véhicule professionnel</strong> et ce qu'il contient : l'outillage laissé dans une camionnette est une cible fréquente.</li>
<li><strong>La protection juridique</strong>, pour vous défendre en cas de litige avec un client qui ne paie pas, un fournisseur ou votre bailleur.</li>
<li><strong>Le bris de machine</strong> et le matériel informatique, caisse comprise.</li>
</ul>
<div class="note"><p><strong>Un point souvent oublié :</strong> prévenez-moi quand votre activité change. Un nouveau service, une embauche, un stock qui grossit avant les fêtes : un contrat qui n'a pas suivi peut laisser un trou le jour du sinistre.</p></div>''',
        [("La responsabilité civile professionnelle est-elle obligatoire ?", "Elle l'est pour certaines professions réglementées et, sous forme de décennale, pour les métiers du bâtiment. Pour les autres, elle n'est pas imposée par la loi mais elle est indispensable : un seul client blessé peut mettre votre entreprise en péril."),
         ("Je débute mon activité, par quoi commencer ?", "Par la responsabilité civile professionnelle, l'assurance de votre local si vous en avez un, et celle de votre véhicule s'il sert à l'activité. On complète ensuite au fur et à mesure que l'entreprise grandit."),
         ("Je travaille depuis chez moi, mon assurance habitation suffit-elle ?", "En général, non. La plupart des contrats habitation excluent l'activité professionnelle, le matériel et le stock. Il faut le déclarer et prévoir une extension ou un contrat professionnel."),
         ("Vous déplacez-vous dans mon commerce ?", "Oui, et c'est même préférable. Voir vos locaux et votre façon de travailler me permet de vous proposer un contrat juste.")])

    # ------------------------------------------------------------ LIBERALES
    add("assurance-professions-liberales", "pro",
        "Assurance professions libérales à Bougival | RC Pro, cabinet, cyber-risques",
        "Responsabilité civile professionnelle, assurance du cabinet, cyber-risques, protection juridique et prévoyance pour les professions libérales, à l'agence Gan de Bougival.",
        "Professions libérales", "Assurance des professions libérales à Bougival",
        "Professionnels de santé, du conseil, du droit, du chiffre ou de la création : votre risque principal, c'est votre responsabilité. Le second, c'est vous.",
        '''<h2>La responsabilité civile professionnelle</h2>
<p>Une erreur, un oubli, un conseil qui s'avère inadapté, un retard : quand votre client subit un préjudice du fait de votre prestation, il peut vous en demander réparation. La responsabilité civile professionnelle prend en charge l'indemnisation, mais aussi vos frais de défense, ce qui est loin d'être un détail.</p>
<p>Elle est obligatoire pour de nombreuses professions réglementées : professionnels de santé, avocats, experts-comptables, architectes, agents immobiliers, entre autres. Pour les consultants, formateurs, graphistes ou développeurs, elle n'est pas imposée par la loi, mais vos clients la demandent de plus en plus souvent avant de signer.</p>
<p>Trois points à regarder de près :</p>
<ul>
<li><strong>Les activités déclarées.</strong> Le contrat ne couvre que ce qui y est décrit. Si votre métier a évolué, le contrat doit suivre.</li>
<li><strong>Les plafonds de garantie</strong>, à mettre en rapport avec la taille de vos missions.</li>
<li><strong>La durée de la garantie après l'arrêt de l'activité.</strong> Une réclamation peut arriver plusieurs années après la prestation.</li>
</ul>
<h2>Votre cabinet et votre matériel</h2>
<p>Local, mobilier, matériel médical ou informatique, salle d'attente ouverte au public : l'assurance du cabinet couvre les dommages aux biens et votre responsabilité vis-à-vis des personnes que vous recevez. Si vous exercez à domicile ou en espace partagé, il existe des solutions adaptées. Pensez aussi au matériel que vous transportez : ordinateur portable, appareils de mesure, mallette de soins.</p>
<h2>Les cyber-risques ne concernent pas que les grandes entreprises</h2>
<p>Un rançongiciel qui bloque vos dossiers, un vol de données de patients ou de clients, une usurpation de votre messagerie pour détourner un paiement : les petites structures sont aujourd'hui des cibles de choix, justement parce qu'elles sont moins protégées.</p>
<p>Une assurance cyber prend en charge l'intervention d'experts pour remettre votre système en état, les frais de notification aux personnes concernées, la perte d'activité et votre responsabilité si des données ont fuité.</p>
<h2>Et si vous ne pouviez plus exercer ?</h2>
<p>En libéral, vos revenus dépendent directement de votre présence. Les régimes obligatoires prévoient des indemnités souvent limitées, et parfois après un long délai. Une prévoyance complémentaire maintient votre revenu en cas d'arrêt de travail, et une garantie de frais professionnels paie le loyer et les charges du cabinet pendant ce temps.</p>
<div class="note"><p><strong>Bon à savoir :</strong> la définition de l'invalidité est essentielle. Une garantie qui apprécie votre incapacité par rapport à votre profession, et non à n'importe quel travail, change tout pour un chirurgien-dentiste, un kinésithérapeute ou un architecte.</p></div>
<h2>La protection juridique</h2>
<p>Un patient ou un client mécontent, un impayé, un désaccord avec un associé ou un bailleur, un contrôle : la protection juridique vous donne accès à des juristes et prend en charge les frais de procédure, dans les limites du contrat.</p>''',
        [("Je suis en micro-entreprise, ai-je besoin d'une RC Pro ?", "Votre statut ne change rien à votre responsabilité : en cas de dommage causé à un client, vous êtes engagé sur vos biens. Une RC Pro est fortement recommandée, et obligatoire si votre profession est réglementée."),
         ("Mon assurance couvre-t-elle les missions réalisées à l'étranger ?", "Cela dépend de l'étendue territoriale prévue au contrat. Si vous travaillez pour des clients étrangers ou vous déplacez hors de France, il faut le préciser dès le départ."),
         ("Je partage mon cabinet avec des confrères, qui assure quoi ?", "Chacun doit assurer sa propre responsabilité professionnelle et son matériel. Les locaux et les parties communes peuvent être assurés par la structure commune ou répartis entre vous. Je vous aide à clarifier la situation."),
         ("Pouvez-vous reprendre un contrat en cours ?", "Oui. Je compare vos garanties actuelles, je vérifie qu'il n'y aura aucun trou de couverture au moment du changement, en particulier sur la reprise du passé en responsabilité civile.")])

    # ------------------------------------------------------------ DIRIGEANT
    add("protection-dirigeant", "ent",
        "Garantie chômage et protection du dirigeant | Prévoyance, retraite, homme-clé",
        "Prévoyance, retraite, perte d'emploi, responsabilité des dirigeants, assurance homme-clé : faites le point sur votre protection de chef d'entreprise à l'agence Gan de Bougival.",
        "Garantie chômage et protection du dirigeant", "Garantie chômage et protection sociale du dirigeant",
        "Vous protégez votre entreprise, vos salariés, vos locaux. Et vous ? Selon votre statut, votre couverture personnelle peut être bien plus mince que vous ne le pensez.",
        '''<h2>Votre statut décide de votre protection</h2>
<p>Gérant majoritaire de SARL, président de SAS, entrepreneur individuel : vous ne cotisez pas aux mêmes régimes, et vous n'avez pas les mêmes droits. Un travailleur non salarié paie moins de charges, mais reçoit moins en cas d'arrêt de travail et à la retraite. Un dirigeant assimilé salarié est mieux couvert, sauf sur un point : dans les deux cas, pas d'assurance chômage.</p>
<p>La première étape est donc un bilan de votre protection sociale. Je vous montre, chiffres à l'appui, ce que vous toucheriez réellement en cas d'arrêt de travail, d'invalidité, et à la retraite. C'est souvent une surprise.</p>
<h2>La prévoyance : maintenir vos revenus</h2>
<p>Que devient votre rémunération si vous êtes arrêté trois mois ? Et votre famille, si vous disparaissez ? Une prévoyance de dirigeant prévoit :</p>
<ul>
<li>des <strong>indemnités journalières</strong> en cas d'arrêt de travail, pour compléter celles de votre régime obligatoire ;</li>
<li>une <strong>rente d'invalidité</strong> si vous ne pouvez plus exercer ;</li>
<li>un <strong>capital décès</strong>, une rente pour votre conjoint ou une rente éducation pour vos enfants.</li>
</ul>
<p>Pour les travailleurs non salariés, les cotisations sont, sous conditions, déductibles du revenu professionnel.</p>
<h2>La retraite : compenser l'écart</h2>
<p>La baisse de revenu au moment de la retraite est en général plus marquée pour un chef d'entreprise que pour un salarié. Le plan d'épargne retraite permet de se constituer un complément, avec des versements déductibles dans certaines limites. Plus on commence tôt, moins l'effort est lourd. <a href="{R}preparer-retraite/">En savoir plus sur la préparation de la retraite</a>.</p>
<h2>La garantie chômage du dirigeant</h2>
<p>En cas de liquidation, de révocation ou de cession contrainte, un dirigeant n'a pas droit aux allocations chômage. Une assurance perte d'emploi spécifique peut lui verser un revenu de remplacement pendant une durée définie au contrat.</p>
<h2>Protéger l'entreprise si vous êtes absent</h2>
<ul>
<li><strong>L'assurance homme-clé</strong> : si la personne dont dépend l'activité, vous ou un collaborateur essentiel, est durablement absente, l'entreprise reçoit un capital pour compenser la perte de chiffre d'affaires et réorganiser l'activité.</li>
<li><strong>La garantie entre associés</strong> : en cas de décès de l'un d'eux, elle donne aux autres les moyens de racheter ses parts à ses héritiers.</li>
</ul>
<h2>Votre responsabilité personnelle de dirigeant</h2>
<p>Une faute de gestion, un manquement à une obligation légale, un litige avec un salarié : votre responsabilité personnelle peut être recherchée, y compris sur votre patrimoine privé. L'assurance de responsabilité des dirigeants prend en charge vos frais de défense et les éventuelles condamnations civiles.</p>
<div class="note"><p><strong>Mon conseil :</strong> faites ce bilan avec votre expert-comptable dans la boucle. Les choix de rémunération, de statut et de protection sociale se tiennent, et la meilleure solution se construit à trois.</p></div>''',
        [("Mon conjoint travaille avec moi, est-il protégé ?", "Cela dépend de son statut : conjoint collaborateur, salarié ou associé. Chaque statut ouvre des droits différents. C'est un point à vérifier absolument, car beaucoup de conjoints sont moins bien couverts qu'ils ne le croient."),
         ("Qui paie les cotisations, moi ou l'entreprise ?", "Les deux sont possibles selon votre statut et le type de contrat, avec des conséquences fiscales et sociales différentes. On regarde la solution la plus pertinente avec votre comptable."),
         ("Je viens de créer mon entreprise, est-ce trop tôt ?", "Au contraire. C'est quand l'entreprise est jeune que tout repose sur vous, et que votre arrêt serait le plus difficile à absorber. On peut commencer par une couverture simple et la faire évoluer."),
         ("Faut-il un bilan médical pour souscrire une prévoyance ?", "Un questionnaire de santé est généralement demandé, et des examens peuvent l'être selon votre âge et les montants garantis. Tout est traité de manière confidentielle.")])

    # ------------------------------------------------------------ COLLECTIVE FLOTTE
    add("sante-collective-flotte", "pro",
        "Mutuelle d'entreprise et flotte automobile à Bougival | TPE et PME",
        "Mutuelle d'entreprise obligatoire, prévoyance collective, assurance flotte automobile et véhicules professionnels : des solutions pour les TPE et PME à l'agence Gan de Bougival.",
        "Santé collective et flotte auto", "Mutuelle d'entreprise et flotte automobile",
        "Dès votre premier salarié, vous avez des obligations. Dès vos premiers véhicules, vous avez des risques. Deux sujets très différents, que je gère pour vous avec la même logique : simple et carré.",
        '''<h2>La mutuelle d'entreprise : ce que la loi vous impose</h2>
<p>Tout employeur du secteur privé doit proposer une complémentaire santé collective à ses salariés, quelle que soit la taille de l'entreprise. Trois règles à retenir :</p>
<ul>
<li>vous financez <strong>au moins la moitié</strong> de la cotisation ;</li>
<li>le contrat respecte un <strong>socle minimal de garanties</strong> ;</li>
<li>votre <strong>convention collective</strong> peut prévoir des obligations plus exigeantes, sur les garanties comme sur votre participation.</li>
</ul>
<p>Certains salariés peuvent demander à être dispensés d'adhésion, dans des cas précis : ils sont déjà couverts par la mutuelle de leur conjoint, ou sont en contrat court, par exemple. Ces dispenses doivent être formalisées par écrit. Je vous fournis les modèles.</p>
<h2>Bien la mettre en place</h2>
<p>La mise en place ne se résume pas à signer un contrat. Il faut un acte fondateur, le plus souvent une décision unilatérale de l'employeur, une information remise à chaque salarié, et le respect des conditions qui permettent à vos cotisations de bénéficier d'un régime social favorable. Une erreur de forme peut coûter cher lors d'un contrôle. Je vous accompagne à chaque étape.</p>
<h2>La prévoyance collective</h2>
<p>La prévoyance couvre vos salariés en cas d'arrêt de travail, d'invalidité ou de décès. Elle est obligatoire pour les cadres, et de nombreuses conventions collectives l'imposent aussi pour les autres salariés. Même quand elle ne l'est pas, c'est un vrai argument pour recruter et fidéliser : vos salariés savent que leur famille est protégée.</p>
<div class="note"><p><strong>Avant de venir :</strong> apportez-moi le nom de votre convention collective et votre contrat actuel. Je vérifie que vous êtes en conformité, ce qui n'est pas toujours le cas des contrats signés il y a plusieurs années.</p></div>
<h2>Vos véhicules professionnels</h2>
<p>Un utilitaire, deux voitures de fonction, une camionnette de livraison : dès que vos véhicules servent à l'activité, ils doivent être assurés pour un usage professionnel. Je regarde avec vous :</p>
<ul>
<li><strong>qui conduit</strong> : un conducteur désigné, ou tous les salariés autorisés ;</li>
<li><strong>ce qui est transporté</strong> : marchandises, outillage, matériel ;</li>
<li><strong>les aménagements</strong> du véhicule, qui doivent être déclarés pour être indemnisés ;</li>
<li><strong>l'immobilisation</strong> : un véhicule à l'arrêt, c'est du chiffre d'affaires en moins.</li>
</ul>
<h2>Le contrat flotte : un seul contrat pour tous vos véhicules</h2>
<p>À partir de quelques véhicules, un contrat flotte remplace les contrats individuels. Les avantages sont concrets : une seule échéance, une gestion simplifiée quand un véhicule entre ou sort du parc, et un tarif établi sur la sinistralité de l'ensemble plutôt que sur le bonus de chaque conducteur.</p>
<p>Je vous remets chaque année un point sur vos sinistres, avec des pistes pour les réduire. Moins d'accidents, c'est une prime qui baisse, et surtout des salariés en sécurité.</p>
<h2>Garages et professionnels de l'automobile</h2>
<p>Garagistes, carrossiers, concessionnaires, loueurs : votre métier a ses propres risques. Les véhicules que vos clients vous confient, les essais sur route, les véhicules en stock ou en dépôt-vente, l'outillage et les ponts élévateurs demandent un contrat conçu pour les professionnels de l'automobile. C'est un domaine que je connais bien.</p>
<h2>Vos salariés utilisent leur propre voiture ?</h2>
<p>Quand un salarié se déplace pour vous avec son véhicule personnel, son assurance doit le prévoir, et votre responsabilité d'employeur peut être engagée. Une garantie spécifique permet de couvrir ces déplacements. C'est un point très souvent oublié.</p>''',
        [("Je n'ai qu'un seul salarié, la mutuelle est-elle obligatoire ?", "Oui. L'obligation s'applique dès le premier salarié, quels que soient son contrat et son temps de travail, sous réserve des cas de dispense prévus par les textes."),
         ("Le dirigeant peut-il bénéficier de la mutuelle de l'entreprise ?", "Cela dépend de votre statut. Un dirigeant assimilé salarié peut en général en bénéficier. Un travailleur non salarié relève d'un contrat individuel, dont les cotisations peuvent être déductibles sous conditions."),
         ("À partir de combien de véhicules parle-t-on de flotte ?", "Le seuil varie selon les contrats, mais on peut l'envisager dès quelques véhicules. En dessous, des contrats individuels à usage professionnel restent la bonne solution."),
         ("Que se passe-t-il si un salarié a un accident avec un véhicule de la société ?", "L'assurance du véhicule indemnise les tiers, et les dommages au véhicule selon les garanties souscrites. Si le salarié est blessé pendant son travail, il s'agit d'un accident du travail. D'où l'importance d'un contrat qui autorise bien tous les conducteurs concernés.")])

    get = lambda slug: next(x for x in out if x["slug"] == slug)
    def cut(body, start, end):
        i = body.index(start); j = body.index(end, i)
        return body[:i] + body[j:]

    # Sante seule (la prevoyance a sa propre page)
    x = get("mutuelle-sante-prevoyance")
    x["slug"] = "mutuelle-sante"
    x["title"] = "Mutuelle santé à Bougival | Complémentaire santé sur mesure | Agent Gan"
    x["desc"] = "Complémentaire santé à Bougival : comparez vos garanties avec votre agent général Gan. Hospitalisation, optique, dentaire, familles, retraités, indépendants."
    x["crumbs"][-1] = ("Complémentaire santé", None)
    x["hero"].update(h1="Mutuelle santé à Bougival", lead="Une bonne complémentaire santé rembourse bien ce dont vous avez réellement besoin, sans vous faire payer le reste. On la choisit à partir de vos dépenses réelles.")
    x["body"] = cut(x["body"], "<h2>La prévoyance, la grande oubliée</h2>", '<div class="note">') + '''<h2>Et vos revenus, en cas d'arrêt de travail ?</h2>
<p>La mutuelle rembourse vos soins. Elle ne remplace pas votre salaire si vous êtes arrêté plusieurs mois. C'est le rôle de la prévoyance, un contrat différent et complémentaire. <a href="{R}prevoyance/">Découvrir la prévoyance</a>.</p>'''

    # Epargne seule (la retraite a sa propre page)
    x = get("epargne-retraite")
    x["slug"] = "epargne-assurance-vie"
    x["title"] = "Assurance vie et épargne à Bougival | Patrimoine, transmission | Agent Gan"
    x["desc"] = "Assurance vie, épargne, structuration du patrimoine et transmission : faites le point avec votre agent général Gan à Bougival, au service des familles et des dirigeants depuis 2005."
    x["crumbs"][-1] = ("Épargne et assurance vie", None)
    x["hero"].update(h1="Épargne et assurance vie à Bougival", lead="Mettre de l'argent de côté, le faire fructifier, protéger vos proches : avant de parler de produits, on parle de vos projets et du temps que vous avez devant vous.")
    x["body"] = cut(x["body"], "<h2>Le plan d'épargne retraite (PER)</h2>", "<h2>Gestion de patrimoine") .replace("comment préparer des revenus pour la retraite,", 'comment <a href="{R}preparer-retraite/">préparer des revenus pour la retraite</a>,')
    x["faq"] = [f for f in x["faq"] if "PER" not in f[0]]

    # Salaries / vehicules : deux pages Entreprises
    old = get("sante-collective-flotte"); out.remove(old)
    mark = "<h2>Vos véhicules professionnels</h2>"
    b1, b2 = old["body"].split(mark)
    i = b1.index("<h2>La prévoyance collective</h2>"); j = b1.index('<div class="note">')
    b1 = b1[:i] + b1[j:] + '''<h2>Et la prévoyance ?</h2>
<p>La mutuelle rembourse les soins. La prévoyance, elle, protège vos salariés en cas d'arrêt de travail, d'invalidité ou de décès. Ce sont deux contrats distincts, avec des obligations différentes. <a href="{R}prevoyance-collective/">Voir la prévoyance collective</a>.</p>'''
    add("mutuelle-entreprise", "ent",
        "Mutuelle d'entreprise obligatoire | Santé collective | Agent Gan à Bougival",
        "Mutuelle d'entreprise obligatoire : mise en place, participation de l'employeur, dispenses, conformité à votre convention collective. Agence Gan Assurances de Bougival.",
        "Santé collective", "Mutuelle d'entreprise : la santé collective de vos salariés",
        "Dès votre premier salarié, vous devez proposer une complémentaire santé. Bien menée, cette obligation devient un vrai atout pour recruter et garder vos équipes.",
        b1, old["faq"][:2] + [("Peut-on changer de mutuelle d'entreprise ?", "Oui. Après la première année, le contrat collectif peut être résilié à tout moment par l'employeur. Il faut informer les salariés et veiller à ce que le nouveau contrat respecte la convention collective. Je m'occupe du dossier avec vous.")])
    add("flotte-automobile-garages", "ent",
        "Assurance flotte automobile et garages | Agent Gan à Bougival",
        "Assurance des véhicules de société, contrat flotte, garages et professionnels de l'automobile : une gestion simple et un suivi de vos sinistres à l'agence Gan de Bougival.",
        "Flotte automobile et garages", "Flotte automobile et garages",
        "Un utilitaire, dix véhicules de fonction ou un atelier de mécanique : dès que l'automobile fait partie de votre activité, le contrat doit suivre.",
        mark + b2, old["faq"][2:])
    return out
