from collections import namedtuple

listaAtletas = []

Atleta = namedtuple("Atleta", "atleta nota1 nota2 nota3 nota4 nota5")

for i in range(0, 5):
   nome = input('Nome do Atleta: ')
   nota1 = float(input('Nota 1: '))
   nota2 = float(input('Nota 2: '))
   nota3 = float(input('Nota 3: '))
   nota4 = float(input('Nota 4: '))
   nota5 = float(input('Nota 5: '))
   listaAtletas.append(Atleta(atleta=nome, nota1=nota1, nota2=nota2, nota3=nota3, nota4=nota4, nota5=nota5))
   print('\n')

for atleta in listaAtletas:
    print(
        f"Atleta : {atleta.atleta} >> notas: {atleta.nota1}||{atleta.nota2}||{atleta.nota3}||{atleta.nota4}||{atleta.nota5}")
