## TP 10

### Exo 1

_*Invariants*_

invariant i * i <= x
invariant i >= 0

_*Preuve*_
Notre fonctionnement de boucle repose sur l'incrément d'une variable unique jusqu'à atteindre une valeur souhaité.
Il est donc nécessaire d'avoir deux invariant afin de réaliser les bornes de fin de boucle lorsque la variable aura atteint de résultat souhaité.
On sais que le résultat d'une racine carré est au minimum 0 d'où le fait que i doit au moins être égal à 0.
Pour le deuxième invariant qui donne la limite de fin de boucle cela repose sur la formule de la racine carré.
La formule de la racine carré étant a = racine(a * a):
d'où l'invariant suivant i * i = x.
Comme nous recherchons une approximation à l'entier le plus proche sans dépasser la valeur souhaité on obtient: i * i <= x

### Exo 2

_*Invariants*_
invariant i <= tab.Length;
invariant cpt == sum{int n in (0:i); (tab[n] == 5 ? 1 : 0)};

_*Preuve*_
Le fonctionnement de notre boucle repose sur le parcours d'un tableau commençant à la position 0 et compte chaque occurence du nombre 5. Ainsi deux invariants doivent être présent : le test de fin de boucle et le test de bon résultat à tout moment du parcours de table.
Le premier invariant doit être de la forme i < table.length or pour la condition de fin de boucle cette condition doit être dépacé à + 1 soit donc l'invariant suivant :
i <= table.length
Pour le cas du deuxième invariant il doit vériier que le nombre de 5 rencontré est bien le nombre de ses occurence entre 0 et l'index du tableau courrant. Pour cela il faut utiliser une somme avec comme valeur à sommer 0 ou 1 en fonction de la valeur rencontrée dans le tableau d'où:
cpt == sum{int n in (0:i); (tab[n] == 5 ? 1 : 0)}

### Exo 3

_*Invariants*_


_*Preuve*_
