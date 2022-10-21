"# Rapport final" 
+ faire un état de l'art 
Nous sommes 4 joueurs d'échec de niveau débutant et nous essayons par ce projet d'avoir des clés permettant de battre nos adversaires. A la manière de Deep Blue ( superordinateur spécialisé dans le jeu d'échecs), nous récupérons des parties d'echecs dans le but de les analyser et d'établir le profil d'un joueur pour s'adapter en conséquence.
Dans une première partie nous analysons les bases de données d'un site d'échec en ligne, Lichess. Puis établirons des profils de joueur en fonction de leur type de jeu.  Nous adaptons ensuite un 'bot' qui nous donnera des indices/consignes pour savoir comment jouer en fonction de notre adversaire 
Première partie : Selection des datas et préparation : 
Afin d'avoir des données intéréssantes à analyser nous avons choisi les parties des "bons joueurs d'échec". C'est à dire des joueurs ayant un ELO élevé (système universel de classsement des joueurs) situé entre 2200 et 2800. L'interêt de ce choix et d'avoir des parties plus structurées (supprimer les parties qui ne suivent aucune statégie, le 'bruit de notre jeu de donnée). Les mouvements d bons joueurs suivent une certaine logique qui permet d'entrainer efficassement notre 'bot'. 
Exemple d'ojectif, à l'aide du nom d'un joueur au début de partie, savoir quel est son style de jeu. C'est à dire :
- Son ouverture principal décrite selon une arborescence de coup comportant une ligne principale
- Son style : agressif ou défensif 
Puis proposer une strétégie :
- Les meilleurs ouvertures contre son ouverture principale
- Et le stype de jeu à adopter (voir une strétégie qui fonctionne bien) 
- Ex: Contre ce joueur A qui joue une Queen Gambit (65% de ses parties avec les blancs), Faire une défence Caro-Khan (47% de victoire contre lui et 46% de victoire contre des joueur avec un profil similaire, en attaquant l'aile roi). 



Data selection and preparation

The scientific question is well formulated --> Avec l'aide d'une base de donnée de partie Lichess, établir le profil d'un joueur et adapter une statégie (ouverture + conseil en sortie d'overture) afin de battre le joueur adverse.  
The dataset has the potential to answer the question --> utilisation d'un dataset avec un header de méta donné précisant le type de partie, le joueur, la date, le contexte ... et la partie en elle même   
The data is large enough  --> Nous avons utilisé 20 000 partie (et 5 000 joueurs) pour les analyses de base et jusqu'à 400 000 parties pour entrainer notre 'bot'
The data imbalance is handled (if adequate) --> Dans le but d'équilibrer les données, nous avons supprimer les parties de très bas niveau et n'avons pas sélectionner les parties jouer par les ordinateurs entre elle même qui apporte une autre dimention, une autre strétégie complexe. Nous nous somme concentrés sur les parties de niveau élever et équilibré (2200 à 2800 ELO)
Non-assigned values are handled --> la base de données Lichess ne contiennent pas de NaN, nous rajoutons des features afin de créer le profil des joueurs.  
The data is well-described (descriptive statistics, distributions...)
Outliers are handled (if adequate) appropriately
Feature conversion make sense for the data/problem at hand
Visualisation of the data shows its key characteristics

Technical choices
The task is well-identified (classification, anomaly detection...)
The chosen algorithms are suited to the task
Hyperparameter setting is clear and justified
The implementation runs in a reasonable time (i.e. scales)
The hypotheses of the model are respected
Evaluation
The right evaluation metrics for this context are used (F1-score, RMSE...)
The proposed method(s) are compared to baselines
The reported scores are good compared to the baselines
The evaluation gives a good picture of the model’s performance
The train/validation/test separation principles are used
The results help answer the initial question
Limitations
The authors describe well the limits of their approach
The authors outline relevant perspectives
Report
The report fits within the ascribed limits (10 pages of content)
There is a paragraph detailing the contributions of each group member
The report is well-written and easy to follow
The formalism is rigorous and correct
Extras
The code is available and easy to run / well documented
The dataset was not pre-existing
Algorithm(s) were reimplemented from scratch
...and are more efficient than ”official” librairies
