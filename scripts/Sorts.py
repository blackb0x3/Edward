from scripts.Algorithm import Algorithm, AlgorithmError

class Sort(Algorithm):
    """
    Base class for sorting algorithms.
    """

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
            for j in range(0, length - i - 1):
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


############### ALGORITHMS TO DO ###############
"""
class Sorts(object):
    @staticmethod
    def selectionSort(self.newcollection):
        return None

    @staticmethod
    def mergeSort(self.newcollection):
        return None

    @staticmethod
    def heapSort(self.newcollection):
        return None

    @staticmethod
    def quickSort(self.newcollection):
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
