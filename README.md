# Content Managment System

## Übersicht

[Setup](#Setup)

[Documentation](#Documentation)

## Setup

### Checke Dependencies
Wir benutzen Wagtail als CMS Tool welches Python 3.6, 3.7, 3.8, 3.9 und 3.10 unterstützt
Schaue zunächst ob du eine passende Python Version installiert hast

`python3 --version`


### Klone die Github Repo
`git clone https://github.com/hrw-fablab/cms`

### Erstelle und Aktiviere eine Virtuelle Python Umgebung

#### Unter Windows
```
cd cms
python3 -m venv env
env\Scripts\activate.bat
```

### Installiere die Dependencies
```
pip install -r requirements.txt
```


### Erstelle die Database
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
