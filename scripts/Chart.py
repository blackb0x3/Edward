import os

from config import ROOT_DIR, algorithm_names
from datetime import datetime, timedelta

import numpy as np
import matplotlib.pyplot as plt
import random
import string

class TestChart(object):
    @staticmethod
    def new(algorithm_results: dict):
        execution_times = {}
        for size, algorithms in algorithm_results.items():
            average_execution_time = np.average([algorithm.timetaken.total_seconds() for algorithm in algorithms])
            execution_times.update({size: average_execution_time})

        sizes = list(execution_times.keys())
        times = list(execution_times.values())

        plt.plot(sizes, times, 'bo')
        plt.xlabel("Collection Size")
        plt.ylabel("Average Execution Time (seconds)")
        plt.xscale('linear')
        plt.yscale('linear')

        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))
        filepath = os.path.join(ROOT_DIR, 'images/graphs/', filename)
        plt.savefig(filepath + ".png", bbox_inches='tight')

        return filename


class CompareChart(object):
    @staticmethod
    def new(two_results: dict):
        first_algorithm_set = two_results["first_algorithm"]["result"]
        second_algorithm_set = two_results["second_algorithm"]["result"]

        first_algorithm_name = algorithm_names[two_results["first_algorithm"]["name"]]
        second_algorithm_name = algorithm_names[two_results["second_algorithm"]["name"]]

        names = (first_algorithm_name, second_algorithm_name)

        first_average_execution_time = np.average([
            result.timetaken.total_seconds() for result in first_algorithm_set
        ])
        
        second_average_execution_time = np.average([
            result.timetaken.total_seconds() for result in second_algorithm_set
        ])

        times = (first_average_execution_time, second_average_execution_time)

        alg_ticks = np.arange(len(names))

        plt.bar(alg_ticks, times, align="center")
        plt.xticks(alg_ticks, names)
        plt.xlabel("Algorithm")
        plt.ylabel("Average Execution Time (seconds)")
        plt.title("Comparison of {0} and {1}".format(names[0], names[1]))

        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))
        filepath = os.path.join(ROOT_DIR, 'images/graphs/', filename)
        plt.savefig(filepath + ".png", bbox_inches='tight')

        return filename
