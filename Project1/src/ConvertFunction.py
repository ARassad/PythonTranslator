import Classes as cl
import Enums as en
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

    return main_class



