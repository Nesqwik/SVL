# Compte rendu TP8

## Exercice 3

### Q1.

L'outil permet de valider 4 invariants:
* La taille de buffer est supérieur à 0
* La taille du buffer est égale à la taille configurée
* L'index pour le get est compris dans les bornes du buffer
* L'index pour le put est compris dans les bornes du buffer
* Le nombre d'éléments dans le buffer est compris entre 0 et la taille du buffer

### Q2.

L'outil Valide le programme OPEN JML. Open JML est moins performant ou en tout cas moins restrictif que CodeContract.

### Q3.

Notre code est conforme dans les deux cas. Toutefois pour pouvoir avoir un code conforme nous avons du changer légèrement les demandes par rapport aux spécifications et plus particulièrement comment savoir le nombre d'éléments dans le buffer.

### Q4.

La partie spec# a été écrite mais ne fonctionne pas
