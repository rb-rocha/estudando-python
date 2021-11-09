import os
from time import localtime, strftime, time, sleep

num_exec = 11


def potencia(valor):
    return valor**3


def potencia2(valor):
    return valor**2


def create_list(string):
    return list(map(lambda s: [s.upper(), s.lower(), len(s)], string))


def transposed_matrix(matrix):
    transpose = [[row[i] for row in matrix] for i in range(2)]
    return transpose


def potencias(value):
    return [potencia2(value), potencia(value)]


def lower_than_zero(number):
    if number < 0:
        return number


def potencia_lists(valor, potencia):
    return valor**potencia


def find_matchs(value, list):
    for number in list:
        if number == value:
            return number


while (num_exec != 0):
    num_exec = int(input('Digite o número do exercício desejado (01-10): '))

    if(num_exec == 1):
        lista = [1, 3, 5, 7, 9]
        print(list(map(potencia, lista)))

    if(num_exec == 2):
        palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
        result = []
        position = 0
        print(create_list(palavras))

    if(num_exec == 3):
        matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
        print(transposed_matrix(matrix))

    if(num_exec == 4):
        lista = [0, 1, 2, 3, 4]
        print(list(map(potencias, lista)))

    if(num_exec == 5):
        listaA = [2, 3, 4]
        listaB = [10, 11, 12]
        print(list(map(potencia_lists, listaA, listaB)))

    if(num_exec == 6):
        numbers = range(-5, 5)
        print(list(filter(lower_than_zero, numbers)))

    if(num_exec == 7):
        a = [1, 2, 3, 5, 7, 9]
        b = [2, 3, 5, 6, 7, 8]
        print(list(filter(lambda x: x in a, b)))

    if(num_exec == 8):
        print(strftime("%d/%m/%Y %H:%M", localtime()))

    if(num_exec == 9):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 4, 'd': 5}
        dict3 = dict((zip(dict1, dict2.values())))

        print(dict3)

    if(num_exec == 10):
        lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for index, value in enumerate(lista):
            if index > 5:
                print(value)

    elif (num_exec == 0):
        continue

    else:
        print('valor do exercício inválido!', end='\n')

    sleep(3)
    os.system('cls')
