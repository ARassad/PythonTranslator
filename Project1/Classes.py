from enum import Enum
# from fileReader import text
import List


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
    ET_FUNC_CALL = 44
    ET_RETURN = 45
    ET_BOOL = 46
    ET_NONE = 47
    ET_ID_AS = 48
    ET_LAMBDA = 49
    ET_EXPR_AS = 50


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


class EXPR:
    def __init__(self):
        self.type = ExprType.ET_UNDEFINED
        self.intVal = 0
        self.floatVal = 0.0
        self.boolVal = False
        self.stringVal = ""
        self.left = object
        self.right = object
        self.middle = object
        self.list = object
        self.identifier = object

    def read_expr(self, index, last, text):
        i = index + 1
        string = text[i]
        self.left = EXPR()
        self.right = EXPR()
        self.middle = EXPR()
        self.list = List.List()
        self.identifier = EXPR()
        if string == "ET_OR":
            self.type = ExprType.ET_OR
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_AND":
            self.type = ExprType.ET_AND
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_NOT":
            self.type = ExprType.ET_NOT
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_IN":
            self.type = ExprType.ET_IN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_NOT_IN":
            self.type = ExprType.ET_NOT_IN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_IS":
            self.type = ExprType.ET_IS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_IS_NOT":
            self.type = ExprType.ET_IS_NOT
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_PLUS_ASSIGN":
            self.type = ExprType.ET_PLUS_ASSIGN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MINUS_ASSIGN":
            self.type = ExprType.ET_MINUS_ASSIGN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MULT_ASSIGN":
            self.type = ExprType.ET_MULT
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_POW_ASSIGN":
            self.type = ExprType.ET_POW_ASSIGN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_DIV_ASSIGN":
            self.type = ExprType.ET_DIV_ASSIGN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MOD_ASSIGN":
            self.type = ExprType.ET_MOD_ASSIGN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LESSER":
            self.type = ExprType.ET_LESSER
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LESSER_EQUAL":
            self.type = ExprType.ET_LESSER_EQUAL
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_GREATER":
            self.type = ExprType.ET_GREATER
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_GREATER_EQUAL":
            self.type = ExprType.ET_GREATER_EQUAL
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_NOT_EQUAL":
            self.type = ExprType.ET_NOT_EQUAL
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_EQUAL":
            self.type = ExprType.ET_EQUAL
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LEFT_SHIFT":
            self.type = ExprType.ET_LEFT_SHIFT
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_RIGHT_SHIFT":
            self.type = ExprType.ET_RIGHT_SHIFT
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_PLUS":
            self.type = ExprType.ET_PLUS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MINUS":
            self.type = ExprType.ET_MINUS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MULT":
            self.type = ExprType.ET_MULT
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_DIV":
            self.type = ExprType.ET_DIV
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MOD":
            self.type = ExprType.ET_MOD
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_FLOOR_DIV":
            self.type = ExprType.ET_FLOOR_DIV
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_UPLUS":
            self.type = ExprType.ET_UPLUS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_UMINUS":
            self.type = ExprType.ET_UMINUS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_POW":
            self.type = ExprType.ET_POW
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_DOT":
            self.type = ExprType.ET_DOT
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_ID":
            self.type = ExprType.ET_ID
            self.stringVal = text[i + 1]
            i += 1
        elif string == "ET_INT":
            self.type = ExprType.ET_INT
            self.intVal = int(text[i + 1])
            i += 1
        elif string == "ET_FLOAT":
            self.type = ExprType.ET_FLOAT
            self.floatVal = float(text[i + 1])
            i += 1
        elif string == "ET_STRING":
            self.type = ExprType.ET_STRING
            self.stringVal = text[i + 1]
            i += 1
        elif string == "ET_SQUARE_BRACKETS":
            self.type = ExprType.ET_SQUARE_BRACKETS
            i = self.list.read_list(index=i + 2, last=int(text[i+2]), text=text)
        elif string == "ET_ARRAY_APPEAL":
            self.type = ExprType.ET_ARRAY_APPEAL
            i = self.left.read_expr(index=i + 2, last=int(text[i + 2]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_ARRAY_SLICE":
            self.type = ExprType.ET_ARRAY_SLICE
            i = self.left.read_expr(index= i + 2, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_ARRAY_SLICE_ARGUMENTS":
            self.type = ExprType.ET_ARRAY_SLICE_ARGUMENTS
            i = self.left.read_expr(index=i + 2, last=int(text[i + 1]), text=text)
            i = self.middle.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            if text[i] == "Expression":
                i = self.right.read_expr(index=i, last=int(text[i+1]), text=text)
        elif string == "ET_ASSIGN":
            self.type = ExprType.ET_ASSIGN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_ARRAY_GENERATOR":
            self.type = ExprType.ET_ARRAY_GENERATOR
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.identifier.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            if int(text[i + 1]) != last:
                i = self.middle.read_expr(index=i+1, last=int(text[i+1]), text=text)

        elif string == "ET_FUNC_PARAM":
            self.type = ExprType.ET_FUNC_PARAM
            i = self.identifier.read_expr(index=i + 1, last=int(text[i+1]), text=text)
            if int(text[i + 1]) != last:
                i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_FUNC_CALL":
            self.type = ExprType.ET_FUNC_CALL
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.list.read_list(index=i + 2, last=int(text[i+2]), text=text)
        elif string == "ET_BOOL":
            self.type = ExprType.ET_BOOL
            if text[i + 2] == "1":
                self.boolVal = True
        elif string == "ET_NONE":
            self.type = ExprType.ET_NONE
        elif string == "ET_ID_AS":
            self.type = ExprType.ET_ID_AS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LAMBDA":
            self.type = ExprType.ET_LAMBDA
            i = self.left.read_expr(index=i + 2, last=int(text[i + 1]), text=text)
            i = self.list.read_list(index=i + 2, last=int(text[i+2]), text=text)
        elif string == "ET_EXPR_AS":
            self.type = ExprType.ET_EXPR_AS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.identifier.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        return i + 1


class STMT:
    def __init__(self):
        self.value = 1
        self.type = StmtType(0)
        self.expr = EXPR()
        self.firstSuite = object
        self.secondSuite = object
        self.thirdSuite = object
        self.stmtList = object
        self.identifier = EXPR()

    def read_stmt(self, index, last, text):
        self.firstSuite = List.List()
        self.secondSuite = List.List()
        self.thirdSuite = List.List()
        self.stmtList = List.List()
        i = index + 1
        string = text[i]
        if string == "ST_EXPRESSION":
            self.type = StmtType.ST_EXPRESSION
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_CONDITION":
            self.type = StmtType.ST_CONDITION
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
            if text[i + 1] == "List":
                i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            if text[i + 1] == "List" and text[i + 3] == "LT_STMT_ELIF_LIST":
                i = self.stmtList.read_list(i + 2, last=int(text[i + 2]), text=text)
            if text[i + 1] == "List" and int(text[i]) != last:
                i = self.secondSuite.read_list(i + 2, last, text=text)
        elif string == "ST_FUNCTION_DEF":
            self.type = StmtType.ST_FUNCTION_DEF
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            if text[i + 1] != "List":
                i = self.expr.read_expr(i + 1, last=int(text[i+1]), text=text)
            i = self.stmtList.read_list(i + 2, last=int(text[i+2]), text=text)
            i = self.firstSuite.read_list(i + 2, last=int(text[i+2]), text=text)
        elif string == "ST_CLASS_DEF":
            self.type = StmtType.ST_CLASS_DEF
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            i = self.stmtList.read_list(i + 2, last=int(text[i+2]), text=text)
        elif string == "ST_WHILE":
            self.type = StmtType.ST_WHILE
            i = self.expr.read_expr(i + 1, last=int(text[i+1]), text=text)
            i = self.firstSuite.read_list(i + 2, last=int(text[i+2]), text=text)
            if int(text[i + 1]) != last:
                i = self.secondSuite.read_list(i + 2, last=int(text[i+2]), text=text)
        elif string == "ST_FOR":
            self.type = StmtType.ST_FOR
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            if int(text[i + 1]) != last:
                i = self.secondSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_TRY":
            self.type = StmtType.ST_TRY
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            i = self.stmtList.read_list(i + 2, last=int(text[i + 2]), text=text)
            i = self.secondSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            i = self.thirdSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_WITH":
            self.type = StmtType.ST_WITH
        elif string == "ST_ELIF":
            self.type = StmtType.ST_ELIF
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_EXCEPT":
            self.type = StmtType.ST_EXCEPT
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            if text[i + 2] == "ET_EXPR_AS":
                i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_RETURN":
            self.type = StmtType.ST_RETURN
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_PASS":
            self.type = StmtType.ST_PASS
        elif string == "ST_BREAK":
            self.type = StmtType.ST_BREAK
        elif string == "ST_CONTINUE":
            self.type = StmtType.ST_CONTINUE
        elif string == "ST_YIELD":
            self.type = StmtType.ST_YIELD
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_ASSERT":
            self.type = StmtType.ST_ASSERT
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_IMPORT":
            self.type = StmtType.ST_IMPORT
            i = self.stmtList.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_FROM_IMPORT":
            self.type = StmtType.ST_FROM_IMPORT
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            if text[i] == "List":
                i = self.stmtList.read_list(i + 1, last=int(text[i + 1]), text=text)
        return i + 1








