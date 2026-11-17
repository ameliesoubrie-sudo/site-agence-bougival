def pages(g):
    out = []
    PARENTS = {"part": ("Particuliers", "assurance-particuliers"), "pro": ("Professionnels", "assurance-professionnels"), "ent": ("Entreprises", "assurance-entreprises")}
    BTN = '<div class="btn-row"><a class="btn btn-main" href="{R}contact/">%s</a></div>'

    def add(slug, family, title, desc, kicker, h1, lead, body, faq):
        out.append(dict(slug=slug, family=family, kind="product", title=title, desc=desc,
                        crumbs=[PARENTS[family], (kicker, None)],
                        hero=dict(type="product", kicker=kicker, h1=h1, lead=lead), body=body, faq=faq))

    # ------------------------------------------------------------ PREVOYANCE (particuliers)
    add("prevoyance", "part",
        "Prévoyance à Bougival | Arrêt de travail, invalidité, décès | Agent Gan",
        "Assurance prévoyance : maintenez vos revenus en cas d'arrêt de travail ou d'invalidité et protégez vos proches en cas de décès. Bilan gratuit à l'agence Gan de Bougival.",
        "Prévoyance", "Prévoyance : protéger vos revenus et vos proches",
        "On assure sa voiture et sa maison, mais rarement ce qui les finance : ses revenus. La prévoyance sert à cela.",
        '''<h2>La prévoyance, ce n'est pas la mutuelle</h2>
<p>On confond souvent les deux. La mutuelle rembourse vos frais de santé : consultations, hôpital, lunettes. La prévoyance, elle, vous verse de l'argent quand un accident ou une maladie vous empêche de travailler, ou quand vos proches doivent continuer sans vous.</p>
<p>Autrement dit : la mutuelle paie vos soins, la prévoyance paie vos factures.</p>
<h2>Les trois situations couvertes</h2>
<ul>
<li><strong>L'arrêt de travail.</strong> Vous recevez des indemnités journalières qui complètent celles de la Sécurité sociale, pour maintenir votre niveau de vie.</li>
<li><strong>L'invalidité.</strong> Si vous ne pouvez plus exercer votre métier, une rente vous est versée.</li>
<li><strong>Le décès.</strong> Vos proches reçoivent un capital, et selon le contrat une rente pour le conjoint ou pour les études des enfants.</li>
</ul>
<h2>Êtes-vous bien couvert aujourd'hui ?</h2>
<p>Posez-vous une seule question : si je suis arrêté six mois, combien vais-je toucher, et pendant combien de temps ? La plupart des gens ne le savent pas.</p>
<ul>
<li><strong>Salarié</strong> : votre employeur vous couvre en partie, mais rarement à 100 % et pas toujours longtemps.</li>
<li><strong>Indépendant</strong> : votre régime obligatoire verse peu, et parfois tard. <a href="{R}protection-sociale-independants/">Voir la protection des indépendants</a>.</li>
<li><strong>Parent, ou seul revenu du foyer</strong> : c'est là que la question du décès et de l'invalidité compte le plus.</li>
<li><strong>Emprunteur</strong> : l'assurance du prêt rembourse la banque, pas vos autres dépenses.</li>
</ul>
<div class="note"><p><strong>Le bilan prévoyance :</strong> apportez votre dernier bulletin de salaire ou votre attestation de régime. Je calcule avec vous ce que vous toucheriez réellement, et ce qui manque. C'est gratuit et sans engagement.</p></div>
''' + BTN % "Demander mon bilan prévoyance" + '''
<h2>La garantie des accidents de la vie</h2>
<p>Une chute dans l'escalier, un accident de bricolage, une brûlure en cuisine : ces accidents du quotidien, sans tiers responsable, ne sont couverts ni par votre assurance habitation ni par votre assurance auto. La garantie des accidents de la vie indemnise les conséquences d'un accident grave de la vie privée. Elle peut couvrir toute la famille.</p>
<h2>Combien ça coûte ?</h2>
<p>Le tarif dépend de votre âge, de votre métier et du niveau de protection choisi. On peut commencer par l'essentiel et renforcer ensuite. Le plus simple est d'en parler : dix minutes suffisent pour un premier chiffrage.</p>''',
        [("Quelle est la différence entre mutuelle et prévoyance ?", "La mutuelle rembourse vos dépenses de santé. La prévoyance vous verse un revenu ou un capital en cas d'arrêt de travail, d'invalidité ou de décès. Les deux se complètent."),
         ("Je suis salarié, ai-je besoin d'une prévoyance personnelle ?", "Cela dépend de ce que prévoit votre entreprise. Certaines couvrent bien leurs salariés, d'autres se limitent au minimum. Je regarde votre contrat collectif avec vous et je ne vous propose un complément que s'il y a un vrai manque."),
         ("Faut-il passer une visite médicale ?", "Un questionnaire de santé est généralement demandé. Des examens peuvent s'y ajouter selon votre âge et les montants garantis. Tout est confidentiel.")])

    # ------------------------------------------------------------ RETRAITE (particuliers)
    add("preparer-retraite", "part",
        "Préparer sa retraite à Bougival | PER, bilan retraite | Agent Gan",
        "Préparer sa retraite : bilan retraite, plan d'épargne retraite (PER), complément de revenu. Faites le point avec votre agent général Gan à Bougival, depuis 2005.",
        "Retraite", "Préparer sa retraite, sans attendre",
        "À la retraite, les revenus baissent. De combien, cela dépend de votre carrière. La bonne nouvelle : plus on s'y prend tôt, moins l'effort est lourd.",
        '''<h2>Savez-vous combien vous toucherez ?</h2>
<p>C'est la première question, et peu de gens connaissent la réponse. Votre pension dépend de votre statut, de vos années de cotisation et de vos revenus. Pour un cadre, un indépendant ou un dirigeant, l'écart entre le dernier revenu et la pension peut être important.</p>
<p>Avant de parler de placement, je vous propose donc un bilan retraite : où vous en êtes, ce que vous pouvez attendre, et l'écart à combler pour garder votre niveau de vie.</p>
''' + BTN % "Demander mon bilan retraite" + '''
<h2>Le plan d'épargne retraite (PER)</h2>
<p>Le PER est conçu pour une chose : vous constituer un complément de revenu pour la retraite. Son principal atout est fiscal : les sommes que vous versez peuvent être déduites de votre revenu imposable, dans la limite d'un plafond. Plus vous êtes imposé, plus l'avantage est important.</p>
<p>En contrepartie, l'épargne est bloquée jusqu'à la retraite, sauf dans quelques cas prévus par la loi, comme l'achat de votre résidence principale ou certains accidents de la vie. À la sortie, vous choisissez entre un capital, une rente, ou un mélange des deux.</p>
<h2>À quel âge commencer ?</h2>
<ul>
<li><strong>Avant 40 ans</strong> : de petits versements réguliers suffisent, le temps fait le reste.</li>
<li><strong>Entre 40 et 55 ans</strong> : c'est souvent le moment où les revenus sont les plus élevés, et l'avantage fiscal le plus intéressant.</li>
<li><strong>Après 55 ans</strong> : il n'est pas trop tard. On organise ce qui existe déjà et on prépare le passage à la retraite.</li>
</ul>
<h2>Le PER n'est pas la seule solution</h2>
<p>Selon votre situation, l'assurance vie, qui reste disponible à tout moment, peut être plus adaptée, ou venir en complément. Si vous êtes peu imposé, elle est même souvent préférable. <a href="{R}epargne-assurance-vie/">Voir l'épargne et l'assurance vie</a>.</p>
<div class="note"><p><strong>Bon à savoir :</strong> si vous avez d'anciens contrats retraite (Madelin, PERP, article 83), ils peuvent être regroupés sur un PER. Apportez vos relevés, je regarde si c'est intéressant pour vous.</p></div>
<h2>Vous approchez de la retraite ?</h2>
<p>C'est le moment de vérifier votre relevé de carrière, de choisir entre capital et rente, d'adapter votre mutuelle et de mettre à jour les bénéficiaires de vos contrats. Je vous accompagne sur l'ensemble.</p>
<p style="font-size:.9rem;color:var(--mute)">Ces informations sont générales et ne constituent pas un conseil personnalisé. Les règles fiscales dépendent de votre situation et peuvent évoluer.</p>''',
        [("Le PER est-il intéressant si je paie peu d'impôts ?", "L'avantage fiscal à l'entrée est proportionnel à votre taux d'imposition. Si vous êtes peu ou pas imposé, l'assurance vie est souvent plus adaptée. C'est le genre de calcul que je fais avec vous."),
         ("Puis-je récupérer mon argent avant la retraite ?", "Oui dans certains cas prévus par la loi : l'achat de votre résidence principale, ou des accidents de la vie comme l'invalidité, le décès du conjoint ou la fin de droits au chômage."),
         ("Combien faut-il verser ?", "Il n'y a pas de bon montant dans l'absolu. On part de l'écart entre votre pension estimée et le revenu que vous souhaitez, puis on adapte l'effort à votre budget. Les versements peuvent être modifiés ou suspendus.")])

    # ------------------------------------------------------------ INDEPENDANTS
    add("protection-sociale-independants", "pro",
        "Indépendants : santé, prévoyance et retraite du TNS | Agent Gan à Bougival",
        "Artisans, commerçants, professions libérales : complémentaire santé, prévoyance et retraite des travailleurs non salariés. Bilan de protection sociale à l'agence Gan de Bougival.",
        "Protection sociale des indépendants", "Indépendants : votre protection sociale",
        "À votre compte, vous cotisez moins qu'un salarié. La contrepartie, c'est une couverture plus mince, que l'on découvre souvent le jour où on en a besoin.",
        '''<h2>Ce que votre régime ne couvre pas</h2>
<p>Artisan, commerçant ou profession libérale, vous relevez du régime des travailleurs non salariés. Il vous protège, mais avec des limites nettes :</p>
<ul>
<li><strong>En cas d'arrêt de travail</strong> : des indemnités plafonnées, parfois après un long délai, et aucune pour certaines professions libérales les premiers mois.</li>
<li><strong>En cas d'invalidité</strong> : une pension souvent très inférieure à vos revenus.</li>
<li><strong>À la retraite</strong> : une pension généralement plus faible que celle d'un salarié à revenu égal.</li>
<li><strong>Et pas de mutuelle d'entreprise</strong> : c'est à vous de la choisir.</li>
</ul>
<p>Pendant ce temps, vos charges professionnelles, elles, continuent.</p>
<h2>Trois contrats, trois besoins différents</h2>
<h3>La complémentaire santé</h3>
<p>Elle rembourse vos frais de soins et ceux de votre famille. Vous la choisissez librement, selon vos dépenses réelles.</p>
<h3>La prévoyance</h3>
<p>Elle maintient votre revenu si vous êtes arrêté, vous verse une rente en cas d'invalidité et protège vos proches en cas de décès. Une garantie de frais professionnels peut aussi payer votre loyer et vos charges pendant votre arrêt.</p>
<h3>La retraite</h3>
<p>Le plan d'épargne retraite vous permet de vous constituer un complément de revenu, à votre rythme.</p>
<div class="note"><p><strong>L'avantage fiscal :</strong> vos cotisations santé, prévoyance et retraite peuvent, dans certaines limites, être déduites de votre revenu professionnel. Une partie de l'effort est donc financée par l'économie d'impôt.</p></div>
<h2>Par où commencer ?</h2>
<p>Par un bilan. J'ai besoin de votre statut, de votre caisse et de vos revenus. Je vous montre, chiffres à l'appui, ce que vous toucheriez en cas d'arrêt de travail, d'invalidité et à la retraite, puis ce qu'il est raisonnable de compléter en priorité.</p>
''' + BTN % "Demander mon bilan d'indépendant" + '''
<h2>Et votre conjoint ?</h2>
<p>S'il travaille avec vous, son statut (collaborateur, salarié ou associé) détermine ses droits. C'est un point à vérifier absolument.</p>''',
        [("Je suis en micro-entreprise, suis-je concerné ?", "Oui. Votre couverture dépend de vos cotisations, donc de votre chiffre d'affaires. Avec un petit chiffre d'affaires, les indemnités en cas d'arrêt peuvent être très faibles. Une prévoyance de base est souvent le premier contrat à envisager."),
         ("Quelle garantie souscrire en premier ?", "Le plus souvent la prévoyance, car un arrêt de travail peut mettre votre activité en danger en quelques semaines. Viennent ensuite la santé, puis la retraite."),
         ("Les cotisations sont-elles vraiment déductibles ?", "Oui, dans la limite de plafonds qui dépendent de vos revenus. Je vous indique le montant déductible et votre expert-comptable le valide.")])

    # ------------------------------------------------------------ MULTIRISQUE ENTREPRISE
    add("multirisque-entreprise", "ent",
        "Assurance multirisque entreprise et responsabilité civile | Agent Gan Bougival",
        "Multirisque professionnelle, responsabilité civile, locaux, équipements, perte d'exploitation, protection juridique, cyber-risques : l'assurance de votre entreprise à Bougival.",
        "Multirisque et responsabilité civile", "Assurance multirisque et responsabilité civile de l'entreprise",
        "Vos locaux, vos machines, vos stocks, votre responsabilité : ce qui fait tourner l'entreprise doit pouvoir repartir vite après un sinistre.",
        '''<h2>Ce que couvre la multirisque professionnelle</h2>
<ul>
<li><strong>Les locaux</strong>, que vous soyez propriétaire ou locataire : incendie, dégât des eaux, tempête, vol, vandalisme.</li>
<li><strong>Les équipements</strong> : machines, matériel informatique, mobilier, installations.</li>
<li><strong>Les stocks et les marchandises</strong>, y compris pendant le transport.</li>
<li><strong>Le bris de machine</strong> et les dommages électriques.</li>
</ul>
<h2>La responsabilité civile de l'entreprise</h2>
<p>Elle prend en charge les dommages que votre entreprise cause à un client, un fournisseur ou un tiers : pendant l'activité, après la livraison d'un produit ou la fin d'une prestation, ou du fait d'une erreur professionnelle. Elle couvre l'indemnisation et vos frais de défense.</p>
<h2>La perte d'exploitation</h2>
<p>Après un sinistre important, les réparations sont payées par l'assurance. Mais pendant l'arrêt, les salaires, les loyers et les charges continuent sans recettes en face. La garantie perte d'exploitation compense la baisse de chiffre d'affaires et finance les frais fixes jusqu'à la reprise. C'est elle qui permet à l'entreprise de survivre.</p>
<h2>Les garanties qui complètent l'ensemble</h2>
<ul>
<li><strong>La protection juridique</strong> : litiges avec un client, un fournisseur, un salarié ou l'administration.</li>
<li><strong>Les cyber-risques</strong> : piratage, rançongiciel, fuite de données, fraude au virement.</li>
<li><strong>La <a href="{R}flotte-automobile-garages/">flotte automobile</a></strong> et les déplacements professionnels.</li>
</ul>
<div class="note"><p><strong>Ma méthode :</strong> je viens dans vos locaux. On fait le tour de l'activité, je relève ce qui a changé depuis la signature de vos contrats (surface, matériel, effectif, chiffre d'affaires) et je vous remets un point clair sur ce qui est couvert et ce qui ne l'est plus.</p></div>
''' + BTN % "Demander un audit de mes contrats",
        [("Mon entreprise a grandi, mon contrat est-il toujours valable ?", "Il reste valable, mais il peut être sous-dimensionné. Si les capitaux déclarés sont inférieurs à la réalité, l'indemnité peut être réduite en proportion. D'où l'intérêt de le revoir régulièrement."),
         ("La responsabilité civile est-elle obligatoire ?", "Elle l'est pour certaines activités réglementées. Pour les autres, elle est exigée dans les faits par les clients, les bailleurs et les donneurs d'ordre."),
         ("Assurez-vous aussi les locaux dont je suis seulement locataire ?", "Oui. Le locataire assure sa responsabilité vis-à-vis du propriétaire, ses aménagements et tout son contenu. Le bail précise en général ce qui est à votre charge.")])

    # ------------------------------------------------------------ PREVOYANCE COLLECTIVE
    add("prevoyance-collective", "ent",
        "Prévoyance collective des salariés | Obligations de l'employeur | Agent Gan",
        "Prévoyance collective : arrêt de travail, invalidité, décès. Obligations pour les cadres et selon votre convention collective, mise en place et suivi à l'agence Gan de Bougival.",
        "Prévoyance collective", "Prévoyance collective : protéger vos salariés",
        "Un salarié arrêté plusieurs mois, un décès dans l'équipe : la prévoyance collective protège vos salariés et leurs familles, et vous évite de porter seul ce coût.",
        '''<h2>À quoi sert la prévoyance collective ?</h2>
<p>Elle n'a rien à voir avec la mutuelle, qui rembourse les soins. La prévoyance verse de l'argent quand un salarié ne peut plus travailler, ou à sa famille s'il décède :</p>
<ul>
<li><strong>Arrêt de travail</strong> : un complément de salaire, en plus de la Sécurité sociale.</li>
<li><strong>Invalidité</strong> : une rente.</li>
<li><strong>Décès</strong> : un capital pour les proches, et selon le contrat une rente pour le conjoint ou les enfants.</li>
</ul>
<h2>Est-ce obligatoire ?</h2>
<ul>
<li><strong>Pour vos cadres</strong> : oui. L'employeur doit financer une couverture décès minimale.</li>
<li><strong>Pour les autres salariés</strong> : cela dépend de votre convention collective. Beaucoup l'imposent, avec des garanties précises.</li>
<li><strong>Dans tous les cas</strong> : vous devez maintenir une partie du salaire pendant un arrêt maladie. Un contrat de prévoyance peut prendre ce coût en charge à votre place.</li>
</ul>
<div class="note"><p><strong>À vérifier :</strong> une prévoyance absente ou non conforme peut vous obliger, en cas de décès d'un salarié, à verser vous-même le capital prévu par les textes. Donnez-moi le nom de votre convention collective, je vérifie où vous en êtes.</p></div>
<h2>Un avantage pour l'entreprise aussi</h2>
<p>Les cotisations bénéficient d'un cadre social et fiscal favorable, sous conditions. Et pour vos salariés, savoir que leur famille est protégée compte vraiment : c'est un argument de recrutement et de fidélisation, souvent moins coûteux qu'une augmentation équivalente.</p>
''' + BTN % "Faire vérifier ma conformité" + '''
<h2>Mise en place et suivi</h2>
<p>Je m'occupe de l'acte de mise en place, de la notice à remettre aux salariés et de l'adhésion de chacun. Chaque année, je fais le point avec vous sur les arrêts et sur l'évolution du contrat. Pour la santé, voir la page <a href="{R}mutuelle-entreprise/">mutuelle d'entreprise</a>.</p>''',
        [("La prévoyance est-elle obligatoire pour tous mes salariés ?", "Elle l'est pour les cadres. Pour les autres, tout dépend de votre convention collective ou d'un accord de branche. Je le vérifie pour vous."),
         ("Qui paie les cotisations ?", "L'employeur, en totalité ou en partie selon les garanties et les textes applicables. La part du salarié, quand il y en a une, est prélevée sur sa paie."),
         ("Le dirigeant est-il couvert par ce contrat ?", "S'il est assimilé salarié, il peut en bénéficier. Sinon, il relève d'un contrat individuel. Dans les deux cas, je recommande de regarder sa situation à part : voir la protection du dirigeant.")])

    # ------------------------------------------------------------ EPARGNE SALARIALE
    add("epargne-salariale", "ent",
        "Épargne salariale : intéressement, participation, PEE | Agent Gan Bougival",
        "Épargne salariale pour TPE et PME : intéressement, participation, plan d'épargne entreprise, abondement. Fidélisez vos salariés et profitez-en aussi comme dirigeant.",
        "Épargne salariale", "Épargne salariale : associer vos salariés aux résultats",
        "Verser une prime qui coûte moins cher à l'entreprise et rapporte plus au salarié qu'une augmentation : c'est tout l'intérêt de l'épargne salariale. Et elle n'est pas réservée aux grands groupes.",
        '''<h2>Comment ça marche ?</h2>
<p>L'épargne salariale repose sur quelques outils simples, que l'on combine selon vos objectifs :</p>
<ul>
<li><strong>L'intéressement</strong> : une prime liée aux résultats ou aux performances de l'entreprise, selon une formule que vous définissez.</li>
<li><strong>La participation</strong> : une part des bénéfices redistribuée aux salariés. Elle est obligatoire à partir de 50 salariés.</li>
<li><strong>Le plan d'épargne entreprise (PEE)</strong> : un compte sur lequel le salarié place ces sommes, ainsi que ses propres versements.</li>
<li><strong>L'abondement</strong> : le coup de pouce de l'entreprise, qui complète les versements du salarié.</li>
</ul>
<h2>Pourquoi c'est intéressant pour l'entreprise</h2>
<ul>
<li>Les sommes versées bénéficient d'un régime social allégé par rapport à un salaire.</li>
<li>Elles sont déductibles du bénéfice imposable.</li>
<li>Vous motivez et fidélisez vos équipes, avec une prime qui dépend des résultats.</li>
</ul>
<h2>Pourquoi c'est intéressant pour le salarié</h2>
<p>Les sommes placées sur le plan d'épargne sont exonérées d'impôt sur le revenu, en contrepartie d'un blocage de cinq ans. De nombreux cas permettent de les récupérer plus tôt : achat de la résidence principale, mariage, naissance du troisième enfant, entre autres.</p>
<div class="note"><p><strong>Le dirigeant aussi :</strong> dans les entreprises de 1 à moins de 250 salariés, le chef d'entreprise et son conjoint collaborateur ou associé peuvent bénéficier de l'épargne salariale. C'est souvent ce qui déclenche la mise en place.</p></div>
<h2>Votre entreprise est-elle concernée ?</h2>
<p>Dès le premier salarié, vous pouvez mettre en place un dispositif. Et depuis 2025, les entreprises de 11 à 49 salariés qui dégagent des bénéfices réguliers doivent, sous conditions, proposer un mécanisme de partage de la valeur. Je fais le point avec vous et votre expert-comptable.</p>
''' + BTN % "Étudier la mise en place" + '''
<p>Pour aller plus loin, l'épargne salariale se combine avec un plan de <a href="{R}retraite-entreprise/">retraite collective</a>.</p>
<p style="font-size:.9rem;color:var(--mute)">Informations générales. Les régimes sociaux et fiscaux dépendent de la taille de l'entreprise et peuvent évoluer.</p>''',
        [("Faut-il un nombre minimum de salariés ?", "Non. Un seul salarié, en plus du dirigeant, suffit pour mettre en place un plan d'épargne ou un accord d'intéressement."),
         ("Est-ce compliqué à mettre en place ?", "Moins qu'on ne le pense. Dans les petites entreprises, l'intéressement et le plan d'épargne peuvent être mis en place par décision de l'employeur dans certains cas. Je prépare les documents avec vous."),
         ("Que se passe-t-il si l'entreprise ne fait pas de bénéfices ?", "L'intéressement et la participation dépendent des résultats : une mauvaise année, il n'y a rien à verser. C'est ce qui en fait un outil souple.")])

    # ------------------------------------------------------------ RETRAITE ENTREPRISE
    add("retraite-entreprise", "ent",
        "Retraite collective : PER d'entreprise pour salariés et dirigeant | Agent Gan",
        "Plan d'épargne retraite d'entreprise (PER collectif, PER obligatoire) : un complément de retraite pour vos salariés et pour vous, dans un cadre social et fiscal favorable.",
        "Retraite collective", "Retraite collective : le plan d'épargne retraite d'entreprise",
        "Aider vos salariés à préparer leur retraite, et préparer la vôtre par la même occasion : c'est ce que permet le plan d'épargne retraite d'entreprise.",
        '''<h2>Deux formules, selon votre objectif</h2>
<h3>Le PER d'entreprise collectif</h3>
<p>Il est ouvert à tous les salariés. Chacun y verse ce qu'il souhaite : son intéressement, sa participation, des jours de repos non pris ou des versements personnels. L'entreprise peut compléter par un abondement.</p>
<h3>Le PER d'entreprise obligatoire</h3>
<p>Il peut être réservé à une catégorie de salariés, par exemple les cadres. L'entreprise y verse une cotisation régulière, à laquelle le salarié peut ajouter la sienne. C'est un outil efficace pour fidéliser vos collaborateurs clés.</p>
<h2>Les avantages pour l'entreprise</h2>
<ul>
<li>Les versements de l'employeur sont déductibles du résultat et bénéficient, dans certaines limites, d'un régime social allégé.</li>
<li>Vous proposez un avantage concret, apprécié des cadres et des profils expérimentés.</li>
<li>Vous pouvez en bénéficier vous-même si votre statut le permet.</li>
</ul>
<h2>Les avantages pour le salarié</h2>
<p>Le salarié se constitue une épargne pour sa retraite, qu'il récupère en capital ou en rente. S'il quitte l'entreprise, il garde son épargne et peut la transférer. Elle peut être débloquée plus tôt pour l'achat de sa résidence principale ou en cas d'accident de la vie.</p>
<div class="note"><p><strong>Pour le dirigeant :</strong> la retraite collective est l'un des moyens les plus efficaces de préparer votre propre retraite avec la trésorerie de l'entreprise. C'est un point que j'étudie toujours avec votre expert-comptable.</p></div>
''' + BTN % "Étudier un plan pour mon entreprise" + '''
<h2>Vous avez déjà un ancien contrat ?</h2>
<p>Les anciens contrats de retraite d'entreprise (article 83, PERCO) peuvent être transformés ou transférés vers un PER. Je regarde avec vous si l'opération est intéressante.</p>
<p>Voir aussi : <a href="{R}epargne-salariale/">l'épargne salariale</a> et la <a href="{R}protection-dirigeant/">protection du dirigeant</a>.</p>
<p style="font-size:.9rem;color:var(--mute)">Informations générales. Les régimes sociaux et fiscaux dépendent de la situation de l'entreprise et peuvent évoluer.</p>''',
        [("Peut-on réserver la retraite collective aux cadres ?", "Oui, avec un PER d'entreprise obligatoire, à condition de viser une catégorie objective de salariés, définie selon les règles en vigueur."),
         ("Que devient l'épargne d'un salarié qui part ?", "Elle lui appartient. Il peut la laisser sur le plan ou la transférer vers le PER de son nouvel employeur ou vers un PER individuel."),
         ("Quelle différence avec l'épargne salariale ?", "L'épargne salariale se récupère au bout de cinq ans. La retraite collective est bloquée jusqu'à la retraite, sauf cas particuliers, avec un cadre fiscal différent. Les deux se complètent.")])

    return out
