from typing import List
from enum import Enum

class OrderingAlgorithm(Enum):
  MERGESORT = 'mergesort'
  QUICKSORT = 'quicksort'
  SELECTION = 'selection'
  NATIVE = 'native'

def mergesort(v: List[int]):
  if len(v) <= 1: return v
  else:
    m = len(v) // 2
    e = mergesort(v[:m])
    d = mergesort(v[m:])
    return merge(e, d)

def merge(e, d):
  r = []
  i, j = 0, 0
  while i < len(e) and j < len(d):
    if e[i] <= d[j]:
      r.append(e[i])
      i += 1
    else:
      r.append(d[j])
      j += 1
  r += e[i:]
  r += d[j:]
  return r

def quicksort(v: List[int]):
  if len(v) <= 1: return v
  pivô = v[0]
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x <  pivô]
  maiores = [x for x in v if x >  pivô]
  return quicksort(menores) + iguais + quicksort(maiores)

def selection(v: List[int]):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r

def native(v: List[int]):
  items = v.copy()
  items.sort()
  return items
