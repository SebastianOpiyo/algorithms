# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:21:39 2020

@author: SebastianOpiyo
"""

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('Selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

testList = [1,3,8,7,6,2,25,19,15,30]
print('')
print(selection_sort(testList))
print(testList)
