elements = [1, 2, 3, 8, 14, 30, 5]

number = input("Say a number to find in the array container: ")

elements.append(int(number))

i = 0

while elements[i] != int(number):
    i += 1

if i == len(elements) - 1:
    print('The number is not in the array container.')
else:
    print('The number ' + number + ' exists in the array.') 
