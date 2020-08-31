"""
Faça um programa que permita ao usuário digitar a quantidade de vitórias, empates e derrotas de um
time de futebol, o número de jogos que este time disputou e o número de pontos obtidos(cada vitória
vale 3 pontos e o empate 1 ponto).
"""
print(input('Nome do time: '))
v = int(input('Vitórias: '))
d = int(input('Derrotas: '))
e = int(input('Empates: '))
total = v + d + e
p = v * 3 + e
print('Total de Partidas:', int(total),'Partidas')
print('Total de Pontos:', p,'Pontos')