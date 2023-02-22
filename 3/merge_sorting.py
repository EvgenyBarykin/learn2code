heights = [5, 566, 2343, 672, -5245, 545]


# сливаем массивы
def merge(left, right):
    sorted_list = []
    left_pos = 0
    right_pos = 0
    while (left_pos < len(left) and right_pos < len(right)):
        if left[left_pos] < right[right_pos]:
            sorted_list.append(left[left_pos])
            left_pos += 1
        else:
            sorted_list.append(right[right_pos])
            right_pos += 1
    if left_pos == len(left):
        sorted_list.extend(right[right_pos::])
    else:
        sorted_list.extend(left[left_pos::])
    return sorted_list


# делим массивы
def mergesort(heights):
    if len(heights) <= 1:
        return heights

    center = len(heights) // 2
    left = mergesort(heights[:center])
    right = mergesort(heights[center:])

    heights = merge(left, right)
    return heights


result = mergesort(heights)
print(result)


