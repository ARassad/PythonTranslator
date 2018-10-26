%{
	#include "tree_structs.h"
	#include <stdio.h>
	#include <malloc.h>
	
	void yyerror(char const *s);
	extern int yylex(void);
	
%}

%union {
	int int_value;
	float float_value;
	char* string_value;
	char* identifier;

	struct Program *prog;
	
	struct Expression *expr;
	struct Statement *stmt;
	struct StatementList *stmtList;
	struct ConditionStatement *condStmt;
	struct ElifStatement *elifStmt;
	struct WhileStatement *whileStmt;
	struct ForStatement *forStmt;
	struct ClassDefinition *classDef;
	struct FuncDefinition *funcDef;
	struct ImportStatement *impStmt;
	struct LambdaStatement *lmbdStmt;
	struct GeneratorStatement *genStmt;
	struct TryStatement *tryStmt;
}

%type <prog> program
%type <expr> expression
%type <stmt> statement
%type <stmtList> statement_list
%type <condStmt> condition_statement
%type <elifStmt> elif_statement
%type <whileStmt> while_statement
%type <forStmt> for_statement
%type <classDef> class_definition
%type <funcDef> function_definition
%type <impStmt> import_statement
%type <lmbdStmt> lambda_statement
%type <genStmt> generator_statement
%type <tryStmt> try_statement

%token <int_value> INT
%token <float_value> FLOAT
%token <string_value> STRING
%token <identifier> ID
%token FALSE
%token IF
%token IMPORT
%token FROM
%token IN
%token IS
%token AS
%token LAMBDA
%token NOT
%token OR
%token PASS
%token RAISE
%token RETURN
%token TRY
%token WHILE
%token FOR
%token WITH
%token NONE
%token TRUE
%token AND
%token ASSERT
%token BREAK
%token CLASS
%token CONTINUE
%token DEF
%token ELIF
%token ELSE
%token EXCEPT
%token FINALLY
%token YIELD

%token ARROW
%token NEWLINE

%token INDENT
%token DEDENT

%left OR
%left AND
%left NOT
%left IN NOT_IN
%left IS IS_NOT
%right '=' PLUS_ASSIGN MINUS_ASSIGN MULT_ASSIGN POW_ASSIGN DIV_ASSIGN MOD_ASSIGN
%left '<' LESSER_EQUAL '>' GREATER_EQUAL  NOT_EQUAL EQUAL
%left LEFT_SHIFT RIGHT_SHIFT
%left '+' '-'
%left '*' '/' '%' FLOOR_DIV
%left UMINUS
%left UPLUS
%right POW
%left '.'
%nonassoc ')'
%nonassoc ']'
%nonassoc '}'

%%

program : statement_list 
		;
		
expression  : expression OR expression
			| expression AND expression
			| NOT expression
			| expression IN expression
			| expression NOT IN expression %prec NOT_IN
			| expression IS expression
			| expression IS NOT expression %prec IS_NOT
			| expression PLUS_ASSIGN expression
			| expression MINUS_ASSIGN expression
			| expression MULT_ASSIGN expression
			| expression POW_ASSIGN expression
			| expression DIV_ASSIGN expression
			| expression MOD_ASSIGN expression
			| expression '<' expression
			| expression LESSER_EQUAL expression
			| expression '>' expression
			| expression GREATER_EQUAL expression
			| expression NOT_EQUAL expression
			| expression EQUAL expression
			| expression LEFT_SHIFT expression
			| expression RIGHT_SHIFT expression
			| expression '+' expression
			| expression '-' expression
			| expression '*' expression
			| expression '/' expression
			| expression '%' expression
			| expression FLOOR_DIV expression
			| '+' expression %prec UPLUS
			| '-' expression %prec UMINUS
			| expression POW expression
			| expression '.' expression
			| '(' expression ')'
			| ID
			| INT
			| FLOAT
			| STRING
			| ID 
			| '[' arguments ']'
			| expression '[' expression ']'
			| expression '[' array_slice ']'
			;

assign_expression	: assign_expression '=' assign_expression
					| expression
					;
						
arguments	: arg_value
			| arguments arg_value
			;
			
arg_value	: expression
			| expression ','
			|
			;

array_slice : arr_slic_dim ':' arr_slic_dim ':' arr_slic_dim
			| arr_slic_dim ':' arr_slic_dim
			;
			
arr_slic_dim: expression 
			| 
			;
			
statement	:	expression
			|	condition_statement
			;

statement_list  : statement NEWLINE
				| statement_list statement NEWLINE
				;

suite		: NEWLINE INDENT statement_list DEDENT
			;
				
function_definition : DEF ID '(' parameters ')' ':' suite
					: DEF ID '(' parameters ')' ARROW expression ':' suite
					;

parameters	: parameter
			| parameters parameter
			;
					
parameter	: ID 
			| ID ':' expression
			| parameter ','
			;

class_definition	: CLASS ID ':' suite
					| CLASS ID '(' class_parents ')' ':' suite
					;
					
class_parents		: class_parent
					| class_parents class_parent
					;

class_parent		: ID
					: class_parent ','
					;

condition_statement : IF expression ':' suite
					| IF expression ':' suite elif_statement_list
					| IF expression ':' suite elif_statement_list ELSE ':' suite 
					| IF expression ':' suite ELSE ':' suite

elif_statement 		: ELIF expression ':' suite
					;
					
elif_statement_list : elif_statement NEWLINE
					| elif_statement_list elif_statement NEWLINE 
					;

while_statement 	: WHILE expression ':' suite
					;

for_statement 		: FOR expression IN expression ':' suite
					;
					
try_statement 		: try_except 
					| try_finally
					;
					
try_except			: TRY ':' suite except_list_statement
					| TRY ':' suite except_list_statement ELSE ':' suite
					| TRY ':' suite except_list_statement FINALLY ':' suite
					| TRY ':' suite except_list_statement ELSE ':' suite FINALLY ':' suite
					;
					

except_statement		: EXCEPT ':' suite 
						| EXCEPT expression AS ID ':' suite
						
except_list_statement	: except_statement NEWLINE 
						| except_list_statement except_statement NEWLINE
						;
try_finally 			: TRY ':' suite FINALLY ':' suite

%%

void yyerror(char const *s)
{
	printf("%s",s);
}