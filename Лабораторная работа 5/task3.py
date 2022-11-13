import random


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(set(list_)) != 15:
        random_number = random.randint(-10, 10)
        if random_number not in list_:
            list_.append(random_number)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
