import os
from time import sleep

num_exec = 11

while (num_exec != 0):
    num_exec = int(
        input('Escolha o número do exercício que deseja visualizar: (1-10, 0 para parar) \n'))

    if(num_exec == 1):
        dia_semana = input('\nQue dia da semana é hoje? (Ex:sexta) \n')
        if(dia_semana == 'sabado' or dia_semana == 'domingo'):
            print('Vá para casa, hoje é dia de descanso!', end='\n')
        elif(dia_semana == 'segunda' or dia_semana == 'terça' or dia_semana == 'quarta' or dia_semana == 'quinta' or dia_semana == 'sexta'):
            print('Ok, hora de trabalhar!', end='\n')
        else:
            print('\n Dia da semana inválido!')

    elif(num_exec == 2):
        frutas = ['Banana', 'Maçã', 'Pera', 'Morango', 'Abacate']
        count = 0
        validated = False
        for fruta in frutas:
            count += 1
            if (fruta == 'Morango'):
                validated = True
                print('Você tem morango na sua lista!')
            if(count == len(frutas) and validated == False):
                print('Você não possui morangos na lista!')

    elif(num_exec == 3):
        tupla_num = (1, 4, 7)
        lista_num = []
        for num in tupla_num:
            lista_num.append(num*2)

        print(tupla_num)
        print(lista_num)

    elif(num_exec == 4):
        for number in range(100, 152):
            if(number % 2 == 0):
                print(number, end=' | ')

        print('\n')

    elif(num_exec == 5):
        temp = 40
        while (temp >= 35):
            if(temp != 35):
                print('Temperatura está boa: %s' % (temp))
                temp = temp-1
            else:
                print('Temperatura está muito baixa: %s' % (temp))
                temp = temp-1

    elif(num_exec == 6):
        for number in range(0, 100):
            contador = 0
            contador = number
            if(contador <= 23):
                print('Contagem: %s' % (contador))
            else:
                break

    elif(num_exec == 7):
        lista = []
        num = 4
        while(num <= 20):
            lista.append(num)
            num += 1

        print(lista)

    elif(num_exec == 8):
        lista = []
        for number in range(5, 45, 2):
            lista.append(number)

        print(lista)

    elif(num_exec == 9):
        temperatura = float(input('Qual a temperatura? \n'))
        if temperatura > 30:
            print('Vista roupas leves!')
        else:
            print('Busque seus casacos!')

    elif(num_exec == 10):
        frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
        repeat = frase.count('r')
        print('A letra R aparece %s vezes na frase!' % (repeat))

    elif (num_exec == 0):
        continue

    else:
        print('valor do exercício inválido!', end='\n')

    sleep(3)
    os.system('cls')
