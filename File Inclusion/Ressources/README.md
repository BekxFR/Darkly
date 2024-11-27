# README : Exploit de chemin absolu dans l'URL

## Description

Cette brèche met en évidence une vulnérabilité dans la gestion des chemins absolus dans les paramètres de l'URL d'une application web. Elle permet à un attaquant potentiel d'accéder à des fichiers sensibles sur le serveur en exploitant cette faille.

## Fonctionnement

- Sur la page principale ou une page secondaire, modifiez le chemin dans le paramètre `page` pour pointer vers un fichier potentiel contenant un mot de passe utilisateur, par exemple : `http://X.X.X.X/index.php?page=../../../../../../var/www/../../../../../../../../../etc/passwd`
- Alternativement, utilisez une version plus simple pour accéder à /etc/passwd : `http://X.X.X.X/index.php?page=../../../../../../../../../etc/passwd`

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Accéder aux fichiers sensibles sur le serveur
- Potentiellement exposer des informations confidentielles
- Obtenir un aperçu de la structure du système de fichiers
- Potentiellement accéder à des mots de passe utilisateur

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser tous les paramètres d'URL côté serveur avant de les utiliser ou de les interpréter.
- Utiliser une validation robuste pour empêcher l'accès aux chemins absolus dans les paramètres.
- Implémenter une protection anti-XSS pour éviter l'exécution de code malveillant dans le navigateur.
- Limiter les permissions du serveur web pour restreindre l'accès aux dossiers sensibles.
- Crypter ou chiffrer les mots de passe utilisateur stockés sur le serveur.
