import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

algorithm_names = {
    "insertion-sort":          "Insertion Sort",
    "selection-sort":          "Selection Sort",
    "optimised-bubble-sort":   "Optimised Bubble Sort",
    "traditional-bubble-sort": "Traditional Bubble Sort",
    "recursive-quick-sort":    "Recursive Quick Sort",
    "iterative-quick-sort":    "Iterative Quick Sort",
    "top-down-merge-sort":     "Top Down Merge Sort",
    "bottom-up-merge-sort":    "Bottom Up Merge Sort",
    "heap-sort":               "Heap Sort",
    "shell-sort":              "Shell Sort",
    "counting-sort":           "Counting Sort",
    "bucket-sort":             "Bucket Sort",
}

DEFAULT_MIN_COLLECTION_SIZE = 5
DEFAULT_MAX_COLLECTION_SIZE = 10
ABS_MIN_COLLECTION_SIZE = 0
