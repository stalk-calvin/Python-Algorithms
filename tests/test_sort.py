import unittest

from calvin.sort import SortAlgorithms

class SortAlgorithmsTest(unittest.TestCase):
    """
    Test Sorting methods
    """
    def setUp(self):
        self.fixture = SortAlgorithms()

    def test_bubble_sort(self):
        input=[1, 5, 12, 2, 9, 7]
        self.fixture.bubble_sort(input)
        self.assertEqual([1, 2, 5, 7, 9, 12], input)
        input = [1, 2, 12, 7, 8, 9]
        self.fixture.bubble_sort(input)
        self.assertEqual([1, 2, 7, 8, 9, 12], input)

    def test_selection_sort(self):
        input=[1, 5, 12, 2, 9, 7]
        self.fixture.selection_sort(input)
        self.assertEqual([1, 2, 5, 7, 9, 12], input)
        input = [1, 2, 12, 7, 8, 9]
        self.fixture.selection_sort(input)
        self.assertEqual([1, 2, 7, 8, 9, 12], input)

    def test_insertion_sort(self):
        input=[1, 5, 12, 2, 9, 7]
        self.fixture.insertion_sort(input)
        self.assertEqual([1, 2, 5, 7, 9, 12], input)
        input = [1, 2, 12, 7, 8, 9]
        self.fixture.insertion_sort(input)
        self.assertEqual([1, 2, 7, 8, 9, 12], input)

    def test_merge_sort(self):
        input=[1, 5, 12, 2, 9, 7]
        self.fixture.merge_sort(input, 0, len(input)-1)
        self.assertEqual([1, 2, 5, 7, 9, 12], input)
        input = [1, 2, 12, 7, 8, 9]
        self.fixture.merge_sort(input, 0, len(input)-1)
        self.assertEqual([1, 2, 7, 8, 9, 12], input)

    def test_quick_sort(self):
        input=[1, 5, 12, 2, 9, 7]
        self.fixture.quick_sort(input, 0, len(input)-1)
        self.assertEqual([1, 2, 5, 7, 9, 12], input)
        input = [1, 2, 12, 7, 8, 9]
        self.fixture.quick_sort(input, 0, len(input)-1) 
        self.assertEqual([1, 2, 7, 8, 9, 12], input)
    
    def test_counting_sort(self):
        input=[1, 5, 12, 2, 9, 7]
        self.fixture.counting_sort(input)
        self.assertEqual([1, 2, 5, 7, 9, 12], input)
        input = [1, 2, 12, 7, 8, 9]
        self.fixture.counting_sort(input)
        self.assertEqual([1, 2, 7, 8, 9, 12], input)