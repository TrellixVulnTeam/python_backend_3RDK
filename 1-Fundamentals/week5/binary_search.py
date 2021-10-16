def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound) // 2
        if the_list[mid_point] == target:
            return mid_point
        elif the_list[mid_point] < target:
            lower_bound = mid_point + 1
        else:
            upper_bound = mid_point - 1

    return -1

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list, 10))
print(binary_search(test_list, 4))
print(binary_search(test_list, 33))