from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "pensar", ou seja, sorteia um número entre 0 e 5.
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5... Tente adivinhar.')
print('-=-' * 20)

jogador = int(input('Em qual número eu pensei?: ')) # Jogador tenta adivinhar
print('Processando...')
sleep(2) #aguarda 2 segundos para dar a resposta.
if jogador == computador:
    print(f'Você venceu! eu pensei no {computador} mesmo.')
else: 
    print(f'Você perdeu! eu pensei no {computador} e não no {jogador}.')


