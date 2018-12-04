import List
program = List.List()
file = open("resultGraph2.txt", mode="r")
text = file.read().splitlines()
nextEl = program.nextEl = List.List()


def read_graph():
    i = 0
    while i < len(text):
        if text[i] == "List":
            i = program.read_list(i + 1, int(text[i+1]), text)
        elif text[i] == "Program":
            i += 1
        else:
            i += 1


if __name__ == "__main__":
    read_graph()
