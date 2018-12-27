import random

elements = random.sample(range(1000), 10)

print('There is a list of elements builded!')

print(elements)

number = int(input('Say a number to find in the array container: '))

found = False

for i in range(0, len(elements)):
    print(elements[i])
    if elements[i] == number:
        tmp = elements[i-1]
        elements[i-1] = elements[i]
        elements[i] = tmp
        found = True

if not found:
    print('The element {} was not found!'.format(number))
else:
    print('The element {} was found!'.format(number))
    print('There is the new list ordered by transposition!')
    print(elements)