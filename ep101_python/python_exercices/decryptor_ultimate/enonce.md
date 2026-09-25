# Decryptor Ultimate

**Ce projet est optionnel.** Il est nettement plus difficile que Decryptor, faites-le si vous avez fini le reste et que vous voulez vous challenger.

Un programme qui reçoit un message chiffré et tente de retrouver le message d'origine, sans connaître ni l'algorithme utilisé pour le chiffrer, ni la clé de déchiffrage.

## Objectif

Le programme reçoit uniquement un message chiffré (les mêmes algorithmes que dans "Encryptor" et "Decryptor" ont pu être utilisés pour le chiffrer : César, César progressif, Vigenère, Atbash).

À partir de ce seul message, le programme doit :

- essayer les algorithmes et les clés plausibles
- éliminer les résultats absurdes (un déchiffrage qui ne ressemble à rien de lisible)
- attribuer un pourcentage de confiance aux résultats restants (une estimation de la probabilité que ce soit le bon déchiffrement)

Le programme affiche ensuite toutes les possibilités jugées probables, triées par ordre décroissant de confiance (la plus probable en premier).

## Contraintes

- Le message chiffré ne doit contenir que des caractères ascii.
- Les algorithmes de chiffrement ne modifient par défaut que les caractères alphabétiques. La casse des caractères restent inchangés.
- Partez du principe que l'utilisateur n'est pas bête. Il n'y a pas besoin de valider les entrées utilisateur.
- Vous pouvez créer autant de fichiers que vous le souhaitez.
- Vous pouvez reprendre du code des projets Encryptor et Decryptor.
- Vous pouvez utiliser d'autres librairies, tant que les algorithmes de chiffrement eux-mêmes sont codés par vous.

## Pistes

- Pour César (et César progressif), le nombre de décalages possibles est limité : rien ne vous empêche de tous les essayer.
- Pour évaluer si un résultat est "lisible", vous pouvez vous baser sur la présence de mots courants (français ou anglais) dans le texte déchiffré, ou sur la fréquence des lettres (certaines lettres reviennent statistiquement plus souvent qu'une autre dans un texte).
- Le pourcentage de confiance peut être une mesure toute simple (ex : proportion de mots reconnus dans le résultat) : il n'est pas nécessaire de faire quelque chose de très sophistiqué.

## Bonus

Faites également fonctionner votre programme sur les messages chiffrés avec la variante ASCII (voir le bonus d'Encryptor).
