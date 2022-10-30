# Utlisation du script chessbot_avec_clic :

Le joueur humain joue les blancs, l'algo joue les noirs.

Pour jouer un coup, cliquer sur la pièce qu'on veut bouger, puis sur la case d'arrivée :
- Si le clic n'est pas fait sur l'échiquier, il ne se passe rien.
- Si le coup choisi n'est pas légal, il faut recommencer la sélection du coup
- Si on clique sur une pièce par erreur, il suffit de recliquer de telle sorte à faire un coup illégal, puis on peut jouer notre coup voulu.

Le "niveau" de l'algo est modifiable avec le paramètre 'depth'. Actuellement, 4 semble une valeur raisonnable (5 devient un peu lent sur des positions complexes).

Le temps de calcul de l'algo n'est pas encore adapté à la complexité de la position. Il joue très vite dans des positions simples, mais peut prendre quelques secondes sur des positions complexes, notamment avec depth >= 4 

La promotion se fait automatiquement en dame pour l'instant.
