mtype {libre, occupe, inactif, enAttente, actif};

mtype etatHaut = inactif;
mtype etatBas = inactif;
mtype lock = libre;

proctype procHaut() {
  do
    :: etatHaut = enAttente; atomic {lock == libre -> lock = occupe;} etatHaut = actif; etatHaut = inactif; lock = libre;
  od
}

proctype procBas() {
  do
    :: etatBas = enAttente; atomic {lock == libre && etatHaut == inactif -> lock = occupe;} etatBas = actif; etatBas = inactif; lock = libre;
  od
}

init {
  run procHaut();
  run procBas();
}

ltl acces_exclusion_mutuelle { [] ! (etatHaut == actif && etatBas == actif)}
ltl a_non_etatHautctif_infini { [] (etatHaut == actif -> <> (etatHaut != actif))}
ltl a_actif_implique_verrou_ferme { [] (etatHaut == actif -> lock == occupe)}
ltl a_en_attente_suivi_obligatoirement_etat_actif { [] (etatHaut == enAttente -> <> etatHaut == actif)}
