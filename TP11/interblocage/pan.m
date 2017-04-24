#define rand	pan_rand
#define pthread_equal(a,b)	((a)==(b))
#if defined(HAS_CODE) && defined(VERBOSE)
	#ifdef BFS_PAR
		bfs_printf("Pr: %d Tr: %d\n", II, t->forw);
	#else
		cpu_printf("Pr: %d Tr: %d\n", II, t->forw);
	#endif
#endif
	switch (t->forw) {
	default: Uerror("bad forward move");
	case 0:	/* if without executable clauses */
		continue;
	case 1: /* generic 'goto' or 'skip' */
		IfNotBlocked
		_m = 3; goto P999;
	case 2: /* generic 'else' */
		IfNotBlocked
		if (trpt->o_pm&1) continue;
		_m = 3; goto P999;

		 /* PROC :init: */
	case 3: // STATE 1 - blocage_double.pml:24 - [(run proc())] (0:0:0 - 1)
		IfNotBlocked
		reached[3][1] = 1;
		if (!(addproc(II, 1, 0)))
			continue;
		_m = 3; goto P999; /* 0 */
	case 4: // STATE 2 - blocage_double.pml:24 - [(run proc_debloque_par_2())] (0:0:0 - 1)
		IfNotBlocked
		reached[3][2] = 1;
		if (!(addproc(II, 1, 1)))
			continue;
		_m = 3; goto P999; /* 0 */
	case 5: // STATE 3 - blocage_double.pml:24 - [(run proc_debloque_par_3())] (0:0:0 - 1)
		IfNotBlocked
		reached[3][3] = 1;
		if (!(addproc(II, 1, 2)))
			continue;
		_m = 3; goto P999; /* 0 */
	case 6: // STATE 4 - blocage_double.pml:25 - [-end-] (0:0:0 - 1)
		IfNotBlocked
		reached[3][4] = 1;
		if (!delproc(1, II)) continue;
		_m = 3; goto P999; /* 0 */

		 /* PROC proc_debloque_par_3 */
	case 7: // STATE 1 - blocage_double.pml:20 - [((ma_var==3))] (0:0:0 - 1)
		IfNotBlocked
		reached[2][1] = 1;
		if (!((((int)now.ma_var)==3)))
			continue;
		_m = 3; goto P999; /* 0 */
	case 8: // STATE 2 - blocage_double.pml:21 - [-end-] (0:0:0 - 1)
		IfNotBlocked
		reached[2][2] = 1;
		if (!delproc(1, II)) continue;
		_m = 3; goto P999; /* 0 */

		 /* PROC proc_debloque_par_2 */
	case 9: // STATE 1 - blocage_double.pml:16 - [((ma_var==2))] (0:0:0 - 1)
		IfNotBlocked
		reached[1][1] = 1;
		if (!((((int)now.ma_var)==2)))
			continue;
		_m = 3; goto P999; /* 0 */
	case 10: // STATE 2 - blocage_double.pml:17 - [-end-] (0:0:0 - 1)
		IfNotBlocked
		reached[1][2] = 1;
		if (!delproc(1, II)) continue;
		_m = 3; goto P999; /* 0 */

		 /* PROC proc */
	case 11: // STATE 1 - blocage_double.pml:10 - [ma_var = 2] (0:0:1 - 1)
		IfNotBlocked
		reached[0][1] = 1;
		(trpt+1)->bup.oval = ((int)now.ma_var);
		now.ma_var = 2;
#ifdef VAR_RANGES
		logval("ma_var", ((int)now.ma_var));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 12: // STATE 2 - blocage_double.pml:11 - [ma_var = 3] (0:0:1 - 1)
		IfNotBlocked
		reached[0][2] = 1;
		(trpt+1)->bup.oval = ((int)now.ma_var);
		now.ma_var = 3;
#ifdef VAR_RANGES
		logval("ma_var", ((int)now.ma_var));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 13: // STATE 5 - blocage_double.pml:13 - [-end-] (0:0:0 - 3)
		IfNotBlocked
		reached[0][5] = 1;
		if (!delproc(1, II)) continue;
		_m = 3; goto P999; /* 0 */
	case  _T5:	/* np_ */
		if (!((!(trpt->o_pm&4) && !(trpt->tau&128))))
			continue;
		/* else fall through */
	case  _T2:	/* true */
		_m = 3; goto P999;
#undef rand
	}

