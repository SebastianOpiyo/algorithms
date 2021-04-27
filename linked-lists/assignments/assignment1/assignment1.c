#include <stdio.h>
#include <stdlib.h>

/*
*Use logical steps and the FlowChart to write a Program
*/

// We define a node of "int" data type and "next" node address
struct Node {
	int data;
	struct Node * next;
};

struct Node* head;   // This a global pointer variable, that can be accessed anywhere.

// Node functions
void InsertToList(int num_entered);
void PrintList();

int main() {
    head = NULL; //we initiate an empty list.
    printf("Enter number of nodes you want to create: ");
    int num_of_nodes, num_entered, i;  // declare variables for nodes, user input & iterator
    scanf("%d", &num_of_nodes); 
    // We can use a while loop instead.
    i = 1; // Because counting begins from zero.
    while (i <= num_of_nodes)
    {
        printf("\nEnter value for new node: ");
        scanf("%d", &num_entered);
        InsertToList(num_entered);
        PrintList();
        i ++;
    }
    //PrintList();
}

void InsertToList(int num_entered){
    // Implement node insertion to a list
    // This implements insertion at the beginning of a list.
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node)); // create memory allocation for new node.
    temp ->data = num_entered; // assign new value to  created node
    temp->next = head; // set next node addr to head
    head = temp; // create new head from temp node created.
}

void PrintList(){
    //Implement code that prints the whole list.
    struct Node* temp = head;  // a temp variable that secures head data from accidental manipulation.
    printf("Created Linked List: ");
    while(temp!=NULL){
        printf("%d -->", temp->data); // print the data
        temp = temp->next; // move to the next node.
    }
    printf("%d", NULL); // Ensures the last node points to null for illustration reasons.
}

