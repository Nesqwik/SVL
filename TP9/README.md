# TP9

**Pensez-vous que l'utilisation d'Hypothesis assure une couverture de 100% ?**

Non car Hypothesis génère de façon aléatoire des valeurs de tests. Il est donc possible que certains cas prévu par le programme ne soient pas généré par l'outil.

**Est-il possible qu'un test utilisant hypothesis passe certaines fois et d'autres non ?**

Oui car si le programme est buggé, il se peut que Hypothesis ne génère pas le cas de test problématique.
