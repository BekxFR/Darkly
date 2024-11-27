# README : Recover

## Description

Cette brèche met en évidence une vulnérabilité dans le processus de soumission d'un formulaire web. Elle permet à un attaquant potentiel d'inspecter et manipuler le contenu du champ caché contenant l'e-mail lors de la soumission du formulaire.

## Fonctionnement

- Accédez à la page : `http://x.x.x.x/?page=recover#`
- Inspectez le code HTML de la page pour identifier le champ caché contenant l'e-mail.
- Modifiez le contenu du champ caché pour remplacer l'e-mail légitime par votre propre adresse e-mail.
- Soumettez le formulaire avec la nouvelle valeur modifiée en utilisant la méthode POST.

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Recevoir les formulaires soumis par d'autres utilisateurs
- Envoyer des e-mails frauduleux depuis l'adresse de l'application
- Accéder aux informations sensibles transmises via le formulaire

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser toutes les entrées utilisateur côté serveur avant de les utiliser ou de les stocker.
- Utiliser JavaScript pour vérifier la validité des champs cachés avant leur soumission.
- Implémenter une protection anti-CSRF pour éviter les requêtes malveillantes.
- Limiter les permissions du navigateur pour empêcher l'accès direct au DOM.
