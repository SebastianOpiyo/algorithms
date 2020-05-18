# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:43:39 2020

@author: SebastianOpiyo
"""

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' + str(result))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2 :
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

testList = [1,3,8,7,6,2,25,19,15,30]
print('')
print(merge_sort(testList))
print(testList)
