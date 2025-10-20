import dicionario as dic
import random
import busca as busca

def jogar_partida():
    
    palavra_secreta = random.choice(dic.dicionario)
    palavra_mostrada = ['_' for _ in palavra_secreta]
    letras_tentadas = set()
    palavras_candidatas = list(dic.dicionario)

    palpites_corretos = 0
    palpites_incorretos = 0
    
    print("\n" + "="*40)
    print("Iniciando nova partida...")
    print(f"O sistema precisa adivinhar uma palavra de {len(palavra_secreta)} letras.")
    print(f"Estado inicial: {' '.join(palavra_mostrada)}")
    print("="*40)

     
    while '_' in palavra_mostrada:
        
        letra_escolhida = busca.escolher_proxima_letra(palavras_candidatas, letras_tentadas)
        
        if letra_escolhida is None:
            print("O sistema não conseguiu encontrar uma letra para tentar. Encerrando o jogo.")
            break
        
        print(f"\nTurno Atual:")
        print(f"Palavras candidatas restantes: {len(palavras_candidatas)}")
        print(f"Heurística escolheu a letra: '{letra_escolhida}'")
        
        letras_tentadas.add(letra_escolhida)
        
        if letra_escolhida in palavra_secreta:
            print(f"A letra '{letra_escolhida}' está na palavra!")
            palpites_corretos += 1
            
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra_escolhida:
                    palavra_mostrada[i] = letra_escolhida
                    
            palavras_candidatas = busca.filtrar_palavras(palavras_candidatas, palavra_mostrada)
        else:
            print(f"A letra '{letra_escolhida}' NÃO está na palavra.")
            palpites_incorretos += 1
            
            palavras_candidatas = busca.filtrar_por_erro(palavras_candidatas, letra_escolhida)
            
        print(f"Palavra atual: {' '.join(palavra_mostrada)}")
        print(f"Letras tentadas: {sorted(list(letras_tentadas))}")
        print("-"*40)
                    
    
    if '_' not in palavra_mostrada:
        print("\n--- Jogo Concluído! ---")
        print(f"O sistema adivinhou a palavra: '{palavra_secreta}'")
    else:
        print(f"\n--- Falha ---")
        print(f"O sistema não conseguiu adivinhar a palavra. A palavra era: '{palavra_secreta}'")
        
    print("\n--- Estatísticas Finais ---")
    print(f"Palavra Secreta: '{palavra_secreta}'")
    print(f"Total de Palpites: {len(letras_tentadas)}")
    print(f"  - Palpites Corretos: {palpites_corretos}")
    print(f"  - Palpites Incorretos: {palpites_incorretos}")
    print("-" * 27)


if __name__ == "__main__":
    print("--- Jogo da Forca - Jogador Inteligente ---")
    print(f"O sistema usará um dicionário com {len(dic.dicionario)} palavras.")
    
    input("\nPressione ENTER para começar o primeiro jogo...")
    
    while True:
        jogar_partida()
        
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar. Até mais!")
            break