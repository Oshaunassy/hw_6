def bubble_sort(number):
    n = len(number)
    for i in range(n - 1):
        for j in range(n - 1):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    return number


number = [256, 354, 548, 145, 99, 52]
sorted_list = bubble_sort(number)

print(f'sorted list by bubble_sort {sorted_list}')

n = len(number)
element_to_found = 99
result = False
first = 0
last = n - 1
while first <= last:
    middle = (first + last) // 2
    if element_to_found == number[middle]:
        result = True
        pos = middle
        break
    elif element_to_found > number[middle]:
        first = middle + 1
    else:
        last = middle - 1

if result:
    print(f'Element {element_to_found} has found {pos} index in number')
else:
    print('Element has not found')


def binary_search(number, element_of_found):
    left, right = 0, len(number) - 1

    while left <= right:
        middle = (left + right) // 2
        if number[middle] == element_of_found:
            return middle
        elif number[middle] < element_of_found:
            left = middle + 1
        else:
            right = middle - 1
    return -1


element_to_found = 145
result = binary_search(number, element_to_found)

n = len(number)
if result != -1:
    print(f'Element {element_to_found} was find by index {result}')
else:
    print(f'Element {element_to_found} has not found in list')
