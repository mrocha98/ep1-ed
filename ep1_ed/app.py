from time import time

from ep1_ed.ordering_algorithms import mergesort, quicksort, selection, native, OrderingAlgorithm
from ep1_ed.ordering_execution import OrderingExecution

def countTimeSpendWith(algorithm, items):
    start = time()
    algorithm(items)
    end = time()

    return end - start

def main():
  numbers = []
  scores = {
    OrderingAlgorithm.MERGESORT: OrderingExecution(),
    OrderingAlgorithm.QUICKSORT: OrderingExecution(),
    OrderingAlgorithm.SELECTION: OrderingExecution(),
    OrderingAlgorithm.NATIVE: OrderingExecution()
  }
  t_start = time()
  t_end = time() + 5
  quantity = 2000
  while time() < t_end:
    print(f'QTD: {quantity}')

    numbers.extend(OrderingExecution.generateSource())

    # print(f'mergesort: {round(countTimeSpendWith(mergesort, numbers), 3)}')
    # print(f'quicksort: {round(countTimeSpendWith(quicksort, numbers), 3)}')
    # print(f'selection: {round(countTimeSpendWith(selection, numbers), 3)}')
    # print(f'native: {round(countTimeSpendWith(native, numbers), 5)}')

    quantity += 2000

  print(f'time elapsed: {time() - t_start}')
