import numpy as np
import matplotlib
from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print()
    

def ListSorter(array):
    sortedlist = [1]
    n = len(array)
    for x in range(n):
        already_sorted = True
        for j in range(n - x - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array
   
if __name__ == "__main__":
    array = [5,2,1,6,2,3,9,7,8,11]
    run_sorting_algorithm(algorithm="ListSorter", array=array)
