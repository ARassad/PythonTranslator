%{
	#include "tree_struct.h"
	#include <stdio.h>
	#include <malloc.h>
	
	void yyerror(char const *s);
	extern int yylex(void);
	struct Expression* createExpression(enum ExpressionType type, struct Expression* left, struct Expression* middle, struct Expression* right, struct List* exprs, int intVal, float floatVal, char* strVal, struct Expression* id);
	struct Expression* createBaseTypeExpression(enum ExpressionType type, int intVal, float floatVal, char* strVal);
	struct Expression* createBinaryExpression(enum ExpressionType type, struct Expression* left, struct Expression* right);
	
	struct List* createList(enum ExpressionListType type, struct Expression* expr, struct Statement* stmt);
	struct List* appendToList(struct List* list, struct Expression* expr, struct Statement* stmt);
	
	struct Statement* createStatement(enum StatementType type, struct Expression* expr, struct List* firstSuite, struct List* secondSuite, struct List* thirdSuite, struct List* stmtList, struct Expression* identifier);
	struct Statement* createFuncDefStatement(struct Expression* identifier, struct List* params, struct Expression* returnType, struct List* suite);
	struct Statement* createClassDefStatement(struct Expression* identifier, struct List* parents, struct List* suite);
	struct Statement* createConditionStatement(struct Expression* condition, struct List* ifSuite, struct List* elifs, struct List* elseSuite);
	struct Statement* createWhileStatement(struct Expression* condition, struct List* mainSuite, struct List* elseSuite);
	struct Statement* createForStatement(struct Expression* identifier, struct Expression* condition, struct List* mainSuite, struct List* elseSuite);
	struct Statement* createTryStatement(struct List* mainSuite, struct List* elseSuite, struct List* finallySuite, struct List* excepts);
	
	struct List* head;
%}

%union {
	int int_value;
	float float_value;
	char* string_value;
	
	struct Expression* expr;
	struct Statement* stmt;
	struct List* list;
}

%type <expr> expression
%type <expr> identifier
%type <expr> arg_value
%type <expr> array_slice
%type <expr> arr_slic_dim
%type <expr> parameter
%type <expr> class_parent

%type <stmt> statement
%type <stmt> function_definition
%type <stmt> class_definition
%type <stmt> condition_statement
%type <stmt> elif_statement
%type <stmt> while_statement
%type <stmt> for_statement
%type <stmt> try_statement
%type <stmt> except_statement

%type <list> program
%type <list> arguments
%type <list> statement_list
%type <list> suite
%type <list> parameters
%type <list> class_parents
%type <list> elif_statement_list
%type <list> except_list_statement

%token <int_value> INT
%token <float_value> FLOAT
%token <string_value> STRING
%token <string_value> ID

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
%left IN
%left NOT_IN
%left IS
%left IS_NOT
%right '=' PLUS_ASSIGN MINUS_ASSIGN MULT_ASSIGN POW_ASSIGN DIV_ASSIGN MOD_ASSIGN
%left '<' LESSER_EQUAL '>' GREATER_EQUAL NOT_EQUAL EQUAL
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

program : statement_list 				{ $$ = head = $1; }
		;
		
