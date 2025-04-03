import timeit

def take_first(my_list):
  return my_list[0]

short_list = [13, 25, 42]
print(timeit.timeit('take_first(short_list)', globals=globals(),number=10000000))

long_list = [42] * 10**8
print(timeit.timeit('take_first(long_list)', globals=globals(),number=10000000))