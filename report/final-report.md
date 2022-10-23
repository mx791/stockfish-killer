"# Rapport final" (Salut les gars, tout ça n'est qu'une première vision du projet, rien n'est définitif et tout peut être remis en cause biensur, il faut faire 10 pages) 

+ faire un état de l'art 
+ En terme d'évaluation des parties d'échec, il existe plusieurs supers ordinateurs très connus (deep blue, stock fish) utilisant plusieurs méthodes d'apprentissage.
+ En 1997 le super ordinateur d'IBM, Deep Blue, battait le champion du monde d'échec Gary Kasparov pour la première fois (quatre parties à deux). Deep Blue utilisait un algorithme relativement classique, l'algorithme Minimax couplé avec une énorme base de données de 60 000 parties. --epi.asso.fr--
+ En 2017, AlphaZero a choqué le monde des échecs en écrasant Stockfish dans un match de 100 parties. Depuis, les moteurs d'échecs ont subi une révision substantielle basée sur des méthodes d'apprentissage profond pour développer un réseau neuronal -- chessbase.com --
+ La plus impressionnante avancée d'AlphaZero est qu'à la différence des générations précédentes de logiciels de jeux, il n'a pas été programmé ou entraîné à partir de données venant de parties jouées par des humains. L'algorithme s'est entraîné tout seul à partir des règles du jeu, en jouant des centaines de milliers de coups contre lui-même --developpez.com--
+ Actuellement, trois sites Web d'échecs se démarquent clairement chess24, chess.com et lichess.
Parmi les plateformes d'échecs en ligne. Tous vous offrent l'accès à un ensemble puissant d'outils de jeu et d'apprentissage et un service complet. -- ichess.net--. Elles permettent à la fois de faire des parties contre des joueurs mais aussi de s'entrainer. Pour les entrainements, plusieurs algorithmes existent afin de guider les joueurs dans les parties pédagogiques, tous se basent sur une grande base de partie afin de présenter les meilleurs coups aux joueurs. 
Voici quelques exemples : 5 PHOTO + COM 


 
Intro : 
  Nous sommes 4 joueurs d'échec de niveau débutant et nous essayons par ce projet d'avoir des clés permettant de battre nos adversaires. A la manière de Deep Blue ( superordinateur spécialisé dans le jeu d'échecs), nous récupérons des parties d'echecs dans le but de les analyser et d'établir le profil d'un joueur pour s'adapter en conséquence.
  
Dans une première partie nous analysons les bases de données d'un site d'échec en ligne, Lichess. Puis établirons des profils de joueur en fonction de leur type de jeu.  Nous adaptons ensuite un 'bot' qui nous donnera des indices/consignes pour savoir comment jouer en fonction de notre adversaire 

Afin d'avoir des données intéréssantes à analyser nous avons choisi les parties des "bons joueurs d'échec". Un bon joueur se caractérise par une connaissance de nombreuses stratégies, plans d'action, de tactiques et de la théorie des ouvertures. Il développe des qualités comme : 
L'attention et la concentration, Jugement et plan, L'imagination et la prévoyance, La mémoire , La volonté de vaincre, l'endurance et la maîtrise de soi, L'esprit de décision, La logique mathématique et l'esprit d'analyse et de synthèse.
De nombreuse compétition existent et un classement permet de 'ranger' les joueurs par niveau. Le ELO score est le système universel de classsement des joueurs. Dans notre étude des 'bons joueurs' nous avons choisi un ELO élevé situé entre 2200 et 2800. Voici la répartition des joueurs sur Lichess en fonction de ELO et voici ou, nous 4, nous nous situons 
(GRAPH NONTRANT LA REPARTITION DES JOUEURS x=nb de joueur, y=elo avec nos 4 points représantants nos niveau (800 Charles par exemple :), 1200, 1300 et 1500)
et notre intervalle selectionné [2200 2800]). L'interêt de choisir des parties de 'bons joueurs' est d'avoir des parties plus structurées (supprimer les parties qui ne suivent aucune statégie, le 'bruit' de notre jeu de donnée). Les mouvements des bons joueurs suivent logique qui permet d'entrainer efficassement notre 'bot'. 

Exemple d'ojectif, à l'aide du nom d'un joueur au début de partie, savoir quel est son style de jeu. C'est à dire :
- Son ouverture principale décrite selon une arborescence de coup comportant une ligne principale 
- Son style : agressif ou défensif 
Puis proposer une strétégie :
- Les meilleurs ouvertures contre son ouverture principale
- Et le stype de jeu à adopter (voir une strétégie qui fonctionne bien) 
- Ex: Contre ce joueur A, qui joue une Queen Gambit (65% de ses parties avec les blancs), Faire une défence Caro-Khan (47% de victoire contre lui et 46% de victoire contre des joueur avec un profil similaire, en attaquant l'aile roi en sortie d'ouverture). 


1 Explications de la base de donnée : 
[Event "Rated Blitz game"]   --> Type d'événement dans lequel c'est jouer la partie, ici 'rated Blitz game : partie de Blitz classée(d'une durée de 3 à 5 minutes par joueur)
#dans les bases de données le temps n'est pas précisé, mais il est possible en allant sur le lien ci dessous d'avoir la partie complète#
[LichessURL "https://lichess.org/kuUOsOML"] --> Lien vers la partie complète sur le site Lichess
[Date "2020.06.01"] --> Date de la partie
[Round "-"] --> Précision sur le le nombre de partie jouer entre ces deux joueurs consécutivement, ici c'est leur première partie donc pas de précision. 
[White "Cor64"] --> Nom du joueur avec les blancs 
[Black "matapalo"] --> Nom du joueur avec les noirs 
[Result "1/2-1/2"] --> Résultat de la partie, ici nul 
[WhiteElo "2413"] --> Précision de l'ELO du joueur blanc 
[BlackElo "2254"]--> Précision de l'ELO du joueur noir 
[ECO "C18"] --> Référence de l'ouverture
[Opening "French Defense: Winawer Variation, Poisoned Pawn Variation"] --> Type d'ouverture jouer par les blanc 
[TimeControl "180+2"] --> Temps de la partie 180s par joueur (soit 3 minutes) et +2 (secondes) indique le temps gagner à chaque coup jouer.
[UTCDate "2020.06.01"] --> Date UTC 
[UTCTime "00:00:00"] -->  Heure à laquelle c'est jouer la partie
[Termination "Normal"] --> Comment s'est terminer la partie, ici par répétition, cela peut être "Time forfeit" : défaite car le joueur n'a plus de temps
[WhiteRatingDiff "-2"] --> Ce que je joueur blanc a gagné ou a perdu sur son ELO score 
[BlackRatingDiff "+3"] --> Ce que je joueur noir a gagné ou a perdu sur son ELO score 

