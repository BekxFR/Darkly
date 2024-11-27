# README : Modification redirect

## Description

Cette brèche met en évidence une vulnérabilité dans le processus de redirection d'un site web. Elle permet à un attaquant potentiel de modifier l'URL de destination d'un lien hypertexte, potentiellement menant les utilisateurs vers un site malveillant.

## Fonctionnement

- Accédez à la page racine : `http://X.X.X.X/index.php`
- Inspectez le code HTML de la page pour identifier un élément d'hypertexte (comme une icône Facebook).
- Modifiez l'attribut `href` du lien pour pointer vers une URL malveillante, par exemple : index.php?page=redirect&site=http://fakesite.com
- Cliquez sur le lien modifié.

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Rediriger les utilisateurs légitimes vers des sites malveillants
- Potentiellement exécuter des attaques phising ou distribuer du malware

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser toutes les entrées utilisateur côté serveur avant de les utiliser ou de les stocker.
- Utiliser JavaScript pour vérifier la validité et la sécurité des URLs avant leur insertion dans le DOM.
- Implémenter une protection anti-XSS pour éviter l'exécution de code malveillant dans le navigateur.
- Limiter les permissions du navigateur pour empêcher l'accès direct au DOM.
