given_arr = [4, 3, 2, 4, 1, 3, 2]


def find_unique_inmperative(arr):
    unique_arr = []
    duplicate_arr = []

    for el in arr:
        if el not in unique_arr:
            unique_arr.append(el)
        elif el in unique_arr and el not in duplicate_arr:
            duplicate_arr.append(el)

    unique_elements = [el for el in unique_arr if el not in duplicate_arr]

    return unique_elements




print("Результат: ", find_unique(given_arr))

from collections import Counter

given_arr = [4, 3, 2, 4, 1, 3, 2]

def find_unique(arr):
    counter = Counter(arr)
    unique_arr = [el for el, count in counter.items() if count == 1]
    return unique_arr

unique_arr = find_unique(given_arr)
print("Результат: ", unique_arr)