expression  : expression OR expression									{ $$ = createBinaryExpression(ET_OR, $1, $3); }
			| expression AND expression									{ $$ = createBinaryExpression(ET_AND, $1, $3); }
			| NOT expression											{ $$ = createBinaryExpression(ET_NOT, NULL, $2); }
			| expression IN expression									{ $$ = createBinaryExpression(ET_IN, $1, $3); }
			| expression NOT_IN expression								{ $$ = createBinaryExpression(ET_NOT_IN, $1, $3); }
			| expression IS expression									{ $$ = createBinaryExpression(ET_IS, $1, $3); }
			| expression IS_NOT expression								{ $$ = createBinaryExpression(ET_IS_NOT, $1, $3); }
			| expression PLUS_ASSIGN expression							{ $$ = createBinaryExpression(ET_PLUS_ASSIGN, $1, $3); }
			| expression MINUS_ASSIGN expression						{ $$ = createBinaryExpression(ET_MINUS_ASSIGN, $1, $3); }
			| expression MULT_ASSIGN expression							{ $$ = createBinaryExpression(ET_MULT_ASSIGN, $1, $3); }
			| expression POW_ASSIGN expression							{ $$ = createBinaryExpression(ET_POW_ASSIGN, $1, $3); }
			| expression DIV_ASSIGN expression							{ $$ = createBinaryExpression(ET_DIV_ASSIGN, $1, $3); }
			| expression MOD_ASSIGN expression							{ $$ = createBinaryExpression(ET_MOD_ASSIGN, $1, $3); }
			| expression '<' expression									{ $$ = createBinaryExpression(ET_LESSER, $1, $3); }
			| expression LESSER_EQUAL expression						{ $$ = createBinaryExpression(ET_LESSER_EQUAL, $1, $3); }
			| expression '>' expression									{ $$ = createBinaryExpression(ET_GREATER, $1, $3); }
			| expression GREATER_EQUAL expression						{ $$ = createBinaryExpression(ET_GREATER_EQUAL, $1, $3); }
			| expression NOT_EQUAL expression							{ $$ = createBinaryExpression(ET_NOT_EQUAL, $1, $3); }
			| expression EQUAL expression								{ $$ = createBinaryExpression(ET_EQUAL, $1, $3); }
			| expression LEFT_SHIFT expression							{ $$ = createBinaryExpression(ET_LEFT_SHIFT, $1, $3); }
			| expression RIGHT_SHIFT expression							{ $$ = createBinaryExpression(ET_RIGHT_SHIFT, $1, $3); }
			| expression '+' expression									{ $$ = createBinaryExpression(ET_PLUS, $1, $3); }
			| expression '-' expression									{ $$ = createBinaryExpression(ET_MINUS, $1, $3); }
			| expression '*' expression									{ $$ = createBinaryExpression(ET_MULT, $1, $3); }
			| expression '/' expression									{ $$ = createBinaryExpression(ET_DIV, $1, $3); }
			| expression '%' expression									{ $$ = createBinaryExpression(ET_MOD, $1, $3); }
			| expression FLOOR_DIV expression							{ $$ = createBinaryExpression(ET_FLOOR_DIV, $1, $3); }
			| '+' expression %prec UPLUS								{ $$ = createBinaryExpression(ET_UPLUS, $2, NULL); }
			| '-' expression %prec UMINUS								{ $$ = createBinaryExpression(ET_UMINUS, $2, NULL); }
			| expression POW expression									{ $$ = createBinaryExpression(ET_POW, $1, $3); }
			| expression '.' expression									{ $$ = createBinaryExpression(ET_DOT, $1, $3); }
			| '(' expression ')'										{ $$ = $2; }
			| identifier												{ $$ = $1; }
			| INT														{ $$ = createBaseTypeExpression(ET_INT, $1, 0.0, NULL); }
			| FLOAT														{ $$ = createBaseTypeExpression(ET_FLOAT, 0, $1, NULL); }
			| STRING													{ $$ = createBaseTypeExpression(ET_STRING, 0, 0.0, $1); }
			| '[' arguments ']'											{ $$ = createExpression(ET_SQUARE_BRACKETS, NULL, NULL, NULL, $2, 0, 0.0, NULL, NULL); }
			| expression '[' expression ']'								{ $$ = createBinaryExpression(ET_ARRAY_APPEAL, $1, $3); }
			| expression '[' array_slice ']'							{ $$ = createBinaryExpression(ET_ARRAY_SLICE, $1, $3); }
			| expression '=' expression									{ $$ = createBinaryExpression(ET_ASSIGN, $1, $3); }
			| '[' expression FOR identifier IN expression ']'			{ $$ = createExpression(ET_ARRAY_GENERATOR, $2, $6, NULL, NULL, 0, 0.0, NULL, $4); }
			| '[' expression FOR identifier IN expression IF expression ']'		{ $$ = createExpression(ET_ARRAY_GENERATOR, $2, $6, $8, NULL, 0, 0.0, NULL, $4); }
			;

identifier  : ID														{ $$ = createBaseTypeExpression(ET_ID, 	0, 0.0, $1); }
			;
			
arguments	: arg_value													{ $$ = createList(LT_EXPR_ARRAY_INITIAL_ARGUMENTS, $1, NULL); }
			| arguments arg_value										{ $$ = appendToList($1, $2, NULL); }
			;

arg_value	: expression												{ $$ = $1; }
			| expression ','											{ $$ = $1; }
			|															{ $$ = NULL; }
			;

