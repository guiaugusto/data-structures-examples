elements = [1, 2, 3, 8, 14, 30, 5]

number = input("Say a number to find in the array container: ")

is_valid = False

for i in elements:
    if i == int(number):
        is_valid = True
        break

if is_valid:
    print('The number ' + number + ' exists in the array.')
else:
    print('The number is not in the array container.')
