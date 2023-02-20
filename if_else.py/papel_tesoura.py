Jogador1 = int(input("Jogador1, digite 0 p/ pedra, 1 p/ papel ou 2 p/ tesoura: "))
Jogador2 = int(input("Jogador2, digite 0 p/ pedra, 1 p/ papel ou 2 p/ tesoura: "))
pedra = 0
papel = 1
tesoura = 2
if (Jogador1 == Jogador2):
  print("Empatou!!!")
elif ((Jogador1 == pedra and Jogador2 == tesoura )or(Jogador1 == tesoura and Jogador2 == papel)or (Jogador1 == papel and Jogador2 == pedra)):
  print("Jogador 1 ganhou !!!")


