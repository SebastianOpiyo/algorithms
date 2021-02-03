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
        // print function call before recursion begins
        printf("The count before recursion call is: %d\n", count);
        recursion(count + 1);
        // This will print from 9, decreamenting to 1.
        // Why ? Because what we have in place is a stack data structure.
        // Print function call result after occurance of recursion.
        printf("The count after recursion call is: %d\n", count);
    }
}

int main()
{
    recursion(1);
    return 0;
}
