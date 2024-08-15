def exibir_tabuleiro(tabuleiro):
    print("\n" + " | ".join(tabuleiro[0]))
    print("---------")
    print(" | ".join(tabuleiro[1]))
    print("---------")
    print(" | ".join(tabuleiro[2]))
    print()

def verificar_vencedor(tabuleiro, jogador):
    # Checar linhas, colunas e diagonais
    for i in range(3):
        if all([celula == jogador for celula in tabuleiro[i]]):
            return True
        if all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True

    if all([tabuleiro[i][i] == jogador for i in range(3)]):
        return True
    if all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogadores[jogador_atual]} faz a jogada.")
        
        while True:
            try:
                linha = int(input("Digite a linha (0, 1, 2): "))
                coluna = int(input("Digite a coluna (0, 1, 2): "))
                
                if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
                    print("Linha e coluna devem estar entre 0 e 2.")
                elif tabuleiro[linha][coluna] != " ":
                    print("Esta célula já está ocupada.")
                else:
                    break
            except ValueError:
                print("Por favor, digite um número válido.")

        tabuleiro[linha][coluna] = jogadores[jogador_atual]
        
        if verificar_vencedor(tabuleiro, jogadores[jogador_atual]):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogadores[jogador_atual]} venceu!")
            break
        
        if all([celula != " " for linha in tabuleiro for celula in linha]):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        
        jogador_atual = 1 - jogador_atual

# Executa o jogo
jogo_da_velha()
