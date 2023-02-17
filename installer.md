# Installation et configuration de MkDocs

## Prérequis

- Python 3.9 (de préférence) ou 3.10.
- un terminal bash : terminal d'un système Linux ou git bash sous Windows


## Création et activation d'un environnement virtuel Python

Il faut mettre en place un virtualenv Python propre à Mkdocs.

### Sous Linux

```bash
python -m venv venv_mkdocs
source venv_mkdocs/bin/activate
```

### Sous Windows

Utiliser un terminal bash, type git-bash.

```bash
python -m venv venv_mkdocs
source venv_mkdocs/Scripts/activate
```

## Installer les modules Python requis 

MkDocs est un module python. Notre template de documentation fait également appel à des modules complémentaires.

Il y a 3 possibilité pour installer ces modules.

### utiliser les requirements

C'est la meilleure méthode car elle permet de s'assurer que l'on travaille tous sur les mêmes versions.

```bash
pip install -r requirements.txt
```

Pour vérifier :

`mkdocs --version` ==> `mkdocs, version 1.4.2`


### fresh install

Installation des dernières versions disponibles :

```bash
pip install mkdocs mkdocs-toc-md html5lib mkdocs-material mkdocs-git-revision-date-localized-plugin
```

### Utiliser les wheels

Si vous êtes dans un environnement réseau restreint / sans accès à internet et sous Windows (désolé…), utilisez les wheels disponibles : `python -m pip install --trusted-host pypi.org modules/3.9_windows/*.whl`.