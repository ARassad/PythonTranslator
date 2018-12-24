import List
import printGraph
import checkErrors as check
import convert as conv
program = List.List()
file = None
try:
    file = open("tree_to_python.txt", mode="r")
    text = file.read().splitlines()
except:
    pass


def read_graph(filename=None):
    if filename is not None:
        global file
        file = open(filename, mode="r")
        text = file.read().splitlines()
    i = 0
    while i < len(text):
        if text[i] == "List":
            i = program.read_list(i + 1, int(text[i+1]), text)
        elif text[i] == "Program":
            i += 1
        else:
            i += 1
    file.close()


if __name__ == "__main__":
    read_graph()
    check.find_and_output_errors(program)
    conv.convert(program)
    printGraph.print_program(program)
