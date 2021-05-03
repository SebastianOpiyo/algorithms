#include<stdio.h>
#include<stdlib.h>
struct Node {
	int data;
	struct Node* link;
};

struct Node* top = NULL;

void Push(int x) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node*));
    temp -> data = x;
    temp-> link = top;
    top = temp;
}

void Pop(){
    struct Node* temp;
    if(top == NULL) return;
    temp = top;
    top = top -> link;
    free(temp);
}

void Print() {
	struct Node* temp = top;
	while(temp != NULL) {
		printf("%d ",temp->data);
		temp = temp->link;
	}
	printf("\n");
}

int main(){
	/* Drive code to test the implementation. */
	// Printing elements in Queue after each Enqueue or Dequeue 
	Push(2); Print(); 
	Push(4); Print();
	Push(6); Print();
	Pop();  Print();
	Push(8); Print();
}