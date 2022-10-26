'''
Depth First Search Algorithm design
'''

import numpy as np

class LinkedList:
    def __init__(self, row: int, col: int, next = None):
        self.col = col
        self.row = row
        self.next = next

class DFS:

    def __init__(self, row: int, col: int, arr: np.array):
        self.linked_lst = LinkedList(row, col)
        self.arr = arr
        self.rd, self.cd = arr.shape
        self.row = row
        self.col = col
    
    def iteration(self, row: int, col: int, arr: np.array):

        if self.row < self.rd - 1 and arr[self.row + 1, self.col] == 0:
           self.row = self.row + 1
           self.linked_lst.next = LinkedList(self.row, self.col)


        elif self.col < self.cd - 1 and arr[self.row, self.cd + 1] == 0:
           self.col = self.col + 1
           self.linked_lst.next = LinkedList(self.row, self.col)


        elif self.col >= self.cd - 1 and arr[self.row, self.cd] == 0:
           self.col = self.col + 1
           self.linked_lst.next = LinkedList(self.row, self.col)

        #else:
