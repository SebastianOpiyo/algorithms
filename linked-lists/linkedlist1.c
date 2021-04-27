
/*
 * SINGLY LINKED LIST
 * Note, this code should guide you and not really be used as is for your answers.
 * I adds a some complexity to the first code.
 */

#include <stdio.h>
#include <stdlib.h>
struct Node {
	int data;
	struct Node * next;
};

typedef struct Node NODE;

NODE * createNewNode(int data) {
	NODE * newNode = (NODE *) malloc (sizeof(NODE));
	newNode -> data = data;
	newNode -> next = NULL;
	return newNode;
}

void display(NODE * head) {
	NODE * current = head;
	while (current != NULL) {
		printf(" %d ", current -> data);
		current = current -> next;
	}
}

int length(NODE * head) {
	// recursively determines the length of list
	return head == NULL ? 0 : 1 + length(head -> next);
}

NODE * insertAtHead(NODE * head, int data) {
	NODE * newNode = createNewNode(data);
	newNode -> next = head;
	head = newNode;
	return head;
}

NODE * insertAtEnd(NODE * head, int data) {
	NODE * newNode = createNewNode(data), * current = head;
	if (current == NULL) {
		head = newNode;
	} else {
		// traverse until end of list is reached
		while (current -> next != NULL) current = current -> next;
		current -> next = newNode;
	}
	return head;
}

NODE * insertAtArbitrary(NODE * head, int data, int location) {
	int len = length(head), i;
	if (location < 1 || location > len + 1) {
		printf("\nInvalid Location to enter data\n");
	} else if (location == 1) {
		return insertAtHead(head, data);
	} else {
		NODE * newNode = createNewNode(data), * current = head;	
		for (i = 2; i != location; i++)	current = current -> next;
		newNode -> next = current -> next;
		current -> next = newNode;
	}
	return head;
}

NODE * deleteByValue(NODE * head, int data) {
	NODE * current = head, * previous;
	while (current != NULL) {
		if (current -> data == data) {
			if (current == head) {
				head = head -> next;
				free(current);
				current = head;
			} else {
				previous -> next = current -> next;
				free(current);
				current = current -> next;
			}
		} else {
			previous = current;
			current = current -> next;
		}
	}
	return head;
}

NODE * deleteByLocation(NODE * head, int location) {
	NODE * current = head, * previous;
	int curloc = 1, i, len = length(head);
	if (location < 1 || location > len) {
		printf("\nInvalid location\n");
	} else {
		if (location == 1) {
			head = head -> next;
		} else {
			for (i = 1; i < location; i++) {
				previous = current;
				current = current -> next;
			}
			previous -> next = current -> next;
		}
		free(current);
	}
	return head;
}

NODE * sort(NODE * head) {
	if (length(head) < 2) return head;
	NODE * ptr1 = head, * ptr2, * min;
	int temp;
	// selection sort implementation
	while (ptr1 -> next != NULL) {
		min = ptr1;
		ptr2 = ptr1 -> next;
		while (ptr2 != NULL) {
			if (min -> data > ptr2 -> data) min = ptr2;
			ptr2 = ptr2 -> next;
		}
		if (min != ptr1) {
			temp = min -> data;
			min -> data = ptr1 -> data;
			ptr1 -> data = temp;
		}
		ptr1 = ptr1 -> next;
	}
	return head;
}


int main() {
	NODE * sll = NULL;
	int option, data, location;
	while (1) {
		printf("\n\n\n SLL =");
		display(sll);

		printf("\n\nEnter your choice:\n1. Insert at head\n2. Insert at end\n3. Insert at arbitrary location\n4. Delete by value\n5. Delete by location\n6. Sort\n7. Exit\n >> ");
		scanf("%d", &option);
		
		if (option == 1) {
			printf("Enter data to be inserted: ");
			scanf("%d", &data);
			sll = insertAtHead(sll, data);
		} else if (option == 2) {
			printf("Enter data to be inserted at end: ");
			scanf("%d", &data);
			sll = insertAtEnd(sll, data);
		} else if (option == 3) {
			printf("Enter data to be inserted: ");
			scanf("%d", &data);
			printf("Enter location to be inserted into: ");
			scanf("%d", &location);
			sll = insertAtArbitrary(sll, data, location);
		} else if (option == 4) {
			printf("Enter value to be deleted: ");
			scanf("%d", &data);
			sll = deleteByValue(sll, data);
		} else if (option == 5) {
			printf("Enter location to be deleted: ");
			scanf("%d", &location);
			sll = deleteByLocation(sll, location);
		} else if(option == 6) {
			sort(sll);
		} else if (option == 7) {
			break;
		}
	}
	return 0;
}