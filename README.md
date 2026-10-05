# Outil de gestion des tâches

Ce document décrit comment installer et utiliser l'outil de gestion des tâches.

## Installation

Pour installer l'outil, suivez les étapes suivantes :

1. Clonez le dépôt GitHub :
   ```sh
   git clone https://github.com/votre_nom_d_utilisateur/outil-gestion-taches.git
   ```

2. Naviguez vers le répertoire du projet :
   ```sh
   cd outil-gestion-taches
   ```

3. Installez les dépendances nécessaires :
   ```sh
   pip install -r requirements.txt
   ```

## Utilisation

Pour exécuter l'outil, utilisez la commande suivante :

```sh
python main.py
```

Cela lancera l'interface de l'outil de gestion des tâches.

## Aide

Pour obtenir de l'aide sur les commandes disponibles, utilisez :

```sh
python main.py --help
```

## Exemple d'utilisation

Voici un exemple de comment ajouter une nouvelle tâche :

```sh
python main.py add "Faire les courses"
```

Pour afficher la liste des tâches :

```sh
python main.py list
```

Pour supprimer une tâche :

```sh
python main.py remove 1
```

## Contribuer

Si vous souhaitez contribuer à ce projet, veuillez suivre les instructions dans le fichier [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