2 informations ne sont pas présentent dans cette partie 
[WhiteTitle "NM"] --> Précise le 'grad' du joueur NM : national master 
[BlackTitle "IM"] --> International master

1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 Ne7 5. a3 Bxc3+ 6. bxc3 c5 7. Qg4 Qc7 8.
Qxg7 Rg8 9. Qxh7 cxd4 10. Ne2 dxc3 11. f4 d4 12. h4 Nbc6 13. h5 Bd7 14. h6
O-O-O 15. Qd3 Rg6 16. h7 Rh8 17. Nxd4 Nxd4 18. Qxd4 Kb8 19. Rh3 Nf5 20. Qb4
Bc6 21. a4 Bxg2 22. Rxc3 Qb6 23. Qxb6 axb6 24. Ba3 Bxf1 25. O-O-O Bg2 26.
Bd6+ Ka7 27. Rc7 Rxh7 28. Rc8 Rhg7 29. Bb8+ Ka6 30. Bc7 Rg8 31. Rdd8 Rxd8
32. Rxd8 Ka7 33. Bb8+ Ka6 34. Bc7 Ka7 35. Bb8+ Ka8 36. Bc7+ Ka7 1/2-1/2  

--> Description de la partie : N : Night (cavalier), B : Bichop (fou), Q : Queen (reine), R Rock (tour), pas de précision : pion 
                               Prennons par exemple (5. a3 BXC3+) cela signifie : c'est le 5ième coup de la partie, le joueur blanc avance son pion sur la position a3, le joueur noir avance son fou sur la case C3, le X signifie une prise de pièce, (dans cette partie c'est le cavalier blanc qui est pris par le fou noir). le + signifie que le roi blanc est en échec. 
 *
                               











