from Classes import *
from Enums import *
import src.fileReader as fr
import src.printGraph as pg
import src.checkErrors as check
import src.convert as conv
from ConstantTable import convert_tree, create_tables
import os
from subprocess import Popen


class Func_Class:
    def __init__(self, root):
        self.root = root


def generate_classes_for_function(root: STMT, dir_with_std_classes: str, dir_output: str):
    funcs = __get_all_func_def(root)

    __generate_PyGenericObject(funcs, root.constant_table, dir_with_std_classes, dir_output)
    pass


def __get_all_func_def(root: STMT):
    funcs = []

    def call(node, name, funcs):
        atr = getattr(node, name, None)
        if atr is not None:
            procces(atr, funcs)

    def procces(node, funcs):
        if node.type.value == StmtType.ST_FUNCTION_DEF.value:
            funcs.append(Func_Class(node))

        # LIST
        call(node, "stmt", funcs)
        call(node, "nextEl", funcs)

        # STMT, LIST
        call(node, "expr", funcs)

        # EXPR
        call(node, "left", funcs)
        call(node, "right", funcs)
        call(node, "middle", funcs)
        call(node, "list", funcs)
        call(node, "identifier", funcs)

        # STMT
        call(node, "firstSuite", funcs)
        call(node, "secondSuite", funcs)
        call(node, "thirdSuite", funcs)
        call(node, "stmtList", funcs)
        call(node, "identifier", funcs)

    procces(root, funcs);
    return funcs


def __generate_PyGenericObject(funcs, const_table, dir_with_std_classes, dir_output):
    class_file = bytearray()
    with open(dir_with_std_classes + '\\__PyGenericObject.class', 'rb') as base:
        class_file.extend(base.read(8))
        base_const_count = int.from_bytes(base.read(2), byteorder='big')
        const_count = base_const_count + len(const_table)
        class_file.extend(const_count.to_bytes(2, 'big'))

        base_const_table = base.read(4016 - 2)
        res_table = bytearray()
        res_table.extend(base_const_table)
        res_table.extend(const_table.to_string(base_const_count))
        class_file.extend(res_table)

        basement = base.read()
        class_file.extend(basement)

    if not os.path.exists(dir_output):
        os.makedirs(dir_output)
    with open(dir_output + '\\__PyGenericObject.class', 'wb') as f:
        f.write(class_file)


if __name__ == "__main__":
    fr.read_graph("../tree_to_python.txt")
    prog = fr.program

    check.find_and_output_errors(prog)
    conv.convert(prog)
    prog = convert_tree(prog)
    create_tables(prog)

    generate_classes_for_function(prog, "D:\\Translator\\PythonTranslator\\Project1\\rtl\\build\\classes\\std", "D:\\Translator\\PythonTranslator\\Project1\\rtl\\build\\classes\\std\\Gen")

    pg.print_program(prog)

    p = Popen(r"SemanticTreeImage.bat", cwd=r".\.")
    stdout, stderr = p.communicate()
