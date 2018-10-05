from scripts.Algorithm import Algorithm, AlgorithmError
from models.Stack import Stack

import numpy as np

class Sort(Algorithm):
    """
    Base class for sorting algorithms.
    """

    def generate_collection(self, *args, **kwargs):
        min = kwargs.get('min', 1)
        max = kwargs.get('max', 1000)
        size = kwargs.get('size', 10)

        coll = [int(v) for v in np.random.choice(range(min, max + 1), size)]

        shuffles = 5

        # shuffle collection 5 times using fisher yates
        for x in range(shuffles):
            s = size

            while (s > 0):
                s = s - 1
                i = int(np.floor(np.random.random() * s) - 1)

                if i < 0:
                    i = 0

                temp = coll[s]
                coll[s] = coll[i]
                coll[i] = temp

        self.oldcollection = list(coll)

    def collection_is_valid(self):
        """
        Determines if the collection is valid for this algorithm.
        In this case, a list.
        :return: 2-Tuple: 1: boolean which tells if the collection is a list, the name of the expected type.
        """

        return isinstance(self.oldcollection, list)

    def has_worked(self):
        """
        Determines if the sorting algorithm worked correctly as intended.
        :raise: AlgorithmError if the collection wasn't sorted correctly.
        :return: True if the collection was sorted correctly.
        """

        if self.is_sorted() is False:
            raise AlgorithmError("The algorithm did not sort the collection correctly.")

        return True

    def is_sorted(self, desc=False):
        """
        Determines if a collection has been sorted. Default is ascending order.
        :param desc: Checks collection is sorted in descending order.
        :return: True if collection is sorted in the specified order, false otherwise.
        """

        if desc is True:
            return all(self.newcollection[i] >= self.newcollection[i + 1] for i in range(len(self.newcollection) - 1))
        else:
            return all(self.newcollection[i] <= self.newcollection[i + 1] for i in range(len(self.newcollection) - 1))


class InsertionSort(Sort):
    description = """
An in-place, comparison-based sorting algorithm. It sorts array by shifting elements one by one and inserting the right
element at the right position.
"""

    steps = []
    best_case = ""
    average_case = ""
    worst_case = ""

    def execute(self):
        """
        Sorts a collection by using the insertion sort algorithm.
        """

        length = len(self.newcollection)

        for i in range(1, length):
            key = self.newcollection[i]
            j = i - 1

            while j >= 0 and key < self.newcollection[j]:
                self.newcollection[j + 1] = self.newcollection[j]
                j = j - 1

            self.newcollection[j + 1] = key

    @staticmethod
    def metadata():
        return {
            "description": InsertionSort.description.replace('\n', '')
        }


class TraditionalBubbleSort(Sort):
    def execute(self):
        """
        Sorts a collection by using the traditional bubble sort algorithm.
        """

        length = len(self.newcollection)

        for i in range(length):
            for j in range(length - i - 1):
                if self.newcollection[j] > self.newcollection[j + 1]:
                    temp = self.newcollection[j]
                    self.newcollection[j] = self.newcollection[j + 1]
                    self.newcollection[j + 1] = temp

    @staticmethod
    def metadata():
        return {}


class OptimisedBubbleSort(Sort):
    def execute(self):
        """
        Sorts a collection by using the optimised bubble sort algorithm.
        """

        length = len(self.newcollection)

        for i in range(length):
            swapped = False

            for j in range(0, length - i - 1):
                if self.newcollection[j] > self.newcollection[j + 1]:
                    temp = self.newcollection[j]
                    self.newcollection[j] = self.newcollection[j + 1]
                    self.newcollection[j + 1] = temp
                    swapped = True

            if not swapped:
                break

    @staticmethod
    def metadata():
        return {}


class SelectionSort(Sort):
    def execute(self):
        """
        Sorts a collection using the selection sort algorithm.
        """

        length = len(self.newcollection)

        for i in range(length):
            first = i

            for j in range(i + 1, length):
                if self.newcollection[first] > self.newcollection[j]:
                    first = j

            temp = self.newcollection[i]
            self.newcollection[i] = self.newcollection[first]
            self.newcollection[first] = temp

    @staticmethod
    def metadata():
        return {}


