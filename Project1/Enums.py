from enum import Enum


class ListType(Enum):
    LT_UNDEFINED = 0
    LT_ELEMENT = 1
    LT_EXPR_ARRAY_INITIAL_ARGUMENTS = 2
    LT_EXPR_FUNCTION_PARAMS = 3
    LT_EXPR_IDENTIFIERS_E = 4
    LT_STATEMENT_LIST = 5
    LT_STMT_ELIF_LIST = 6
    LT_STMT_EXCEPT_LIST = 7
    LT_EXPR_ID_AS_LIST = 8
    LT_EXPR_WITH = 9


class StmtType(Enum):
    ST_UNDEFINED = 0
    ST_EXPRESSION = 1
    ST_CONDITION = 2
    ST_FUNCTION_DEF = 3
    ST_CLASS_DEF = 4
    ST_WHILE = 5
    ST_FOR = 6
    ST_TRY = 7
    ST_WITH = 8
    ST_ELIF_LISTS = 9
    ST_ELIF = 10
    ST_EXCEPT = 11
    ST_RETURN = 12
    ST_PASS = 13
    ST_RAISE = 14
    ST_BREAK = 15
    ST_CONTINUE = 16
    ST_YIELD = 17
    ST_ASSERT = 18
    ST_IMPORT = 19
    ST_FROM_IMPORT = 20


class ExprType(Enum):
    ET_UNDEFINED = 0
    ET_OR = 1
    ET_AND = 2
    ET_NOT = 3
    ET_IN = 4
    ET_NOT_IN = 5
    ET_IS = 6
    ET_IS_NOT = 7
    ET_PLUS_ASSIGN = 8
    ET_MINUS_ASSIGN = 9
    ET_MULT_ASSIGN = 10
    ET_POW_ASSIGN = 11
    ET_DIV_ASSIGN = 12
    ET_MOD_ASSIGN = 13
    ET_LESSER = 14
    ET_LESSER_EQUAL = 15
    ET_GREATER = 16
    ET_GREATER_EQUAL = 17
    ET_NOT_EQUAL = 18
    ET_EQUAL = 19
    ET_LEFT_SHIFT = 20
    ET_RIGHT_SHIFT = 21
    ET_PLUS = 22
    ET_MINUS = 23
    ET_MULT = 24
    ET_DIV = 25
    ET_MOD = 26
    ET_FLOOR_DIV = 27
    ET_UPLUS = 28
    ET_UMINUS = 29
    ET_POW = 30
    ET_DOT = 31
    ET_PARENTHNESES = 32
    ET_ID = 33
    ET_INT = 34
    ET_FLOAT = 35
    ET_STRING = 36
    ET_SQUARE_BRACKETS = 37
    ET_ARRAY_APPEAL = 38
    ET_ARRAY_SLICE = 39
    ET_ARRAY_SLICE_ARGUMENTS = 40
    ET_ASSIGN = 41
    ET_ARRAY_GENERATOR = 42
    ET_FUNC_PARAM = 43
    ET_FUNC_PARAM_DEFAULT = 44
    ET_FUNC_CALL = 45
    ET_RETURN = 46
    ET_BOOL = 47
    ET_NONE = 48
    ET_ID_AS = 49
    ET_LAMBDA = 50
    ET_EXPR_AS = 51
