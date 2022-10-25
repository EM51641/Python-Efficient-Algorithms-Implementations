'''
Efficient Recursive Merge algorithm using recursive approach

Time Complexity: O(NlogN)
Space Complexity: O(N)
'''


def merge(L: list, R: list):
    '''
    Merge

    Attribute
    ------------------
             L: list - left list
             R: list - right list

    Returns
    -----------------
             nlist: list
    '''
    i = j = 0
    nlist = []

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            nlist.append(L[i])
            i = i + 1
        else:
            nlist.append(R[j])
            j = j + 1

    if i == len(L) and j < len(R):
        nlist.extend(R[j:])

    if j == len(L) and i < len(L):
        nlist.extend(L[i:])

    return nlist


def DivideandConquer(lst: list):
    '''
    Divide and Conquer

    Attribute
    ------------------
             lst: list - list

    Returns
    -----------------
             None
    '''

    if len(lst) < 2:
        return lst

    Cutoff = len(lst)//2
    first_list = DivideandConquer(lst[:Cutoff])
    second_list = DivideandConquer(lst[Cutoff:])

    return merge(first_list, second_list)
