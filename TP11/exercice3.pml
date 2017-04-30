mtype {libre, occupe, inactif, enAttente, actif};

mtype etatHaut = inactif;
mtype etatMoyen = inactif;
mtype etatBas = inactif;
mtype lock = libre;

proctype procHaut() {
  do
    :: etatHaut = enAttente; atomic {lock == libre -> lock = occupe;} etatHaut = actif; etatHaut = inactif; lock = libre;
  od
}

proctype procMoyen() {
  do
    :: etatMoyen = enAttente; atomic {etatHaut == inactif -> lock = occupe;} etatMoyen = actif; etatMoyen = inactif; lock = libre;
  od
}

proctype procBas() {
  do
    :: etatBas = enAttente; atomic {etatMoyen == inactif -> lock = occupe;} etatBas = actif; etatBas = inactif; lock = libre;
  od
}

init {
  run procHaut();
  run procMoyen();
  run procBas();
}


ltl Haut_attente_forcement_actif_apres { [] (etatHaut == enAttente && X (etatHaut == actif))}
ltl acces_exclusion_mutuelle { [] ! (etatHaut == actif && etatMoyen == actif || etatHaut == actif && etatBas == actif || etatMoyen == actif && etatBas == actif)}
ltl a_non_etatHautctif_infini { [] (etatHaut == actif -> <> (etatHaut != actif))}
ltl a_actif_implique_verrou_ferme { [] (etatHaut == actif -> lock == occupe)}
ltl a_en_attente_suivi_obligatoirement_etat_actif { [] (etatHaut == enAttente -> <> etatHaut == actif)}
