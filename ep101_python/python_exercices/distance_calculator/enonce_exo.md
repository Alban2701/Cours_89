# Calculateur de distance

## Objectif

Écrire des fonctions qui permet de faire des calculs sur des unités de distances.

exemple :

```python
>>> add("500m", "1.6km")
"2.1km"
>>> sub("2m", "10m")
"-8m"
>>> div("1km", 2)
"500m"
>>> mul("990m", 3)
"2.97km" 
```

Les unitées disponibles sont les suivantes : km ; m ; cm ; µm ("um")

## Subtilités

- Il faut choisir la plus grande unité de distance de sorte à ce que le chiffre des unité soit supérieur à 0 :
~~"0.5km"~~ -> "500m"

- Si l'unité la plus basse ne permet pas de valider cette règle, alors on accepte la valeur :
"0.7um" -> ok

## Astuces et conseils

Vous pouvez, et c'est fortement conseillé, écrire d'autres fonctions (une fonction = un job)
Donc dès que vous codez une fonctionnalité qui se répète, il se peut qu'elle puisse devenir une fonction

Pour les fonctions add et sub, vous pouvez leur faire accepter un nombre illimité d'arguments avec `*args`.
exemple d'utilisation :

```python
def display_things(*args):
    for arg in args:
        print(arg)
```

Il ne vous est pas demandé de vérifier les arguments : partez du principe que l'utilisateur n'est pas trop bête.

Bloquer la division par 0 pour `div` est un plus.

## En cas de blocage

Si vous avez des difficultés sur le code, n'hésitez pas à vous entre-aider, à regarder la doc sur internet, ou à me poser une question.
Mon bureau est en 201, et vous pouvez m'envoyer un mail ou m'envoyer un message sur teams sur l'un de ces deux emails : [alban.genta@edu.ecole-89.com](mailto:alban.genta@edu.ecole-89.com) | [alban.genta@htechvalley.io](mailto:alban.genta@htechvalley.io)

S'il vous plaît, n'utilisez pas de LLM, je souhaite savoir à quel point l'exo est difficile et si je peux vous expliquer les notions qu'il vous manque. Donc jouez le jeu !
