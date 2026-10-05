# cookies-txt

Projet TI-LEX de laboratoire local.

Le dépôt contient actuellement :

- `index.html` : interface web locale
- `scan_ports.py` : diagnostic de ports sur `127.0.0.1`
- `main.py` : prototype en développement
- `attacks_analysis.py` : prototype en développement

> Utiliser uniquement sur ton propre ordinateur ou dans un laboratoire autorisé.

## Windows PowerShell

### Télécharger le projet

```powershell
cd $HOME
git clone https://github.com/alexmarceauprevost812-source/cookies-txt.git
cd cookies-txt
git checkout supabase
```

Si le dépôt est déjà téléchargé :

```powershell
cd "$HOME\cookies-txt"
git pull
```

### Ouvrir l'interface

```powershell
Start-Process .\index.html
```

### Lancer l'interface avec un serveur local

```powershell
python -m http.server 8000
```

Puis ouvre une deuxième fenêtre PowerShell :

```powershell
Start-Process http://127.0.0.1:8000/index.html
```

Pour arrêter le serveur :

```text
Ctrl+C
```

### Tester le diagnostic local Python

```powershell
python .\scan_ports.py
```

Le script utilise actuellement `127.0.0.1`, donc il reste sur ton propre ordinateur.

---

## Kali Linux / Ubuntu

### Télécharger le projet

```bash
sudo apt update
sudo apt install -y git python3
cd ~
git clone https://github.com/alexmarceauprevost812-source/cookies-txt.git
cd cookies-txt
git checkout supabase
```

Si le dépôt est déjà téléchargé :

```bash
cd ~/cookies-txt
git pull
```

### Ouvrir l'interface

```bash
xdg-open index.html
```

### Lancer un serveur web local

```bash
python3 -m http.server 8000
```

Puis ouvre :

```text
http://127.0.0.1:8000/index.html
```

### Tester le diagnostic local Python

```bash
python3 scan_ports.py
```

## Important

Il n'y a actuellement aucun fichier `requirements.txt`, donc il ne faut pas utiliser :

```text
pip install -r requirements.txt
```

Les commandes `add`, `list` et `remove` de l'ancien README ne font pas partie de ce projet.

`main.py` et `attacks_analysis.py` sont encore des prototypes et ne sont pas les commandes de lancement recommandées pour cette version.
