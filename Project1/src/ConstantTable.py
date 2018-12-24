import Classes as cl
import Enums as en
from Enums import ExprType, ListType, StmtType
import uuid
import ConvertFunction as cf


def convert_tree(root):

    root = cf.create_main_class(root)

    return root


OBJECT_NAME = "<__PyObject>"


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
    Double = 6
    InvokeDynamic = 18
    MethodType = 16


class ConstantElement:
    def __init__(self, ctype=ECONSTANT.UNDEFINED, value=None):
        self.ctype = ctype
        self.value = value
        self.index = None

    def to_bytes(self, offset=0):
        bs = bytearray()
        bs.extend(self.ctype.to_bytes(1, "big"))
        if self.ctype in [ECONSTANT.Class, ECONSTANT.String, ECONSTANT.MethodType]:
            bs.extend((self.value[0] + offset).to_bytes(2, "big"))
        elif self.ctype in [ECONSTANT.Fieldref, ECONSTANT.Methodref, ECONSTANT.NameAndType, ECONSTANT.InvokeDynamic]:
            bs.extend((self.value[0] + offset).to_bytes(2, "big"))
            bs.extend((self.value[1] + offset).to_bytes(2, "big"))
        elif self.ctype in [ECONSTANT.Int, ECONSTANT.Float]:
            bs.extend(self.value.to_bytes(4, "big"))
        elif self.ctype in [ECONSTANT.Utf8]:
            bs.extend(len(self.value).to_bytes(2, "big"))
            bs.extend(bytes(self.value, 'utf-8'))

        return bs


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

    def to_string(self, offset=0):
        allC = []
        for v in self.table.values():
            allC.extend(v.values())
        allC.sort(key=lambda x: x.index)
        bs = bytearray()
        for c in allC:
            bs.extend(c.to_bytes(offset))
        return bs


def convert():
    pass


def create_tables(prog):
    table = ConstantTable()

    __procces(prog, table, [table_create_node])

    prog.constant_table = table
    return table


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
    elif node.type.value == StmtType.ST_FUNCTION_DEF.value:
        # Class for function
        class_name = ConstantElement(ECONSTANT.Utf8, "{}_{}".format(node.identifier.stringVal, str(uuid.uuid1())))
        index = table.add(class_name)
        class_const = ConstantElement(ECONSTANT.Class, [index])
        class_index = table.add(class_const)

        # Name and Type
        func_name = ConstantElement(ECONSTANT.Utf8, node.identifier.stringVal)
        func_name_index = table.add(func_name)

        descripter = get_func_descripter(node)
        descripter_name = ConstantElement(ECONSTANT.Utf8, descripter)
        descripter_index = table.add(descripter_name)

        name_and_type = ConstantElement(ECONSTANT.NameAndType, [func_name_index, descripter_index])
        nat_index = table.add(name_and_type)

        # Method Ref
        method_ref = ConstantElement(ECONSTANT.Methodref, [class_index, nat_index])
        node.constant_index = table.add(method_ref)


def get_func_descripter(func_node):
    num_params = 0
    param = func_node.stmtList
    while param is not None:
        num_params += 1
        param = param.nextEl
    return "({})L<{}>;".format('L<{}>;'.format(OBJECT_NAME)*num_params, OBJECT_NAME)


def __procces(node, table, handlers):
    if node is None:
        return

    for h in handlers:
        h(node, table)

    call = lambda name: __procces(getattr(node, name, None), table, handlers)

    # LIST
    call("stmt")
    call("nextEl")

    # STMT, LIST
    call("expr")

    # EXPR
    call("left")
    call("right")
    call("middle")
    call("list")
    call("identifier")

    # STMT
    call("firstSuite")
    call("secondSuite")
    call("thirdSuite")
    call("stmtList")
    call("identifier")
