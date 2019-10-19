from functools import lru_cache

def flatten(array):
    all_types = list(map(lambda x: type(x) != list, array))
    if all(all_types):
        return array
    else:
        index = all_types.index(False)
        return array[:index] + flatten(array[index]) + flatten(array[index+1:])
