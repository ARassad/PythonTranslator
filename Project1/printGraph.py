import List
from Enums import ListType
from Enums import StmtType
from Enums import ExprType
import Classes

writefile = open("graph.txt", mode="w")


def print_program(program):
    root = program
    writefile.write('graph resultGraph\n{\n')
    current_id = 1
    max_id = 1
    writefile.write(str(max_id) + '[label = \"program\"]\n')
    root.write(writefile=writefile, max_id=max_id, parent_id=current_id)
    writefile.write('}')



