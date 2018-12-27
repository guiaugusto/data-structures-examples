# Uniformly distributed elements
elements = [i for i in range(100)]

print(elements)

selected_element = int(input('Say a number to find in the array container: '))

inferior = 0
superior = 100

found = False
latest = inferior
i = inferior

if selected_element < superior:
    while True:
        latest = i
        i = int(inferior + (superior - inferior) * ((selected_element-elements[inferior])/(elements[superior-1]-elements[inferior])))

        if latest == i:
            break
        
        if elements[i-1] == selected_element:
            found = True
            break        

if not found:
    print('Number {} was not found!'.format(selected_element))
else:
    print('Number {} was found!'.format(selected_element))
