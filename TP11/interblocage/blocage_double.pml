/*
SVL 16-17 - M. Nebut
Spin et les interblocages.
*/

byte ma_var = 1;

proctype proc() {
  if
    :: ma_var = 2;
    :: ma_var = 3;
  fi	 
}

proctype proc_debloque_par_2() {
  ma_var == 2;
}

proctype proc_debloque_par_3() {
  ma_var == 3;
}

init {
  run proc(); run proc_debloque_par_2(); run proc_debloque_par_3();
}

/*
spin -a blocage_double.pml
gcc -o verificateur pan.c
./verificateur // indique si état invalide
./verificateur -e -c0 // indique tous les états invalides et produit une trace par état
spin -t1 -p blocage_double.pml // exec premiere trace
spin -t2 -p blocage_double.pml // exec 2nde trace

*/