import Classes
from Enums import ListType


class List:
    def __init__(self):
        self.stmt = Classes.STMT()
        self.expr = Classes.EXPR()
        self.nextEl = object
        self.type = ListType.LT_UNDEFINED

    def read_list(self, index, last, text):
        i = index + 1
        if text[i] == "LT_ELEMENT":
            self.type = ListType.LT_ELEMENT
            if text[i + 1] == "Statement":
                i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
            else:
                i = self.expr.read_expr(i + 2, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_ARRAY_INITIAL_ARGUMENTS":
            self.type = ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_FUNCTION_PARAMS":
            self.type = ListType.LT_EXPR_FUNCTION_PARAMS
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_IDENTIFIERS_E":
            self.type = ListType.LT_EXPR_IDENTIFIERS_E
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_STATEMENT_LIST":
            self.type = ListType.LT_STATEMENT_LIST
            i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
        elif text[i] == "LT_STMT_ELIF_LIST":
            self.type = ListType.LT_STMT_ELIF_LIST
            i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
        elif text[i] == "LT_STMT_EXCEPT_LIST":
            self.type = ListType.LT_STMT_EXCEPT_LIST
            i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
        elif text[i] == "LT_EXPR_ID_AS_LIST":
            self.type = ListType.LT_EXPR_ID_AS_LIST
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_WITH":
            self.type = ListType.LT_EXPR_WITH
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        if text[i + 1] == "List":
            self.nextEl = List()
            i = self.nextEl.read_list(i + 2, int(text[i + 2]), text=text)
        return i + 1
