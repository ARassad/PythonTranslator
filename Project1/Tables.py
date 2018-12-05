import fileReader as fr
import printGraph as pg
import Classes as cl
import Enums as en
from Project1.ConstantTable import create_table


if __name__ == "__main__":
    fr.read_graph()
    prog = fr.program
    prog.convert()
    const_table = create_table(prog)
    pg.print_program(prog)

pass