import os

from config import ROOT_DIR

import numpy as np
import matplotlib.pyplot as plt
import random
import string


class Chart(object):

    @staticmethod
    def new(algorithm_results: dict):
        execution_times = {}
        for size, algorithms in algorithm_results.items():
            average_execution_time = np.average([algorithm.timetaken.total_seconds() for algorithm in algorithms])
            execution_times.update({size: average_execution_time})

        sizes = list(execution_times.keys())
        times = list(execution_times.values())

        plt.plot(sizes, times, 'b')
        plt.xlabel("Collection Size")
        plt.ylabel("Average Execution Time")
        plt.xscale('linear')
        plt.yscale('linear')
        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))
        filepath = os.path.join(ROOT_DIR, 'images/graphs/', filename)
        plt.savefig(filepath + ".png", bbox_inches='tight')

        return filename
