#include <stdlib.h>

struct node {
    int x;
    struct node *next;
};

int main ()
{
    // The unchanging first node.
    struct node *root;

    // Root points to a node struct
    root = (struct node *) malloc(sizeof(struct node));

    // The node root points to has its next pointer equal to null pointer
    root -> next = 0;

    // By using the -> operator, you can modify what the node, a pointer, (root in this case) points to.
    root -> x = 5;
}
