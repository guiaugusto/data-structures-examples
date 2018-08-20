import random

# Método para realizar busca binária
def busca_binaria(list_elements, element):
    inicio = 0
    fim = len(list_elements)
    pivo = int((inicio+fim)/2)

    while inicio+1 != fim:

        if(element < list_elements[pivo]):
            fim = pivo
            pivo = int((inicio+fim)/2)
        elif(element > list_elements[pivo]):
            inicio = pivo
            pivo = int((inicio+fim)/2)
        else:
            return True

# Método para realizar busca sequencial comum

# Método para realizar busca sequencial com sentinela

# Método para realizar busca sequencial pelo método mover-para-frente

# Método para realizar busca sequencial pelo método da transposição

# Método para realizar busca sequencial indexada

# Método para realizar busca sequencial duplamente indexada

# Método para inserir elementos dentro do vetor a ser utilizado
def insere_elementos_ordenados(number_of_elements, list_elements, limit):
    i = number_of_elements
    while i >= 0:
        list_elements.append(i)
        i-=1

def insere_elementos_desordenados(number_of_elements, list_elements, limit):
    for x in range(number_of_elements):
        value = random.randint(1, limit)

        while(value in list_elements):
            value = random.randint(1, limit)

        list_elements.append(value)


# Método para ordenar os elementos utilizando o algoritmo QuickSort
def ordena_elementos(list_elements, ponteiro_inicio, ponteiro_fim):
    inicio = ponteiro_inicio
    fim = ponteiro_fim-1
    pivo = int((ponteiro_inicio+ponteiro_fim)/2)

    while inicio <= fim:
        while list_elements[inicio] < list_elements[pivo]:
            inicio += 1

        while list_elements[fim] > list_elements[pivo]:
            fim -= 1

        if inicio <= fim:
            temporario = list_elements[inicio]
            list_elements[inicio] = list_elements[fim]
            list_elements[fim] = temporario
            # print('Trocou {} por {}'.format(list_elements[inicio], list_elements[fim]))
            inicio+=1
            fim-=1

        # print('Ponteiro pro inicio -> {}'.format(inicio))
        # print('Ponteiro pro fim -> {}'.format(fim))

    # Trabalha na sublista da esquerda
    if fim > ponteiro_inicio:
        ordena_elementos(list_elements, ponteiro_inicio, fim+1)

    # Trabalha na sublista da direita
    if inicio < ponteiro_fim:
        ordena_elementos(list_elements, inicio, ponteiro_fim)

# Método para imprimir a lista de elementos contidos no vetor
def imprime_lista(list_elements):
    for element in list_elements:
        print(element)

list_elements = []

print('Digite a quantidade de números a ser adicionado no vetor:')
number_of_elements = int(input())

print('Digite o limite do valor a ser adicionado no vetor:')
limit = int(input())

# insere_elementos_ordenados(number_of_elements, list_elements, limit)
insere_elementos_desordenados(number_of_elements, list_elements, limit)
# list_elements = [3, 8, 15, 6, 9, 2, 1, 12]

print('Digite um elemento para procurar dentro do vetor:')
element = int(input())

# Chama o método para ordenar a lista de elementos
ponteiro_inicio = 0
ponteiro_fim = len(list_elements)
ordena_elementos(list_elements, ponteiro_inicio, ponteiro_fim)

# Realiza a busca através do método de busca binária
if(busca_binaria(list_elements, element)):
    print('O elemento foi encontrado com sucesso!')
else:
    print('O elemento não foi encontrado no vetor')

imprime_lista(list_elements)
