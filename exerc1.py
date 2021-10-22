listaNum = []

print('Exercício 1:')

for number in range(0, 10):
    listaNum.append(number)
    # end é utilizado para não pular linha e definir o que deve vir depois
    print(number, end=' ')

print('-----------------------------')

# -----------------------------------------------------------------------------

print('Exercício 2:')


def peaple_factory(nome, sobrenome, idade):
    return {
        'name': nome,
        'last_name': sobrenome,
        'age': idade
    }


pessoa1 = peaple_factory('Roberto', 'Rocha', 22)
pessoa2 = peaple_factory('Rychard', 'Megda', 23)
pessoa3 = peaple_factory('Rafael', 'Rosario', 23)
pessoa4 = peaple_factory('Bruno', 'Rodrigues', 23)
pessoa5 = peaple_factory('Mateus', 'Rangel', 23)

peaples = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]

for peaple in peaples:
    print(peaple)

# -----------------------------------------------------------------------------

print('Exercício 3:')

frase1 = 'Estou estundado'
frase2 = 'Python'

frase3 = frase1 + ' ' + frase2

print(frase3)

# ------------------------------------------------------------------------------


print('Exercício 4:')

tupla_numbers = (1, 2, 2, 3, 4, 4, 4, 5)

numbers_of_4 = tupla_numbers.count(4)

print("Número de repetições do 4 :", numbers_of_4)

# ------------------------------------------------------------------------------


print('Exercício 5:')

dict1 = {}

print(dict1)

# ------------------------------------------------------------------------------


print('Exercício 6:')

dict1 = {
    'rua': 'General Ozorio',
    'bairro': 'Lapa',
    'num': 189
}

print(dict1)

# ------------------------------------------------------------------------------


print('Exercício 7:')


def dict_factory(rua, bairro, numero):
    return {
        'rua': rua,
        'bairro': bairro,
        'num': numero
    }


endereco = {'rua2': 'Rua dos bobos',
            'bairo2': 'Candelabrio',
            'num2': 0}

dict1.update(endereco)

print(dict1)

# ------------------------------------------------------------------------------


print('Exercício 8:')

dict2 = {
    'pessoa': 'Carlos',
    'chaves': [12, 36],
    'status': 1
}

print(dict2)

# ------------------------------------------------------------------------------

print('Exercício 9:')

dict3 = {
    'name': 'Casa da Moeda',
    'coins': ('Dollar', 'Real Brasileiro'),
    'dict4': {
        'open': '08:00hr',
        'close': '17:00hr'
    },
    'balance': 147325.78
}

print(dict3)

# ------------------------------------------------------------------------------


print('Exercício 10:')

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

for i in range(1, 18):
    print(frase[i], end='')
