# README : Exploit du formulaire Survey

## Description

Cette brèche met en évidence une vulnérabilité dans le processus de soumission d'un formulaire web. Elle permet à un attaquant potentiel de manipuler les options du formulaire pour obtenir une réponse spécifique.

## Fonctionnement

- Accédez à la page : `http://X.X.X.X/index.php?page=survey`
- Inspectez le code HTML de la page pour identifier une option du formulaire.
- Changez la valeur de cette option par une valeur non souhaitée.
- Soumettez le formulaire avec la nouvelle valeur.

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Obtenir une réponse spécifique au formulaire survey
- Potentiellement influencer les résultats du formulaire

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser toutes les entrées utilisateur côté serveur avant de les utiliser ou de les stocker.
- Utiliser JavaScript pour vérifier la validité des options du formulaire avant leur soumission.
- Implémenter une protection anti-CSRF pour éviter les requêtes malveillantes.
- Limiter les permissions du navigateur pour empêcher l'accès direct au DOM.
