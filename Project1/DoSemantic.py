import src.fileReader as fr
import src.printGraph as pg
import src.checkErrors as check
import src.convert as conv
from ConstantTable import convert_tree, create_tables
import os
from subprocess import Popen


if __name__ == "__main__":
    fr.read_graph()
    prog = fr.program

    check.find_and_output_errors(prog)
    conv.convert(prog)
    prog = convert_tree(prog)
    create_tables(prog)

    pg.print_program(prog)

    p = Popen(r"SemanticTreeImage.bat", cwd=r".\.")
    stdout, stderr = p.communicate()
