from random import randint

selecionado = randint(1, 100)
chute = 0
print('-------Bem vindo!-------')
while chute != selecionado:
  chute = int(input('Digite um número de 1 a 100: '))
  if chute == selecionado:
    print(f'Parabéns, você ganhou!\n O numero era o {selecionado}')
  if chute > selecionado:
    print('Chute um número menor')
  if chute < selecionado:
    print('Chute um número maior')