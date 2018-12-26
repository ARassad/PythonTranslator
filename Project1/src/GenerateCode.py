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


def gen_if(root, table: ConstantTable, code=None):
    if code is None:
        code = bytearray()
    #Тут условие генерится
    param = cl.EXPR()
    param.list = cf.List()
    param.list.expr = root.expr
    c, offset = cast_to_int(param, table)
    code += c
    first_suite = root.firstSuite
    first_suite_code = bytearray()
    first_suite_offset = 0
    end_if_offset = 0
    while first_suite is not None:
        current_code, suite_offset = generate_code(first_suite.stmt, table, first_suite_code)
        first_suite_code += current_code
        first_suite_offset += suite_offset
        first_suite = first_suite.nextEl
    code += b'\x99'
    if root.secondSuite is not None or root.stmtList is not None:
        first_suite_offset += 6
    else:
        first_suite_offset += 3
    code += first_suite_offset.to_bytes(2, 'big')
    offset += first_suite_offset
    code += first_suite_code


    stmt_list = root.stmtList
    stmt_list_code = bytearray()
    while stmt_list is not None:
        current_code,suite_offset = generate_code(stmt_list.stmt, table, stmt_list_code)
        code = 1



    second_suite = root.secondSuite
    second_suite_code = bytearray()
    second_suite_offset = 0
    if root.secondSuite is not None:
        while second_suite is not None:
            current_code, suite_offset = generate_code(second_suite.stmt, table, second_suite_code)
            second_suite_code += current_code
            second_suite_offset += suite_offset
            second_suite = second_suite.nextEl
        end_if_offset += second_suite_offset + 3
        code += b'\xA7'
        code += end_if_offset.to_bytes(2, byteorder='big')
        offset += second_suite_offset
        code += second_suite_code
    return code, offset


def gen_while(root, table: ConstantTable,code=None):
    if code is None:
        code = bytearray()
    param = cl.EXPR()
    param.list = cf.List()
    param.list.expr = root.expr
    c, offset = cast_to_int(param, table)
    code += c
    first_suite = root.firstSuite
    first_suite_code = bytearray()
    first_suite_offset = 0
    offset += 3
    while first_suite is not None:
        current_code, suite_offset = generate_code(first_suite.stmt, table, first_suite_code)
        first_suite_code += current_code
        first_suite_offset += suite_offset
        first_suite = first_suite.nextEl
    first_suite_offset += 3
    first_suite_code += b'\xA7'
    first_suite_code += ((-1)*(first_suite_offset - 3 + offset)).to_bytes(2, byteorder='big', signed=True)
    code += b'\x99'
    code += (first_suite_offset + 3).to_bytes(2, byteorder='big')
    code += first_suite_code
    offset += first_suite_offset
    return code, offset


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


gen_functions = {
    ExprType.ET_FUNC_CALL: generate_func_call,
    ExprType.ET_ASSIGN: generate_assign,
    StmtType.ST_EXPRESSION: lambda x, y: generate_code(x.expr, y),
    StmtType.ST_RETURN: gen_return,
    StmtType.ST_CONDITION: gen_if,
    StmtType.ST_WHILE: gen_while,
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


}


def ldc_w(indexConst: int):
    return b'\x13' + indexConst.to_bytes(2, "big")


def aload(indexLocal: int):
    return b'\x19' + indexLocal.to_bytes(1, "big")


def invoke_virtual(indexMeth: int):
    return b"\xB6" + indexMeth.to_bytes(2, 'big')