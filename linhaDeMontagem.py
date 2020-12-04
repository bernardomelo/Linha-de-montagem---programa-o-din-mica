def melhor_caminho(estacoes, trocas, entrada, saida, n):
    caminho = [[0 for x in range(n)], [0 for x in range(n)]]
    custo = [[0 for x in range(n)], [0 for x in range(n)]]

    custo[0][0] = entrada[0]+estacoes[0][0]
    custo[1][0] = entrada[1]+estacoes[1][0]

    for j in range(1, n):
        linha_atual = custo[0][j-1] + estacoes[0][j]
        outra_linha = custo[1][j-1] + \
            trocas[1][j-1] + estacoes[0][j]

        if linha_atual <= outra_linha:
            caminho[0][j - 1] = 0
            custo[0][j] = linha_atual
        else:
            caminho[0][j - 1] = 1
            custo[0][j] = outra_linha

        linha_atual = custo[1][j-1] + estacoes[1][j]
        outra_linha = custo[0][j-1] + \
            trocas[0][j-1] + estacoes[1][j]

        if linha_atual <= outra_linha:
            caminho[1][j - 1] = 1
            custo[1][j] = linha_atual
        else:
            caminho[1][j - 1] = 0
            custo[1][j] = outra_linha

    final_linha0 = custo[0][n-1] + saida[0]
    final_linha1 = custo[1][n-1] + saida[1]

    if final_linha0 <= final_linha1:
        caminho[0][n-1] = 0
        return final_linha0, caminho[0]
    else:
        caminho[1][n-1] = 1
        return final_linha1, caminho[1]

estacoes = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
trocas = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
entradas = [2, 4]
saidas = [3, 2]
n = 6

a=melhor_caminho(estacoes, trocas, entradas, saidas, n)

print("Custo: " + str(a[0]))
print("Caminho: " + str(a[1]))

#Output do programa para o problema da questão:
#==============================================
#Custo: 38
#Caminho:[0, 1, 0, 0, 1, 0]
#==============================================
#sendo: 0 -> Linha de montagem 1
#1 -> Linha de montagem 2
#Estação 1 -> Pela linha de montagem 1
#Estação 2 -> Pela linha de montagem 2
#Estação 3 -> Pela linha de montagem 1
#Estação 4 -> Pela linha de montagem 1
#Estação 5 -> Pela linha de montagem 2
#Estação 6 -> Pela linha de montagem 1