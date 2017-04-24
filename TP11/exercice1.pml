mtype {libre, occupe, inactif, enAttente, actif};

mtype etatA = inactif;
mtype etatB = inactif;
mtype lock = libre;

proctype procA() {
  do
    :: etatA = enAttente; atomic {lock == libre -> lock = occupe;} etatA = actif; etatA = inactif; lock = libre;
  od
}

proctype procB() {
  do
    :: etatB = enAttente; atomic {lock == libre -> lock = occupe;} etatB = actif; etatB = inactif; lock = libre;
  od
}

init {
  run procA();
  run procB();
}

ltl acces_exclusion_mutuelle { [] ! (etatA == actif && etatB == actif)}
ltl a_non_etatactif_infini { [] (etatA == actif -> <> (etatA != actif))}
ltl a_actif_implique_verrou_ferme { [] (etatA == actif -> lock == occupe)}
ltl a_en_attente_suivi_obligatoirement_etat_actif { [] (etatA == enAttente -> X etatA == actif)}
