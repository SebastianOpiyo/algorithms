#include <stdio.h>
#include <stdlib.h>


struct node {
    int x;
    struct node *next;
};

int main ()
{
    // The unchanging first node.
    struct node *root;

    // A link that will point to each node during traversal.
    struct node *link;

    // Root points to a node struct
    root = malloc(sizeof(struct node));

    // The node root points to has its next pointer equal to null pointer
    root -> next = 0;

    // By using the -> operator, you can modify what the node, a pointer, (root in this case) points to.
    root -> x = 5;
    link = root;

    if (link != 0 )
    {
        while ( link -> next != 0)
        {
            link = link -> next;
        }
    }
    // Else, we create a node at the end of the list
    link -> next = malloc(sizeof(struct node ));
    link = link -> next;
    // Get to the null pointer or end, which is 0
    // printf("Next link %d\n", link->next);

    if (link == 0)
    {
        printf("Out of memory");
        return 0;
    }
    // Initialize the new memory
    link -> next =0;
    link -> x = 42;
    link -> x = 50;
    printf("Our node is %d \n", root->x);
    printf("Our next node is %d", link->x);
    return 0;
}



