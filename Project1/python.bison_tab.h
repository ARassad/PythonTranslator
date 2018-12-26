typedef union {
	int int_value;
	float float_value;
	char* string_value;
	
	struct Expression* expr;
	struct Statement* stmt;
	struct List* list;
} YYSTYPE;
#define	INT	258
#define	FLOAT	259
#define	STRING	260
#define	ID	261
#define	FALSE	262
#define	IF	263
#define	IMPORT	264
#define	FROM	265
#define	IN	266
#define	IS	267
#define	AS	268
#define	LAMBDA	269
#define	NOT	270
#define	OR	271
#define	PASS	272
#define	RAISE	273
#define	RETURN	274
#define	TRY	275
#define	WHILE	276
#define	FOR	277
#define	WITH	278
#define	NONE	279
#define	TRUE	280
#define	AND	281
#define	ASSERT	282
#define	BREAK	283
#define	CLASS	284
#define	CONTINUE	285
#define	DEF	286
#define	ELIF	287
#define	ELSE	288
#define	EXCEPT	289
#define	FINALLY	290
#define	YIELD	291
#define	ARROW	292
#define	NEWLINE	293
#define	INDENT	294
#define	DEDENT	295
#define	END_OF_FILE	296
#define	PLUS_ASSIGN	297
#define	MINUS_ASSIGN	298
#define	MULT_ASSIGN	299
#define	POW_ASSIGN	300
#define	DIV_ASSIGN	301
#define	MOD_ASSIGN	302
#define	NOT_IN	303
#define	IS_NOT	304
#define	LESSER_EQUAL	305
#define	GREATER_EQUAL	306
#define	NOT_EQUAL	307
#define	EQUAL	308
#define	LEFT_SHIFT	309
#define	RIGHT_SHIFT	310
#define	FLOOR_DIV	311
#define	UMINUS	312
#define	UPLUS	313
#define	POW	314


extern YYSTYPE yylval;
