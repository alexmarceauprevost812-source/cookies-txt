# cookies-txt

Interface locale TI-LEX de laboratoire.

> Le fichier `main.py` actuel contient du HTML, pas du Python. Il ne faut donc pas utiliser `python main.py`, `npm install` ou `pip install -r requirements.txt`.

## Windows

### 1. Installer Git si nécessaire

```powershell
winget install -e --id Git.Git
```

Ferme puis rouvre PowerShell après l'installation de Git.

### 2. Télécharger le projet

```powershell
cd $HOME
git clone https://github.com/alexmarceauprevost812-source/cookies-txt.git
cd cookies-txt
```

### 3. Préparer la page HTML

```powershell
Copy-Item .\main.py .\index.html
```

### 4. Ouvrir l'outil

```powershell
Start-Process .\index.html
```

### Option : lancer avec un petit serveur local

```powershell
python -m http.server 8000
```

Puis, dans un autre PowerShell :

```powershell
Start-Process http://127.0.0.1:8000/index.html
```

### Mise à jour du projet

```powershell
cd "$HOME\cookies-txt"
git pull
Copy-Item .\main.py .\index.html -Force
Start-Process .\index.html
```

---

## Kali Linux / Ubuntu

### 1. Installer Git et Python

```bash
sudo apt update
sudo apt install -y git python3
```

### 2. Télécharger le projet

```bash
cd ~
git clone https://github.com/alexmarceauprevost812-source/cookies-txt.git
cd cookies-txt
```

### 3. Préparer la page HTML

```bash
cp main.py index.html
```

### 4. Ouvrir l'outil

```bash
xdg-open index.html
```

### Option : lancer avec un serveur local

```bash
python3 -m http.server 8000
```

Puis ouvre dans le navigateur :

```text
http://127.0.0.1:8000/index.html
```

### Mise à jour du projet

```bash
cd ~/cookies-txt
git pull
cp main.py index.html
xdg-open index.html
```

## Utilisation

Ce projet doit rester utilisé uniquement dans un laboratoire local et autorisé. L'interface actuelle est une démonstration locale et ne contient pas de moteur d'attaque fonctionnel.
