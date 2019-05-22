from scripts.Algorithm import Algorithm, AlgorithmError
import numpy as np


class OneDimensionalSearch(Algorithm):
    """
    Base class for algorithms searching in linear space complexity (lists, arrays etc.)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self, args, kwargs)

        self.value_to_find = kwargs.get('find')

        self.output = {
            "value_to_find" : self.value_to_find,
              "value_found" : False,
                 "found_at" : -1
        }

    def generate_collection(self, *args, **kwargs):
        """
        Generates a list for a linear search algorithm.
        :param args: Ordered list of args.
        :param kwargs: Keyword args.
        :return: The generated collection.
        """

        list_min = kwargs.get('min', 1)
        list_max = kwargs.get('max', 1000)
        size = kwargs.get('size', 10)

        # pick random integers for the list between given min and max numbers from request
        coll = [int(v) for v in np.random.choice(range(list_min, list_max + 1), size)]

        shuffles = 5

        # shuffle collection 5 times using fisher yates
        while shuffles > 0:
            s = size

            while s > 0:
                s = s - 1
                i = int(np.floor(np.random.random() * s) - 1)

                if i < 0:
                    i = 0

                coll[s], coll[i] = coll[i], coll[s]

            shuffles -= 1

        self.oldcollection = list(coll)

    def collection_is_valid(self):
        """
        Determines if the collection is valid for this algorithm.
        In this case, a list.
        :return: True if the collection is a list, False otherwise.
        """

        return isinstance(self.oldcollection, list)

    def has_worked(self):
        """
        Determines if the search algorithm worked correctly.
        This is achieved by checking whether the algorithm
        correctly identified whether the value could be found or not.
        """

        if self.output["value_found"] is True and self.output["found_at"] > -1:
            return True
        elif self.output["value_found"] is False and self.output["found_at"] == -1 and self.value_to_find not in self.oldcollection:
            return True

        return False


class LinearSearch(OneDimensionalSearch):
    def execute(self):
        """
        Executes the linear search algorithm on the list.
        """
        size = len(self.oldcollection)
        c = 0

        while c < size:
            if self.oldcollection[c] == self.value_to_find:
                self.output["value_found"] = True
                self.output["found_at"] = self.oldcollection[c]
                return
            c += 1


class BilinearSearch(OneDimensionalSearch):
    def execute(self):
        """
        Executes the bilinear search algorithm on the list.
        """
        size = len(self.oldcollection)
        c_left = 0
        c_right = -1

        while c_left < size // 2:
            if self.oldcollection[c_left] == self.value_to_find:
                self.output["value_found"] = True
                self.output["found_at"] = self.oldcollection[c_left]
                return
            elif self.oldcollection[c_right] == self.value_to_find:
                self.output["value_found"] = True
                self.output["found_at"] = self.oldcollection[c_right]
                return
            c_left += 1
            c_right -= 1


class BinarySearch(OneDimensionalSearch):
    def execute(self):
        """
        Executes the binary search algorithm on the list - assuming it is sorted!
        """
        size = len(self.oldcollection)
        c_left = 0
        c_right = size - 1

        while c_left <= c_right:
            pivot = np.floor((c_left + c_right) / 2)

            if self.oldcollection[pivot] < self.value_to_find:
                c_left = pivot + 1
            elif self.oldcollection[pivot] > self.value_to_find:
                c_right = pivot - 1
            else:
                self.output["value_found"] = True
                self.output["found_at"] = self.oldcollection[pivot]
                return


class TernarySearch(OneDimensionalSearch):
    def execute(self):
        """
        Executes the ternary search algorithm on the list - assuming it is sorted!
        """
        # TODO - this looks ridiculously over-complicated to do right now. Come back later!
        raise NotImplementedError("Unavailable. Implementation is not ready yet.")
