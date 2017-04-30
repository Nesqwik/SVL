# TP 11
### Guilbert Louis / Dalencourt Alex


### Section 2

Q1. fichier: exercice1.pml
Q2. fichier: exercice1.pml
  - Pour la vérification de l'interblocage lancer le vérificateur sans choisir de ltl à exécuter
    - Propriété vérifié
  - ltl acces_exclusion_mutuelle { [] ! (etatA == actif && etatB == actif)}
    - Propriété vérifié
  - ltl a_non_etatactif_infini { [] (etatA == actif -> <> (etatA != actif))}
    - Propriété vérifié
  - ltl a_actif_implique_verrou_ferme { [] (etatA == actif -> lock == occupe)}
    - Propriété vérifié
Q3. fichier: exercice1.pml
  - ltl a_en_attente_suivi_obligatoirement_etat_actif { [] (etatA == enAttente -> <> etatA == actif)}
    - La propriété est bien non vérifiée

### Section 3

### Section 4

Q2. Il existe un cas d'interblocage il est possible que le processus haut ne prenne jamais la main si les processus moyen et bas ne font que s'exécuter.

# Pour les sections 3 et 4 nous n'arrivons pas à avoir de cas d'interblocage avec la commande ./verificateur sur nos machine personnelles
# comme cela est expliqué dans la démo interblocage