Réponses qu'on peut apporter à la fiche de notation

1- Data selection and preparation

The scientific question is well formulated --> Avec l'aide d'une base de donnée de parties Lichess, établir le profil d'un joueur et adapter une statégie (ouverture + conseil en sortie d'overture) afin de battre le joueur adverse.  

The dataset has the potential to answer the question --> utilisation d'un dataset avec un header de métas données précisant le type de partie, le joueur, la date, le contexte et la partie en elle même   

The data is large enough  --> Nous avons utilisé 20 000 partie (et 5 000 joueurs) pour les analyses de base et jusqu'à 400 000 parties pour entrainer notre 'bot'

The data imbalance is handled (if adequate) --> Dans le but d'équilibrer les données, nous avons supprimer les parties de très bas niveau. Nous nous somme concentrés sur les parties de niveau élever et équilibré (2200 à 2800 ELO)

Non-assigned values are handled --> la base de données Lichess ne contiennent pas de NaN, nous rajoutons des features afin de créer le profil des joueurs.  
The data is well-described (descriptive statistics, distributions...) 

Outliers are handled (if adequate) appropriately  --> Les valeurs abérantes peuvent être les parties où l'un des joueurs à un gros avantage et perd quand même, cela peut être du à une défaite au temps, un problème technique (connexion), ou ce qu'on appelle un 'miss clic' (un mouvement non voulu par l'un des joueurs. Cependant, le choix du niveau réduit connsidérablement les erreurs et permet d'avoir une base de donnée 'propre'

Feature conversion make sense for the data/problem at hand  --> Nous apportons pour le profil des joueurs des des caractéristiques spécifiques, qui sont pour les echecs, les ouvertures qui les définissent et leur style de jeu (agressif ou défensif). Un joueur peut avoir plusieurs ouvertures ou un style qui change. C'est pourquoi nous indiquons les taux de probabilité pour spécifier la diversité que peut avoir un profil. Les 'bons joueurs' sont ceux qui s'adaptent le mieux. 

Visualisation of the data shows its key characteristics --> plusieurs graphs à l'appui


2 - Technical choices


The task is well-identified (classification, anomaly detection...) --> 1 traitement de la base de donné et étude des anomalies, 2 indentification des joueurs et de leur style 3 faire un rapprochement avec les joueurs de même style, 4 entrainement d'un bot 5 conseils contre un joueur pour une partie 

The chosen algorithms are suited to the task  --> Présentation des algos + code review 

Hyperparameter setting is clear and justified --> Présentation des algos + code review 

The implementation runs in a reasonable time (i.e. scales) --> Choix d'une petite partie de la base de donnée pour rendre le code exécutable. 

The hypotheses of the model are respected --> a voir selon les premières sorties de code 


3 - Evaluation


The right evaluation metrics for this context are used (F1-score, RMSE...) --> Mettre en avant les scores de nos modèls 

The proposed method(s) are compared to baselines --> Analyse des sorties 

The reported scores are good compared to the baselines --> Analyse des sorties 

The evaluation gives a good picture of the model’s performance --> Analyse des sorties 


The train/validation/test separation principles are used --> Entraienement de notre bot 

The results help answer the initial question -->  Analyse des sorties 


4- Limitations


The authors describe well the limits of their approach --> Présenter les faibles taux de victoires de notre modèle comme une limite, la strétégie a adopter trop simplissime car au echec ce n'est pas une strétégie pour une partie mais plutot plusieurs strétégies par coup. 

The authors outline relevant perspectives --> Il serait possible d'établir un 'bot' comme sur chess.COM qui en temps réel explique chaque situation à chaque coup pour aborder la meilleurs trétégie tout au long de la partie. 


5 - Report


The report fits within the ascribed limits (10 pages of content) --> OK 

There is a paragraph detailing the contributions of each group member --> OK 

The report is well-written and easy to follow --> OK 





The formalism is rigorous and correct --> OK 


6 - Extras


The code is available and easy to run / well documented --> OK

The dataset was not pre-existing --> Pas ok, notre dataset existe déjà, mais on le complète. 

Algorithm(s) were reimplemented from scratch --> Plus ou moins 

...and are more efficient than ”official” librairies --> Pas OK 
