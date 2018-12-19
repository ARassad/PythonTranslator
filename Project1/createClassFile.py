import conditionGenerator as da
import sys
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
def print_constant_table():
    prog = da.doAll()
    num = len(prog.constant_table) + 1
    text = bytearray(num.to_bytes(1, byteorder='big'))
    writefile.write(bytes(text))
    index = 0
    constant_table = prog.constant_table.table
    i = 0
    j = 0
    for constant_list in constant_table.values():
        if len(constant_list) is 0:
            break
        for constant in constant_list.values():
            text = bytearray(constant.ctype.to_bytes(1, byteorder='big'))
            text += bytearray(sys.getsizeof(constant.value).to_bytes(1, byteorder='big'))
            text += bytearray(index.to_bytes(1, byteorder='big'))
            writefile.write(text)


def print_access_flags():
    text = '\x02'
    writefile.write(bytes(text.encode('ansi')))


def print_class():
    # Здесь надо напечать номер константы с именем класса с типом CONSTANT CLASS
    text = bytearray(int(1).to_bytes(1, byteorder='big'))
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
def print_methods():
    text = bytearray(int(0).to_bytes(1, byteorder='big'))
    writefile.write(text)


if __name__ == '__main__':
    create_magical_number()
    create_version()
    print_constant_table()
    print_access_flags()
    print_class()
    print_parent()
    print_count_interfaces()
    print_fields()
    print_methods()


