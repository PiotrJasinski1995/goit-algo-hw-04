import numpy as np
from timeit import default_timer as timer
from timeit import timeit
from datetime import timedelta


# defining data to sort
small_data = np.random.random_sample(size = 100)
medium_data = np.random.random_sample(size = 10000)
large_data = np.random.random_sample(size = 40000)


# defining decorator for time measuring
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = func(*args, **kwargs)
        end_time = timer()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper


# defining functions for merge sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

# If there are elements left in the left or right half, 
		# add them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


@measure_execution_time
def merge_sort_decorated(lst):
    data_list = merge_sort(lst)
    return data_list


# defining functions for insertion sort
@ measure_execution_time
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


# defining function for Timsort
@measure_execution_time
def timsort(lst):
    data_list = sorted(lst)
    return data_list


# small data
print('For small data:')
merge_sort_decorated(small_data)
insertion_sort(small_data)
timsort(small_data)

# medium data
print('\nFor medium data:')
merge_sort_decorated(medium_data)
insertion_sort(medium_data)
timsort(medium_data)

# large data
print('\nFor large data:')
merge_sort_decorated(large_data)
insertion_sort(large_data)
timsort(large_data)
