from scripts.Algorithm import Algorithm, AlgorithmError


class LinearSearch(Algorithm):
    """
    Base class for algorithms searching in linear space complexity (lists, arrays etc.)
    """

    def __init__(self, *args, **kwargs):
        self.output = list()
        self.value_to_find = kwargs.get('find')
        super().__init__(self, args, kwargs)

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

        coll = [int(v) for v in np.random.choice(range(list_min, list_max + 1), size)]

        shuffles = 5

        # shuffle collection 5 times using fisher yates
        for x in range(shuffles):
            s = size

            while s > 0:
                s = s - 1
                i = int(np.floor(np.random.random() * s) - 1)

                if i < 0:
                    i = 0

                coll[s], coll[i] = coll[i], coll[s]

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

        if self.output[0] is True and self.output[1] == self.value_to_find:
            return True
        elif self.output[0] is False and self.output[1] is None and self.value_to_find is None:
            return True

        return False