class QuickSort(Sort):
    def partition(self, low, high):
        """
        Sorts current partition
        :param low: lowest index of current partition
        :param high: highest index of current partition
        :return: sorted partition
        """
        index = low - 1
        pivot = self.newcollection[high]

        for i in range(low, high):
            if self.newcollection[i] <= pivot:
                # smaller element's index incremented
                i += 1

                temp = self.newcollection[index]
                self.newcollection[index] = self.newcollection[i]
                self.newcollection[i] = temp

        temp = self.newcollection[index + 1]
        self.newcollection[index + 1] = self.newcollection[high]
        self.newcollection[high] = temp

        return index + 1

class RecursiveQuickSort(QuickSort):
    def execute(self):
        """
        Sorts a collection using the recursive version of the quicksort algorithm.
        """

        self.doIt(0, len(self.newcollection) - 1)

    def doIt(self, low, high):
        """
        Actually sorts the collection.
        :param low: low index of current partition
        :param high: high index of current partition
        :return: sorted array
        """
        if low < high:
            pivot = self.partition(low, high)

            self.doIt(low, pivot - 1)
            self.doIt(pivot + 1, high)

    @staticmethod
    def metadata():
        return {}


class IterativeQuickSort(QuickSort):
    def execute(self):
        """
        Sorts a collection using the iterative version of the quicksort algorithm.
        """

        # Create alternate stack
        size = len(self.newcollection)
        stack = Stack()

        # initialize top of alt stack
        top = -1

        # push initial values
        stack.push(0, size - 1)

        # keep popping from stack if it is not empty
        while stack.pointer >= 0:

            # pop first and last index of partition
            high = stack.pop()
            low = stack.pop()

            # set pivot to it's correct position in order to sort array
            p = self.partition(low, high)

            if p - 1 > low:
                stack.push(low, p - 1)

            if p + 1 < high:
                stack.push(p + 1, high)

        return None

    @staticmethod
    def metadata():
        return {}


class MergeSort(Sort):
    description = """"""
    steps = []
    best_case = "O(n log n)"
    average_case = "O(n log n)"
    worst_case = "O(n log n)"

    @staticmethod
    def metadata():
        return {
            "description": MergeSort.description,
            "steps": dict(list(enumerate(MergeSort.steps, start=1))),
            "best_case": MergeSort.best_case,
            "worst_case": MergeSort.worst_case,
            "average_case": MergeSort.average_case
        }


class TopDownMergeSort(MergeSort):
    def execute(self):
        """Sorts a collection using the top-down implementation of the merge sort."""
        self.newcollection = self.perform_sort(self.newcollection)

    def perform_sort(self, collection):
        """Actually performs the sorting algorithm on the provided collection."""

        size = len(collection)

        if size <= 1:
            return None
        else:
            left = list()
            right = list()

            for i, x in enumerate(collection):
                if i < size / 2:
                    left.append(x)
                else:
                    right.append(x)

            left = self.perform_sort(left)
            right = self.perform_sort(left)

        return self.merge(left, right)

    def merge(self, left, right):
        """Merges two sublists together and returns the ordered union of the two lists."""
        result = list()

        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        return result


# TODO Bottom up approach for merge sort


############### ALGORITHMS TO DO ###############
"""
class Sorts(object):
    @staticmethod
    def mergeSort(self.newcollection):
        return None

    @staticmethod
    def heapSort(self.newcollection):
        return None

    @staticmethod
    def shellSort(self.newcollection):
        return None

    @staticmethod
    def combSort(self.newcollection):
        return None

    @staticmethod
    def countingSort(self.newcollection):
        return None

    @staticmethod
    def bucketSort(self.newcollection):
        return None

    @staticmethod
    def radixSort(self.newcollection):
        return None
"""