array_slice : arr_slic_dim ':' arr_slic_dim ':' arr_slic_dim			{ $$ = createExpression(ET_ARRAY_SLICE_ARGUMENTS, $1, $3, $5, NULL, 0, 0.0, NULL, NULL); }
			| arr_slic_dim ':' arr_slic_dim								{ $$ = createExpression(ET_ARRAY_SLICE_ARGUMENTS, $1, $3, NULL, NULL, 0, 0.0, NULL, NULL); }		
			;
			
arr_slic_dim: expression 												{ $$ = $1; }
			| 															{ $$ = NULL; }
			;
			
statement	: expression												{ $$ = createStatement(ST_EXPRESSION, $1, NULL, NULL, NULL, NULL, NULL); }
			| condition_statement										{ $$ = $1 }
			| function_definition										{ $$ = $1 }
			| class_definition											{ $$ = $1 }
			| while_statement											{ $$ = $1 }
			| for_statement												{ $$ = $1 }
			| try_statement												{ $$ = $1 }
			;

statement_list  : statement NEWLINE										{ $$ = createList(LT_STATEMENT_LIST, NULL, $1); }
				| statement_list statement NEWLINE						{ $$ = appendToList($1, NULL, $2); }
				;

suite		: NEWLINE INDENT statement_list DEDENT						{ $$ = $3 }
			;
				
function_definition : DEF identifier '(' parameters ')' ':' suite					{ $$ = createFuncDefStatement($2, $4, NULL, $7); }
					| DEF identifier '(' parameters ')' ARROW expression ':' suite	{ $$ = createFuncDefStatement($2, $4, $7, $9); }
					;

parameters	: parameter													{ $$ = createList(LT_EXPR_FUNCTION_PARAMS, $1, NULL); }
			| parameters parameter										{ $$ = appendToList($1, $2, NULL); }
			;
					
parameter	: identifier 												{ $$ = $1; }
			| identifier ':' expression									{ $$ = createExpression(ET_FUNC_PARAM, $3, NULL, NULL, NULL, 0, 0.0, NULL, $1); }
			| parameter ',' 											{ $$ = $1; }
			;

class_definition	: CLASS identifier ':' suite						{ $$ = createClassDefStatement($2, NULL, $4)}
					| CLASS identifier '(' class_parents ')' ':' suite	{ $$ = createClassDefStatement($2, $4, $7)}
					;
					
class_parents		: class_parent										{ $$ = createList(LT_EXPR_CLASS_PARENTS, $1, NULL); }			
					| class_parents class_parent						{ $$ = appendToList($1, $2, NULL); }
					;

class_parent		: identifier										{ $$ = $1; }
					| class_parent ','									{ $$ = $1; }
					;

condition_statement : IF expression ':' suite										{ $$ = createConditionStatement($2, $4, NULL, NULL); }
					| IF expression ':' suite elif_statement_list					{ $$ = createConditionStatement($2, $4, $5, NULL); }
					| IF expression ':' suite elif_statement_list ELSE ':' suite 	{ $$ = createConditionStatement($2, $4, $5, $8); }
					| IF expression ':' suite ELSE ':' suite					 	{ $$ = createConditionStatement($2, $4, NULL, $7); }
					;

elif_statement_list : elif_statement NEWLINE										{ $$ = createList(LT_STMT_ELIF_LIST, NULL, $1); }
					| elif_statement_list elif_statement NEWLINE					{ $$ = appendToList($1, NULL, $2); }
					;
			
elif_statement 		: ELIF expression ':' suite										{ $$ = createStatement(ST_ELIF, $2, $4, NULL, NULL, NULL, NULL); }
					;
					
while_statement 	: WHILE expression ':' suite									{ $$ = createWhileStatement($2, $4, NULL); }
					| WHILE expression ':' suite ELSE suite							{ $$ = createWhileStatement($2, $4, $6); }
					;

for_statement 		: FOR identifier IN expression ':' suite						{ $$ = createForStatement($2, $4, $6, NULL); }
					| FOR identifier IN expression ':' suite ELSE suite				{ $$ = createForStatement($2, $4, $6, $8); }
					;
					
try_statement		: TRY ':' suite FINALLY ':' suite											{ $$ = createTryStatement($3, NULL, $6, NULL); }
					| TRY ':' suite except_list_statement										{ $$ = createTryStatement($3, NULL, NULL, $4); }
					| TRY ':' suite except_list_statement ELSE ':' suite						{ $$ = createTryStatement($3, $7, NULL, $4); }
					| TRY ':' suite except_list_statement FINALLY ':' suite						{ $$ = createTryStatement($3, NULL, $7, $4); }
					| TRY ':' suite except_list_statement ELSE ':' suite FINALLY ':' suite		{ $$ = createTryStatement($3, $7, $10, $4); }
					;

