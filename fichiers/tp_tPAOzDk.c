#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure d'un n�ud de la liste cha�n�e
struct Node {
    char data;
    struct Node* next;
};

// Structure de la pile
struct Stack {
    struct Node* top;
};

// Structure de la file
struct Queue {
    struct Node* front;
    struct Node* rear;
};

// Fonction pour initialiser la pile
struct Stack* createStack() {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->top = NULL;
    return stack;
}

// Fonction pour initialiser la file
struct Queue* createQueue() {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->front = queue->rear = NULL;
    return queue;
}

// Fonction pour cr�er un nouveau n�ud dans la liste cha�n�e
struct Node* createNode(char data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Fonction pour pousser un �l�ment sur la pile
void push(struct Stack* stack, char item) {
    struct Node* newNode = createNode(item);
    newNode->next = stack->top;
    stack->top = newNode;
}

// Fonction pour retirer un �l�ment de la pile
char pop(struct Stack* stack) {
    if (stack->top == NULL)
        return '\0';

    char data = stack->top->data;
    struct Node* temp = stack->top;
    stack->top = stack->top->next;
    free(temp);
    return data;
}

// Fonction pour ajouter un �l�ment � la file
void enqueue(struct Queue* queue, char item) {
    struct Node* newNode = createNode(item);

    if (queue->rear == NULL) {
        queue->front = queue->rear = newNode;
        return;
    }

    queue->rear->next = newNode;
    queue->rear = newNode;
}

// Fonction pour retirer un �l�ment de la file
char dequeue(struct Queue* queue) {
    if (queue->front == NULL)
        return '\0';

    char data = queue->front->data;
    struct Node* temp = queue->front;

    queue->front = queue->front->next;
    if (queue->front == NULL)
        queue->rear = NULL;

    free(temp);
    return data;
}

// Fonction pour v�rifier l'�quilibre des parenth�ses dans une expression
int checkParentheses(char* expression) {
    struct Stack* stack = createStack();
    struct Queue* queue = createQueue();

    for (int i = 0; i<strlen(expression); i++) {
        if (expression[i] == '(') {
            push(stack, expression[i]);
            enqueue(queue, expression[i]);
        } else if (expression[i] == ')') {
            if (pop(stack) != '(') {
                free(stack);
                free(queue);
                return 0;  // Parenth�se fermante sans parenth�se ouvrante correspondante
            }S
            dequeue(queue);
        }
    }

    int result = stack->top == NULL ? 1 : 0;
    free(stack);
    free(queue);
    return result;
}

// Fonction principale pour tester l'expression
int main() {
    char expression[100];

    printf("Entrez une expression avec des parenth�ses : ");
    scanf("%s", expression);

    if (checkParentheses(expression))
        printf("L'expression est valide (nombre de parenth�ses pair).\n");
    else
        printf("L'expression n'est pas valide (nombre de parenth�ses impair).\n");

    return 0;
}
