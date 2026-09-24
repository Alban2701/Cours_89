# Règles Pep 8

Ce document résument l'ensemble des règles Pep 8 qui doivent être respectées par les étudiants. Elles seront notamment présentes dans le barème de notation

| Règles | Numérotation |
| --- | --- |
| Une assignation par ligne | pep89.1.1 |
| Lors d'un assignation, le symbole `=` doit être entouré d'espaces à gauche et à droite | pep89.1.2 |
| Lorsqu'une opération contient plusieurs opérateurs, les opérateurs qui ont une priorité moindre sont entourés d'espaces | pep89.1.3 |
| Lors d'une opération avec un seul opérateur, l'opérateur est entouré d'espaces | pep89.1.4 |
| Il ne doit pas y avoir d'espace juste après un caractère ouvrant (`(`, `{`, `[`) | pep89.1.5 |
| Il ne doit pas y avoir d'espace juste avant un caractère fermant (`)`, `}`, `]`) | pep89.1.6 |
| Prioriser l'utilisation de double quotes `"` pour ouvrir et fermer une string | pep89.1.7 |
| Prioriser l'utilisation de **f-string** plutôt que .format() pour formater une string | pep89.1.8 |
| Une ligne ne doit pas dépasser les 79 caractères | pep89.1.9 |
| Les identifiants et déclarations doivent uniquement être des caractères ASCII | pep89.1.10 |
| Les déclarations, définitions de fonctions et identifiants, ainsi que les commentaires et docstring doivent être en anglais | pep89.1.11 |
| Les variables et noms de fonctions doivent être en **snake_case** | pep89.1.12 |
| Niveau d'indentation marqué de 4 espaces | pep89.2.1 |
| Le deux points indiquant le début d'un bloc indenté doit être collé au caractère non-spatial le précédent | pep89.2.2 |
| Si une expression conditionnelle est précédée par une instruction, il faut les espacer d'un saut de ligne pour plus de lisibilité | pep89.2.3 |
| Un bloc conditionnel *b* imbriqué dans un bloc conditionnel *a* doit toujours être justifié par du code qui nécessite *a* et non *b* | pep89.2.4 |
| Le deux point indiquant le début d'une boucle doit être collé au caractère non-spatial le précédent | pep89.3.1 |
| Si une boucle est précédée par une instruction, il faut les espacer d'un saut de ligne plus plus de lisibilité | pep89.3.2 |
| Une boucle while *b* imbriquée dans une boucle while *a* doit toujours être justifiée par du code qui nécessite *a* et non *b* | pep89.3.3 |
| Les deux-points utilisés pour les slices doivent être entourés du même nombre d'espaces (0 ou 1) | pep89.3.4 |
| Les tuples doivent être déclarés dans des parenthèses | pep89.3.5 |
| Les utilisations de **break** et **continue** doivent être extrêmement réduites et justifiées | pep89.3.6 |
| Le deux points indiquant l'attribution d'une valeur à une clé lors d'une définition d'un dictionnaire doit être collé au caractère non-spatial le précédent | pep89.4.1 |
| Toutes fonctions doivent avoir une docstring (simple ou complète en fonction de la complexité de la fonction). | pep89.5.1 |
| Toutes définitions doit être typées | pep89.5.2 |
