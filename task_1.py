from random import randint


def create_list(len_list):
    list = []
    for i in range(len_list):
        list.append(randint(1, 10))
    return list

def print_numbers(list):
    if len(list) == 0:
        return 'element is over'
    if list[0] % 2 != 0:
        print(list[0])
    print_numbers(list[1:])

list = create_list(randint(5, 20))
print(list)
print_numbers(list)
