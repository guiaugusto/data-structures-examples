# Uniformly distributed elements
elements = [i for i in range(0, 100, 2)]

print(elements)

selected_element = int(input('Say a number to find in the array container: '))

inferior = 0
superior = len(elements)

found = False
latest = inferior
meio = inferior

if selected_element < superior:
    while True:
        latest = meio
        meio = int(inferior + (superior - inferior) * ((selected_element-elements[inferior])/(elements[superior-1]-elements[inferior])))

        if meio == latest:
            break

        if selected_element > elements[meio-1]:
            superior = meio
        elif selected_element < elements[meio-1]:
            inferior = meio
        elif selected_element == elements[meio-1]:
            found = True
            break


if not found:
    print('Number {} was not found!'.format(selected_element))
else:
    print('Number {} was found!'.format(selected_element))
