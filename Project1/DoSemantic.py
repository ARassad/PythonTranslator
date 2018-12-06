import fileReader as fr
import printGraph as pg
import checkErrors as check
import convert as conv
import Classes as cl
import Enums as en
from ConstantTable import create_table


if __name__ == "__main__":
    fr.read_graph()
    prog = fr.program
    check.find_and_output_errors(prog)
    conv.convert(prog)
    const_table = create_table(prog)
    pg.print_program(prog)

pass