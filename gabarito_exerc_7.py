def cacular_nota(resposta,gabarito):
    nota = 0
    for i in range(len(gabarito)):
        if resposta[i] == gabarito[i]:
            nota += 1
    return nota

num_quest =int(input('Digite o número de questões da prova: '))
gabarito_aluno = input('Digite o gabarito da prova: ')
num_alunos = int(input("Digite o número de alunos : "))

for alunos in range(num_alunos):
    resp_aluno = input('Digite sua resposta: ')
    nota = cacular_nota(resp_aluno,gabarito_aluno)
    print(f'Você acertou {nota} questões !')
    print(f'Nota final : {nota * 10}')











