# Dragon Ball Versus

## Description
Ce projet est un jeu de cartes de combat en mode console développé en Python. Les joueurs contrôlent une équipe de guerriers et utilisent des cartes pour combattre leurs ennemis.

## Structure du Projet
- `attacks/` : Contient les classes liées aux attaques
- `entities/` : Contient les entités principales du jeu
  - `deck/` : Classes liées aux cartes et aux decks
  - `warrior/` : Classes liées aux guerriers
- `game/` : Contient les classes principales du jeu (menu, écran, etc.)
- `gauge/` : Gestion des jauges
- `managers/` : Contient les différents gestionnaires du jeu
- `objects/` : Classes liées aux objets utilisables dans le jeu
- `races/` : Définitions des différentes races de guerriers
- `states/` : Gestion des états des guerriers
- `transformations/` : Contient les classes lié aux transformations des guerriers
- `main.py` : Point d'entrée du jeu
- `requirements.txt` : Liste des dépendances du projet

## Design Patterns Utilisés

1. **Singleton** : 
   - Utilisé dans les managers (ex: `battle_manager.py`, `deck_manager.py`)
   - Assure une instance unique pour la gestion globale du jeu

2. **Builder** : 
   - Implémenté dans `entities/deck/deck_builder.py`
   - Permet une construction flexible et étape par étape des decks

3. **Decorator** : 
   - Utilisé dans `gauge/gauge.py`
   - Permet de modifier dynamiquement les statistiques des guerriers

4. **Factory** : 
   - Présent dans `attacks/attack_factory.py`, `objects/object_factory.py`, etc.
   - Facilite la création de différents types d'objets (attaques, objets, races)

5. **State** : 
   - Implémenté dans `states/warrior_state.py`
   - Gère les différents états des guerriers pendant le combat

6. **Observer** : 
   - Utilisé dans `managers/observer.py`
   - Implémente un système de notification pour les événements du jeu

## Installation

1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Clonez ce dépôt : 
```bash
git clone https://github.com/Kibishi47/Dragon-Ball-Versus.git
```
3. Naviguez vers le dossier du projet :
```bash
cd Dragon-Ball-Versus
```
4. Installez les dépendances :
 ```bash
pip install -r requirements.txt
```


## Comment Jouer

1. Lancez le jeu en exécutant :
 ```bash
python main.py
```

2. Menu Principal :
- Choisissez parmi les options disponibles (nouvelle partie, quitter, etc.)

3. Création de l'Équipe :
- Créez votre équipe de trois guerriers
- Choisissez le nom et la race de chaque guerrier

4. Construction du Deck :
- Sélectionnez les cartes pour votre deck
- Respectez la limite de cartes autorisées

5. Combat :
- À chaque tour, choisissez une carte à jouer
- Gérez l'énergie de vos guerriers
- Utilisez stratégiquement vos cartes d'attaque et d'objet
- Adaptez votre stratégie en fonction de l'état de vos guerriers et des ennemis

6. Fin de Partie :
- Le jeu se termine lorsque tous vos guerriers sont vaincus ou que vous avez vaincu tous les ennemis
- Vous pouvez choisir de rejouer ou de quitter le jeu

## Conseils de Jeu
- Équilibrez votre deck entre cartes d'attaque et cartes d'objet
- Faites attention à l'énergie de vos guerriers
- Utilisez les transformations et les états à votre avantage
- Adaptez votre stratégie en fonction des races et des capacités de vos ennemis
