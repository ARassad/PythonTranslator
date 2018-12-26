from Classes import *
import Enums as en
from Enums import ExprType, ListType, StmtType
import uuid
from List import *

def create_main_class(root):
    """
    NOT RECURSIVE FUNCTION, PROCCESS ON ROOT AND CREATE MAIN CLASS
    :param root:
    :return: root
    """
    main_class = STMT()
    main_class.type = StmtType.ST_CLASS_DEF

    main_class.identifier = EXPR()
    main_class.identifier.type = ExprType.ET_ID
    main_class.identifier.stringVal = "<MainClass>"

    main_class.firstSuite = root
    create_main_function(main_class)
    return main_class


def create_main_function(root):
    main_funct = STMT()
    main_funct.type = StmtType.ST_FUNCTION_DEF

    main_funct.identifier = EXPR()
    main_funct.identifier.type = ExprType.ET_ID
    main_funct.identifier.stringVal = "<main>"
    # main_funct.stmtList = lt.List()
    # main_funct.stmtList.type = ListType.LT_EXPR_FUNCTION_PARAMS
    # main_funct.stmtList.expr = cl.EXPR()
    # main_funct.stmtList.expr.type = ExprType.ET_FUNC_PARAM
    # main_funct.stmtList.expr.identifier = cl.EXPR()
    # main_funct.stmtList.expr.identifier.stringVal = "args"
    # main_funct.stmtList.expr.identifier.type = ExprType.ET_ID
    main_funct.firstSuite = root.firstSuite
    root.firstSuite = main_funct


def call(node, name, procceser):
    atr = getattr(node, name, None)
    if atr is not None:
        procceser(atr)


def add_return_none_to_functions(root):
    def procces(node):
        if node.type.value == StmtType.ST_FUNCTION_DEF.value:
            cur = node.firstSuite
            while cur.nextEl is not None:
                cur = cur.nextEl
            if cur.stmt.type.value != StmtType.ST_RETURN.value:
                stmt_return = List()
                stmt_return.type = ListType.LT_STATEMENT_LIST

                stmt_return.stmt = STMT()
                stmt_return.stmt.type = StmtType.ST_RETURN

                stmt_return.stmt.expr = EXPR()
                stmt_return.stmt.expr.type = ExprType.ET_FUNC_CALL

                stmt_return.stmt.expr.left = EXPR()
                stmt_return.stmt.expr.left.type = ExprType.ET_ID
                stmt_return.stmt.expr.left.stringVal = "<None>"

                cur.nextEl = stmt_return

        # LIST
        call(node, "stmt",  procces)
        call(node, "nextEl", procces)

        # STMT, LIST
        call(node, "expr", procces)

        # EXPR
        call(node, "left", procces)
        call(node, "right",procces)
        call(node, "middle",procces)
        call(node, "list",procces)
        call(node, "identifier", procces)

        # STMT
        call(node, "firstSuite",procces)
        call(node, "secondSuite",procces)
        call(node, "thirdSuite",procces)
        call(node, "stmtList",procces)
        call(node, "identifier",procces)

    procces(root)

    return root