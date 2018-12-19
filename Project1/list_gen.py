from src.Enums import ListType
import conditionGenerator as cg


def generate_list(list, progr_text, count_nodes):
    if list.type.value == ListType.LT_STATEMENT_LIST.value:
        cg.generate_statement(list.stmt, progr_text, 0)

    if list.nextEl is not None:
        generate_list(list.nextEl, progr_text, 0)
