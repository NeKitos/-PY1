import random


def get_unique_list_numbers(start=-10, end=10) -> list[int]:
    list_ = []
    while len(set(list_)) != 15:
        random_number = random.randint(start, end)
        if random_number not in list_:
            list_.append(random_number)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
