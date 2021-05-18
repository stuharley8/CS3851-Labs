import math

def insertion_sort(lst):
    """
    Sorts the list lst in place using insertion_sort.
    """
    for j in range(1, len(lst)):
        key = lst[j]
        i = j-1
        while i>=0 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i-1
        lst[i+1] = key


def merge_sort(lst, p, r):
    """
    Sorts the list lst in place using merge_sort.

    Args:
        lst: list to be sorted
        p: starting index of the list, i.e 0
        r: ending index of the list, i.e. len(lst) - 1
    """
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(lst, p, q)
        merge_sort(lst, q+1, r)
        merge(lst, p, q, r)


def merge(lst, p, q, r):
    """
    Merges two sorted partitions of lst.  This is
    performed in-place. It is assumed that the
    two partitions are contiguous in the list.

    Args:
        lst: list that is being sorted
        p: starting index of first partition
        q: ending index of first partition
        r: ending index of second partition
    """
    n1 = q - p + 1
    n2 = n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = lst[p + i]
    for i in range(n2):
        R[i] = lst[q + i + 1]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            lst[k] = L[i]
            i = i + 1
        else:
            lst[k] = R[j]
            j = j + 1
