/*
SVL 16-17 - M. Nebut
démo Spin - occupation d'une ressource en exclusion mutuelle
*/

#define un_a_la_ressource (ressource1)
#define deux_a_la_ressource (ressource2)

bool libre = true;
bool ressource1 = false;
bool ressource2 = false;

proctype proc1() {
	 
do
   :: atomic {libre -> libre = false;} ressource1 = true;  ressource1 = false; libre = true;
od	 
}

proctype proc2() {
	 
do
   :: atomic {libre -> libre = false;} ressource2 = true; ressource2 = false; libre = true;
od	 
}

init {
run proc1(); run proc2();
}

ltl exclusion_mutuelle { [] ! (un_a_la_ressource && deux_a_la_ressource)}
ltl lache_la_ressource { [] (un_a_la_ressource -> <> ! un_a_la_ressource)}
ltl si_occupe_la_ressource_alors_variable_prise { [] (un_a_la_ressource -> ! libre)}
ltl un_prendra_la_ressource { <> un_a_la_ressource } /* faux */

/*
spin -a exmut.pml
gcc -o verificateur pan.c
./verificateur -a -N exclusion_mutuelle
spin -t -p exmut.pml
*/