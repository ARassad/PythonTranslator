#include"printTree.h"
extern head;
void printTree()
{
	struct List* H = head;
	printf("graph resultGraph\n{\n");
	int id = 0;
	int maxId = 0;

	printf("%d [label = \"program\"]\n", id);
	printList(0, H, &maxId);
	id++;
	printf("}");
}
void printList(int parentID, struct List* list, int* maxId)
{
	(*maxId)++;
	int currentId = (*maxId);
	switch (list->type)
	{
		case LT_UNDEFINED: 
		{
			break;
		}

		case LT_ELEMENT:
		{
			break;
		}
		case LT_EXPR_ARRAY_INITIAL_ARGUMENTS:
		{
			break;
		}
		case LT_EXPR_FUNCTION_PARAMS:
		{
			printf("%d [label = \"EXPR_FUNCTION_PARAMS_list\"]\n",currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Expression* expr = list->expr_value;
			printExpr(currentId,expr,maxId);
			if(list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_CLASS_PARENTS:
		{
			break;
		}
		case LT_STATEMENT_LIST:
		{
			printf("%d [label = \"stmt_list\"]\n",currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->stmt_value;
			printStmt(currentId,stmt,maxId);
			if(list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_STMT_ELIF_LIST:
		{
			printf("%d [label = \"elif_stmt_list\"]\n",currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->stmt_value;
			printStmt(currentId,stmt,maxId);
			if(list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_STMT_EXCEPT_LIST:
		{
			printf("%d [label = \"except_stmt_list\"]\n",currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->stmt_value;
			printStmt(currentId,stmt,maxId);
			if(list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		default:
			break;
	}
}
void printStmt(int parentID, struct Statement* stmt, int* maxId)
{
	(*maxId)++;
	int currentId = (*maxId);
	switch (stmt->type) {
		case ST_UNDEFINED:
		{
			break;
		}
		case ST_EXPRESSION:
		{
			printf("%d [label=\"expr_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			break;
		}
		case ST_CONDITION:
		{
			printf("%d [label=\"if\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			if (stmt->firstSuite != NULL)
			{
				printList(currentId, stmt->firstSuite, maxId);
			}
			if (stmt->stmtList != NULL)
			{
				printList(currentId, stmt->stmtList, maxId);
			}
			if (stmt->secondSuite != NULL)
			{
				printList(currentId, stmt->secondSuite, maxId);
			}

			break;
		}
		case ST_FUNCTION_DEF:
		{
			printf("%d [label=\"def\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->identifier, maxId);
			printExpr(currentId, stmt->expr, maxId);
			printList(currentId, stmt->stmtList,maxId);
			printList(currentId, stmt->firstSuite, maxId);
			break;
		}
		case ST_CLASS_DEF:
		{
			printf("%d [label=\"class\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->identifier, maxId);
			printList(currentId, stmt->firstSuite, maxId);
			printList(currentId, stmt->stmtList, maxId);
		}
		case ST_WHILE:
		{
			printf("%d [label=\"if\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			if (stmt->firstSuite != NULL)
			{
				printList(currentId, stmt->firstSuite, maxId);
			}
			if (stmt->secondSuite != NULL)
			{
				printList(currentId, stmt->secondSuite, maxId);
			}
		}
		case ST_FOR:
		{
			printf("%d [label=\"for_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->identifier, maxId);
			printExpr(currentId, stmt->expr, maxId);
			if(stmt->firstSuite!= NULL)
				printList(currentId, stmt->firstSuite, maxId);
			if (stmt->firstSuite != NULL)
				printList(currentId, stmt->secondSuite, maxId);
			break;
		}
		case ST_TRY:
		{
			break;
		}
		case ST_WITH:
		{
			break;
		}
		case ST_ELIF_LISTS:
		{
			break;
		}
		case ST_ELIF:
		{
			break;
		}
		case ST_EXCEPT:
		{
			break;
		}
		case ST_RETURN:
		{
			printf("%d [label=\"return_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			break;
		}
	}
}
void printExpr(int parentID, struct Expression* expr, int* maxId)
{
	(*maxId)++;
	int currentId = (*maxId);
	switch (expr->type)
	{
		case ET_UNDEFINED:
		{
			break;
		}
		case ET_OR:
		{
			printf("%d [label = \"OR\"]\n",currentId);
			printf("%d--%d", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_AND:
		{
			printf("%d [label = \"AND\"]", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_NOT:
		{
			printf("%d [label = \"NOT\"]", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_IN:
		{
			printf("%d [label = \"IN\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_NOT_IN:
		{
			printf("%d [label = \"NOT IN\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_IS:
		{
			printf("%d [label = \"IS\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_IS_NOT:
		{
			printf("%d [label = \"IS NOT\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_PLUS_ASSIGN:
		{
			printf("%d [label = \"+=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_MINUS_ASSIGN:
		{
			printf("%d [label = \"-=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_MULT_ASSIGN:
		{
			printf("%d [label = \"*=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_POW_ASSIGN:
		{
			printf("%d [label = \"^=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_DIV_ASSIGN:
		{
			printf("%d [label = \"//=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_MOD_ASSIGN:
		{
			printf("%d [label = \"%=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_LESSER:
		{
			printf("%d [label = \"<\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_LESSER_EQUAL:
		{
			printf("%d [label = \"<=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_GREATER:
		{
			printf("%d [label = \">\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_GREATER_EQUAL:
		{
			printf("%d [label = \">=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_NOT_EQUAL:
		{
			printf("%d [label = \"!=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_EQUAL:
		{
			printf("%d [label = \"==\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_LEFT_SHIFT:
		{
			printf("%d [label = \"<<\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_RIGHT_SHIFT:
		{
			printf("%d [label = \">>\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_PLUS:
		{
			printf("%d [label = \"+\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_MINUS:
		{
			printf("%d [label = \"-\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_MULT:
		{
			printf("%d [label = \"*\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_DIV:
		{
			printf("%d [label = \"//\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_MOD:
		{
			printf("%d [label = \"%\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_FLOOR_DIV:
		{
			break;
		}
		case ET_UPLUS:
		{
			break;
		}
		case ET_UMINUS:
		{
			break;
		}
		case ET_POW:
		{
			break;
		}
		case ET_DOT:
		{
			break;
		}
		case ET_PARENTHNESES:
		{
			break;
		}
		case ET_ID:
		{
			printf("%d", currentId);
			printf("[label = \"%s\"]\n", expr->strVal);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		case ET_INT:
		{
			printf("%d", currentId);
			printf("[label = \"%d\"]\n", expr->intVal);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		case ET_FLOAT:
		{
			printf("%d", maxId);
			printf("[label = %f\"]\n", expr->floatVal);
			printf("%d--%d\n", parentID, maxId);
			break;
		}
		case ET_STRING:
		{
			printf("%d", maxId);
			printf("[label = \"%s\"]\n", expr->strVal);
			printf("%d--%d\n", parentID, maxId);
			break;
		}
		case ET_SQUARE_BRACKETS:
		{
			break;
		}
		case ET_ARRAY_APPEAL:
		{
			break;
		}
		case ET_ARRAY_SLICE:
		{
			break;
		}
		case ET_ARRAY_SLICE_ARGUMENTS:
		{
			break;
		}
		case ET_ASSIGN:
		{
			printf("%d [label = \"=\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_ARRAY_GENERATOR:
		{
			break;
		}
		case ET_FUNC_PARAM:
		{
			break;
		}
		case ET_FUNC_CALL:
		{
			break;
		}
		case ET_RETURN:
		{
			break;
		}
		default:
			break;
	}
}