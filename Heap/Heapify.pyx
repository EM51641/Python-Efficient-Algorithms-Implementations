
'''
Cython Implementation
Turbocharged Non-Recursive Heapify algorithm
Time Complexity: O(N)
Space Complexity: O(1)
'''


cdef compare(double head, double left, double right):
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

    cdef double temp

    if right <= left and head > right:
        temp = head
        head = right
        right = temp

    elif left <= right and head > left:
        temp = head
        head = left
        left = temp  

    return head, left, right


cdef loop_log_n(int pos, list lst, int n):
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

    cdef int left, right
    cdef double temp, temp_left, temp_right

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

    if (n % 2 == 0 and left < n and right >= n and
       lst[pos] > lst[left]):
        lst[left], lst[pos] = lst[pos], lst[left]


cdef remove_uneven_nodes(list lst):
    '''
    Initialise bottom Uneven nodes

    Attribute
    ------------------
             lst: list

    Returns
    -----------------
             lst: list
    '''
    cdef int global_length, length, idx, m

    global_length = length = len(lst)

    if length % 2 == 0:
        idx = length - 1
        m = idx//2
        if lst[idx] < lst[m]:
            lst[m], lst[idx] = lst[idx], lst[m]

        global_length = idx

    return global_length, length


cpdef heapify(list lst):
    '''
    Heapify algorithm

    Attribute
    ------------------
             lst: list

    Returns
    -----------------
             None
    '''
    cdef int global_length, length, i, step, start,  _
    cdef double temp, temp_right

    global_length, length = remove_uneven_nodes(lst)
    step = 2
    start = global_length
    i = global_length

    for _ in range(start//step):
        i = i - step
        temp, temp_right = lst[i//2], lst[i + 1]

        # Bottom-up Approach
        lst[i//2], lst[i], lst[i + 1] = compare(lst[i//2], lst[i], lst[i + 1])

        if lst[i//2] == temp:
            continue

        # Top-Down
        elif lst[i//2] == temp_right:
            loop_log_n(i + 1, lst, length)

        else:
            loop_log_n(i, lst, length)