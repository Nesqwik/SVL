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
    :: etatBas = enAttente; atomic {lock == libre && etatMoyen == inactif -> lock = occupe;} etatBas = actif; etatBas = inactif; lock = libre;
  od
}

init {
  run procHaut();
  run procMoyen();
  run procBas();
}
