import os

from config import ROOT_DIR, algorithm_names
from datetime import datetime, timedelta

import numpy as np
import matplotlib.pyplot as plt
import random
import string


class Chart(object):
    @staticmethod
    def new(data: dict):
        raise NotImplementedError("Please use a more specific chart: TestChart or CompareChart")

    @staticmethod
    def save():
        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(30))
        filepath = os.path.join(ROOT_DIR, 'images/graphs/', filename)
        plt.savefig(filepath + '.png', bbox_inches='tight')

        return filename


class TestChart(Chart):
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
        
        return Chart.save()


class CompareChart(object):
    @staticmethod
    def new(results: dict, original_algorithm: str, other_algorithms: set):
        original_algorithm_name = algorithm_names[original_algorithm]

        original_algorithm_result_set = results["original_algorithm"]["result"]
        other_algorithm_result_sets = results["other_algorithms"]

        times = dict()

        times[original_algorithm_name] = np.average([
            result.timetaken.total_seconds() for result in original_algorithm_result_set
        ])
        
        for k, res in other_algorithm_result_sets.items():
            times[algorithm_names[k]] = np.average([
                res.timetaken.total_seconds()
            ])

        barplot = plt.bar(range(len(times)), list(times.values()), align="center", color=(0.5, 0.5, 0.5, 1))
        plt.xticks(range(len(times)), list(times.keys()))

        i = 1

        baseline = times[original_algorithm_name]
        vs = list(times.values())

        while i < len(barplot):
            curr_time = vs[i]

            if curr_time <= baseline / 2:
                barplot[i].set_color('b')

            elif curr_time <= baseline:
                barplot[i].set_color('g')

            elif curr_time >= baseline * 1.5:
                barplot[i].set_color('r')

            elif curr_time >= baseline:
                barplot[i].set_color('y')

            i += 1

        plt.xlabel("Algorithm")
        plt.ylabel("Average Execution Time (seconds)")
        plt.title("Comparing {0} against similar algorithms".format(original_algorithm_name))

        return Chart.save()
