# Compte rendu TP8

## Exercice 1

### Q1.
Pour l'exemple 2 sur code contract, l'outil nous propose la suggestion suivante :
Contract.Requires((i > 0 || i != Int32.MinValue));

Cela est due aux bornes d'un entier en C#, celui ci allant de -2 147 483 648 à 2 147 483 647.
De ce fait, si la variable i est égale à la limite basse (-2 147 483 648), il dépassera la capacité de l'entier en cas de valeur absolu.


## Exercice 2
### Q2.3 + Q2.4
Le potentiel problème viendrait par la redéfinition d'une nouvelle valeur de découvert après que le sode ai été en découvert.
De ce fait, il faut spécifier que le découvert négatif ne doit pas être inférieur au solde : -maxDecouvert < solde

### Q2.5
L'outil n'accepte pas la comparaison int double avec des égalitées.

### Q2.6
L'outil n'est donc pas assez puissant pour générer cette différence de type