from datetime import datetime
import copy

class Algorithm:
    """
    Base algorithm class.
    """

    description = ""
    steps = []
    best_case = ""
    average_case = ""
    worst_case = ""

    def __init__(self, *args, **kwargs):
        """
        Algorithm constructor
        """

        data = kwargs.get('data', None)
        size = kwargs.get('size', 10)

        if data is None or not data:
            self.generate_collection(size=size)
        else:
            self.oldcollection = data

        self.starttime = None
        self.endtime = None
        self.timetaken = None
        self.newcollection = None
        self.executed = False

    def __dict__(self):
        return {
            "successful_execution": self.executed,
            "input": self.oldcollection,
            "output": self.newcollection,
            "execution_start": self.starttime.strftime("%Y-%m-%d %H:%M:%S"),
            "execution_end": self.endtime.strftime("%Y-%m-%d %H:%M:%S"),
            "execution_time": str(self.timetaken)
        }

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
        except RuntimeError as run_err:
            print("Error: ", run_err)

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

    def generate_collection(self, *args, **kwargs):
        """
        Generates a collection for the algorithm to use.
        This could be a dictionary, an array, a linked list etc.
        """

        raise NotImplementedError("Please use the algorithm's implemented generate_collection() function.")

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
