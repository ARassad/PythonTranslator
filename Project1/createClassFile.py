import conditionGenerator as da
import sys
writefile = open("___________MAINCLASS_______________.class", mode="wb")


def create_magical_number():
    text = b'\xCA\xFE\xBA\xBE'
    writefile.write(bytes(text))
    return text


def create_version():
    text = b'\x00\x00\x00\x34'
    writefile.write(text)
    return text


def print_constant_table():
    prog = da.doAll()
    num = len(prog.constant_table) + 1
    text = str(num).encode('ansi')
    writefile.write(bytes(text))
    index = 0
    constant_table = prog.constant_table.table
    i = 0
    j = 0
    for constant_list in constant_table.values():
        if len(constant_list) is 0:
            break
        for constant in constant_list.values():
            text = bytes(str(constant.ctype).encode('ansi'))
            text += bytes(str(sys.getsizeof(constant.value)).encode('ansi'))
            writefile.write(text)


def print_access_flags():
    text = '\x02'
    writefile.write(bytes(text.encode('ansi')))


if __name__ == '__main__':
    create_magical_number()
    create_version()
    print_constant_table()
    print_access_flags()


