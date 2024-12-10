
'''
Algorithm
We are looking for two elems in the list, when summed equal the target.
1. Create a hashtable of the elements in the list with element as key and index as value
[Improvement: Create a hashmap on the fly, instead of creating it first.]
2. pick the first elem in the list and sub from target to get rem
3. check to see of the rem exists in the dictionary and its index is greater than current iteration
4. if its true return index of the elem

Time Complexity: O(nlog(n))
'''



def list_hasmap(lst:list, target:int) -> list:
    hashmap = {}
    for i, val in enumerate(lst):
        rem = target - val
        if rem in hashmap and hashmap[rem] != i:
            return [hashmap[rem], i]
        # We update the hashmap at this point
        hashmap[val] = i
    return []

print(list_hasmap([3,2,4], target=6))
