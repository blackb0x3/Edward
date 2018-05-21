from scripts.Algorithm import Algorithm, AlgorithmError
import numpy as np
import matplotlib.pyplot as plt
import random
import string


class Graph(object):

    @staticmethod
    def new(app_root_path: str, algorithm_results: dict):
        execution_times = {}
        for size, algorithms in algorithm_results.items():
            average_execution_time = np.average([algorithm.timetaken.total_seconds() for algorithm in algorithms])
            execution_times.update({size: average_execution_time})

        sizes = execution_times.keys()
        times = execution_times.values()

        plt.plot(sizes, times, 'b')
        plt.xscale('linear')
        plt.yscale('linear')
        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))
        filepath = '/var/www/html/edward/images/graphs/' + filename
        plt.savefig(filepath)

        return filepath
