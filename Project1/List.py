import Classes
from Enums import ListType
from Enums import StmtType
forbiddenLists = {ListType.LT_EXPR_ID_AS_LIST, ListType.LT_EXPR_WITH, ListType.LT_UNDEFINED}


class List:
    def __init__(self):
        self.stmt = None
        self.expr = None
        self.nextEl = None
        self.type = ListType.LT_UNDEFINED

    def read_list(self, index, last, text):
        i = index + 1

        if text[i] == "LT_ELEMENT":
            self.type = ListType.LT_ELEMENT
            if text[i + 1] == "Statement":
                self.stmt = Classes.STMT()
                i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
            else:
                self.expr = Classes.EXPR()
                i = self.expr.read_expr(i + 2, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_ARRAY_INITIAL_ARGUMENTS":
            self.type = ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS
            self.expr = Classes.EXPR()
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_FUNCTION_PARAMS":
            self.type = ListType.LT_EXPR_FUNCTION_PARAMS
            self.expr = Classes.EXPR()
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_IDENTIFIERS_E":
            self.type = ListType.LT_EXPR_IDENTIFIERS_E
            self.expr = Classes.EXPR()
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_STATEMENT_LIST":
            self.type = ListType.LT_STATEMENT_LIST
            self.stmt = Classes.STMT()
            i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
        elif text[i] == "LT_STMT_ELIF_LIST":
            self.type = ListType.LT_STMT_ELIF_LIST
            self.stmt = Classes.STMT()
            i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
        elif text[i] == "LT_STMT_EXCEPT_LIST":
            self.type = ListType.LT_STMT_EXCEPT_LIST
            self.stmt = Classes.STMT()
            i = self.stmt.read_stmt(i + 2, int(text[i + 2]), text=text)
        elif text[i] == "LT_EXPR_ID_AS_LIST":
            self.type = ListType.LT_EXPR_ID_AS_LIST
            self.stmt = Classes.EXPR()
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        elif text[i] == "LT_EXPR_WITH":
            self.type = ListType.LT_EXPR_WITH
            self.stmt = Classes.EXPR()
            i = self.expr.read_expr(i + 1, int(text[i + 1]), text=text)
        if text[i + 1] == "List":
            self.nextEl = List()
            i = self.nextEl.read_list(i + 2, int(text[i + 2]), text=text)
        return i + 1

    def write(self, writefile, max_id, parent_id):
        max_id += 1
        cur_id = max_id
        if self.type == ListType.LT_UNDEFINED:
            pass
        elif self.type == ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS:
            writefile.write(str(cur_id) + '[label = \"ARRAY_ARGUMENTS\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) +'\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == ListType.LT_EXPR_FUNCTION_PARAMS:
            writefile.write(str(cur_id) + '[label = \"EXPR_FUNCTION_PARAMS_list\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == ListType.LT_EXPR_IDENTIFIERS_E:
            writefile.write(str(cur_id) + '[label = \"identifiers_e\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == ListType.LT_STATEMENT_LIST:
            writefile.write(str(cur_id) + '[label = \"stmt_list\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.stmt.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == ListType.LT_STMT_ELIF_LIST:
            writefile.write(str(cur_id) + '[label = \"elif_stmt_list\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.stmt.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == ListType.LT_STMT_EXCEPT_LIST:
            writefile.write(str(cur_id) + '[label = \"except_stmt_list\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.stmt.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == ListType.LT_EXPR_ID_AS_LIST:
            writefile.write(str(cur_id) + '[label = \"list_id\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        elif self.type == ListType.LT_EXPR_WITH:
            writefile.write(str(cur_id) + '[label = \"list_with\"]\n')
            writefile.write(str(parent_id) + '--' + str(cur_id) + '\n')
            max_id = self.expr.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        else:
            pass
        if isinstance(self.nextEl, List) and self.nextEl.type != ListType.LT_UNDEFINED:
            max_id = self.nextEl.write(writefile=writefile, max_id=max_id, parent_id=cur_id)
        return max_id

    def find_and_output_errors(self, count_errors, file, pos_return):
        if self.type in forbiddenLists:
            count_errors += 1
            file.write('Ошибка для списка! ' + str(self.type) + ' Такой список не поддерживается\n')
            return count_errors
        else:
            if self.type == ListType.LT_EXPR_ARRAY_INITIAL_ARGUMENTS:
                count_errors = self.expr.find_and_output_errors(count_errors, file)
            elif self.type == ListType.LT_EXPR_FUNCTION_PARAMS:
                count_errors = self.expr.find_and_output_errors(count_errors, file)
            elif self.type == ListType.LT_EXPR_IDENTIFIERS_E:
                count_errors = self.expr.find_and_output_errors(count_errors, file)
            elif self.type == ListType.LT_STATEMENT_LIST:
                count_errors = self.stmt.find_and_output_errors(count_errors, file)
            elif self.type == ListType.LT_STMT_ELIF_LIST:
                count_errors = self.stmt.find_and_output_errors(count_errors, file)
            elif self.type == ListType.LT_STMT_EXCEPT_LIST:
                count_errors = self.stmt.find_and_output_errors(count_errors, file)
            else:
                pass
            if self.stmt is not None and self.stmt.type.value == StmtType.ST_RETURN.value:
                if pos_return == 0:
                    count_errors += 1
                    return count_errors
            if isinstance(self.nextEl, List) and self.nextEl.type != ListType.LT_UNDEFINED:
                count_errors = self.nextEl.find_and_output_errors(count_errors, file,pos_return)
            return count_errors



