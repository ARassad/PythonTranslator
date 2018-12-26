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


gen_functions = {
    ExprType.ET_FUNC_CALL: generate_func_call,
    ExprType.ET_ASSIGN: generate_assign,
    StmtType.ST_EXPRESSION: lambda x, y: generate_code(x.expr, y),
    StmtType.ST_RETURN: gen_return
}


def ldc_w(indexConst: int):
    return b'\x13' + indexConst.to_bytes(2, "big")