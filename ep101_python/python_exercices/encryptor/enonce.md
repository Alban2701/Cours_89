# Encryptor

Un programme qui permet de sélectionner un algorithme de chiffrement et de chiffre un message.

## Objectif

Le programme va demander à l'utilisateur de choisir un algorithme de chiffrage parmi ceux de la liste suivante : 

- César
- César progressif
- Chiffrement de Vigenère
- Atbash

Si nécessaire, le programme demande ensuite la clé de chiffrement pour le chiffrement de Vigenère, ou le nombre de pas pour le César ou César progressif.

Le programme affiche ensuite le message chiffré.

## Détails des algorithmes

- **César** : l'utilisateur choisit un pas de décalage, qui peut être positif ou négatif.
- **César progressif** : l'utilisateur choisit un nombre de départ (le décalage appliqué à la première lettre chiffrée) ainsi qu'un pas (positif ou négatif). Ce pas s'ajoute au décalage à chaque lettre suivante (ex : nombre de départ = 1, pas = 2 → la 1ère lettre est décalée de 1, la 2e de 3, la 3e de 5, etc.).
- **Chiffrement de Vigenère** : si la clé est plus courte que le message, elle se répète de manière cyclique. Un caractère non-alphabétique du message consomme tout de même un caractère de la clé (la clé avance à chaque caractère du message, qu'il soit alphabétique ou non).
- **Atbash** : aucune précision supplémentaire n'est nécessaire.

## Contraintes

- Le message ne doit contenir que des caractères ascii.
- Les algorithmes de chiffrement ne modifient par défaut que les caractères alphabétiques. La casse des caractères restent inchangés.
- Partez du principe que l'utilisateur n'est pas bête : vous n'avez pas besoin de valider les entrées utilisateur.
- Vous pouvez créer autant de fichiers et de fonction que vous voulez
- Votre code doit respecter les règles pep89
- Vous pouvez utiliser d'autres librairies, tant que les algorithmes de chiffrement eux-mêmes sont codés par vous

## Bonus

Au lieu de vous baser uniquement sur l'alphabet, vous pouvez vous baser sur la grille des caractères ascii **imprimables** (de l'espace à `~`, soit les valeurs 32 à 126). Le rang du caractère est donc sa valeur ascii au sein de cette plage, et les décalages se font par rapport à cette valeur.
