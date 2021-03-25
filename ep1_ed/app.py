from time import time

from ep1_ed.ordering_algorithms import mergesort, quicksort, selection, native, OrderingAlgorithm
from ep1_ed.utils import generate_source, count_time_spend_with
from ep1_ed.table import print_table_header, print_table_row, print_table_footer

def main():
  numbers = []
  spend_time = {
    OrderingAlgorithm.MERGESORT: 0,
    OrderingAlgorithm.QUICKSORT: 0,
    OrderingAlgorithm.SELECTION: 0,
    OrderingAlgorithm.NATIVE: 0
  }
  quantity = 0

  print_table_header()

  time_start = time()
  time_execution_limit = time() + 30

  while time() < time_execution_limit:
    numbers.extend(generate_source()) # adds 2000 random numbers
    quantity += 2000

    spend_time[OrderingAlgorithm.MERGESORT] = count_time_spend_with(mergesort, numbers)
    spend_time[OrderingAlgorithm.QUICKSORT] = count_time_spend_with(quicksort, numbers)
    spend_time[OrderingAlgorithm.SELECTION] = count_time_spend_with(selection, numbers)
    spend_time[OrderingAlgorithm.NATIVE] = count_time_spend_with(native, numbers)

    print_table_row(
      quantity,
      spend_time[OrderingAlgorithm.MERGESORT],
      spend_time[OrderingAlgorithm.QUICKSORT],
      spend_time[OrderingAlgorithm.SELECTION],
      spend_time[OrderingAlgorithm.NATIVE]
    )
  print_table_footer()
  print(f'\n\ntime elapsed: {time() - time_start}')
