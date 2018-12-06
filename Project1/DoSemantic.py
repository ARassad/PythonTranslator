import src.fileReader as fr
import src.printGraph as pg
import src.checkErrors as check
import src.convert as conv
from src.ConstantTable import create_table
import os
from subprocess import Popen


if __name__ == "__main__":
    fr.read_graph()
    prog = fr.program
    check.find_and_output_errors(prog)
    conv.convert(prog)
    const_table = create_table(prog)
    pg.print_program(prog)

    p = Popen(r"SemanticTreeImage.bat", cwd=r"D:\UNIVER\Translator\tmp\PythonTranslator\Project1\\")
    stdout, stderr = p.communicate()
