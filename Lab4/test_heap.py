import unittest

import random

from heap import build_max_heap
from heap import heap_extract_max
from heap import heapsort
from heap import max_heap_insert

from heap import _left
from heap import _right

def satisfies_heap_property(heap, i=0):
    """
    Recursively checks that the heap satisfies the heap property.
    I.e., each entry is larger than its two children.
    """
    
    if len(heap) == 0 or i >= len(heap):
        return True

    l = _left(i)
    r = _right(i)
    
    left_valid = True
    right_valid = True
    
    if l < len(heap) and heap[i] < heap[l]:
        left_valid = False
        
    if r < len(heap) and heap[i] < heap[r]:
        right_valid = False
        
    
    return left_valid and right_valid and satisfies_heap_property(heap, l) and satisfies_heap_property(heap, r)
    

class TestHeap(unittest.TestCase):
    def test_max_heap_insert(self):
        heap = []
        
        max_heap_insert(heap, 5)
        self.assertEqual(len(heap), 1)
        self.assertTrue(satisfies_heap_property(heap))
        
        max_heap_insert(heap, 6)
        self.assertEqual(len(heap), 2)
        self.assertTrue(satisfies_heap_property(heap))
        
        max_heap_insert(heap, 4)
        self.assertEqual(len(heap), 3)
        self.assertTrue(satisfies_heap_property(heap))
        
        max_heap_insert(heap, 7)
        self.assertEqual(len(heap), 4)
        self.assertTrue(satisfies_heap_property(heap))
        
        expected = [7, 6, 4, 5]
        self.assertListEqual(heap, expected)
        
        heap = []
        for i in range(10):
            max_heap_insert(heap, i)
            
        self.assertEqual(len(heap), 10)
        expected = [9, 8, 5, 6, 7, 1, 4, 0, 3, 2]
        self.assertListEqual(heap, expected)
        self.assertTrue(satisfies_heap_property(heap))
        
    def test_build_max_heap(self):
        lst = [4, 5, 6, 7]
        
        build_max_heap(lst)
        
        expected = [7, 5, 6, 4]
        self.assertListEqual(lst, expected)
        self.assertTrue(satisfies_heap_property(lst))

    def test_heap_extract_max(self):
        heap = [7, 6, 4, 5]
        
        result = heap_extract_max(heap)
        self.assertEqual(7, result)
        self.assertEqual(len(heap), 3)
        
        result = heap_extract_max(heap)
        self.assertEqual(6, result)
        self.assertEqual(len(heap), 2)
        
        result = heap_extract_max(heap)
        self.assertEqual(5, result)
        self.assertEqual(len(heap), 1)
        
        result = heap_extract_max(heap)
        self.assertEqual(4, result)
        self.assertEqual(len(heap), 0)

        
    def test_heapsort(self):
        lst = [random.random() for i in range(10)]
        expected = lst[:]
        expected.sort()
        
        heapsort(lst)
        
        self.assertListEqual(expected, lst)


if __name__ == "__main__":
    unittest.main()
