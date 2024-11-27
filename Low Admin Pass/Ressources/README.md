# README : Déchiffrement de mot de passe MD5 via robots.txt

## Description

Cette brèche met en évidence une vulnabilité dans la gestion des informations sensibles sur un site web.

## Fonctionnement

- Accédez à la page robots.txt : `http://X.X.X.X/robots.txt`
- Observez le contenu qui interdit l'accès à certains fichiers :

```http
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

- Allez vers le chemin interdit : `http://X.X.X.X/whatever`
  On constate que la page contient des informations sensibles

```shell
root:437394baff5aa33daa618be47b75cb49
```

- Utilisez un site de déchiffrement MD5 comme https://md5decrypt.net/ pour décoder le mot de passe

```txt
Resultat: qwerty123@
```

- Connectez-vous à l'interface admin avec les informations obtenues: `http://X.X.X.X/admin`

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Accéder aux mots de passe administratifs du site
- Potentiellement obtenir des accès non autorisés à l'interface admin
- Déchiffrer d'autres mots de passe stockés sur le serveur

## Recommandations

Pour corriger cette vulnérabilité :

- Ne pas stocker les fichiers .htpasswd dans des dossiers accessibles publiquement
- Utiliser HTTPS pour sécuriser toutes les communications avec le serveur
- Implémenter une gestion robuste des mots de passe côté serveur
- Limiter l'accès aux fichiers de configuration et aux dossiers sensibles
- Utiliser des algorithmes de hachage plus sécurisés que MD5 pour les mots de passe
