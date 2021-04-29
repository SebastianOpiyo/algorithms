#include <stdio.h>
#include<stdbool.h> 
#include <stdlib.h>
#include <time.h>

/*
* ASSIGNMENT3 : Linear/Sequential search algorithm
*/

// We define a node of "int" data type and "next" node address
struct Node {
	int data;
	struct Node * next;
};

struct Node* head;   // This a global pointer variable, that can be accessed anywhere.

// Node functions
double duration;
clock_t start, stop;
bool found;

void InsertAtAnyPosition(int data, int position);
void LinearSearch(int data);
void PrintList();
void calculateTime(int start, int stop);

int main() {
    head = NULL; //we initiate an empty list.
    printf("Linear Search of Nodes at nth position: ");
    printf("\nPlease enter data and position: ");
    int data, position;

    while(&data && &position){
        if(data == 0){
            printf("End of list creation!");
        };
        printf("\nEnter Data: ");
        scanf("%d", &data);
        printf("Enter Position: ");
        scanf("%d", &position);
        InsertAtAnyPosition(data, position);
        PrintList();
    }
    printf("\nEntire List Print!\n");
    PrintList();
    printf("\nEnter Data to Search: \n");
    scanf("%d", &data);
    LinearSearch(data);
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

void LinearSearch(int data){
    //Search for the given data in a linked list.
    struct Node* temp1 = head;
    start = clock();
    printf("\nSearching the list!\n");
        while(temp1 != NULL){
            if (temp1->data == data){
                found = true;
                printf("Item found in list!");
                break;
            };
            printf("Moving to the next node...");
            temp1 = temp1->next;
    };
    stop = clock();
    calculateTime(start, stop);
};

void calculateTime(int start, int stop){
    // calculate the time it takes for linear search.
    duration = ( double ) ( stop - start ) / CLOCKS_PER_SEC;
    printf("Time taken for the linear search is: %.2lf\n", duration);

};