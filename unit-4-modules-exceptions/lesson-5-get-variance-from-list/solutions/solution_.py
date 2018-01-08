# Import the library here (must be python 3.4+)!
try:
  from statistics import variance
except ImportError:
  def variance(a_list):
    mean = sum(a_list) / len(a_list)
    return sum([(x - mean) ** 2 for x in a_list]) / len(a_list)

def get_variance_from_list(a_list):
    return variance(a_list)