from datetime import datetime
import copy
import numpy as np
import random

class Algorithm:
    """
    Base algorithm class.
    """

    def __init__(self, data=None):
        """
        Algorithm constructor
        :param data: The collection to perform the algorithm on.
        """

        if data is None or not data:
            self.generate_collection()
        else:
            self.oldcollection = data
            self.starttime = None
            self.endtime = None
            self.timetaken = None
            self.newcollection = None
            self.executed = False

    def run(self):
        """
        Performs algorithm's pre-execution and post-execution steps.
        :return: self
        """

        try:
            if self.executed is False:
                self.newcollection = copy.deepcopy(self.oldcollection)
                self.starttime = datetime.now()
                self.execute()
                self.executed = self.has_worked()
                self.endtime = datetime.now()
                self.timetaken = self.endtime - self.starttime
        except AlgorithmError as err:
            print("Algorithm runtime error:", err)
        finally:
            return self

    def has_worked(self):
        """
        Determines if the algorithm worked or not.
        """

        raise NotImplementedError("Please use the algorithm's implemented has_worked() function.")

    def execute(self):
        """
        Executes the algorithm's steps on the provided collection.
        """

        raise NotImplementedError("Please use the algorithm's implemented execute() function.")

    def generate_collection(self, min=1, max=1000, size=10):
        coll = np.random.sample(range(min, max + 1), size)

        s = size

        while (s > 0):
            s = s - 1
            i = np.floor(random.random() * s)

            temp = coll[s]
            coll[s] = coll[i]
            coll[i] = temp

        self.oldcollection = coll

    @staticmethod
    def metadata():
        """
        Returns the algorithm's metadata - space complexity, time complexity, algorithm description etc.
        """

        raise NotImplementedError("Please use the algorithm's implemented metadata() function.")


class AlgorithmError(Exception):
    """
    Base exception for errors thrown by algorithms.
    """

    def __init__(self, algorithm, msg=None):
        if msg is None:
            # default message
            msg = "An error occurred in the algorithm %s" % algorithm

        super(AlgorithmError, self).__init__(msg)
        self.algorithm = algorithm
