import random as rn

# Creating array with random integers
my_list = [rn.randint(1, 50) for _ in range(10)]
print(my_list)

# Imperative method of quicksorting
def sort_list_imperative(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less = [i for i in numbers[1:] if i <= pivot]
        greater = [i for i in numbers[1:] if i > pivot]
        return sort_list_imperative(less) + [pivot] + sort_list_imperative(greater)


# Declarative method, using built-in function
def sort_list_declarative(numbers):
    return sorted(numbers)

print(sort_list_imperative(my_list))

print(sort_list_declarative(my_list))