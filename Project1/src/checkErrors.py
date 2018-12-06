

file = open("errors.txt", mode='w')


def find_and_output_errors(program):
    count_errors = 0
    root = program
    count_errors = root.find_and_output_errors(count_errors, file, 0)

    if count_errors == 0:
        return True
    else:
        return False
