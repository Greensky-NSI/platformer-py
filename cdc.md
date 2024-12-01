# Cahier des charges

Cahier des charges des attentes du projet

## Librairie et modules

Le projet doit être codé en [Python 3.10](https://www.python.org/downloads/release/python-3100/), avec la librairie [p5](https://pypi.org/project/p5/)

## Charges

| Fonctionnalité | Implémentation | État |
|:--:|:--:|:----:|
| [Niveau de plateformer](#niveau) | Implémentation par Classe |  ✅   |
| [Plateforme](#plateforme) | Implémentation par une classe |  ✅   |
| [Porte](#porte) | Implémentation par une classe |  ✅   |
| [Personnage](#personnage) | Implémentation par une classe |  ✅   |
| [Liste des cadeaux](#cadeaux) | Implémentation par une pile ou une file |  ✅   |
| [Monstre](#monstres) | Implémentation par une classe |  ✅   |
| [Organisation en modules](#organisation) | Différents dossiers et fichiers dans le projet |  🚧  |
| [Charte Graphique](./charte%20graphique.md) | Charte graphique du projet |  🚧  |

### Signification des signes

| Signe | Signification |
|:--:|:--:|
| ❌ | Non-implémenté |
| ✅ | Implémenté |
| 🚧 | En cours d'implémentation |
| 🚫 | Non-implémentable |
| ➖ | Fonctionnalité abandonnée |

## Liste détaillée des fonctionnalités

La liste détaillée des fonctionnalités à implémenter

> Le jeu doit avoir une taille de `800` par `600` pixels

### Niveau

Un niveau comporte une [porte d'entrée](#porte) en bas et une [porte de sortie](#porte) en haut.
> Le fond est noir, avec potentiellement des décorations telles que des étoiles ou des petites formes.
> ⚠️ Le fond ne **doit pas** être trop chargé.

Il doit y avoir plusieurs [plateformes](#plateforme) qui permettent au joueur de se déplacer verticalement et horizontalement.
> Le nombre de plateformes dans un niveau doit être compris entre **8** et **12**.

#### Porte

Une porte est un passage entre avant le niveau, qui permet l'apparition du joueur, ou après le niveau qui permet de marquer la fin du niveau et ainsi permettre la "sortie" du joueur.

> Design: La porte doit être noire, rectangulaire avec les coins supérieurs arrondis de façon à former un arc de cercle sur le dessus.

#### Plateforme

Une plateforme est un sol semi-solide, que le joueur peut traverser uniquement en passant par dessous. Si il passe par dessus, il reste bloqué dessus.
> Design: La plateforme doit être grise ou blanche, rectangulaire avec les coins arrondis. On pourra potentiellement ajouter des décorations sur les plateformes, mais elles ne doivent pas être trop chargées.

### Personnage

Le personnage est le joueur, il doit être capable de se déplacer horizontalement, de sauter et de ramasser des cadeaux.

> Design: Le personnage doit ressembler à un robot, simple à dessiner (avec des formes basiques). De préférence de couleur uniforme.

#### Contrôles

Les touches que le joueur peut utiliser pour déplacer le personnage

| Touche | Action |
| :--: | :--: |
| `A` | Aller à gauche |
| `D` | Aller à droite |
| `Espace` | Sauter |
| `W` | Sauter |
| `Q` | Aller à gauche |
| `Z` | Sauter |
| `Flèche droite` |  Aller à droite |
| `Flèche gauche` | Aller à gauche |
| `Flèche haut` | Sauter |

### Cadeaux

Les cadeaux sont des bonus que le joueur peut ramasser au cours d'un [niveau](#niveau) pour augmenter son score à la fin du niveau.
> Nombre de cadeaux par niveau: entre **3** et **6**.

En terme de design, les cadeaux doivent être plus ou moins carrés, de couleur un peu vive, avec un ruban autour de couleur plus sombre.

### Monstres

Un monstre est un ennemi du joueur. Il se trouvent sur les plateformes, et uniquement dessus. Ils bougent horizontalement le long de la plateforme, marquant une pause plus ou moins longue à un ou plusieurs endroits de son chemin.

> Design: Ils doivent apparaitre comme des blobs de couleur sombre, avec des yeux blancs. (Design suceptible de changements)

Le joueur perd le niveau et doit le recommencer si il touche un monstre.

Les monstres peuvent adapter leur comportement si le joueur est à proximité, mais ce n'est pas une obligation.

### Organisation

Le projet doit s'organiser en modules, avec un fichier principal qui lance le jeu, et des fichiers dans des dossiers pour chaque classe.

Organisation prévue au moment de la rédaction (suceptible de changer) :

```cs
.gitignore
README.md
LICENSE
src/
  main.py
  classes/
    objects/
      plaform.py
      gift.py
    mobs/
      player.py
      monster.py
    complexes/
      level.py
      door.py
  utils/
    toolbox.py
    constants.py
    globals.py
  types/
    typing.py
```
