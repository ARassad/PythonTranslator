#include"printTree.h"
extern head;
void printForPython(void)
{
	struct List* H = head;
	printf("Program\n");
	int maxId = 0;
	printListPython(0,H,&maxId);
}
void printStatement(int parentID, struct Statement* stmt, int* maxId)
{
	(*maxId)++;
	int currentId = (*maxId);
	printf("Statement\n%d\n",currentId);
	switch (stmt->type) {
	case ST_UNDEFINED:
	{
		break;
	}
	case ST_EXPRESSION:
	{
		printf("ST_EXPRESSION\n");
		printExpression(currentId, stmt->expr, maxId);
		break;
	}
	case ST_CONDITION:
	{
		printf("ST_CONDITION\n", currentId);
		printExpression(currentId, stmt->expr, maxId);
		if (stmt->firstSuite != NULL)
		{
			printListPython(currentId, stmt->firstSuite, maxId);
		}
		if (stmt->stmtList != NULL)
		{
			printListPython(currentId, stmt->stmtList, maxId);
		}
		if (stmt->secondSuite != NULL)
		{
			printListPython(currentId, stmt->secondSuite, maxId);
		}

		break;
	}
	case ST_FUNCTION_DEF:
	{
		printf("ST_FUNCTION_DEF\n", currentId);
		printExpression(currentId, stmt->identifier, maxId);
		if (stmt->expr != NULL)
			printExpression(currentId, stmt->expr, maxId);
		printListPython(currentId, stmt->stmtList, maxId);
		printListPython(currentId, stmt->firstSuite, maxId);
		break;
	}
	case ST_CLASS_DEF:
	{
		printf("ST_CLASS_DEF\n", currentId);
		printExpression(currentId, stmt->identifier, maxId);
		printListPython(currentId, stmt->firstSuite, maxId);
		printListPython(currentId, stmt->stmtList, maxId);
		break;
	}
	case ST_WHILE:
	{
		printf("ST_WHILE\n", currentId);
		printExpression(currentId, stmt->expr, maxId);
		if (stmt->firstSuite != NULL)
		{
			printListPython(currentId, stmt->firstSuite, maxId);
		}
		if (stmt->secondSuite != NULL)
		{
			printListPython(currentId, stmt->secondSuite, maxId);
		}
		break;
	}
	case ST_FOR:
	{
		printf("ST_FOR\n", currentId);
		printExpression(currentId, stmt->identifier, maxId);
		printExpression(currentId, stmt->expr, maxId);
		if (stmt->firstSuite != NULL)
			printListPython(currentId, stmt->firstSuite, maxId);
		if (stmt->secondSuite != NULL)
			printListPython(currentId, stmt->secondSuite, maxId);
		break;
	}
	case ST_TRY:
	{
		printf("ST_TRY\n", currentId);
		printListPython(currentId, stmt->firstSuite, maxId);
		printListPython(currentId, stmt->stmtList, maxId);
		printListPython(currentId, stmt->secondSuite, maxId);
		printListPython(currentId, stmt->thirdSuite, maxId);
		break;
	}
	case ST_ELIF:
	{
		printf("ST_ELIF\n", currentId);
		printExpression(currentId, stmt->expr, maxId);
		printListPython(currentId, stmt->firstSuite, maxId);
		//printListPython(currentId, stmt->secondSuite, maxId);
		break;
	}
	case ST_EXCEPT:
	{
		printf("ST_EXCEPT\n", currentId);
		if (stmt->firstSuite != NULL)
			printListPython(currentId, stmt->firstSuite, maxId);
		printListPython(currentId, stmt->secondSuite, maxId);
		if (stmt->expr != NULL)
			printExpression(currentId, stmt->expr, maxId);
		if (stmt->identifier != NULL)
			printExpression(currentId, stmt->identifier, maxId);
		break;
	}
	case ST_RETURN:
	{
		printf("ST_RETURN\n", currentId);
		printExpression(currentId, stmt->expr, maxId);
		break;
	}
	case ST_RAISE:
	{
		printf("ST_RAISE\n", currentId);
		printExpression(currentId, stmt->expr, maxId);
		break;
	}
	case ST_BREAK:
	{
		printf("ST_BREAK\n", currentId);
		break;
	}
	case ST_CONTINUE:
	{
		printf("ST_CONTINUE\n", currentId);
		break;
	}
	case ST_YIELD:
	{
		printf("ST_YIELD\n", currentId);
		printExpression(currentId, stmt->expr, maxId);
		break;
	}
	case ST_ASSERT:
	{
		printf("ST_ASSERT\n", currentId);
		printExpression(currentId, stmt->expr, maxId);
		break;
	}
	case ST_IMPORT:
	{
		printf("ST_IMPORT\n", currentId);
		printListPython(currentId, stmt->stmtList, maxId);
		break;
	}
	case ST_FROM_IMPORT:
	{
		printf("ST_FROM_IMPORT\n", currentId);
		printExpression(currentId, stmt->identifier, maxId);
		if (stmt->stmtList != NULL)
			printListPython(currentId, stmt->stmtList, maxId);
		else
		{
			(*maxId)++;
			printf("*\n", (*maxId));
		}
		break;
	}
	case ST_WITH:
	{
		printf("ST_WITH\n", currentId);
		printListPython(currentId, stmt->firstSuite, maxId);
		printListPython(currentId, stmt->stmtList, maxId);
		break;
	}
	case ST_PASS:
	{
		printf("ST_PASS\n", currentId);
	}
	}
	printf("%d\n", currentId);
}
void printExpression(int parentID, struct Expression* expr, int* maxId)
{
	(*maxId)++;
	int currentId = (*maxId);
	printf("%d\n",currentId);
	switch (expr->type)
	{
	case ET_UNDEFINED:
	{
		break;
	}
	case ET_OR:
	{
		printf("ET_OR\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_AND:
	{
		printf("ET_AND\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_NOT:
	{
		printf("ET_NOT\n", currentId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_IN:
	{
		printf("ET_IN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_NOT_IN:
	{
		printf("NOT_IN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_IS:
	{
		printf("ET_IS\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_IS_NOT:
	{
		printf("ET_IS_NOT\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_PLUS_ASSIGN:
	{
		printf("ET_PLUS_ASSIGN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_MINUS_ASSIGN:
	{
		printf("ET_MINUS_ASSIGN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_MULT_ASSIGN:
	{
		printf("ET_MULT_ASSIGN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_POW_ASSIGN:
	{
		printf("ET_POW_ASSIGN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_DIV_ASSIGN:
	{
		printf("ET_DIV_ASSIGN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_MOD_ASSIGN:
	{
		printf("ET_MOD_ASSIGN\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_LESSER:
	{
		printf("ET_LESSER\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_LESSER_EQUAL:
	{
		printf("ET_LESSER_EQUAL\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_GREATER:
	{
		printf("ET_GREATER\n", currentId);
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_GREATER_EQUAL:
	{
		printf("ET_GREATER_EQUAL\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_NOT_EQUAL:
	{
		printf("ET_NOT_EQUAL\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_EQUAL:
	{
		printf("ET_EQUAL\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_LEFT_SHIFT:
	{
		printf("ET_LEFT_SHIFT\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_RIGHT_SHIFT:
	{
		printf("ET_RIGHT_SHIFT\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_PLUS:
	{
		printf("ET_PLUS\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_MINUS:
	{
		printf("ET_MINUS\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_MULT:
	{
		printf("ET_MULT\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_DIV:
	{
		printf("ET_DIV\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_MOD:
	{
		printf("ET_MOD\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_FLOOR_DIV:
	{
		printf("ET_FLOOR_DIV\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_UPLUS:
	{
		printf("ET_UPLUS\n");
		printExpression(currentId, expr->left, maxId);
		break;
	}
	case ET_UMINUS:
	{
		printf("ET_UMINUS\n");
		printExpression(currentId, expr->left, maxId);
		break;
	}
	case ET_POW:
	{
		printf("ET_POW\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_DOT:
	{
		printf("ET_DOT\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_ID:
	{
		printf("ET_ID\n%s\n", expr->strVal);
		break;
	}
	case ET_INT:
	{
		printf("ET_INT\n%d\n", expr->intVal);
		break;
	}
	case ET_FLOAT:
	{
		printf("ET_FLOAT\n%f\n", expr->floatVal);
		break;
	}
	case ET_STRING:
	{
		printf("ET_STRING\n\"%s\"\n", expr->strVal);
		break;
	}
	case ET_SQUARE_BRACKETS:
	{
		printf("ET_SQUARE_BRACKETS\n");
		printListPython(currentId, expr->exprs, maxId);
		break;
	}
	case ET_ARRAY_APPEAL:
	{
		printf("ET_ARRAY_APPEAL\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_ARRAY_SLICE:
	{
		printf("ET_ARRAY_SLICE\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_ARRAY_SLICE_ARGUMENTS:
	{
		printf("ET_ARRAY_SLICE_ARGUMENTS\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->middle, maxId);
		if (expr->right != NULL)
			printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_ASSIGN:
	{
		printf("ET_ASSIGN\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_ARRAY_GENERATOR:
	{
		printf("ET_ARRAY_GENERATOR\n");
		printExpression(currentId, expr->left, maxId);
		if (expr->identifier != NULL)
			printExpression(currentId, expr->identifier, maxId);
		printExpression(currentId, expr->middle, maxId);
		if (expr->right != NULL)
			printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_FUNC_PARAM_DEFAULT:
	case ET_FUNC_PARAM:
	{
		printf("ET_FUNC_PARAM\n", currentId);
		printExpression(currentId, expr->identifier, maxId);
		if (expr->left != NULL)
			printExpression(currentId, expr->left, maxId);
		break;
	}
	case ET_FUNC_CALL:
	{
		printf("ET_FUNC_CALL\n");
		printExpression(currentId, expr->left, maxId);
		printListPython(currentId, expr->exprs, maxId);
		break;
	}
	case ET_BOOL:
	{
		printf("ET_BOOL\n%d\n", expr->intVal);
		break;
	}
	case ET_ID_AS:
	{
		printf("ET_ID_AS\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->right, maxId);
		break;
	}
	case ET_LAMBDA:
	{
		printf("ET_LAMBDA\n");
		printExpression(currentId, expr->left, maxId);
		printListPython(currentId, expr->exprs, maxId);
		break;
	}
	case ET_EXPR_AS:
	{
		printf("ET_EXPR_AS\n");
		printExpression(currentId, expr->left, maxId);
		printExpression(currentId, expr->identifier, maxId);
		break;
	}
	case ET_NONE:
	{
		printf("ET_NONE\n", currentId, expr->intVal);
		break;
	}
	default:
		break;
	}
	printf("%d\n",currentId);
}
void printListPython(int parentID, struct List* list, int* maxId)
{
	(*maxId)++;
	int currentId = (*maxId);
	if (list != NULL)
	{
		printf("List\n%d\n",currentId);

		switch (list->type)
		{
		case LT_UNDEFINED:
		{
			break;
		}

		case LT_ELEMENT:
		{
			printf("LT_ELEMENT\n");
			if (list->stmt_value != NULL)
				printStatement(currentId, list->stmt_value, maxId);
			else if (list->expr_value != NULL)
			{
				printExpression(currentId, list->expr_value, maxId);
			}
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_ARRAY_INITIAL_ARGUMENTS:
		{
			printf("LT_EXPR_ARRAY_INITIAL_ARGUMENTS\n");
			struct Expression* expr = list->expr_value;
			printExpression(currentId, expr, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_FUNCTION_PARAMS:
		{
			printf("LT_EXPR_FUNCTION_PARAMS\n", currentId);
			struct Expression* expr = list->expr_value;
			printExpression(currentId, expr, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_IDENTIFIERS_E:
		{
			printf("LT_EXPR_IDENTIFIERS_E\n", currentId);
			struct Expression* expr = list->expr_value;
			printExpression(currentId, expr, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_STATEMENT_LIST:
		{
			printf("LT_STATEMENT_LIST\n", currentId);
			struct Statement* stmt = list->stmt_value;
			printStatement(currentId, stmt, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_STMT_ELIF_LIST:
		{
			printf("LT_STMT_ELIF_LIST\n", currentId);
			struct Statement* stmt = list->stmt_value;
			printStatement(currentId, stmt, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_STMT_EXCEPT_LIST:
		{
			printf("LT_STMT_EXCEPT_LIST\n", currentId);
			struct Statement* stmt = list->stmt_value;
			printStatement(currentId, stmt, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_ID_AS_LIST: {
			printf("LT_EXPR_ID_AS_LIST\n", currentId);
			struct Expression* expr = list->expr_value;
			printExpression(currentId, expr, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		case LT_EXPR_WITH: {
			printf("LT_EXPR_WITH\n", currentId);
			struct Expression* expr = list->expr_value;
			printExpression(currentId, expr, maxId);
			if (list->next != NULL)
				printListPython(currentId, list->next, maxId);
			break;
		}
		default:
			break;
		}
		printf("%d\n",currentId);
	}
}