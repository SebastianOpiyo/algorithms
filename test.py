
'''
Algorithm
We are looking for two elems in the list, when summed equal the target.
1. Create a hashtable of the elements in the list with element as key and index as value
2. pick the first elem in the list and sub from target to get rem
3. check to see of the rem exists in the dictionary and its index is greater than current iteration
4. if its true return index of the elem

Time Complexity: O(nlog(n))
'''

def list_hasmap(lst:list, target:int) -> list:
    hashmap = {val:i for i, val  in enumerate(lst)}
    for i in range(len(lst)):
        rem = target - lst[i]
        if rem in hashmap and hashmap[rem] != i:
            return [hashmap[rem], i]
        else:
            hashmap[rem] =i
    return []

print(list_hasmap([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], target=11))
