#include "tree_struct.h"
#include <stdio.h>
#include <malloc.h>
//#include "python.bison_tab.h"
void printTree(void);
void printStmt(int parentID, struct Statement* stmt, int* maxId);
void printExpr(int parentID, struct Expression* expr, int* maxId);
void printList(int parentID, struct List* list, int* maxId);

void printForPython(void);
void printStatement(int parentID, struct Statement* stmt, int* maxId);
void printExpression(int parentID, struct Expression* expr, int* maxId);
void printListPython(int parentID, struct List* list, int* maxId);
