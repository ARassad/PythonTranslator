#ifndef TREE_STRUCTS
#define TREE_STRUCTS

//----------Expression---------------------
enum ExpressionType 
{
	ET_UNDEFINED,
	ET_OR,
	ET_AND,
	ET_NOT,
	ET_IN,
	ET_NOT_IN,
	ET_IS,
	ET_IS_NOT,
	ET_PLUS_ASSIGN,
	ET_MINUS_ASSIGN,
	ET_MULT_ASSIGN,
	ET_POW_ASSIGN,
	ET_DIV_ASSIGN,
	ET_MOD_ASSIGN,
	ET_LESSER,
	ET_LESSER_EQUAL,
	ET_GREATER,
	ET_GREATER_EQUAL,
	ET_NOT_EQUAL, 
	ET_EQUAL,
	ET_LEFT_SHIFT,
	ET_RIGHT_SHIFT,
	ET_PLUS,
	ET_MINUS,
	ET_MULT,
	ET_DIV,
	ET_MOD,
	ET_FLOOR_DIV,
	ET_UPLUS,
	ET_UMINUS,
	ET_POW,
	ET_DOT,
	ET_PARENTHNESES,
	ET_ID,
	ET_INT,
	ET_FLOAT,
	ET_STRING,
	ET_SQUARE_BRACKETS,
	ET_ARRAY_APPEAL,
	ET_ARRAY_SLICE,
	ET_ARRAY_SLICE_ARGUMENTS,
	ET_ASSIGN,
	ET_ARRAY_GENERATOR,
	ET_FUNC_PARAM,
	ET_FUNC_PARAM_DEFAULT,
	ET_FUNC_CALL,
	ET_RETURN,
	ET_BOOL,
	ET_NONE,
	ET_ID_AS
};

struct Expression 
{
	enum ExpressionType type;
	
	int intVal;
	float floatVal;
	char* strVal;
	
	struct Expression* left;
	struct Expression* middle;
	struct Expression* right;
	
	struct Expression* identifier;
	
	struct List* exprs;
};

//--------------------List---------------------------
enum ListType
{
	LT_UNDEFINED,
	
	LT_ELEMENT,
	
	LT_EXPR_ARRAY_INITIAL_ARGUMENTS,
	LT_EXPR_FUNCTION_PARAMS,
	LT_EXPR_CLASS_PARENTS,
	
	LT_STATEMENT_LIST,
	LT_STMT_ELIF_LIST,
	LT_STMT_EXCEPT_LIST,
	LT_EXPR_ID_AS_LIST
};
	 
struct List
{
	enum ListType type;
	
	struct Expression* expr_value;
	struct Statement* stmt_value;
	
	struct List* next;
};

//------------------Statement-------------
enum StatementType 
{
	ST_UNDEFINED,
	ST_EXPRESSION,
	ST_CONDITION,
	ST_FUNCTION_DEF,
	ST_CLASS_DEF,
	ST_WHILE,
	ST_FOR,
	ST_TRY,
	ST_WITH,
	ST_ELIF_LISTS,
	ST_ELIF,
	ST_EXCEPT,
	ST_RETURN,
	ST_PASS,
	ST_RAISE,
	ST_BREAK,
	ST_CONTINUE,
	ST_YIELD,
	ST_ASSERT,
	ST_IMPORT,
	ST_FROM_IMPORT
};

struct Statement 
{
	enum StatementType type;
	
	struct Expression* expr;
	
	struct List* firstSuite;
	struct List* secondSuite;
	struct List* thirdSuite;
	
	struct List* stmtList;
	
	struct Expression* identifier;
};
#endif