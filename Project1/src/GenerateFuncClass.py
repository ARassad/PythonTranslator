from Classes import *
from Enums import *
import src.fileReader as fr
import src.printGraph as pg
import src.checkErrors as check
import src.convert as conv
from ConstantTable import *
import os
from subprocess import Popen
from GenerateCode import start_generation
import uuid


class Func_Class:
    def __init__(self, root, table: ConstantTable = None, isMainClass=False):
        self.root = root
        self.table = table
        self.my_code = None
        self.this_class = None
        self.this_class = None
        self.constructor = None
        self.class_name = "MainClass" if isMainClass else root.identifier.stringVal + "_" + str(uuid.uuid1())
        self.isMainClass = isMainClass

    def empty_constructor(self):
        bs = bytearray()
        bs += b"\x00\01"
        bs += self.table.add_utf8("<init>").to_bytes(2, 'big')
        bs += self.table.add_utf8("()V").to_bytes(2, 'big')
        bs += b'\x00\x01'
        bs += self.table.add_utf8("Code").to_bytes(2, 'big')
        bs += int(17).to_bytes(4, 'big')
        bs += b'\x00\x01\x00\x01\x00\x00\x00\x05'

        # Code
        bs += b'\x2A\xB7'
        # if self.isMainClass:
        #     parent = "java/lang/Object"
        # else:
        parent = "std/__PyGenericObject"
        bs += self.table.add_MethodRef(parent, "<init>", "()V").to_bytes(2, 'big')
        bs += b'\xB1'

        bs += b'\x00\x00\x00\x00'
        return bs

    def generate_my_function(self):
        bs = bytearray()
        bs += b'\x00\x01'
        bs += self.table.add_utf8("__call__").to_bytes(2, 'big')
        numParametrs = 0
        cur = self.root.stmtList
        while cur is not None:
            numParametrs += 1
            cur = cur.nextEl
        descriptor = "({})Lstd/__PyGenericObject;".format("Lstd/__PyGenericObject;" * numParametrs)
        bs += self.table.add_utf8(descriptor).to_bytes(2, 'big')
        bs += int(2).to_bytes(2, 'big')

        code, offset = start_generation(self.root.firstSuite, self.table)

        bs += self.table.add_utf8("Code").to_bytes(2, 'big')
        code_attr = bytearray()
        code_attr += int(1000).to_bytes(2, "big")
        code_attr += int(numParametrs+1).to_bytes(2, 'big')
        code_attr += offset.to_bytes(4, "big")
        code_attr += code
        code_attr += b'\x00\x00\x00\x00'

        bs += len(code_attr).to_bytes(4, 'big')
        bs += code_attr

        # Exception
        bs += self.table.add_utf8("Exceptions").to_bytes(2, "big")
        bs += b'\x00\x00\x00\x04'
        bs += b'\x00\x01'
        bs += self.table.add_Class("java/lang/Exception").to_bytes(2, "big")
        return bs

    def generate_main_function(self):
        bs = bytearray()
        bs += b'\x00\x09'
        bs += self.table.add_utf8("main").to_bytes(2, 'big')
        bs += self.table.add_utf8("([Ljava/lang/String;)V").to_bytes(2, 'big')
        bs += int(2).to_bytes(2, 'big')

        code, offset = start_generation(self.root.firstSuite, self.table)
        code += b'\xB1'
        offset += 1

        bs += self.table.add_utf8("Code").to_bytes(2, 'big')
        code_attr = bytearray()
        code_attr += int(1000).to_bytes(2, "big")
        code_attr += int(1).to_bytes(2, 'big')
        code_attr += offset.to_bytes(4, "big")
        code_attr += code
        code_attr += b'\x00\x00\x00\x00'

        bs += len(code_attr).to_bytes(4, 'big')
        bs += code_attr

        # Exception
        bs += self.table.add_utf8("Exceptions").to_bytes(2, "big")
        bs += b'\x00\x00\x00\x04'
        bs += b'\x00\x01'
        bs += self.table.add_Class("java/lang/Exception").to_bytes(2, "big")
        return bs

    def initial_func_class(self, table=None):
        self.table = table if table is not None else self.table
        if self.table is None:
            self.table = ConstantTable()
        #self.table.add_MethodRef("std/MainClass", "main", "([Ljava/lang/String;)V")

        self.constructor = self.empty_constructor()

        # if self.isMainClass:
        #     self.my_code = self.generate_main_function()
        # else:
        self.my_code = self.generate_my_function()

    def to_class_file(self, out_dir):
        class_file = bytearray()
        class_file += b'\xCA\xFE\xBA\xBE\x00\x00\x00\x34'

        class_file_2 = bytearray()
        class_file_2 += b'\x00\x21'
        class_file_2 += self.table.add_Class("std/" + self.class_name).to_bytes(2, 'big')
        # if self.isMainClass:
        #     class_file_2 += self.table.add_Class("java/lang/Object").to_bytes(2, 'big')
        # else:
        class_file_2 += self.table.add_Class("std/__PyGenericObject").to_bytes(2, 'big')
        class_file_2 += b'\x00\x00'
        class_file_2 += b'\x00\x00'
        class_file_2 += b'\x00\x02'

        class_file_2 += self.constructor
        class_file_2 += self.my_code

        class_file_2 += b'\x00\x00'

        class_file += int(len(self.table) + 1).to_bytes(2, 'big')
        class_file += self.table.to_string()
        class_file += class_file_2

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        with open(out_dir + '\\{}.class'.format(self.class_name), 'wb') as f:
            f.write(class_file)


def generate_classes_for_function(root: STMT, dir_with_std_classes: str, dir_output: str):
    funcs = __get_all_func_def(root)
    if not hasattr(root, "constant_table"):
        root.constant_table = ConstantTable()
    for f in funcs:
        f.initial_func_class(root.constant_table)
        f.to_class_file(dir_output)

    #__generate_PyGenericObject(funcs, root.constant_table, dir_with_std_classes, dir_output)
    pass


def __get_all_func_def(root: STMT):
    funcs = []

    def call(node, name, funcs):
        atr = getattr(node, name, None)
        if atr is not None:
            procces(atr, funcs)

    def procces(node, funcs):
        if node.type.value == StmtType.ST_FUNCTION_DEF.value:
            isMainClass = node.identifier.stringVal == "<main>"
            funcs.append(Func_Class(node, isMainClass=isMainClass))

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
    #create_tables(prog)

    generate_classes_for_function(prog, "..\\rtl\\build\\classes\\std", "..\\rtl\\build\\classes\\std")

    pg.print_program(prog)

    # p = Popen(r"SemanticTreeImage.bat", cwd=r"..\.")
    # stdout, stderr = p.communicate()
