from random import randint


def create_list(len_list):
    list = []
    for i in range(len_list):
        list.append(randint(1, 10))
    return list

def sum_numbers(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_numbers(list[1:])

list = create_list(randint(5, 20))
print(list)
sum = sum_numbers(list)
print(sum)
