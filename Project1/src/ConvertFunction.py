import Classes as cl
import Enums as en
import List as lt
from Enums import ExprType, ListType, StmtType
import uuid


def create_main_class(root):
    """
    NOT RECURSIVE FUNCTION, PROCCESS ON ROOT AND CREATE MAIN CLASS
    :param root:
    :return: root
    """
    main_class = cl.STMT()
    main_class.type = StmtType.ST_CLASS_DEF

    main_class.identifier = cl.EXPR()
    main_class.identifier.type = ExprType.ET_ID
    main_class.identifier.stringVal = "<MainClass>"

    main_class.firstSuite = root
    create_main_function(main_class)
    return main_class


def create_main_function(root):
    main_funct = cl.STMT()
    main_funct.type = StmtType.ST_FUNCTION_DEF

    main_funct.identifier = cl.EXPR()
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

