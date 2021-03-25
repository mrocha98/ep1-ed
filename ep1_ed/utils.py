from time import time
from random import sample
from typing import List

def generate_source() -> List[int]:
    population = 2000
    return sample(range(population), population)

def count_time_spend_with(algorithm, items: List[int]) -> float:
    start = time()
    algorithm(items)
    end = time()

    return end - start
