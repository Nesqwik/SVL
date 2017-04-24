	switch (t->back) {
	default: Uerror("bad return move");
	case  0: goto R999; /* nothing to undo */

		 /* CLAIM un_prendra_la_ressource */
;
		;
		
	case 4: // STATE 6
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM si_occupe_la_ressource_alors_variable_prise */
;
		
	case 5: // STATE 1
		goto R999;

	case 6: // STATE 10
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM lache_la_ressource */
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

		 /* CLAIM exclusion_mutuelle */
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

		 /* PROC proc2 */

	case 15: // STATE 2
		;
		now.libre = trpt->bup.oval;
		;
		goto R999;

	case 16: // STATE 4
		;
		now.ressource2 = trpt->bup.oval;
		;
		goto R999;

	case 17: // STATE 5
		;
		now.ressource2 = trpt->bup.oval;
		;
		goto R999;

	case 18: // STATE 6
		;
		now.libre = trpt->bup.oval;
		;
		goto R999;

	case 19: // STATE 10
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC proc1 */

	case 20: // STATE 2
		;
		now.libre = trpt->bup.oval;
		;
		goto R999;

	case 21: // STATE 4
		;
		now.ressource1 = trpt->bup.oval;
		;
		goto R999;

	case 22: // STATE 5
		;
		now.ressource1 = trpt->bup.oval;
		;
		goto R999;

	case 23: // STATE 6
		;
		now.libre = trpt->bup.oval;
		;
		goto R999;

	case 24: // STATE 10
		;
		p_restor(II);
		;
		;
		goto R999;
	}

