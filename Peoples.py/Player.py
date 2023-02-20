#exercicio 02
from random import randint
from operator import itemgetter
game = {'player 1': randint(1, 6), 'player 2': randint(1, 6), 'player 3': randint(1, 6), 'player 4': randint(1, 6)}
ranking = list ()
print('Pontuação gerada: ')
for a, b in game.items():
    print(f'{a} tirou {b} jogando o dado.')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' ------High Score Game Dado------')
for c, b in enumerate(ranking):
  print(f'  {c+1} posição: {b[0]} com {b[1]}.')
