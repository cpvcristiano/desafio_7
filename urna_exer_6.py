
def apresentacao():
    print('='*30)
    print('Eleição Presidencial')
    print('='*30)


def id_candidato ():
    totais = [0, 0, 0, 0, 0, 0]
    candidatos = ['1 João', '2 José', '3 Bozzo', '4 Lulu','5 Voto Nulo','6 Voto em Branco']
    for i in candidatos:
        print(i)
    voto = int(input('Digite o número do Candidato:'))
    while voto != 0:
        # voto -1 serve para compatibilizar a posição do candidato na lista
        totais[voto-1] += 1
        print(i)
        voto = int(input('Digite o número do Candidato:'))

    # função sum(lista) soma os valores dos itens da lista
    totalvotos = sum(totais)
    # função max(lista) retorna o maior valor da lista
    vencedor = max(totais)

    for i in range(len(totais)):
        perc = totais[i]/totalvotos * 100
        print(f'\nCandidato: {candidatos[i]}\nvotos: {totais[i]}\nPercentual:{perc:.2f}%')
        if vencedor == totais[i]:
            v = i

    print(f'\n\nO candidato {candidatos[v]}  foi eleito PRESIDENTE')

apresentacao()
id_candidato()