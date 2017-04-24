	switch (t->back) {
	default: Uerror("bad return move");
	case  0: goto R999; /* nothing to undo */

		 /* CLAIM a_en_attente_suivi_obligatoirement_etat_actif */
;
		
	case 3: // STATE 1
		goto R999;

	case 4: // STATE 10
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM a_actif_implique_verrou_ferme */
;
		
	case 5: // STATE 1
		goto R999;

	case 6: // STATE 10
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM a_non_etatactif_infini */
;
		;
		;
		;
		
	case 9: // STATE 13
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM acces_exclusion_mutuelle */
;
		
	case 10: // STATE 1
		goto R999;

	case 11: // STATE 10
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC :init: */

	case 12: // STATE 1
		;
		;
		delproc(0, now._nr_pr-1);
		;
		goto R999;

	case 13: // STATE 2
		;
		;
		delproc(0, now._nr_pr-1);
		;
		goto R999;

	case 14: // STATE 3
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC procB */

	case 15: // STATE 1
		;
		now.etatB = trpt->bup.oval;
		;
		goto R999;

	case 16: // STATE 3
		;
		now.lock = trpt->bup.oval;
		;
		goto R999;

	case 17: // STATE 5
		;
		now.etatB = trpt->bup.oval;
		;
		goto R999;

	case 18: // STATE 6
		;
		now.etatB = trpt->bup.oval;
		;
		goto R999;

	case 19: // STATE 7
		;
		now.lock = trpt->bup.oval;
		;
		goto R999;

	case 20: // STATE 11
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC procA */

	case 21: // STATE 1
		;
		now.etatA = trpt->bup.oval;
		;
		goto R999;

	case 22: // STATE 3
		;
		now.lock = trpt->bup.oval;
		;
		goto R999;

	case 23: // STATE 5
		;
		now.etatA = trpt->bup.oval;
		;
		goto R999;

	case 24: // STATE 6
		;
		now.etatA = trpt->bup.oval;
		;
		goto R999;

	case 25: // STATE 7
		;
		now.lock = trpt->bup.oval;
		;
		goto R999;

	case 26: // STATE 11
		;
		p_restor(II);
		;
		;
		goto R999;
	}

