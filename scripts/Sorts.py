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

    def execute(self):
        """
        Executes this algorithm's steps on the provided collection.
        """

        raise NotImplementedError("Please use a specific sort algorithm's execute() function.")

    @staticmethod
    def metadata():
        """
        Returns the algorithm's metadata - space complexity, time complexity, algorithm description etc.
        """

        raise NotImplementedError("Please use a specific sort algorithm's metadata() function.")


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
        """
        Sorts a collection using the top-down implementation (i.e. using recursion) of the merge sort.
        :return: The sorted collection.
        """
        self.newcollection = self.perform_sort(self.newcollection)

    def perform_sort(self, collection):
        """
        Actually performs the sorting algorithm on the provided collection.
        :param collection: The collection to be sorted.
        :return: The sorted collection, after merging is completed.
        """

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
        """
        Merges two sublists together and returns the ordered union of the two lists.
        :param left: The first sublist.
        :param right: The second sublist.
        :return: The merged collection.
        """
        result = list()

        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        return result


class BottomUpMergeSort(MergeSort):
    def execute(self):
        """
        Sorts a collection using the bottom-up implementation (i.e. using iteration) of the merge sort.
        :return: The sorted list.
        """
        current_size = 1

        while current_size < len(self.newcollection) - 1:

            left = 0

            while left < len(self.newcollection) - 1:

                mid = left + current_size - 1

                right = ((2 * current_size + left - 1, len(self.newcollection) - 1)[2 * current_size + left - 1 > len(self.newcollection)-1])
                self.merge(left, mid, right)
                left = left + (current_size * 2)

            current_size *= 2

    def merge(self, left, mid, right):
        """
        Merges all sublists together to form the sorted array.
        :param left: Lower bound.
        :param mid: Middle value.
        :param right: Upper bound.
        :return: A merged collection.
        """
        n1 = mid - left + 1
        n2 = right - mid
        L = [0] * n1
        R = [0] * n2

        for i in range(0, n1):
            L[i] = self.newcollection[left + i]

        for i in range(0, n2):
            R[i] = self.newcollection[mid + i + 1]

        i, j, k = 0, 0, left

        while i < n1 and j < n2:
            if L[i] > R[j]:
                self.newcolllection[k] = R[j]
                j += 1
            else:
                self.newcollection[k] = L[i]
                i += 1
            k += 1

        while i < n1:
            self.newcollection[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            self.newcollection[k] = R[j]
            j += 1
            k += 1


class HeapSort(Sort):
    description = """"""
    steps = []
    best_case = ""
    average_case = ""
    worst_case = ""

    @staticmethod
    def metadata():
        return {
            "description": HeapSort.description,
            "steps": dict(list(enumerate(HeapSort.steps, start=1))),
            "best_case": HeapSort.best_case,
            "worst_case": HeapSort.worst_case,
            "average_case": HeapSort.average_case
        }

    def execute(self):
        """
        Executes the heap sort algorithm on the provided collection.
        :return: The sorted collection.
        """

        size = len(self.newcollection)

        for i in range(size, -1, -1):
            self.heapify(self.newcollection, size, i)

        for i in range(size - 1, 0, -1):
            self.newcollection[i], self.newcollection[0] = self.newcollection[0], self.newcollection[i]
            self.heapify(self.newcollection, i, 0)

    def heapify(self, collection, heap_size, root_index):
        """
        Creates a max-heap from the provided collection.
        :param collection: The collection to transform into a max-heap.
        :param heap_size: The size of the heap.
        :param root_index: The root index of the subtree to be heapified.
        :return: The generated max-heap.
        """

        largest = root_index

        left  = 2 * root_index + 1
        right = 2 * root_index + 2

        if left < heap_size and collection[root_index] < collection[left]:
            largest = left

        if right < heap_size and collection[largest] < collection[right]:
            largest = right

        if largest != root_index:
            collection[root_index], collection[largest] = collection[largest], collection[root_index]  # swap
            self.heapify(collection, heap_size, largest)


class ShellSort(Sort):
    description = """"""
    steps = []
    best_case = ""
    average_case = ""
    worst_case = ""

    @staticmethod
    def metadata():
        return {
            "description": ShellSort.description,
            "steps": dict(list(enumerate(ShellSort.steps, start=1))),
            "best_case": ShellSort.best_case,
            "worst_case": ShellSort.worst_case,
            "average_case": ShellSort.average_case
        }

    def execute(self):
        """
        Executes the shell sort algorithm on the provided collection.
        :return: The sorted collection.
        """
        size = len(self.newcollection)
        gap = size / 2

        while gap > 0:
            for i in range(gap, size):
                temp = self.newcollection[i]
                j = i

                # shift earlier gap-sorted elements up until the correct
                # location is found
                while j >= gap and self.newcollection[j - gap] > temp:
                    self.newcollection[j] = self.newcollection[j - gap]
                    j -= gap

                # original element is now in its correct location
                self.newcollection[j] = temp
            gap /= 2


############### ALGORITHMS TO DO ###############
"""
class Sorts(object):
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
