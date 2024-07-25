from time import sleep
from random import randint

def limpar():
    print("\n" * 50)

def verifica(m, mp):
    cont = 0
    for l in range(0, 4):
        for c in range(0, 4):
            if m[l][c] == mp:
                cont += 1
    return cont > 2

def mostraMatriz(l1, c1, l2, c2, m):
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    matriz[l1-1][c1-1] = m[l1-1][c1-1]
    matriz[l2-1][c2-1] = m[l2-1][c2-1]
    for l in range(0, 4):
        for c in range(0, 4):
            print(matriz[l][c], end='  ')
        print("\n")

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print("\n" + "\033[1;32m=- "*15 + " JOGO DA MEMÓRIA " + "-=" * 15 + "\033[m")
print("\n\033[1;33mPares certos: 1 Ponto")
print("Pares errados: -1 ponto\033[m")
print("\n\033[1;31mINSTRUÇÕES\n\n"
      "O TABULEIRO POSSUI 4 LINHAS E 4 COLUNAS\n"
      "PARA CONTINUAR APERTE A TECLA S(AO FINAL DA PARTIDA SERÁ PERGUNTADO)" + "\033[m")

a = input("\n\033[1;32mDIGITE C PARA COMEÇAR:\033[m").upper()

if a == 'C':
    print("\n\033[1;34mO JOGO COMEÇA EM 10 SEGUNDOS\n")
    for cont in range(10, 0, -1):
        print(cont)
        sleep(1)
    print("\n\033[m")
    print("VOCÊ TEM 8 SEGUNDOS PARA MEMORIZAR ESSE TABULEIRO....\n")
    for l in range(0, 4):
        for c in range(0, 4):
            matriz[l][c] = randint(1, 8)
            while verifica(matriz, matriz[l][c]):
                matriz[l][c] = randint(1, 8)
            print(matriz[l][c], end="  ")
        print("\n")
    sleep(8)
    limpar()

    r = "S"
    pt = 0

    while r == "S":
        l1 = int(input("INFORME A PRIMEIRA (LINHA, COLUNA)....\nLinha: "))
        c1 = int(input("Coluna: "))
        l2 = int(input("INFORME A SEGUNDA (LINHA, COLUNA)....\nLinha: "))
        c2 = int(input("Coluna: "))
        print("\n" * 2)
        print(matriz[l1-1][c1-1])
        print(matriz[l2-1][c2-1])
        print("\n" * 2)
        mostraMatriz(l1, c1, l2, c2, matriz)
        if matriz[l1-1][c1-1] == matriz[l2-1][c2-1]:
            print("PARABÉNS, VOCÊ ACERTOU!")
            pt += 1
        else:
            pt -= 1
            print("VOCÊ ERROU!")
        r = input("DESEJA CONTINUAR? (S/N): ").upper()

print(f"PONTUAÇÃO = {pt}")
