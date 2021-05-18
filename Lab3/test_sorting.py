import unittest

import random

from sorting import merge
from sorting import merge_sort

N_NUMBERS = 10


class TestMergeSort(unittest.TestCase):
    def test_merge_sort_random(self):
        """
        Tests merge sort using a list of randomly-ordered
        numbers.
        """

        numbers = [random.random() for i in range(N_NUMBERS)]

        # make a copy of the list
        observed = numbers[:]
        merge_sort(observed, 0, len(observed) - 1)

        # make a copy of the list
        # and sort using built-in function
        expected = numbers[:]
        expected.sort()

        self.assertListEqual(observed, expected)

    def test_merge_sort_sorted(self):
        """
        Tests merge sort using a list of sorted
        numbers. Ensures that insertion sort maintains
        the sorted property.
        """

        numbers = [random.random() for i in range(N_NUMBERS)]
        numbers.sort()

        # make a copy of the list
        expected = numbers[:]

        # make a copy of the list
        observed = numbers[:]
        merge_sort(observed, 0, len(observed) - 1)

        self.assertListEqual(observed, expected)

    def test_merge(self):
        """
        Tests that the merge operation successfully
        merges two sorted lists into a single sorted list.
        """

        lst1 = [random.random() for i in range(N_NUMBERS)]
        lst1.sort()

        lst2 = [random.random() for i in range(N_NUMBERS)]
        lst2.sort()

        merged = lst1 + lst2
        merge(merged, 0, len(lst1) - 1, len(merged) - 1)

        expected = lst1 + lst2
        expected.sort()

        self.assertListEqual(expected, merged)



if __name__ == "__main__":
    unittest.main()
