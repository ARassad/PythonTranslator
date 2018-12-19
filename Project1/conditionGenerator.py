import src.fileReader as fr
import src.printGraph as pg
import src.checkErrors as check
import src.convert as conv
from src.Enums import ExprType
from src.Enums import StmtType
from src.Enums import ListType
from ConstantTable import convert_tree, create_tables
import list_gen as lg
import os
from subprocess import Popen

# progr_text = ""
if __name__ == "__main__":
    fr.read_graph()
    prog = fr.program

    check.find_and_output_errors(prog)
    conv.convert(prog)
    prog = convert_tree(prog)
    create_tables(prog)
    test = ""
    lg.generate_list(prog, test, 0)
    pg.print_program(prog)


def generate_condition(stmt, progr_text, count_nodes):
    # Вставить левый операнд
    # Вставить правый операнд

    first_suite_text, count_nodes = lg.generate_list(stmt.firstSuite, progr_text, 0)

    # Это скорее всего не надо, но надо подумать
    # if stmt.stmtList is not None:
    #   count_nodes += find_list_end(stmt.stmtList, count_nodes)
    # if stmt.secondSuite is not None:
    #    count_nodes += find_list_end(stmt.secondSuite, count_nodes)

    if stmt.expr.type.value == ExprType.ET_LESSER.value:
        progr_text += '\xA2 ' + str(count_nodes)
    if stmt.expr.type.value == ExprType.ET_GREATER.value:
        progr_text += '\xA4 ' + str(count_nodes)
    if stmt.expr.type.value == ExprType.ET_EQUAL.value:
        progr_text += '\xA0 ' + str(count_nodes)
    if stmt.expr.type.value == ExprType.ET_NOT_EQUAL.value:
        progr_text += '\x9F ' + str(count_nodes)
    if stmt.expr.type.value == ExprType.ET_ID.value:
        progr_text += '\xA0 '
    count_nodes += 1

    progr_text += first_suite_text

    lg.generate_list(stmt.firstSuite, progr_text, 0)
    if stmt.stmtList is not None:
        lg.generate_list(stmt.stmtList, progr_text, 0)
    if stmt.stmtList is not None:
        lg.generate_list(stmt.stmtList, progr_text, 0)


def find_list_end(list, count_nodes):
    if list.type == ListType.LT_UNDEFINED:
        pass
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
    if expr.type == ExprType.ET_ID:
        return count_nodes + 1
    if expr.list is not None:
        count_nodes = find_list_end(expr.list, count_nodes)
    if expr.left is not None:
        count_nodes = find_expr_end(expr.left, count_nodes)
    if expr.right is not None:
        count_nodes = find_expr_end(expr.left, count_nodes)
    return count_nodes + 1


def generate_statement(stmt, progr_text, count_nodes):
    if stmt.type.value == StmtType.ST_CONDITION.value:
        generate_condition(stmt, progr_text, count_nodes)
    pass








