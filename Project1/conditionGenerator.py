import src.fileReader as fr
import src.printGraph as pg
import src.checkErrors as check
import src.convert as conv
from src.Enums import ExprType
from src.Enums import StmtType
from src.Enums import ListType
from ConstantTable import convert_tree, create_tables
import os
from subprocess import Popen

progr_text = ""
if __name__ == "__main__":
    fr.read_graph()
    prog = fr.program

    check.find_and_output_errors(prog)
    conv.convert(prog)
    prog = convert_tree(prog)
    create_tables(prog)

    pg.print_program(prog)


def generate_condition(stmt, progr_text, count_nodes):
    # Вставить левый операнд
    # Вставить правый операнд
    count_nodes = find_list_end(stmt.firstSuite, 0)

    # Это скорее всего не надо, но надо подумать
    # if stmt.stmtList is not None:
    #   count_nodes += find_list_end(stmt.stmtList, count_nodes)
    # if stmt.secondSuite is not None:
    #    count_nodes += find_list_end(stmt.secondSuite, count_nodes)

    if stmt.expr.type == ExprType.ET_LESSER:
        progr_text += '\xA2 ' + str(count_nodes)
    if stmt.expr.type == ExprType.ET_GREATER:
        progr_text += '\xA4 ' + str(count_nodes)
    if stmt.expr.type == ExprType.ET_EQUAL:
        progr_text += '\xA0 ' + str(count_nodes)
    if stmt.expr.type == ExprType.ET_NOT_EQUAL:
        progr_text += '\x9F ' + str(count_nodes)
    if stmt.expr.type == ExprType.ET_ID:
        progr_text += '\xA0 '

    generate_list(stmt.firstSuite, progr_text, count_nodes)
    if stmt.stmtList is not None:
        generate_list(stmt.stmtList, progr_text, count_nodes)
    if stmt.stmtList is not None:
        generate_list(stmt.stmtList, progr_text, count_nodes)


def find_list_end(list, count_nodes):
    if list.type == ListType.LT_UNDEFINED:
        return 0
    elif list.stmt is not None:
        count_nodes += find_stmt_end(list.stmt, count_nodes)
    elif list.expr is not None:
        count_nodes += find_expr_end(list.expr, count_nodes)
    if list.nextEl is not None:
        find_list_end(list, count_nodes)
    return count_nodes


def find_stmt_end(stmt, count_nodes):
    if stmt.type == StmtType.ST_UNDEFINED:
        return count_nodes
    if stmt.stmtList is not None:
        count_nodes = find_list_end(stmt.stmtList, count_nodes)

    return count_nodes


def find_expr_end(expr, count_nodes):
    pass


def generate_list(list, progr_text, count_nodes):
    pass








