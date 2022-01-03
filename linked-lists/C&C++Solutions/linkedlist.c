// Linked list implementation in C

#include <stdio.h>
#include <stdlib.h>

// Creating a node
struct node {
  int value;
  struct node *next;
};

// print the linked list value
// This performs traversal or search.
void printLinkedlist(struct node *p) {
  while (p != NULL) {
    printf("%d ", p->value);
    p = p->next;
  }
}

int main() {
  // Initialize nodes
  struct node *head;
  struct node *one = NULL;
  struct node *two = NULL;
  struct node *three = NULL;

  // Allocate memory
  one = malloc(sizeof(struct node));
  two = malloc(sizeof(struct node));
  three = malloc(sizeof(struct node));

  // Assign value values (dereferencing)
  one->value = 1; // we could as well use (*one).value or (*one).next
  two->value = 2;
  three->value = 3;

  // Connect nodes
  one->next = two;
  two->next = three;
  three->next = NULL;

  // printing node-value
  head = one;
  printLinkedlist(head);
}// Linked list implementation in C


// Reading resources.
// https://www.geeksforgeeks.org/difference-between-contiguous-and-noncontiguous-memory-allocation/#:~:text=Contiguous%20Memory%20Allocation%20%3A,process%20or%20file%20needing%20it.&text=We%20can%20implement%2Fachieve%20contiguous,partitions%20into%20fixed%20size%20partitions.
// https://people.engr.ncsu.edu/efg/210/s99/Notes/LinkedList.1.html
