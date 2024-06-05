import random

print(''' 
░█████╗░██████╗░██╗░░░██╗██╗███╗░░██╗██╗░░██╗███████╗  ░█████╗░
██╔══██╗██╔══██╗██║░░░██║██║████╗░██║██║░░██║██╔════╝  ██╔══██╗
███████║██║░░██║╚██╗░██╔╝██║██╔██╗██║███████║█████╗░░  ██║░░██║
██╔══██║██║░░██║░╚████╔╝░██║██║╚████║██╔══██║██╔══╝░░  ██║░░██║
██║░░██║██████╔╝░░╚██╔╝░░██║██║░╚███║██║░░██║███████╗  ╚█████╔╝
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝  ░╚════╝░

███╗░░██╗██╗░░░██╗███╗░░░███╗███████╗██████╗░░█████╗░
████╗░██║██║░░░██║████╗░████║██╔════╝██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║██╔████╔██║█████╗░░██████╔╝██║░░██║
██║╚████║██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██║
██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗██║░░██║╚█████╔╝
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░ ''')

print('-----------------------------------------------------------')
print('-----------Bem vindo ao jogo do numero secreto-------------')
print('   Nosso numero secreto esta entre 1 e 100 - Boa Sorte     \n')


numero_secreto = random.randint(1,101)
print(numero_secreto)
print('\n ')
tentativas = 10

for tentativa in range(1, tentativas):
    chute = int(input(f'Tentativa {tentativa} de {tentativas}: '))
    if chute < 1 or chute > 100:
        print('Numero invalido')
        chute = int(input(f'Tentativa {tentativa} de {tentativas}: '))
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    
    if acertou:
         print('Parabens voce acertou o numero secreto com {} tentativas'.format(tentativa))
         break
    elif maior:
         print('O numero secreto é menor.')
    else: 
         print('O numero secreto é maior.')

    tentativa +=1
              







# while numero_secreto != chute:
#         if chute > numero_secreto:
#             print('O seu chute foi maior que o numero secreto')
#             chute = int(input('Digite novamente o numero secreto: '))
#         else:
#             print('O seu chute foi menor que o numero secreto')
#             chute = int(input('Digite novamente o numero secreto: '))
# print('Parabens voce acertou o numero secreto')
    
        

