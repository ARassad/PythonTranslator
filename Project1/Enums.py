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
    ST_UNDEFINED = 100
    ST_EXPRESSION = 101
    ST_CONDITION = 102
    ST_FUNCTION_DEF = 103
    ST_CLASS_DEF = 104
    ST_WHILE = 105
    ST_FOR = 106
    ST_TRY = 107
    ST_WITH = 108
    ST_ELIF_LISTS = 109
    ST_ELIF = 110
    ST_EXCEPT = 111
    ST_RETURN = 112
    ST_PASS = 113
    ST_RAISE = 114
    ST_BREAK = 115
    ST_CONTINUE = 116
    ST_YIELD = 117
    ST_ASSERT = 118
    ST_IMPORT = 119
    ST_FROM_IMPORT = 120


class ExprType(Enum):
    ET_UNDEFINED = 200
    ET_OR = 201
    ET_AND = 202
    ET_NOT = 203
    ET_IN = 204
    ET_NOT_IN = 205
    ET_IS = 206
    ET_IS_NOT = 207
    ET_PLUS_ASSIGN = 208
    ET_MINUS_ASSIGN = 209
    ET_MULT_ASSIGN = 210
    ET_POW_ASSIGN = 211
    ET_DIV_ASSIGN = 212
    ET_MOD_ASSIGN = 213
    ET_LESSER = 214
    ET_LESSER_EQUAL = 215
    ET_GREATER = 216
    ET_GREATER_EQUAL = 217
    ET_NOT_EQUAL = 218
    ET_EQUAL = 219
    ET_LEFT_SHIFT = 220
    ET_RIGHT_SHIFT = 221
    ET_PLUS = 222
    ET_MINUS = 223
    ET_MULT = 224
    ET_DIV = 225
    ET_MOD = 226
    ET_FLOOR_DIV = 227
    ET_UPLUS = 228
    ET_UMINUS = 229
    ET_POW = 230
    ET_DOT = 231
    ET_PARENTHNESES = 232
    ET_ID = 233
    ET_INT = 234
    ET_FLOAT = 235
    ET_STRING = 236
    ET_SQUARE_BRACKETS = 237
    ET_ARRAY_APPEAL = 238
    ET_ARRAY_SLICE = 239
    ET_ARRAY_SLICE_ARGUMENTS = 240
    ET_ASSIGN = 241
    ET_ARRAY_GENERATOR = 242
    ET_FUNC_PARAM = 243
    ET_FUNC_PARAM_DEFAULT = 244
    ET_FUNC_CALL = 245
    ET_RETURN = 246
    ET_BOOL = 247
    ET_NONE = 248
    ET_ID_AS = 249
    ET_LAMBDA = 250
    ET_EXPR_AS = 251
    ET_DOT_ASSIGN = 252
    ET_SQUARE_BRACKETS_ASSIGN = 253