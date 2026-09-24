# Introduction à python

## Installation du nécessaire

### Installation de python

Pour les cours, nous allons utiliser la version 3.12.10 qui est une version stable et permet l'utilisation de toutes les bibliothèques [^1] dont nous aurons besoin.

L'installation se fait différemment selon votre système d'exploitation. Rendez-vous directement à la rubrique qui correspond à votre système (Windows, Linux ou Mac).

#### Installer Python sous Windows

Sous Windows, nous utilisons **Pymanager** (le gestionnaire d'installation officiel de Python). On va d'abord vérifier que vous l'avez d'installé.

Dans le PowerShell, faites la commande suivante : `pymanager`

Si la commande n'est pas reconnue, alors référez-vous à la rubrique **Installer Pymanager**.
Sinon, passez directement à la rubrique **Installer Python 3.12.10 avec Pymanager**.

##### Installer Pymanager

- Allez sur le site officiel de python <https://www.python.org/downloads>
- Cliquez sur "Download Python install manager"
- Cliquez sur "Download Installer (MSIX)"
- Cochez "Lancer une fois prêt", puis lancez l'installation.
- Si le message suivant apparaît :
  "Your app execution alias settings are configured to launch other commands besides 'py' and 'python.'
  [...]
  Open Settings now, so you can modify App execution aliases? [y/N]"
  insérez `y`. Vous serez dirigés vers les paramètres avancés des applications.
  Cliquez sur "Alias d'exécution d'application".
  Une liste d'applications s'affiche.
  Pour toutes les applications python :
  - Si le nom de l'application contient Python Install Manager ou Python (Default), activez-le.
  - Désactivez toutes les autres applications python.
- Si le message suivant apparaît :
  "Windows is not configured to allow paths longer than 260 characters.
  [...]
  Update setting now? [y/N]"
  - insérez `y`.
  - Windows vous demande d'approuver les modifications : faites "Oui".
- Si le message suivant apparaît :
  "The global shortcuts directory is not configured
  [...]
  Add commands directory to your PATH now? [y/N]"
  - insérez `y`.
- Si le message suivant apparaît :
  "You do not have the latest Python runtime.
  [...]
  Install CPython now? [Y/n]"
  - insérez `n`.
- Il demande ensuite si vous voulez afficher l'aide en ligne. Vous pouvez insérer `n`.

Fermez puis rouvrez le PowerShell, et refaites `pymanager` pour vérifier que la commande est maintenant reconnue.

##### Installer Python 3.12.10 avec Pymanager

Dans le PowerShell, faites la commande suivante : `pymanager install 3.12.10`

Une fois l'installation terminée, vérifiez que tout s'est bien passé avec : `py -3.12 --version`
Vous devriez voir s'afficher `Python 3.12.10`.

Vous avez désormais la version 3.12.10 de python. Passez directement à la rubrique **Installation de Jupyter Lab**.

#### Installer Python sous Linux

Sous Linux, nous utilisons **pyenv**, un outil qui installe la version de Python que l'on veut dans votre dossier personnel, sans jamais toucher au Python du système. C'est plus simple et plus sûr qu'une installation manuelle.

- D'abord, installez les dépendances dont pyenv a besoin pour construire Python. Dans le shell :

  ```shell
  sudo apt update
  sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev \
    libffi-dev liblzma-dev curl git wget
  ```

  ça installe tous les outils nécessaires pour que python puisse se construire correctement.
- Installez pyenv avec la commande suivante :

  ```shell
  curl -fsSL https://pyenv.run | bash
  ```

- Il faut maintenant indiquer à votre terminal où trouver pyenv. Copiez-collez ces trois lignes, une par une, dans le shell :

  ```shell
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
  ```

- **Fermez complètement votre terminal et rouvrez-en un nouveau.** C'est indispensable pour que les lignes précédentes soient prises en compte.
- Vérifiez que pyenv répond bien : `pyenv --version`
- Installez Python 3.12.10 (ça compile Python, donc comptez quelques minutes, c'est normal) :

  ```shell
  pyenv install 3.12.10
  ```

- Définissez cette version comme version par défaut :

  ```shell
  pyenv global 3.12.10
  ```

- Vérifiez que tout est en place : `python --version`
  Vous devriez voir s'afficher `Python 3.12.10`.

Vous avez désormais la version 3.12.10 de python.

#### Installer Python sous Mac

Sous Mac, nous utilisons aussi **pyenv**, qui installe la version de Python voulue dans votre dossier personnel sans toucher au Python du système.

- Installez d'abord les outils de développement d'Apple, nécessaires pour construire Python :

  ```shell
  xcode-select --install
  ```

  Une fenêtre peut s'ouvrir pour confirmer l'installation. Acceptez et attendez la fin.
- Si vous n'avez pas encore **Homebrew** (le gestionnaire de paquets du Mac), installez-le en suivant les instructions de <https://brew.sh>.
- Installez pyenv et les bibliothèques nécessaires à la construction de Python :

  ```shell
  brew install pyenv openssl readline sqlite3 xz zlib tcl-tk
  ```

- Indiquez à votre terminal où trouver pyenv. Copiez-collez ces trois lignes, une par une, dans le shell :

  ```shell
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
  ```

- **Fermez complètement votre terminal et rouvrez-en un nouveau.** C'est indispensable pour que les lignes précédentes soient prises en compte.
- Vérifiez que pyenv répond bien : `pyenv --version`
- Installez Python 3.12.10 (ça compile Python, donc comptez quelques minutes, c'est normal) :

  ```shell
  pyenv install 3.12.10
  ```

- Définissez cette version comme version par défaut :

  ```shell
  pyenv global 3.12.10
  ```

- Vérifiez que tout est en place : `python --version`
  Vous devriez voir s'afficher `Python 3.12.10`.

Vous avez désormais la version 3.12.10 de python.

### Et si la version affichée n'est pas 3.12.10 ?

Pas de panique : si la commande de vérification affiche une autre version (par exemple 3.14), ça ne veut pas dire que l'installation a échoué. Ça veut dire qu'un autre Python déjà présent sur la machine est sélectionné à la place du nôtre. Les outils que nous utilisons sont faits pour que plusieurs versions cohabitent, il suffit de remettre la bonne au premier plan. Voici quoi faire selon votre système.

#### Corriger la version sous Windows

Une ancienne installation de Python (faite avec l'installeur classique de python.org) peut se disputer la commande `py` avec Pymanager.

- Vérifiez d'abord la version de notre Python avec la commande non ambiguë : `py -3.12 --version`. Si elle affiche bien `Python 3.12.10`, tout va bien : c'est juste le `py` tout seul qui est détourné, et ça n'empêche rien.
- Pour créer votre environnement virtuel, utilisez toujours la forme explicite `py -3.12 -m venv .venv` (et jamais `python -m venv`). Ça garantit que le venv est bien construit avec le 3.12.10, même si une autre version traîne sur la machine.
- Une fois le venv activé, vous êtes verrouillés sur le 3.12.10 : l'autre version n'a plus aucun effet à l'intérieur.

#### Corriger la version sous Linux

Si `python --version` affiche autre chose que 3.12.10, c'est presque toujours que l'initialisation de pyenv n'a pas été chargée.

- Vérifiez quel Python est utilisé : `which python`. Le chemin affiché doit contenir `.pyenv/shims`. S'il pointe ailleurs (vers `/usr/bin/python` par exemple), pyenv n'est pas passé au premier plan.
- Assurez-vous que les trois lignes d'initialisation sont bien dans votre `~/.bashrc` (au besoin, réexécutez les trois commandes `echo` de la rubrique d'installation).
- **Fermez complètement le terminal et rouvrez-en un neuf**, puis revérifiez avec `python --version`. C'est l'oubli le plus fréquent : les lignes ne sont prises en compte qu'au démarrage d'un nouveau terminal.

#### Corriger la version sous Mac

Même logique que sous Linux, avec une cause supplémentaire possible : un Python installé par Homebrew qui passe devant.

- Vérifiez quel Python est utilisé : `which python`. Le chemin doit contenir `.pyenv/shims`. S'il pointe vers `/opt/homebrew/bin` ou `/usr/bin`, c'est un autre Python qui passe devant.
- Vérifiez que les trois lignes d'initialisation sont bien dans votre `~/.zshrc`, puis fermez et rouvrez le terminal.
- Si le problème persiste et que `which python` montre `/opt/homebrew/bin`, c'est le Python de Homebrew qui prend le dessus. Les lignes d'initialisation de pyenv doivent être chargées après Homebrew : en cas de doute, vérifiez qu'elles figurent bien en bas de votre `~/.zshrc`.

### Installation de Jupyter Lab

Jupyter Lab sera notre interface principale pour apprendre le code et le tester. L'installation diffère un peu selon votre système, suivez la rubrique qui vous concerne.

#### Installer Jupyter Lab sous Linux et Mac

Comme pyenv a placé Python 3.12.10 en version par défaut, vous pouvez installer Jupyter Lab directement. Dans le terminal :

```shell
pip install jupyterlab
```

Attendez que l'installation se fasse, puis lancez : `jupyter lab`

> Si jamais `jupyter lab` n'est pas reconnu juste après l'installation, faites une fois `pyenv rehash` puis réessayez. pyenv a juste besoin de prendre en compte la nouvelle commande.

Votre navigateur internet devrait s'ouvrir et afficher une interface ressemblant à votre explorateur de fichier. Vous pouvez vous balader dans vos dossiers et fichiers, écrire de nouveaux fichiers, etc.

À chaque séance, il vous suffira d'ouvrir un terminal et de lancer `jupyter lab`. Rien d'autre à faire.

#### Installer Jupyter Lab sous Windows

Sous Windows, on installe Jupyter Lab dans un **environnement virtuel** [^2]. C'est une bulle isolée qui contient nos outils du cours, et qui rend la commande `jupyter lab` directement utilisable.

- Créez un dossier pour le cours là où vous voulez (par exemple `cours-python`), puis placez-vous dedans dans le PowerShell.
- Créez l'environnement virtuel avec Python 3.12.10 :

  ```powershell
  py -3.12 -m venv .venv
  ```

- **À faire une seule fois**, pour autoriser PowerShell à activer l'environnement. Sans ça, l'activation sera bloquée par un message du type "l'exécution de scripts est désactivée sur ce système". Faites :

  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```

  (Répondez `O` ou `Y` si une confirmation est demandée.)
- Activez l'environnement virtuel :

  ```powershell
  .venv\Scripts\Activate
  ```

  Vous devriez voir apparaître `(.venv)` au début de la ligne de commande : c'est le signe que l'environnement est bien activé.
- Installez Jupyter Lab :

  ```powershell
  pip install jupyterlab
  ```

- Attendez que l'installation se fasse, puis lancez : `py -m jupyterlab`

Votre navigateur internet devrait s'ouvrir et afficher une interface ressemblant à votre explorateur de fichier. Vous pouvez vous balader dans vos dossiers et fichiers, écrire de nouveaux fichiers, etc.

##### À chaque séance de code (Windows)

L'environnement virtuel se crée une seule fois, mais il faut l'**activer** à chaque nouvelle séance. Le déroulé est donc :

1. Ouvrez un PowerShell et placez-vous dans votre dossier `cours-python`.
2. Activez l'environnement : `.venv\Scripts\Activate`
3. Lancez Jupyter Lab : `jupyter lab`

C'est tout. Quand vous voyez `(.venv)` au début de la ligne, vous êtes prêts à travailler.

[^1]: Une bibliothèque est un code que l'on importe dans notre programme pour intégrer et utiliser des fonctionnalités sans avoir à la développer.

[^2]: Un environnement virtuel est un dossier isolé qui contient sa propre copie de Python et ses propres bibliothèques. Ça évite que les outils d'un projet n'entrent en conflit avec ceux d'un autre projet ou avec le système.