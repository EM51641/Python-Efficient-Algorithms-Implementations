'''
Depth First Search Algorithm design
'''

import numpy as np

class LinkedList:
    def __init__(self, col: int, row: int, next = None, prev=None):
        self.col = col
        self.row = row
        self.next = next
        self.prev = prev

class DFS:

    def __init__(self, row: int, col: int, arr: np.array):
        self.arr = arr
        self.rd, self.cd = arr.shape
        self.row = row
        self.col = col
        self.linked_lst = LinkedList(row, col)

    def iteration(self):

      while self.linked_lst != None:

         if (self.row < self.rd - 1 and self.arr[self.row + 1, self.col] == 0 and
            (self.linked_lst.next == None or (self.linked_lst.next.row != self.row + 1 and self.linked_lst.next.col == self.col))
            ):
 
            self.row = self.row + 1
            temp = self.linked_lst
            self.linked_lst.next = LinkedList(self.row, self.col)
            self.linked_lst = self.linked_lst.next
            self.linked_lst.prev = temp
 
         elif (self.col < self.cd - 1 and self.arr[self.row, self.col + 1] == 0 and
           (self.linked_lst.next == None or (self.linked_lst.next.row == self.row and self.linked_lst.next.col != self.col + 1))
           ):

           self.col = self.col + 1
           temp = self.linked_lst
           self.linked_lst.next = LinkedList(self.row, self.col)
           self.linked_lst = self.linked_lst.next
           self.linked_lst.prev = temp

         elif (self.row >= self.row - 1 and self.arr[self.row - 1, self.col] == 0 and
           (self.linked_lst.next == None or (self.linked_lst.next.row != self.row - 1 and self.linked_lst.next.col == self.col))
         ):

           self.row = self.row - 1
           temp = self.linked_lst
           self.linked_lst.next = LinkedList(self.row, self.col)
           self.linked_lst = self.linked_lst.next
           self.linked_lst.prev = temp

         elif (self.col >= self.col - 1 and self.arr[self.row, self.col - 1] == 0 and
           (self.linked_lst.next == None or (self.linked_lst.next.row == self.row and self.linked_lst.next.col != self.col - 1))
         ):

           self.col = self.col - 1
           temp = self.linked_lst
           self.linked_lst.next = LinkedList(self.row, self.col)
           self.linked_lst = self.linked_lst.next
           self.linked_lst.prev = temp

         else:
            print(self.linked_lst.row, self.linked_lst.col)
            self.linked_lst = self.linked_lst.prev
            self.row, self.col = self.linked_lst.row, self.linked_lst.col
