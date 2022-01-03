# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:23:39 2020

@author: SebastianOpiyo
"""

def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,3,8,7,6,2,25,19,15,30]
print('')
print(bubble_sort(testList))
print(testList)
