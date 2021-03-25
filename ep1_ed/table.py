def print_table_border():
  print('-'*81)

def print_table_header():
  print_table_border()
  print('\t\t|\t\t\ttime (s)\t\t\t\t|')
  print_table_border()
  print('\t\t|\tMergesort\tQuicksort\tSelection\tNative\t|')

def print_table_row(quantity: int, mergesort_time: float, quicksort_time: float, selection_time: float, native_time: float):
  print(f'{quantity}\t\t|', end='')
  print(f'\t{mergesort_time:.3f}', end='\t')
  print(f'\t{quicksort_time:.3f}', end='\t')
  print(f'\t{selection_time:.3f}', end='\t')
  print(f'\t{native_time:.3f}', end='\t|\n')

def print_table_footer():
  print_table_border()
