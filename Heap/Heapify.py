'''
Turbocharged Non-Recursive Heapify algorithm
Time Complexity: O(N)
Space Complexity: O(1)

Warning !!
Use Arrays if you want to it with numba
'''

from numba import njit


@njit(fastmath=True)
def compare(head, left, right):
    '''
    Loop Around Nodes

    Attribute
    ------------------
             head: int - Top of the node
             left: int - Bottom left of the node
             right: int -  Top right of the node

    Returns
    -----------------
             None
    '''

    if right <= left and head > right:
        temp = head
        head = right
        right = temp

    if left <= right and head > left:
        temp = head
        head = left
        left = temp

    return head, left, right


@njit(fastmath=True)
def loop_node(j, lst, n):
    '''
    Loop Around Nodes

    Attribute
    ------------------
             j: int - starting point
             lst: list
             n: length of the list

    Returns
    -----------------
             None

    '''
    while 2 * j + 2 < n:

        left = 2 * j + 1
        right = 2 * j + 2

        lst[j], lst[left], lst[right] = compare(
            lst[j], lst[left], lst[right]
            )

        j = j + 1

    if (n % 2 == 0 and 2 * j + 1 < n and 2 * j + 2 >= n and
       lst[j] > lst[2 * j + 1]):
        lst[2 * j + 1], lst[j] = lst[j], lst[2 * j + 1]


@njit(fastmath=True)
def loop_log_n(pos, lst, n):
    '''
    Loop Around Nodes

    Attribute
    ------------------
             j: int - starting point
             lst: list
             n: length of the list

    Returns
    -----------------
             None

    '''

    left = 2 * pos + 1
    right = left + 1

    while right < n:
        temp, temp_left, temp_right = lst[pos], lst[left], lst[right]

        lst[pos], lst[left], lst[right] = compare(
            lst[pos], lst[left], lst[right]
            )

        # We by default the right node is selected first
        if lst[pos] == temp_right and lst[pos] != temp:
            pos = right

        elif lst[pos] == temp_left and lst[pos] != temp:
            pos = left

        else:
            break

        left = 2 * pos + 1
        right = left + 1

    if (n % 2 == 0 and 2 * pos + 1 < n and 2 * pos + 2 >= n and
       lst[pos] > lst[2 * pos + 1]):
        lst[2 * pos + 1], lst[pos] = lst[pos], lst[2 * pos + 1]


@njit
def remove_uneven_nodes(lst: list):
    '''
    Initialise bottom Uneven nodes

    Attribute
    ------------------
             lst: list

    Returns
    -----------------
             lst: list
    '''

    global_length = length = len(lst)

    if length % 2 == 0:
        idx = length - 1
        m = idx//2
        if lst[idx] < lst[m]:
            lst[m], lst[idx] = lst[idx], lst[m]

        global_length = idx

    return global_length, length


@njit(fastmath=True)
def heapify(lst: list):
    '''
    Heapify algorithm

    Attribute
    ------------------
             lst: list

    Returns
    -----------------
             None
    '''
    global_length, length = remove_uneven_nodes(lst)

    for i in range(global_length - 2, 0, -2):
        temp, temp_right = lst[i//2], lst[i + 1]

        # Bottom-up Approach
        lst[i//2], lst[i], lst[i + 1] = compare(lst[i//2], lst[i], lst[i + 1])

        if lst[i//2] == temp:
            continue

        # Top-Down
        if lst[i//2] == temp_right:
            loop_log_n(i + 1, lst, length)

        else:
            loop_log_n(i, lst, length)
