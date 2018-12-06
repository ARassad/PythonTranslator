import Classes as cl
import Enums as en
from Enums import ExprType, ListType, StmtType
import uuid


class ECONSTANT:
    UNDEFINED = 0
    Utf8 = 1
    Int = 3
    Float = 4
    String = 8
    NameAndType = 12
    Class = 7
    Fieldref = 9
    Methodref = 10


class ConstantElement:
    def __init__(self, ctype=ECONSTANT.UNDEFINED, value=None):
        self.ctype = ctype
        self.value = value
        self.index = None


class ConstantTable:
    def __init__(self):
        self.table = {
            ECONSTANT.Utf8: {},
            ECONSTANT.Int: {},
            ECONSTANT.Float: {},
            ECONSTANT.String: {},
            ECONSTANT.NameAndType: {},
            ECONSTANT.Class: {},
            ECONSTANT.Fieldref: {},
            ECONSTANT.Methodref: {}
        }
        self.length = 0

    def add(self, const: ConstantElement):
        table = self.table[const.ctype]
        el = table.get(str(const.value))
        if el is not None:
            if el.ctype != const.ctype:
                raise BaseException("Adding in constants table constant already in table with another type")
            return el.index
        const.index = self.length
        table[str(const.value)] = const
        self.length += 1
        return const.index

    def __len__(self):
        return self.length

    def print_table(self):
        pass


def convert():
    pass


def create_table(prog):
    table = ConstantTable()

    __procces(prog, table)
    return table


def call_procces(node, name, table):
    __procces(getattr(node, name, None), table)


def table_create_node(node, table):
    if node.type.value == ExprType.ET_ID.value:
        const = ConstantElement(ECONSTANT.Utf8, node.stringVal)
        index = table.add(const)
        node.constant_index = index
        # return
    elif node.type.value == ExprType.ET_INT.value:
        const = ConstantElement(ECONSTANT.Int, node.intVal)
        const.int_as_str = str(node.intVal)
        index = table.add(const)
        node.constant_index = index
        # return
    elif node.type.value == ExprType.ET_FLOAT.value:
        const = ConstantElement(ECONSTANT.Float, node.floatVal)
        const.float_as_str = str(node.floatVal)
        index = table.add(const)
        node.constant_index = index
        # return
    elif node.type.value == ExprType.ET_STRING.value:
        const = ConstantElement(ECONSTANT.Utf8, node.stringVal)
        index = table.add(const)
        const = ConstantElement(ECONSTANT.String, [index])
        index = table.add(const)
        node.constant_index = index
        # return


def __procces(node, table):
    if node is None:
        return




    call = lambda name: call_procces(node, name, table)
    # LIST
    call("stmt")
    call("expr")
    call("nextEl")

    # EXPR
    call("left")
    call("right")
    call("middle")
    call("list")
    call("identifier")

    # STMT
    # call("expr")
    call("firstSuite")
    call("secondSuite")
    call("thirdSuite")
    call("stmtList")
    call("identifier")
