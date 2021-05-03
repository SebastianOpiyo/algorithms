#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
   int data;
   int key;
	
   struct Node* next;
   struct Node* prev;
};

// Create link that points to the first LINK and last LINK
// First Link
struct Node* head; // Global variable pointer to head node.

// For the sake of having DRY code
// We implement a function that creates nodes. This will need at different places
struct Node* createNewNode(int node_data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = node_data;
    newNode -> next = NULL;
    newNode -> prev = NULL
    return newNode;
};

// Insert node at the beginning of a doubly-linked list
void insertAtHead(int x){
    struct Node* newNode = createNewNode(x);
	if(head == NULL) {
		head = newNode;
		return;
	}
	head->prev = newNode; // set the new node as the first node in the list.
	newNode->next = head; // set the previous head as next element
	head = newNode; // set the new node inserted as head
};

// Insert node at the end of a doubly linked list.
void insertAtTail(int x){
    struct Node* tempNode = head;
	struct Node* newNode = createNewNode(x);
	if(head == NULL) {
		head = newNode;
		return;
	}
	while(tempNode->next != NULL)
    temp = tempNode->next; // Go To last Node
	tempNode->next = newNode;
	newNode->prev = temp;

};

// print contents of a DLL in a reverse order.
void printReverseList(){
    struct Node* temp = head;
	if(temp == NULL) return; // empty list, exit
	// Going to last Node
	while(temp->next != NULL) {
		temp = temp->next;
	}
	// Traversing backward using prev pointer
	printf("Reverse: ");
	while(temp != NULL) {
		printf("%d ",temp->data);
		temp = temp->prev;
	}
	printf("\n");

};

void PrintList(){
    //Implement code that prints the whole list.
    struct Node* temp = head;
    printf("Created Linked List: ");
    while(temp!=NULL){
        printf("%d -->", temp->data);
        temp = temp->next;
    printf("%d", NULL);
    printf("\n");
};
};