#
# Matthew Marino
#
# Put your name up here in a comment.
# Then implement the insertion sort and merge sort
# algorithms in the functions that follow.  Also implement
# the is_sorted function to check if a list is sorted, and
# the random_list function to generate a list of random integers.
#
# Don't change the names of the functions or parameters.
# If you find it useful to have additional helper functions,
# you may do so.  Naming conventions in Python for helper functions
# is to begin with an _ at the start of the name.
#
# Note: You don't need the pass statements that I inserted, so you
# can delete them after you implement the functions.  I put them
# in temporarily so that you have valid syntax to start with.
#
# IMPORTANT: DO NOT have any print statements in the functions in this
# Python file (e.g., in the is_sorted, random_list, insertion_sort,
# merge_sort, and helper functions.  In general, you want to separate
# output from the computation.  You'll be outputting results
# (e.g., using print) in the if block at the bottom.

import random
import math


def is_sorted(A):
    """Returns True if A is sorted in non-decreasing order,
    and returns False if A is not sorted.

    Keyword arguments:
    A - a Python list.
    """

    for i in range(len(A) - 1):
        if A[i] <= A[i + 1]:
            pass
        else:
            return False
    return True

    # Hints for implementing is_sorted:
    # Hint 1: DO NOT use the built-in function sorted in this function.
    #       E.g., if you are tempted to call sorted and then compare
    #       result to A, this would be wrong.  Python's sorted function
    #       actually does a sort generating a new list tat is a sorted copy
    #       of the original.  This would be a silly, and costly, way to check
    #       if your list is sorted.  You will get 0 points for the is_sorted
    #       function if you call Python's sorted function.
    # Hint 2: If A is sorted then A[0] <= A[1] <= A[2] <= ....
    #       So, what you can do here is write a loop that does one
    #       comparison of adjacent elements.  If they are in the wrong order
    #       then return False from within the loop. If you manage to get
    #       through the loop without returning, then the list must be sorted,
    #       so return True.


def random_list(length, low_value=0, high_value=100):
    """Generates and returns a Python list of random integer values.
    The integers in the list are generated uniformly at random from
    the interval [low_value, high_value].

    Keyword arguments:
    length - the length of the list.
    low_value - the lower bound for the random integers.
    high_value - the upper bound for the random integers.
    """

    return [random.randrange(low_value, high_value) for x in range(length)]


    # Hint: Look at the documentation for the random module.
    # There are useful functions there for generating random numbers.

    # Another hint: You can use a Python list comprehension to
    # generate the list.

    # Yet another hint: If you follow the above hints, it is possible
    # to implement this function with a single line of code,
    # a return statement with a list comprehension.


def insertion_sort(A):
    """Implementation of the insertion sort algorithm
    as specified on page 18 of the textbook.

    Keyword arguments:
    A - a Python list.
    """

    for i in range(len(A)):
        cur = A[i]
        pos = i

        while pos > 0 and A[pos - 1] > cur:
            A[pos] = A[pos - 1]
            pos -= 1

        A[pos] = cur
    return A


def merge_sort(A):
    """Implementation of the mergesort algorithm.

    Keyword arguments:
    A - a Python list.
    """

    # This function is the top level call, and should simply
    # call _merge_sort(A, p, r) passing the appropriate indices
    # to sort the entire list.

    # Set default parameters for easy call to function
    _merge_sort(A, 0, len(A) - 1)


def _merge_sort(A, p, r):
    """The mergesort algorithm as specified on page 34 of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of portion of list to sort
    r - the right most index of portion of list to sort
    """

    if p < r:
        # Find mid and use // for floor
        m = (p + r) // 2
        _merge_sort(A, p, m)
        _merge_sort(A, m + 1, r)
        _merge(A, p, m, r)


def _merge(A, p, q, r):

    """The merge operation for mergesort, as specified on page 31
    of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of left sublist
    q - right most index of left sublist
    r - right most index of right sublist
    """

    n1 = q - p + 1
    n2 = r - q

    # Empty arrays
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = A[p + i]

    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    # Sentinel values (infinity-esq) at the end
    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == "__main__":
    # Indented within this if block, do the following:
    # 1) Write a few lines of code to demonstrate that your
    #    is_sorted works correctly (i.e., that it returns True
    #    if given a list that is sorted, and False otherwise).
    # 2) Write a few lines of code to demonstrate that insertion_sort
    #    correctly sorts a list (your random_list function will be useful
    #    here).  Output (i.e., with print statements) the contents
    #    odf the list before sorting, and then again after sorting).
    # 3) Repeat 2 to demostrate that your merge_sort sorts correctly.

    # is_sorted testing
    print(is_sorted([1, 2, 3, 5, 5]))
    print(is_sorted([1, 5, 3, 4, 5]))

    # insertion_sort testing
    print(insertion_sort(random_list(10)))

    # merge_sort testing
    L = random_list(7)
    print(L)
    merge_sort(L)
    print(L)
