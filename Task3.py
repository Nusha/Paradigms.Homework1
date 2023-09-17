def find_miss_repeat_imperative(arr, n):
    final_array = [0 for i in range(n)]
    repeating, missing = 0, 0
    for i in arr:
        if final_array[i - 1] == 1:
            repeating = i
        else:
            final_array[i - 1] = 1
    for i in range(len(final_array)):
        if final_array[i] == 0:
            missing = i + 1
            break
    return repeating, missing

def getTwoElements_declarative(arr, n):
    xor1 = arr[0]
    for i in range(1, n):
        xor1 = xor1 ^ arr[i]
    for i in range(1, n + 1):
        xor1 = xor1 ^ i
    set_bit_no = xor1 & ~(xor1 - 1)
    x = y = 0
    for i in range(n):
        if (arr[i] & set_bit_no) != 0:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    for i in range(1, n + 1):
        if (i & set_bit_no) != 0:
            x = x ^ i
        else:
            y = y ^ i
    return x, y

arr = [2, 3, 1, 5, 3]

repeating, missing = find_miss_repeat_imperative(arr, 5)
x, y = getTwoElements_declarative(arr, 5)

print("Повторяющееся число:", repeating)
print("Пропущенное число:", missing)
print("Повторяющееся число:", x)
print("Пропущенное число:", y)