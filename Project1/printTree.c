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
	if (list != NULL)
	{
		switch (list->type)
		{
		case LT_UNDEFINED:
		{
			break;
		}

		case LT_ELEMENT:
		{
			printf("%d [label = \"List_Element\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			if (list->stmt_value != NULL)
				printStmt(currentId, list->stmt_value, maxId);
			else if (list->expr_value != NULL)
			{
				printExpr(currentId, list->expr_value, maxId);
			}
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_ARRAY_INITIAL_ARGUMENTS:
		{
			printf("%d [label = \"ARRAY_ARGUMENTS\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Expression* expr = list->expr_value;
			printExpr(currentId, expr, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_FUNCTION_PARAMS:
		{
			printf("%d [label = \"EXPR_FUNCTION_PARAMS_list\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Expression* expr = list->expr_value;
			printExpr(currentId, expr, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_CLASS_PARENTS:
		{
			printf("%d [label = \"CLASS_PARENTS_list\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Expression* expr = list->expr_value;
			printExpr(currentId, expr, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_STATEMENT_LIST:
		{
			printf("%d [label = \"stmt_list\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->stmt_value;
			printStmt(currentId, stmt, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_STMT_ELIF_LIST:
		{
			printf("%d [label = \"elif_stmt_list\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->stmt_value;
			printStmt(currentId, stmt, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_STMT_EXCEPT_LIST:
		{
			printf("%d [label = \"except_stmt_list\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->stmt_value;
			printStmt(currentId, stmt, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_ID_AS_LIST: {
			printf("%d [label = \"list_id\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->expr_value;
			printExpr(currentId, stmt, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_WITH: {
			printf("%d [label = \"list_with\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			struct Statement* stmt = list->expr_value;
			printExpr(currentId, stmt, maxId);
			if (list->next != NULL)
				printList(currentId, list->next, maxId);
			break;
		}
		default:
			break;
		}
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
			if(stmt ->expr!= NULL)
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
			break;
		}
		case ST_WHILE:
		{
			printf("%d [label=\"while\"]\n", currentId);
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
			break;
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
			printf("%d [label=\"try\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printList(currentId, stmt->firstSuite, maxId);
			printList(currentId, stmt->stmtList, maxId);
			printList(currentId, stmt->secondSuite, maxId);
			printList(currentId, stmt->thirdSuite, maxId);
			break;
		}
		case ST_ELIF:
		{
			printf("%d [label=\"elif\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			printList(currentId, stmt->firstSuite, maxId);
			printList(currentId, stmt->secondSuite, maxId);
			break;
		}
		case ST_EXCEPT:
		{
			printf("%d [label=\"except\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			if(stmt->firstSuite != NULL)
				printList(currentId, stmt->firstSuite, maxId);
			printList(currentId, stmt->secondSuite, maxId);
			if (stmt->expr != NULL)
				printExpr(currentId, stmt->expr, maxId);
			if (stmt->identifier != NULL)
				printExpr(currentId, stmt->identifier, maxId);
			break;
		}
		case ST_RETURN:
		{
			printf("%d [label=\"return_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			break;
		}
		case ST_RAISE:
		{
			printf("%d [label=\"raise_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			break;
		}
		case ST_BREAK:
		{
			printf("%d [label=\"break_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		case ST_CONTINUE:
		{
			printf("%d [label=\"continue_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		case ST_YIELD: 
		{
			printf("%d [label=\"yield_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			break;
		}
		case ST_ASSERT:
		{
			printf("%d [label=\"yield_stmt\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->expr, maxId);
			break;
		}
		case ST_IMPORT:
		{
			printf("%d [label=\"import\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printList(currentId, stmt->stmtList, maxId);
			break;
		}
		case ST_FROM_IMPORT:
		{
			printf("%d [label=\"from_import\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, stmt->identifier, maxId);
			if(stmt->stmtList != NULL)
				printList(currentId, stmt->stmtList, maxId);
			else
			{
				(*maxId)++;
				printf("%d [label=\"*\"]\n", (*maxId));
				printf("%d--%d\n", currentId, (*maxId));
			}
			break;
		}
		case ST_WITH:
		{
			printf("%d [label=\"from_import\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printList(currentId, stmt->firstSuite, maxId);
			printList(currentId, stmt->stmtList, maxId);
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
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_AND:
		{
			printf("%d [label = \"AND\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_NOT:
		{
			printf("%d [label = \"NOT\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
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
			printf("%d [label = \"/\"]\n", currentId);
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
			printf("%d [label = \"floor div\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_UPLUS:
		{
			printf("%d [label = \"+\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			break;
		}
		case ET_UMINUS:
		{
			printf("%d [label = \"-\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			break;
		}
		case ET_POW:
		{
			printf("%d [label = \"pow\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_DOT:
		{
			printf("%d [label = \".\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
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
			printf("%d", currentId);
			printf("[label = \"%f\"]\n", expr->floatVal);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		case ET_STRING:
		{
			printf("%d", currentId);
			printf("[label = \"%s\"]\n", expr->strVal);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		case ET_SQUARE_BRACKETS:
		{
			printf("%d [label = \"[]\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printList(currentId, expr->exprs, maxId);
			break;
		}
		case ET_ARRAY_APPEAL:
		{
			printf("%d [label = \"[]\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_ARRAY_SLICE:
		{
			printf("%d [label = \"Array_Slice\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printList(currentId, expr->left, maxId);
			printList(currentId, expr->right, maxId);
			break;
		}
		case ET_ARRAY_SLICE_ARGUMENTS:
		{
			printf("%d [label = \"Array_Slice\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printList(currentId, expr->left, maxId);
			printList(currentId, expr->middle, maxId);
			if(expr->right != NULL)
				printList(currentId, expr->right, maxId);
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
			printf("%d [label = \"array_generator\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->middle, maxId);
			if (expr->right != NULL)
				printList(currentId, expr->right, maxId);
			break;
		}
		case ET_FUNC_PARAM_DEFAULT:
		case ET_FUNC_PARAM:
		{
			printf("%d [label = \"function_params\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->identifier, maxId);
			//printExpr(currentId, expr->left, maxId);
			if (expr->left != NULL)
				printExpr(currentId, expr->left, maxId);
			break;
		}
		case ET_FUNC_CALL:
		{
			printf("%d [label = \"function_call\"]\n", currentId);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printList(currentId, expr->exprs, maxId);
			break;
		}
		case ET_BOOL:
		{
			printf("%d [label = \"bool %d\"]\n", currentId,expr->intVal);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		case ET_ID_AS:
		{
			printf("%d [label = \"ID AS\"]\n", currentId, expr->intVal);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->right, maxId);
			break;
		}
		case ET_LAMBDA:
		{
			printf("%d [label = \"Lambda\"]\n", currentId, expr->intVal);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printList(currentId, expr->exprs, maxId);
			break;
		}
		case ET_EXPR_AS:
		{
			printf("%d [label = \"expr\"]\n", currentId, expr->intVal);
			printf("%d--%d\n", parentID, currentId);
			printExpr(currentId, expr->left, maxId);
			printExpr(currentId, expr->identifier, maxId);
			break;
		}
		case ET_NONE: 
		{
			printf("%d [label = \"None\"]\n", currentId, expr->intVal);
			printf("%d--%d\n", parentID, currentId);
			break;
		}
		default:
			break;
	}
}