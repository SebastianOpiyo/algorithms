#include <stdio.h>
#include <stdlib.h>

/*
* ASSIGNMENT2 : Design from the flowchart program to implement the insertion of 
* a new element into an existing list.
*/

// We define a node of "int" data type and "next" node address
struct Node {
	int data;
	struct Node * next;
};

struct Node* head;   // This a global pointer variable, that can be accessed anywhere.

// Node functions
void InsertAtAnyPosition(int data, int position);
void PrintList();

int main() {
    head = NULL; //we initiate an empty list.
    printf("Insert Nodes at nth position: ");
    // Could improve this so that it takes input from the command prompt.
    InsertAtAnyPosition(2,1);
    InsertAtAnyPosition(10,2);
    InsertAtAnyPosition(5,3);
    InsertAtAnyPosition(6,2);
    PrintList();
    
    //PrintList();
}

void InsertAtAnyPosition(int data, int position){
    // Implement node insertion to a list at any position
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node)); // create memory allocation for new node.
    newNode ->data = data; // assign new value to  created node
    newNode->next = NULL; // Create empty list
    if (position == 1){
        newNode->next = head;
        head = newNode;
        return;
    };
   // Create a node to insert at nth position
   struct Node* tempNode = head;
   for(int i=2; i<position; i++){
       // the condition could as well be <int i=0; i< position -2; i++>
       tempNode = tempNode->next;
   }
   newNode->next = tempNode->next;
   tempNode->next = newNode;
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