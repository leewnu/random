from random import randint

def create_random_list(size=10, int_max=100): 
    return [randint(0, int_max) for _ in range(size)]


def merge(l1, l2):
    l = []
    l1_idx, l2_idx = 0, 0
    while l1_idx < len(l1) and l2_idx < len(l2):
        if l1[l1_idx] < l2[l2_idx]: 
            l.append(l1[l1_idx])
            l1_idx += 1
        else: 
            l.append(l2[l2_idx])
            l2_idx += 1

    if l1_idx == len(l1): 
        l.extend(l2[l2_idx:])
    else:
        l.extend(l1[l1_idx:])

    return l


def merge_sort(input_list): 
    if len(input_list) <= 1: 
        return input_list
    left, right = merge_sort(input_list[:int(len(input_list)/2)]), merge_sort(input_list[int(len(input_list)/2):])
    return merge(left, right)


random_list = create_random_list(size=11)
print(random_list)

sorted_list = merge_sort(random_list)
print(sorted_list)