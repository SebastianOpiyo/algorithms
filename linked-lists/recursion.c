#include <stdio.h>
#include <stdlib.h>

// Will run out of memory, since the stack trace will "Overflow with recursive calls."
// So at the end of the day, will have a segment fault.

void recursion (int count)
{
    // The the condition below, is called a base case
    // and serves to ensure that the recursive function terminates
    // Otherwise, it will result to a stack overflow / segmentation fault.
    if (count < 10 )
    {
        recursion(count + 1);
        // This will print from 9, decreamenting to 1.
        // Why ? Because what we have in place is a stack data structure.
        printf("The count is %d\n", count);
    }
}

int main()
{
    recursion(1);
    return 0;
}
