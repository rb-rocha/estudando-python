import os
from time import sleep
import pandas as pd

num_exec = 11


def numPar(numIni, numFim):
    for number in range(numIni, numFim+1):
        if (number % 2 == 0):
            print('%s é par!' % (number))
        else:
            print('%s é impar!' % (number))


def upper(string):
    print(string.upper())


def insert_data(lista):
    count = 0
    while(count < 2):
        data = str(input('Digite o dado que quer inserir: \n'))
        lista.append(data)
        count += 1


def print_data(data, *arg):
    print(data)
    for argumento in arg:
        print(argumento)


def soma_num(num1, num2):
    return num1 + num2


def soma(arg1, arg2):
    total = arg1 + arg2
    print("Dentro da função o total é: ", total)
    return total


def to_fahrenheit(celsius):
    return ((celsius * (9/5)) + 32)


while (num_exec != 0):
    num_exec = int(input('Digite o número do exercício desejado (01-10): '))

    if(num_exec == 1):
        numPar(2, 22)

    elif(num_exec == 2):
        entrada = str(input('Digite uma frase: \n'))
        upper(entrada)

    elif(num_exec == 3):
        nomes = ['Roberto', 'Rafael', 'Rangel', 'Bruno']
        insert_data(nomes)
        print(nomes)

    elif(num_exec == 4):
        nome = 'Carlos'
        args = ('Teste', 'Sempre', 'Que', 'Der')
        print_data(nome)
        print_data(args)

    elif(num_exec == 5):
        num1 = 3
        num2 = 4

        print('A soma de %s e %s é: %s' % (num1, num2, soma_num(num1, num2)))

    elif(num_exec == 6):
        total = 0
        soma(10, 20)
        print("Fora da função o total é: ", total)

    elif(num_exec == 7):
        Celsius = [39.2, 36.5, 37.3, 37.8]
        Fahrenheit = map(lambda c: ((c * (9/5)) + 32), Celsius)
        print(list(Fahrenheit))

    elif(num_exec == 8):
        dict = {}
        print(dir(dict))

    elif(num_exec == 9):
        print(dir(pd))

    elif(num_exec == 10):
        data_csv = pd.read_csv(
            'E:/Trampo/Estudando/estudando-python/binary.csv')
        print(data_csv.describe())

    elif (num_exec == 0):
        continue

    else:
        print('valor do exercício inválido!', end='\n')

    sleep(3)
    os.system('cls')
