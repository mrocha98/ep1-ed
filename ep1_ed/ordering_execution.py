from random import sample
from typing import List

class OrderingExecution:
  def __init__(self):
    self.quantity = 0
    self.timeSpend = 0

  @staticmethod
  def generateSource() -> List:
    population = 2000
    return sample(range(population), population)
