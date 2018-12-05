from enum import Enum
# from fileReader import text
import List
from Enums import ExprType
from Enums import StmtType

forbiddenEXPRS = {ExprType.ET_NOT_IN, ExprType.ET_IS, ExprType.ET_PLUS_ASSIGN, ExprType.ET_MINUS_ASSIGN,
                  ExprType.ET_MULT_ASSIGN, ExprType.ET_POW_ASSIGN, ExprType.ET_DIV_ASSIGN,  ExprType.ET_MOD_ASSIGN,
                  ExprType.ET_LESSER_EQUAL, ExprType.ET_GREATER_EQUAL, ExprType.ET_LEFT_SHIFT, ExprType.ET_RIGHT_SHIFT,
                  ExprType.ET_POW, ExprType.ET_MOD, ExprType.ET_FLOOR_DIV, ExprType.ET_ID_AS, ExprType.ET_EXPR_AS}

forbiddenSTMTS = {StmtType.ST_WITH, StmtType.ST_FOR, StmtType.ST_BREAK, StmtType.ST_CONTINUE, StmtType.ST_YIELD,
                  StmtType.ST_ASSERT, StmtType.ST_FROM_IMPORT, StmtType.ST_IMPORT}


class EXPR:
    def __init__(self):
        self.type = ExprType.ET_UNDEFINED
        self.intVal = None
        self.floatVal = None
        self.boolVal = None
        self.stringVal = None
        self.left = None
        self.right = None
        self.middle = None
        self.list = None
        self.identifier = None

    def read_expr(self, index, last, text):
        i = index + 1
        string = text[i]
        if string == "ET_OR":
            self.type = ExprType.ET_OR
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_AND":
            self.left = EXPR()
            self.right = EXPR()
            self.type = ExprType.ET_AND
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_NOT":
            self.right = EXPR()
            self.type = ExprType.ET_NOT
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_IN":
            self.type = ExprType.ET_IN
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_NOT_IN":
            self.type = ExprType.ET_NOT_IN
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_IS":
            self.type = ExprType.ET_IS
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_IS_NOT":
            self.type = ExprType.ET_IS_NOT
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_PLUS_ASSIGN":
            self.type = ExprType.ET_PLUS_ASSIGN
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MINUS_ASSIGN":
            self.type = ExprType.ET_MINUS_ASSIGN
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MULT_ASSIGN":
            self.type = ExprType.ET_MULT
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_POW_ASSIGN":
            self.type = ExprType.ET_POW_ASSIGN
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_DIV_ASSIGN":
            self.type = ExprType.ET_DIV_ASSIGN
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MOD_ASSIGN":
            self.type = ExprType.ET_MOD_ASSIGN
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LESSER":
            self.type = ExprType.ET_LESSER
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LESSER_EQUAL":
            self.type = ExprType.ET_LESSER_EQUAL
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_GREATER":
            self.type = ExprType.ET_GREATER
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_GREATER_EQUAL":
            self.type = ExprType.ET_GREATER_EQUAL
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_NOT_EQUAL":
            self.type = ExprType.ET_NOT_EQUAL
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_EQUAL":
            self.type = ExprType.ET_EQUAL
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LEFT_SHIFT":
            self.type = ExprType.ET_LEFT_SHIFT
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_RIGHT_SHIFT":
            self.type = ExprType.ET_RIGHT_SHIFT
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_PLUS":
            self.type = ExprType.ET_PLUS
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MINUS":
            self.type = ExprType.ET_MINUS
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MULT":
            self.type = ExprType.ET_MULT
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_DIV":
            self.type = ExprType.ET_DIV
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_MOD":
            self.type = ExprType.ET_MOD
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_FLOOR_DIV":
            self.type = ExprType.ET_FLOOR_DIV
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_UPLUS":
            self.type = ExprType.ET_UPLUS
            self.left = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_UMINUS":
            self.type = ExprType.ET_UMINUS
            self.left = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_POW":
            self.type = ExprType.ET_POW
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_DOT":
            self.type = ExprType.ET_DOT
            self.left = EXPR()
            self.right = EXPR()
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
            self.list = List.List()
            i = self.list.read_list(index=i + 2, last=int(text[i+2]), text=text)
        elif string == "ET_ARRAY_APPEAL":
            self.type = ExprType.ET_ARRAY_APPEAL
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_ARRAY_SLICE":
            self.type = ExprType.ET_ARRAY_SLICE
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 2, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_ARRAY_SLICE_ARGUMENTS":
            self.type = ExprType.ET_ARRAY_SLICE_ARGUMENTS
            self.left = EXPR()
            self.middle = EXPR()
            i = self.left.read_expr(index=i + 2, last=int(text[i + 1]), text=text)
            i = self.middle.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            if text[i] == "Expression":
                self.right = EXPR()
                i = self.right.read_expr(index=i, last=int(text[i+1]), text=text)
        elif string == "ET_ASSIGN":
            self.type = ExprType.ET_ASSIGN
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_ARRAY_GENERATOR":
            self.type = ExprType.ET_ARRAY_GENERATOR
            self.left = EXPR()
            self.right = EXPR()
            self.identifier = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.identifier.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            if int(text[i + 1]) != last:
                self.middle = EXPR()
                i = self.middle.read_expr(index=i+1, last=int(text[i+1]), text=text)

        elif string == "ET_FUNC_PARAM":
            self.type = ExprType.ET_FUNC_PARAM
            self.identifier = EXPR()
            i = self.identifier.read_expr(index=i + 1, last=int(text[i+1]), text=text)
            if int(text[i + 1]) != last:
                self.left = EXPR()
                i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_FUNC_CALL":
            self.type = ExprType.ET_FUNC_CALL
            self.left = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            self.list = List.List()
            i = self.list.read_list(index=i + 2, last=int(text[i+2]), text=text)
        elif string == "ET_BOOL":
            self.type = ExprType.ET_BOOL
            if text[i + 2] == "1":
                self.boolVal = True
            else:
                self.boolVal = False
            i += 1
        elif string == "ET_NONE":
            self.type = ExprType.ET_NONE
        elif string == "ET_ID_AS":
            self.type = ExprType.ET_ID_AS
            self.left = EXPR()
            self.right = EXPR()
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.right.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
        elif string == "ET_LAMBDA":
            self.type = ExprType.ET_LAMBDA
            self.left = EXPR()
            self.list = List.List()
            i = self.left.read_expr(index=i + 2, last=int(text[i + 1]), text=text)
            i = self.list.read_list(index=i + 2, last=int(text[i+2]), text=text)
        elif string == "ET_EXPR_AS":
            self.type = ExprType.ET_EXPR_AS
            self.identifier = EXPR()
            self.left = EXPR()
            i = self.identifier.read_expr(index=i + 1, last=int(text[i + 1]), text=text)
            i = self.left.read_expr(index=i + 1, last=int(text[i + 1]), text=text)

        return i + 1

    def write(self, writefile, max_id, parent_id):
        max_id += 1
        cur_id = max_id
        if self.type == ExprType.ET_UNDEFINED:
            pass
        elif self.type == ExprType.ET_OR:
            writefile.write(str(cur_id) + '[label=\"OR\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) +'\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_AND:
            writefile.write(str(cur_id) + '[label=\"AND\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_NOT:
            writefile.write(str(cur_id) + '[label=\"NOT\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_IN:
            writefile.write(str(cur_id) + '[label=\"IN\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_NOT_IN:
            writefile.write(str(cur_id) + '[label=\"NOT_IN\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_IS:
            writefile.write(str(cur_id) + '[label=\"IS\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_IS_NOT:
            writefile.write(str(cur_id) + '[label=\"IS_NOT\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_PLUS_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"+=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MINUS_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"-=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MULT_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"*=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_POW_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"^=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_DIV_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"\/=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MOD_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"\%=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_LESSER:
            writefile.write(str(cur_id) + '[label=\"<\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_LESSER_EQUAL:
            writefile.write(str(cur_id) + '[label=\"<=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_GREATER:
            writefile.write(str(cur_id) + '[label=\">\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_GREATER_EQUAL:
            writefile.write(str(cur_id) + '[label=\">=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_NOT_EQUAL:
            writefile.write(str(cur_id) + '[label=\"!=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_EQUAL:
            writefile.write(str(cur_id) + '[label=\"==\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_LEFT_SHIFT:
            writefile.write(str(cur_id) + '[label=\"<<\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_RIGHT_SHIFT:
            writefile.write(str(cur_id) + '[label=\">>\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_PLUS:
            writefile.write(str(cur_id) + '[label=\"+\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MINUS:
            writefile.write(str(cur_id) + '[label=\"-\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MULT:
            writefile.write(str(cur_id) + '[label=\"*\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_DIV:
            writefile.write(str(cur_id) + '[label=\"\/\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MOD:
            writefile.write(str(cur_id) + '[label=\"%\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_FLOOR_DIV:
            writefile.write(str(cur_id) + '[label=\"floor div\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_UPLUS:
            writefile.write(str(cur_id) + '[label=\"+\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            self.left.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MULT_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"-\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_POW:
            writefile.write(str(cur_id) + '[label=\"^\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_DOT:
            writefile.write(str(cur_id) + '[label=\".\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_ID:
            writefile.write(str(cur_id) + '[label=\"' + self.stringVal + '\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == ExprType.ET_INT:
            writefile.write(str(cur_id) + '[label=\"' + str(self.intVal) + '\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == ExprType.ET_FLOAT:
            writefile.write(str(cur_id) + '[label=\"' + str(self.floatVal) + '\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == ExprType.ET_STRING:
            writefile.write(str(cur_id) + '[label="\\"' + str(self.stringVal)[1:self.stringVal.__len__() -1] + '\\""]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == ExprType.ET_SQUARE_BRACKETS:
            writefile.write(str(cur_id) + '[label=\"[]\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.list.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_ARRAY_APPEAL:
            writefile.write(str(cur_id) + '[label=\"[]\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_ARRAY_SLICE:
            writefile.write(str(cur_id) + '[label=\"Array_Slice\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_ARRAY_SLICE_ARGUMENTS:
            writefile.write(str(cur_id) + '[label=\"Array_Slice_ARGS\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.middle.write(writefile, max_id, cur_id)
            if isinstance(self.right, EXPR):
                max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_ARRAY_GENERATOR:
            writefile.write(str(cur_id) + '[label=\"array_generator\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            if isinstance(self.identifier, EXPR):
                max_id = self.identifier.write(writefile, max_id, cur_id)
            max_id = self.middle.write(writefile, max_id, cur_id)
            if isinstance(self.right, EXPR):
                max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_FUNC_PARAM or self.type ==ExprType.ET_FUNC_PARAM_DEFAULT:
            writefile.write(str(cur_id) + '[label=\"function_params\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.identifier.write(writefile, max_id, cur_id)
            if isinstance(self.left, EXPR):
                max_id = self.left.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_FUNC_CALL:
            writefile.write(str(cur_id) + '[label=\"function_call\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.list.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_BOOL:
            writefile.write(str(cur_id) + '[label=\"bool' + str(self.intVal) + '\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == ExprType.ET_NONE:
            writefile.write(str(cur_id) + '[label=\"None\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == ExprType.ET_ID_AS:
            writefile.write(str(cur_id) + '[label=\"ID_AS\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_MULT_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"lambda\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.list.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_EXPR_AS:
            writefile.write(str(cur_id) + '[label=\"EXPR_AS\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.identifier.write(writefile, max_id, cur_id)
            max_id = self.left.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_DOT_ASSIGN:
            writefile.write(str(cur_id) + '[label=\".=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.middle.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        elif self.type == ExprType.ET_SQUARE_BRACKETS_ASSIGN:
            writefile.write(str(cur_id) + '[label=\"[]=\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.left.write(writefile, max_id, cur_id)
            max_id = self.middle.write(writefile, max_id, cur_id)
            max_id = self.right.write(writefile, max_id, cur_id)
        else:
            pass
        return max_id

    def find_and_output_errors(self, count_errors, file , pos_return):
        if self.type in forbiddenEXPRS:
            count_errors += 1
            file.write('Ошибка выражения! ' + str(self.type) + ' Такое выражение не поддерживается!\n')
            return count_errors
        else:
            if self.left is not None:
                count_errors = self.left.find_and_output_errors(count_errors, file, pos_return)
            if self.right is not None:
                count_errors = self.right.find_and_output_errors(count_errors, file, pos_return)
            if self.identifier is not None:
                count_errors = self.identifier.find_and_output_errors(count_errors, file, pos_return)
            if self.list is not None:
                count_errors = self.list.find_and_output_errors(count_errors, file, pos_return)
            if self.middle is not None:
                count_errors = self.identifier.find_and_output_errors(count_errors, file, pos_return)
            if self.type == ExprType.ET_ASSIGN:
                if not(self.left.type == ExprType.ET_ID or self.left.type == ExprType.ET_DOT or
                       self.left.type == ExprType.ET_ARRAY_APPEAL):
                    count_errors += 1
            return count_errors

    def convert(self):
        if self.type.value == ExprType.ET_INT.value:
            num = self.intVal
            self.intVal = None
            self.type = ExprType.ET_FUNC_CALL
            self.left = EXPR()
            self.left.type = ExprType.ET_ID
            self.left.stringVal = 'int'
            self.list = List.List()
            self.list.type = List.ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS
            self.list.expr = EXPR()
            self.list.expr.type = ExprType.ET_INT
            self.list.expr.intVal = num
        elif self.type.value == ExprType.ET_FLOAT:
            num = self.floatVal
            self.floatVal = None
            self.type = ExprType.ET_FUNC_CALL
            self.left = EXPR()
            self.left.type = ExprType.ET_ID
            self.left.stringVal = 'float'
            self.list = List.List()
            self.list.type = List.ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS
            self.list.expr = EXPR()
            self.list.expr.type = ExprType.ET_FLOAT
            self.list.expr.floatVal = num.value
        elif self.type.value == ExprType.ET_STRING.value:
            num = self.stringVal
            self.stringVal = None
            self.type = ExprType.ET_FUNC_CALL
            self.left = EXPR()
            self.left.type = ExprType.ET_ID
            self.left.stringVal = 'str'
            self.list = List.List()
            self.list.type = List.ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS
            self.list.expr = EXPR()
            self.list.expr.type = ExprType.ET_STRING
            self.list.expr.stringVal = num
        elif self.type.value == ExprType.ET_BOOL.value:
            num = self.boolVal
            self.boolVal = None
            self.type = ExprType.ET_FUNC_CALL
            self.left = EXPR()
            self.left.type = ExprType.ET_ID
            self.left.stringVal = 'int'
            self.list = List.List()
            self.list.type = List.ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS
            self.list.expr = EXPR()
            self.list.expr.type = ExprType.ET_INT
            if num:
                self.list.expr.intVal = 1
            else:
                self.list.expr.intVal = 0
        else:
            if self.left is not None:
                self.left.convert()
            if self.right is not None:
                self.right.convert()
            if self.identifier is not None:
                self.identifier.convert()
            if self.middle is not None:
                self.middle.convert()
            if self.list is not None:
                self.list.convert()

        if self.type.value == ExprType.ET_ASSIGN.value and self.left.type == ExprType.ET_DOT:
            self.type = ExprType.ET_DOT_ASSIGN
            self.middle = self.left.right
            self.left = self.left.left
        if self.type.value == ExprType.ET_ASSIGN.value and self.left.type == ExprType.ET_ARRAY_APPEAL:
            self.type = ExprType.ET_SQUARE_BRACKETS_ASSIGN
            self.middle = self.left.right
            self.left = self.left.left


class STMT:
    def __init__(self):
        self.value = None
        self.type = StmtType.ST_UNDEFINED
        self.expr = None
        self.firstSuite = None
        self.secondSuite = None
        self.thirdSuite = None
        self.stmtList = None
        self.identifier = None

    def read_stmt(self, index, last, text):
        i = index + 1
        string = text[i]
        if string == "ST_EXPRESSION":
            self.type = StmtType.ST_EXPRESSION
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_CONDITION":
            self.type = StmtType.ST_CONDITION
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
            if text[i + 1] == "List":
                self.firstSuite = List.List()
                i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            if text[i + 1] == "List" and text[i + 3] == "LT_STMT_ELIF_LIST":
                self.stmtList = List.List()
                i = self.stmtList.read_list(i + 2, last=int(text[i + 2]), text=text)
            if text[i + 1] == "List" and int(text[i]) != last:
                self.secondSuite = List.List()
                i = self.secondSuite.read_list(i + 2, last, text=text)
        elif string == "ST_FUNCTION_DEF":
            self.type = StmtType.ST_FUNCTION_DEF
            self.identifier = EXPR()
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            if text[i + 1] != "List":
                self.expr = EXPR()
                i = self.expr.read_expr(i + 1, last=int(text[i+1]), text=text)
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i+2]), text=text)
            if text[i + 1] == "List":
                self.stmtList = List.List()
                i = self.stmtList.read_list(i + 2, last=int(text[i+2]), text=text)
        elif string == "ST_CLASS_DEF":
            self.type = StmtType.ST_CLASS_DEF
            self.identifier = EXPR()
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            self.secondSuite = List.List()
            i = self.stmtList.read_list(i + 2, last=int(text[i+2]), text=text)
        elif string == "ST_WHILE":
            self.type = StmtType.ST_WHILE
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i+1]), text=text)
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i+2]), text=text)
            if int(text[i + 1]) != last:
                i = self.secondSuite.read_list(i + 2, last=int(text[i+2]), text=text)
        elif string == "ST_FOR":
            self.type = StmtType.ST_FOR
            self.identifier = EXPR()
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            if int(text[i + 1]) != last:
                self.secondSuite = List.List()
                i = self.secondSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_TRY":
            self.type = StmtType.ST_TRY
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            self.stmtList = List.List()
            i = self.stmtList.read_list(i + 2, last=int(text[i + 2]), text=text)
            self.secondSuite = List.List()
            i = self.secondSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            self.thirdSuite = List.List()
            i = self.thirdSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_WITH":
            self.type = StmtType.ST_WITH
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            self.stmtList = List.List()
            i = self.stmtList.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_ELIF":
            self.type = StmtType.ST_ELIF
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_EXCEPT":
            self.type = StmtType.ST_EXCEPT
            self.firstSuite = List.List()
            i = self.firstSuite.read_list(i + 2, last=int(text[i + 2]), text=text)
            if text[i + 2] == "ET_EXPR_AS":
                self.identifier = EXPR()
                i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_RETURN":
            self.type = StmtType.ST_RETURN
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_PASS":
            self.type = StmtType.ST_PASS
        elif string == "ST_BREAK":
            self.type = StmtType.ST_BREAK
        elif string == "ST_CONTINUE":
            self.type = StmtType.ST_CONTINUE
        elif string == "ST_YIELD":
            self.type = StmtType.ST_YIELD
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_ASSERT":
            self.type = StmtType.ST_ASSERT
            self.expr = EXPR()
            i = self.expr.read_expr(i + 1, last=int(text[i + 1]), text=text)
        elif string == "ST_IMPORT":
            self.type = StmtType.ST_IMPORT
            self.stmtList = List.List()
            i = self.stmtList.read_list(i + 2, last=int(text[i + 2]), text=text)
        elif string == "ST_FROM_IMPORT":
            self.type = StmtType.ST_FROM_IMPORT
            self.identifier = EXPR()
            i = self.identifier.read_expr(i + 1, last=int(text[i + 1]), text=text)
            if text[i] == "List":
                self.stmtList = List.List()
                i = self.stmtList.read_list(i + 1, last=int(text[i + 1]), text=text)
        return i + 1

    def write(self, writefile, max_id, parent_id):
        max_id += 1
        cur_id = max_id
        if self.type == StmtType.ST_UNDEFINED:
            pass
        elif self.type == StmtType.ST_EXPRESSION:
            writefile.write(str(cur_id) + '[label=\"expr_stmt\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id)+'\n')
            max_id = self.expr.write(writefile=writefile,max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_CONDITION:
            writefile.write(str(cur_id) + '[label=\"if_stmt\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if isinstance(self.stmtList, List.List):
                max_id = self.stmtList.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if isinstance(self.secondSuite, List.List):
                max_id = self.secondSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_FUNCTION_DEF:
            writefile.write(str(cur_id) + '[label=\"def\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.identifier.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if self.expr is not None:
                max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if self.stmtList is not None:
                max_id = self.stmtList.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_CLASS_DEF:
            writefile.write(str(cur_id) + '[label=\"class\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.identifier.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.stmtList.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_WHILE:
            writefile.write(str(cur_id) + '[label=\"while\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if isinstance(self.secondSuite, List.List):
                max_id = self.secondSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_FOR:
            writefile.write(str(cur_id) + '[label=\"for\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.identifier.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if isinstance(self.secondSuite, List.List):
                max_id = self.secondSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_TRY:
            writefile.write(str(cur_id) + '[label=\"try\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.stmtList.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.secondSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.thirdSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_ELIF:
            writefile.write(str(cur_id) + '[label=\"elif\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_EXCEPT:
            writefile.write(str(cur_id) + '[label=\"except\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if isinstance(self.secondSuite, List.List):
                max_id = self.secondSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.identifier.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_RETURN:
            writefile.write(str(cur_id) + '[label=\"return\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_RAISE:
            writefile.write(str(cur_id) + '[label=\"raise\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_BREAK:
            writefile.write(str(cur_id) + '[label=\"break\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == StmtType.ST_CONTINUE:
            writefile.write(str(cur_id) + '[label=\"continue\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        elif self.type == StmtType.ST_YIELD:
            writefile.write(str(cur_id) + '[label=\"yield\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_YIELD:
            writefile.write(str(cur_id) + '[label=\"yield\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_ASSERT:
            writefile.write(str(cur_id) + '[label=\"yield\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_IMPORT:
            writefile.write(str(cur_id) + '[label=\"yield\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_FROM_IMPORT:
            writefile.write(str(cur_id) + '[label=\"yield\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.identifier.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            if isinstance(self.stmtList, List.List):
                max_id = self.stmtList.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            else:
                max_id += 1
                writefile.write(str(max_id) + '[label=\"*\"]\n')
                writefile.write(str(cur_id) + '--' + str(max_id) + '\n')
        elif self.type == StmtType.ST_WITH:
            writefile.write(str(cur_id) + '[label=\"yield\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.firstSuite.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
            max_id = self.stmtList.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == StmtType.ST_PASS:
            writefile.write(str(cur_id) + '[label=\"pass\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
        else:
            pass
        return max_id

    def find_and_output_errors(self, count_errors, file, pos_return):
        if self.type.value == StmtType.ST_FUNCTION_DEF:
            pos_return = 1
        if self.type in forbiddenSTMTS:
            count_errors += 1
            file.write('Ошибка statementа! ' + str(self.type) + ' Такой тип statementа не поддерживается!\n')
            return count_errors
        if self.identifier is not None:
            count_errors = self.identifier.find_and_output_errors(count_errors, file, pos_return)
        if self.expr is not None:
            count_errors = self.expr.find_and_output_errors(count_errors, file, pos_return)
        if self.stmtList is not None:
            count_errors, pos_return = self.stmtList.find_and_output_errors(count_errors, file, pos_return)
        if self.firstSuite is not None:
            count_errors, pos_return = self.firstSuite.find_and_output_errors(count_errors, file, pos_return)
        if self.secondSuite is not None:
            count_errors, pos_return = self.secondSuite.find_and_output_errors(count_errors, file, pos_return)
        if self.thirdSuite is not None:
            count_errors, pos_return = self.thirdSuite.find_and_output_errors(count_errors, file, pos_return)
        if self.type.value == StmtType.ST_RETURN.value:
            if pos_return == 0:
                file.write('Ошибка return! Return должен быть внутри тела функции\n')
                count_errors += 1
            else:
                pos_return = 0

        return count_errors, pos_return

    def convert(self):
        if self.expr is not None:
            self.expr.convert()
        if self.identifier is not None:
            self.identifier.convert()
        if self.firstSuite is not None:
            self.firstSuite.convert()
        if self.secondSuite is not None:
            self.secondSuite.convert()
        if self.thirdSuite is not None:
            self.thirdSuite.convert()
        if self.stmtList is not None:
            self.stmtList.convert()
        if self.type.value == StmtType.ST_FUNCTION_DEF.value:
            func_list = self.firstSuite
            while func_list.nextEl is not None:
                func_list = func_list.nextEl
            if func_list.stmt.type.value != StmtType.ST_RETURN.value:
                func_list.nextEl = List.List()
                func_list.nextEl.type = List.ListType.LT_STATEMENT_LIST
                func_list.nextEl.stmt = STMT()
                func_list.nextEl.stmt.type = StmtType.ST_RETURN
                func_list.nextEl.stmt.expr = EXPR()
                func_list.nextEl.stmt.expr.type = ExprType.ET_NONE

