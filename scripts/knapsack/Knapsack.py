from models.Knapsack import KnapsackCollection, KnapsackItem
from scripts.Algorithm import Algorithm, AlgorithmError

import random

class KnapsackAlgorithm(Algorithm):
    """
    Base class for algorithms involving the knapsack data structure.
    """

    def _build_knapsack(self, min_cost, max_cost, min_val, max_val, size):
    	items = []

    	cost_step = (min_cost + max_cost) // size
    	val_step = (min_val + max_val) // size

    	current_cost = min_cost
    	current_val = min_val

    	i = size

    	while i > 0:
    		rand_cost = random.randint(current_cost, current_cost + cost_step)
    		rand_val = random.randint(current_val, current_val + val_step)

    		items.append(KnapsackItem(rand_cost, rand_val))

    		current_cost += cost_step
    		current_val += val_step

    		i -= 1

    	return KnapsackCollection(items)

    def _parse_knapsack(knapsack_obj):
    	return KnapsackCollection()

    def generate_collection(self, *args, **kwargs):
    	"""
    	Generates a knapsack for a knapsack algorithm.
    	:param min_cost: The minimum possible cost of each knapsack item.
    	:param max_cost: The maximum possible cost of each knapsack item.
    	:param min_val: The minimum possible value of each knapsack item.
    	:param max_val: The maximum possible value of each knapsack item.
    	:param size: The number of items in the knapsack.
    	:return The generated knapsack.
    	"""

    	if kwargs.get('knapsack', None) is not None:
    		self.oldcollection = self._parse_knapsack(kwargs.get('knapsack'))

    	else:
	    	min_cost = kwargs.get('min_cost', 1)
	    	max_cost = kwargs.get('max_cost', 50)

	    	if min_cost > max_cost:
	    		raise ValueError("min_cost must be less than max_cost! min_cost is {0}, max_cost is {1}".format(min_cost, max_cost))

	    	min_val = kwargs.get('min_val', 1)
	    	max_val = kwargs.get('max_val', 50)

	    	if min_val > max_val:
	    		raise ValueError("min_val must be less than max_val! min_val is {0}, max_val is {1}".format(min_val, max_val))

	    	size = kwargs.get('size', 10)

	    	self.oldcollection = self._build_knapsack(min_cost, max_cost, min_val, max_val, size)

	def collection_is_valid(self):
		"""
		Determine if the collection is valid for this algorithm.
		In this case, a knapsack.
		:return: True if the collection is a SORTED knapsack, False otherwise.
		"""

		return isinstance(self.oldcollection, KnapsackCollection)

	def has_worked(self):
		"""
		Determines if the knapsack algorithm worked correctly as intended.
		:raise: AlgorithmError if the collection didn't work correctly.
		:return: True if the collection produced the correct result, False otherwise.
		"""

		raise NotImplementedError("Please use a specific knapsack algorithm's has_worked() function.")

	def execute(self):
		"""
		Executes this algorithm's steps on the provided knapsack.
		"""

		raise NotImplementedError("Please use a specific knapsack algorithm's execute() function.")

	@staticmethod
	def metadata():
		"""
		Returns the algorithm's metadata - space complexity, time complexity, algorithm description etc.
		"""

		raise NotImplementedError("Please use a specific knapsack algorithm's metadata() function.")


class DPZeroOneKnapsackAlgorithm(KnapsackAlgorithm):
	"""
	Class which models DP implementation of solving the knapsack problem.

	:return: The list of knapsack items which yield the highest value given the cost constraint.
	"""

	pass

