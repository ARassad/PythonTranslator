from builtins import bytearray

import Classes as cl
from Enums import *
from Enums import ExprType, ListType, StmtType
import uuid
import ConvertFunction as cf
from ConstantTable import *


def start_generation(root, table=None):
    if root.type != ListType.LT_STATEMENT_LIST or table is None:
        raise AttributeError()
    code = bytearray()
    offset = 0
    nextEl = root
    while nextEl != None:
        c, o = generate_code(nextEl.stmt, table)
        code.extend(c)
        offset += o
        nextEl = nextEl.nextEl
    return code, offset


def generate_code(rootNext, table: ConstantTable, code=None, rootPrev=None):
    return gen_functions[rootNext.type](rootNext, table)


def generate_func_call(root, table, code=None):
    if root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == '<int>':
        code, offset = new_int(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == '<float>':
        code, offset = new_float(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == '<str>':
        code, offset = new_string(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == '<None>':
        code, offset = new_none(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == 'str':
        code, offset = cast_to_str(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == 'int':
        code, offset = cast_to_int(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == 'float':
        code, offset = cast_to_float(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == 'bool':
        code, offset = cast_to_bool(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == 'print':
        code, offset = generate_print(root, table)
    elif root.type.value == ExprType.ET_FUNC_CALL.value and root.left.stringVal == 'input':
        code, offset = generate_input(root, table)
    else:
        code, offset = generate_custom_function_call(root, table)
    return code, offset


def generate_call_from_dot(root, table, code=None):
    if root.right.type.value == ExprType.ET_FUNC_CALL.value and root.right.left.stringVal == 'append':
        code, offset = generate_append(root, table)
    else:
        raise Exception("TO4KY NELZA")
    return code, offset


def generate_square(root, table, code=None):
    if True or root.list.type.value == ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS.value:
        code, offset = new_array(root, table)
    else:
        raise Exception("Unexpected square!!!")
    return code, offset


def generate_assign(root, table: ConstantTable, code=None):
    return gen_setAttr(root, table)


def new_int(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    # new
    code += b"\xBB"
    code.extend(table.add_Class("std/__PyInteger").to_bytes(2, "big"))
    # dup
    code += b"\x59"
    # ldc
    code += ldc_w(table.add_int(root.list.expr.intVal))
    # invokeSpecial
    code += b"\xB7"
    code.extend(table.add_MethodRef("std/__PyInteger", "<init>", "(I)V").to_bytes(2, "big"))
    return code, 10


def new_float(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    # new
    code += b"\xBB"
    code.extend(table.add_Class("std/__PyFloat").to_bytes(2, "big"))
    # dup
    code += b"\x59"
    # ldc
    code += ldc_w(table.add_float(root.list.expr.floatVal))
    # invokeSpecial
    code += b"\xB7"
    code.extend(table.add_MethodRef("std/__PyFloat", "<init>", "(F)V").to_bytes(2, "big"))
    return code, 10


def new_string(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    # new
    code += b"\xBB"
    code.extend(table.add_Class("std/__PyString").to_bytes(2, "big"))
    # dup
    code += b"\x59"
    # ldc
    code += ldc_w(table.add_string(root.list.expr.stringVal))
    # invokeSpecial
    code += b"\xB7"
    code.extend(table.add_MethodRef("std/__PyString", "<init>", "(Ljava/lang/String;)V").to_bytes(2, "big"))
    return code, 10


def new_array(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()
    # new
    my_code += b"\xBB"
    my_code.extend(table.add_Class("std/__PyList").to_bytes(2, "big"))

    # dup
    my_code += b"\x59"

    # invokeSpecial
    my_code += b"\xB7"
    my_code.extend(table.add_MethodRef("std/__PyList", "<init>", "()V").to_bytes(2, "big"))

    cur = root.list
    while cur is not None and cur.expr is not None:
        c, o = generate_code(cur.expr, table)
        my_code += c
        my_code += invoke_virtual(
            table.add_MethodRef("std/__PyGenericObject", "append", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))
        cur = cur.nextEl

    code += my_code
    return code, len(my_code)


def generate_append(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right.list.expr, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "append", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def new_none(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    # new
    code += b"\xBB"
    code.extend(table.add_Class("std/__PyNone").to_bytes(2, "big"))
    # dup
    code += b"\x59"
    # invokeSpecial
    code += b"\xB7"
    code.extend(table.add_MethodRef("std/__PyNone", "<init>", "()V").to_bytes(2, "big"))
    return code, 7


def gen_setAttr(root, table: ConstantTable, code=None, inAssignSeq=False):
    if code is None:
        code = bytearray()
    # aload 0
    code += b'\x19\x00'
    # ldc1
    code += ldc_w(table.add_string(root.left.stringVal))

    c, offset = generate_code(root.right, table)
    code.extend(c)

    # invokeVirtual
    code += b"\xB6"
    code.extend(table.add_MethodRef("std/__PyGenericObject", "__setattr__", "(Ljava/lang/String;Lstd/__PyGenericObject;)Lstd/__PyGenericObject;").to_bytes(2, "big"))

    # pop
    if not inAssignSeq:
        code += b"\x57"
        offset += 1
    offset += 8
    return code, offset


def gen_return(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    c, o = generate_code(root.expr, table)
    code += c
    code += b'\xB0'
    return code, o + 1


def generate_getattr(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()
    my_code += aload(int(0))
    my_code += ldc_w(table.add_string(root.stringVal))
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__getattr__", "(Ljava/lang/String;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_add(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__add__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_minus(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__sub__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_pow(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__pow__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_mul(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__mul__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_div(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__truediv__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_array_appeal(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__getitem__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_array_setter(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.middle, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__replaceitem", "(Lstd/__PyGenericObject;Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_equal(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__eq__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_not_equal(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__ne__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_less(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__lt__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_less_equal(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__le__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_great(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__gt__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_great_eq(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c
    c, o = generate_code(root.right, table)
    my_code += c

    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__ge__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def cast_to_str(root, table: ConstantTable, code=None):
    if root.list.nextEl is not None:
        raise Exception("Cast to string get only one argument!!!")
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, offset = generate_code(root.list.expr, table)
    my_code.extend(c)

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__str__", "()Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def cast_to_int(root, table: ConstantTable, code=None):
    if root.list.nextEl is not None:
        raise Exception("Cast to int get only one argument!!!")
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, offset = generate_code(root.list.expr, table)
    my_code.extend(c)

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__int__", "()Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_uminus(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, offset = generate_code(root.left, table)
    my_code.extend(c)

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__neg__", "()Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def cast_to_float(root, table: ConstantTable, code=None):
    if root.list.nextEl is not None:
        raise Exception("Cast to float get only one argument!!!")
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, offset = generate_code(root.list.expr, table)
    my_code.extend(c)

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__float__", "()Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def cast_to_bool(root, table: ConstantTable, code=None):
    if root.list.nextEl is not None:
        raise Exception("Cast to bool get only one argument!!!")
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, offset = generate_code(root.list.expr, table)
    my_code.extend(c)

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__bool__", "()Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_function_definition(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    # aload 0
    my_code += aload(int(0))

    # ldc1
    my_code += ldc_w(table.add_string(root.identifier.stringVal))

    my_code += new_obj(table.add_Class("std/" + root.func_class_name))

    # dup
    my_code += b"\x59"


    # invokeSpecial
    my_code += b"\xB7"
    my_code.extend(table.add_MethodRef("std/" + root.func_class_name, "<init>", "()V").to_bytes(2, "big"))

    # # dup2_x1
    # my_code += b"\x5D"
    # # dup2_x1
    # my_code += b"\x5D"
    # # pop
    # my_code += b"\x57"

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__setattr__", "(Ljava/lang/String;Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    # pop
    my_code += b"\x57"
    #
    #my_code += dup()

    my_code += aload(int(0))
    my_code += ldc_w(table.add_string(root.identifier.stringVal))
    my_code += invoke_virtual(
        table.add_MethodRef("std/__PyGenericObject", "__getattr__", "(Ljava/lang/String;)Lstd/__PyGenericObject;"))

    my_code += get_field(table.add_FieldRef("std/__PyObject", "__dir__", "Ljava/util/HashMap;"))

    my_code += aload(int(0))

    my_code += get_field(table.add_FieldRef("std/__PyObject", "__dir__", "Ljava/util/HashMap;"))

    my_code += invoke_virtual(table.add_MethodRef("java/util/HashMap", "putAll", "(Ljava/util/Map;)V"))

    # my_code += b"\x57"
    # my_code += b"\x57"

    code += my_code
    return code, len(my_code)


def generate_custom_function_call(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    my_code = bytearray()

    c, o = generate_code(root.left, table)
    my_code += c



    numParams = 0
    cur = root.list
    while cur is not None and root.list.type.value != ListType.LT_UNDEFINED.value:
        c, o = generate_code(cur.expr, table)
        my_code += c
        numParams += 1
        cur = cur.nextEl

    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__call__", "({})Lstd/__PyGenericObject;".format("Lstd/__PyGenericObject;" * numParams)))

    code += my_code
    return code, len(my_code)


def generate_print(root, table: ConstantTable, code=None):
    if root.list.nextEl is not None:
        raise Exception("Print function get only one argument!!!")
    if code is None:
        code = bytearray()
    my_code = bytearray()

    my_code += aload(int(0))

    c, offset = generate_code(root.list.expr, table)
    my_code.extend(c)

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__print__", "(Lstd/__PyGenericObject;)Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


def generate_input(root, table: ConstantTable, code=None):
    if root.list.nextEl is not None:
        raise Exception("Print function get only one argument!!!")
    if code is None:
        code = bytearray()
    my_code = bytearray()

    my_code += aload(int(0))

    # invokeVirtual
    my_code += invoke_virtual(table.add_MethodRef("std/__PyGenericObject", "__input__", "()Lstd/__PyGenericObject;"))

    code += my_code
    return code, len(my_code)


gen_functions = {
    ExprType.ET_FUNC_CALL: generate_func_call,
    ExprType.ET_ASSIGN: generate_assign,
    StmtType.ST_EXPRESSION: lambda x, y: generate_code(x.expr, y),
    StmtType.ST_RETURN: gen_return,
    ExprType.ET_ID: generate_getattr,
    ExprType.ET_PLUS: generate_add,
    ExprType.ET_MINUS: generate_minus,
    ExprType.ET_MULT: generate_mul,
    ExprType.ET_DIV: generate_div,
    ExprType.ET_EQUAL: generate_equal,
    ExprType.ET_NOT_EQUAL: generate_not_equal,
    ExprType.ET_LESSER: generate_less,
    ExprType.ET_LESSER_EQUAL: generate_less_equal,
    ExprType.ET_GREATER: generate_great,
    ExprType.ET_GREATER_EQUAL: generate_great_eq,
    StmtType.ST_FUNCTION_DEF: generate_function_definition,
    ExprType.ET_NONE: new_none,
    ExprType.ET_POW: generate_pow,
    ExprType.ET_SQUARE_BRACKETS: generate_square,
    ExprType.ET_DOT: generate_call_from_dot,
    ExprType.ET_ARRAY_APPEAL: generate_array_appeal,
    ExprType.ET_SQUARE_BRACKETS_ASSIGN: generate_array_setter,
    ExprType.ET_UMINUS: generate_uminus
}


def ldc_w(indexConst: int):
    return b'\x13' + indexConst.to_bytes(2, "big")


def aload(indexLocal: int):
    return b'\x19' + indexLocal.to_bytes(1, "big")


def invoke_virtual(indexMeth: int):
    return b"\xB6" + indexMeth.to_bytes(2, 'big')


def new_obj(indexCl: int):
    return b"\xBB" + indexCl.to_bytes(2, 'big')


def dup():
    return b"\x59"


def get_field(indexF: int):
    return b'\xB4' + indexF.to_bytes(2, 'big')


def pop():
    return b"\x57"
