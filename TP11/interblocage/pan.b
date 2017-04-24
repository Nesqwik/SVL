	switch (t->back) {
	default: Uerror("bad return move");
	case  0: goto R999; /* nothing to undo */

		 /* PROC :init: */

	case 3: // STATE 1
		;
		;
		delproc(0, now._nr_pr-1);
		;
		goto R999;

	case 4: // STATE 2
		;
		;
		delproc(0, now._nr_pr-1);
		;
		goto R999;

	case 5: // STATE 3
		;
		;
		delproc(0, now._nr_pr-1);
		;
		goto R999;

	case 6: // STATE 4
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC proc_debloque_par_3 */
;
		;
		
	case 8: // STATE 2
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC proc_debloque_par_2 */
;
		;
		
	case 10: // STATE 2
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC proc */

	case 11: // STATE 1
		;
		now.ma_var = trpt->bup.oval;
		;
		goto R999;

	case 12: // STATE 2
		;
		now.ma_var = trpt->bup.oval;
		;
		goto R999;

	case 13: // STATE 5
		;
		p_restor(II);
		;
		;
		goto R999;
	}

