any_list = [1, 4, 5, 6, 12, 4, 7]

for j in range(len(any_list)-1):
    already_sorted = True
    for i in range(len(any_list)-1):
        if any_list[i] > any_list[i+1]:
            any_list[i], any_list[i+1] = any_list[i+1], any_list[i]
            already_sorted = False
    if already_sorted:
        break
print(any_list)
