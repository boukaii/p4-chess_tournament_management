# Gestion de tournois d'échec
Projet 4 de la formation de développeur d'application python d'Openclassrooms.

Application permettant la gestion de tournois d'échecs( joueurs , rounds et matchs, scores) 



L'objectif de ce projet est de concevoir un logiciel de gestion de tournoi d'échecs avec plusieurs conditions spécifiques.


DÉROULEMENT DE BASE DU TOURNOI:


Un tournoi a un nombre de tours défini.
● Chaque tour est une liste de matchs.
● Chaque match consiste en une paire de joueurs.
● À la fin du match, les joueurs reçoivent des points selon leurs résultats.
● Le gagnant reçoit 1 point.
● Le perdant reçoit 0 point.
● Chaque joueur reçoit 0,5 point si le match se termine par un match nul.


SCHÉMA DES TOURNOIS:


Chaque tournoi doit contenir au moins les informations suivantes :
● nom ;
● lieu ;
● date de début et de fin ;
● nombre de tours – valeur par défaut sur 4 ;
● numéro correspondant au tour actuel ;
● une liste des tours ;
● une liste des joueurs enregistrés ;
● description pour les remarques générales du directeur du tournoi.


TOURS / MATCHS:


Un match unique est stocké sous la forme d'un tuple contenant deux listes, chacune
contenant deux éléments : un joueur et un score. Les matchs sont stockés sous
forme de liste dans l'instance du tour auquelle ils appartiennent.
En plus de la liste des matchs, l'instance du tour doit contenir un nom.
Un tour est appelé "Round 1", "Round 2", etc. Elle doit également
contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
tous deux être auto.


GÉNÉRATION DES PAIRES:


Au début du premier tour, on mélange les joueurs de façon aléatoire.
● Chaque tour est généré dynamiquement en fonction des résultats des joueurs dans
le tournoi en cours.
● Trie de tous les joueurs en fonction de leur nombre total de points dans le
tournoi.
● Association des joueurs dans l’ordre (le joueur 1 avec le joueur 2, le joueur 3
avec le joueur 4 et ainsi de suite.)
● Si plusieurs joueurs ont le même nombre de points, on les choisis
de façon aléatoire.
● Lors de la génération des paires, il faut éviter de créer des matchs identiques
(c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un contre l’autre).
■ Par exemple, si le joueur 1 a déjà joué contre le joueur 2,
il faut plutôt l'associer au joueur 3.
● Mettre à jour les points de tous les joueurs après chaque tour et répéter le
processus de triage et d’association jusqu'à ce que le tournoi soit terminé.

RAPPORTS:

● liste de tous les joueurs par ordre alphabétique ;
● liste de tous les tournois ;
● nom et dates d’un tournoi donnés ;
● liste des joueurs du tournoi par ordre alphabétique ;
● liste de tous les tours du tournoi et de tous les matchs du tour.


SAUVEGARDE / CHARGEMENT DES DONNÉES:


On doit pouvoir sauvegarder et charger l'état du programme à tout moment entre
deux actions de l'utilisateur.


Les fichiers JSON doivent être mis à jour à chaque fois qu'une modification est apportée
aux données afin d'éviter toute perte. Le programme doit s'assurer que les objets en
mémoire sont toujours synchronisés avec les fichiers JSON. Le programme doit également
charger toutes ses données à partir des fichiers JSON et pouvoir restaurer son état entre
les exécutions.

En réalisant ce projet,  j'ai appris à programmer en utilisant la Programmation Orientée Objet
et en utilisant également la conception MVC.






# Installation :

### **_Cloner le référentiel :_**
git clone `https://github.com/boukaii/p4-tournoi_echecs.git`

###  **_Déplacer vers le nouveau dossier :_**
`cd pythonProject1`

### **_Créez l'environnement virtuel :_**
`python -m venv env`

### _**Activez l'environnement virtuel :**_
Pour macOS et Linux: `env/bin/activate`

Pour Windows: `env\Scripts\activate`

### **_Installez les packages :_**
`pip install -r requirements.txt`

## **_Générer un rapport HTML Flake 8 :_**

### Installer le package :

`pip install flake8-html`

### Tapez ensuite cette ligne de commande et un rapport complet sera généré :

`flake8 --format=html --htmldir=flake8_report`
