from random import randint


def create_list(len_list):
    list = []
    for i in range(len_list):
        list.append(randint(1, 10))
    return list
def next_element(lst):
    index = [0]

    def get_next():
        result = None
        if index[0] < len(lst):
            result = lst[index[0]]
            index[0] += 1
        return result
    return get_next

lst = create_list(randint(5, 20))
print(lst)
next = next_element(lst)
for i in range(len(lst)):
    print(next())