except_list_statement	: except_statement NEWLINE 								{ $$ = createList(LT_STMT_EXCEPT_LIST, NULL, $1); }
						| except_list_statement except_statement NEWLINE		{ $$ = appendToList($1, NULL, $2); }
						;
					
except_statement	: EXCEPT ':' suite 											{ $$ = createStatement(ST_EXCEPT, NULL, $3, NULL, NULL, NULL, NULL); }
					| EXCEPT expression AS identifier ':' suite					{ $$ = createStatement(ST_EXCEPT, $2, $6, NULL, NULL, NULL, $4); }
					;
%%

void yyerror(char const *s)
{
	printf("%s",s);
}

struct Expression* createBaseTypeExpression(enum ExpressionType type, int intVal, float floatVal, char* strVal)
{
	return createExpression(type, NULL, NULL, NULL, NULL, intVal, floatVal, strVal, NULL);
}

struct Expression* createBinaryExpression(enum ExpressionType type,struct Expression *left, struct Expression *right)
{
	return createExpression(type, left, NULL, right, NULL, 0, 0.0, NULL, NULL);
}

struct Expression* createExpression(enum ExpressionType type, struct Expression* left, struct Expression* middle, struct Expression* right, struct List* exprs, int intVal, float floatVal, char* strVal, struct Expression* id)
{
	struct Expression* result = (struct Expression*)malloc(sizeof(struct Expression));
	result->type = type;
	result->left = left;
	result->middle = middle;
	result->right = right;
	result->exprs = exprs;
	result->intVal = intVal;
	result->floatVal = floatVal;
	result->strVal = strVal;
	result->identifier = id;
	return result;
}

struct List* createList(enum ExpressionListType type, struct Expression* expr, struct Statement* stmt)
{ 
	struct List* result = (struct List*)malloc(sizeof(struct List));
	result->type = type;
	result->expr_value = expr;
	result->stmt_value = stmt;
	result->next = NULL;
	
	return result;
}

struct List* appendToList(struct List* list, struct Expression* expr, struct Statement* stmt)
{
	struct List* cur = list;
	while(cur->next != NULL)
		cur = cur->next;
	cur->next = createList(LT_ELEMENT, expr, stmt);
	
	return list;
}

struct Statement* createStatement(enum StatementType type, struct Expression* expr, struct List* firstSuite, struct List* secondSuite, struct List* thirdSuite, struct List* stmtList, struct Expression* identifier)
{
	struct Statement* result = (struct Statement*)malloc(sizeof(struct Statement));
	result->type = type;
	result->expr = expr;
	result->firstSuite = firstSuite;
	result->secondSuite = secondSuite;
	result->thirdSuite = thirdSuite;
	result->stmtList = stmtList;
	result->identifier = identifier;
	
	return result;
}

struct Statement* createFuncDefStatement(struct Expression* identifier, struct List* params, struct Expression* returnType, struct List* suite)
{
	return createStatement(ST_FUNCTION_DEF, returnType, suite, NULL, NULL, params, identifier);
}

struct Statement* createClassDefStatement(struct Expression* identifier, struct List* parents, struct List* suite)
{
	return createStatement(ST_CLASS_DEF, NULL, suite, NULL, NULL, parents, identifier);
}

struct Statement* createConditionStatement(struct Expression* condition, struct List* ifSuite, struct List* elifs, struct List* elseSuite)
{
	return createStatement(ST_CONDITION, condition, ifSuite, elseSuite, NULL, elifs, NULL);
}

struct Statement* createWhileStatement(struct Expression* condition, struct List* mainSuite, struct List* elseSuite)
{
	return createStatement(ST_WHILE, condition, mainSuite, elseSuite, NULL, NULL, NULL);
}

struct Statement* createForStatement(struct Expression* identifier, struct Expression* inExpr, struct List* mainSuite, struct List* elseSuite)
{
	return createStatement(ST_FOR, inExpr, mainSuite, elseSuite, NULL, NULL, identifier);
}

struct Statement* createTryStatement(struct List* mainSuite, struct List* elseSuite, struct List* finallySuite, struct List* excepts)
{
	return createStatement(ST_TRY, NULL, mainSuite, elseSuite, finallySuite, excepts, NULL);
}
