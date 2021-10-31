from functools import reduce
import pandas as pd

# Criando arquivos


def create_file_txt():
    fileName = input('Escolha o nome do arquivo: ')

    fileName += '.txt'

    arq2 = open('./arquivos/'+fileName, 'w')

    arq2.write(input('Digite o conteudo do arquivo: '))

    arq2.close()

    arq2 = open('./arquivos/'+fileName, 'r')

    print(arq2.read())

    arq2.close()


# create_file_txt()

# Abrir arquivos CSV de forma nativa
# Não é a melhor forma mas é possivel

def open_csv():
    csv = open('./arquivos/salarios.csv', 'r')

    data = csv.read()

    rows = data.split('\n')

    print(rows)


# open_csv()

# Abrindo arquivo com o pandas


file1 = "./arquivos/binary.csv"

binary = pd.read_csv(file1)

# print(binary.head())

# funcao Map
# Percorre uma lista e executa uma funcao


def double_value(value):
    return value * 2


lista_valores = [1, 2, 3, 4, 5, 6]

#print(list(map(double_value, lista_valores)))

# funcao Reduce
# Itera os valores de uma lista até que o resultado seja apenas um


def sum_values(a, b):
    return a+b


#print(reduce(sum_values, lista_valores))

# funcao filter
# Retorna os valores que resultarem true

def bigger_then(value):
    if(value >= 5):
        return True


#print(list(filter(bigger_then, lista_valores)))

# funcao list comprehension

lista = [valor for valor in lista_valores if valor % 2 == 0]

print(lista)
