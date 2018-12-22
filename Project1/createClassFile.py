import conditionGenerator as da
import sys
from ConstantTable import ECONSTANT
writefile = open("___________MAINCLASS_______________.class", mode="wb")


# Печать магического числа и версии
def create_magical_number():
    text = b'\xCA\xFE\xBA\xBE'
    writefile.write(bytes(text))
    return text


def create_version():
    text = b'\x00\x00\x00\x34'
    writefile.write(text)
    return text


# Печать таблицы констант
def print_constant_table(prog):

    num = prog.constant_table.length + 1
    text = bytearray(num.to_bytes(1, byteorder='big'))
    writefile.write(bytes(text))
    index = 0
    constant_table = prog.constant_table.table
    i = 0
    j = 0
    sorted_table = []
    for constant_list in constant_table.values():
        if len(constant_list) is 0:
            pass
        for constant in constant_list.values():
            sorted_table.append(constant)
    sorted_table.sort(key=lambda i: i.index)
    for constant in sorted_table:
        text = bytearray(constant.ctype.to_bytes(1, byteorder='big'))
        if constant.ctype == ECONSTANT.Utf8:
            text += bytearray(sys.getsizeof(constant.value).to_bytes(1, byteorder='big'))
            text += bytes(constant.value.encode('ansi'))
        elif constant.ctype == ECONSTANT.Int:
            text += bytearray(constant.value.to_bytes(1, byteorder='big'))
        elif constant.ctype == ECONSTANT.String:
            text += bytearray(constant.index.to_bytes(1, byteorder='big'))
        elif constant.ctype == ECONSTANT.Float:
            text += bytearray(constant.value.to_bytes(1, byteorder='big'))
        elif constant.ctype == ECONSTANT.NameAndType:
            text += bytearray(constant.value[0].to_bytes(1, byteorder='big')) + \
                    bytearray(constant.value[1].to_bytes(1, byteorder='big'))
        elif constant.ctype == ECONSTANT.Class:
            text += bytearray(constant.value[0].to_bytes(1, byteorder='big'))
        elif constant.ctype == ECONSTANT.Fieldref:
            text += bytearray(constant.value[0].to_bytes(1, byteorder='big')) + \
                    bytearray(constant.value[1].to_bytes(1, byteorder='big'))
        elif constant.ctype == ECONSTANT.Methodref:
            text += bytearray(constant.value[0].to_bytes(1, byteorder='big')) + \
                    bytearray(constant.value[1].to_bytes(1, byteorder='big'))
        writefile.write(text)


def print_access_flags():
    text = '\x02\x01'
    writefile.write(bytes(text.encode('ansi')))


def print_class(prog):
    # Здесь надо напечать номер константы с именем класса с типом CONSTANT CLASS

    text = int(1).to_bytes(1, byteorder='big')
    writefile.write(text)


# Здесь печатать индекс родителя из таблицы констант
def print_parent():
    text = bytearray(int(0).to_bytes(1, byteorder='big'))
    writefile.write(text)


def print_count_interfaces():
    text = bytearray(int(0).to_bytes(1, byteorder='big'))
    writefile.write(text)


# Сначала напечатать кол-во полей, потом сами методы
def print_fields():
    text = bytearray(int(0).to_bytes(1, byteorder='big'))

    writefile.write(text)


# Сначала напечатать кол-во полей, потом сами методы
def print_methods(prog):

    text = bytearray(int(1).to_bytes(1, byteorder='big'))
    writefile.write(text)


if __name__ == '__main__':
    prog = da.doAll()
    create_magical_number()
    create_version()
    print_constant_table(prog)
    print_access_flags()
    print_class(prog)
    print_parent()
    print_count_interfaces()
    print_fields()
    print_methods(prog)


