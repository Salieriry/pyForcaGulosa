# Sistema de Jogo da Forca com Busca Gulosa (Hangman Solver)

Este projeto implementa um jogador automático (IA) para o Jogo da Forca em Python. O sistema utiliza um algoritmo de busca gulosa (greedy search) para adivinhar uma palavra secreta com o mínimo de erros possível, baseando-se em um dicionário de palavras fornecido.

## Como Funciona o Algoritmo (Busca Gulosa)

O "cérebro" da IA está no arquivo `busca.py` e é coordenado pelo `forca.py`. A lógica segue estes passos:

1.  **Inicialização:** O jogo começa (`forca.py`) selecionando uma "palavra secreta" aleatória do `dicionario.py`. A IA mantém uma lista de "palavras candidatas", que inicialmente é uma cópia completa do dicionário.

2.  **Heurística Gulosa (A Escolha):** Em cada turno, a IA precisa decidir qual letra chutar. Ela faz isso da seguinte forma (`escolher_proxima_letra`):
    * Analisa **todas** as palavras ainda restantes na lista de "candidatas".
    * Conta a frequência de cada letra que aparece nessas palavras (ignorando letras já tentadas).
    * A "escolha gulosa" é chutar a letra que aparece com **maior frequência**. A heurística assume que a letra mais comum entre as palavras possíveis é a mais provável de estar na palavra secreta.

3.  **Filtragem do Dicionário:** Após cada chute, a lista de candidatas é atualizada:
    * **Se o chute for correto:** O sistema atualiza o padrão da palavra (ex: `_ _ _ _ A`). A IA então filtra (`filtrar_palavras`) sua lista de candidatas, mantendo apenas as palavras que se encaixam perfeitamente nesse novo padrão (ex: palavras de 5 letras que terminam com 'A' e não têm 'A' em outras posições já reveladas).
    * **Se o chute for incorreto:** A IA filtra (`filtrar_por_erro`) sua lista de candidatas, removendo todas as palavras que contêm a letra errada.

4.  **Conclusão:** O processo se repete a cada turno, com a lista de palavras candidatas diminuindo drasticamente, até que a IA encontre a palavra correta.

## Estrutura dos Arquivos

* `forca.py`: Script principal. Controla o loop do jogo, seleciona a palavra secreta e exibe o progresso da IA.
* `busca.py`: Contém a lógica da IA. Inclui as funções para escolher a próxima letra (heurística gulosa) e para filtrar a lista de palavras candidatas.
* `dicionario.py`: Um módulo simples que contém uma única lista de palavras em português, usada como base de conhecimento da IA.
* `README.md`: Este arquivo.

## Pré-requisitos

* Python 3.12.3

O projeto **não requer a instalação de nenhuma biblioteca externa**, pois utiliza apenas módulos padrão do Python (`random`, `collections.Counter`).

## Instruções de Uso

1.  Certifique-se de que todos os arquivos (`forca.py`, `busca.py`, `dicionario.py`) estejam no mesmo diretório.
2.  Abra um terminal ou prompt de comando.
3.  Navegue até o diretório onde os arquivos estão localizados.
4.  Execute o script principal com o seguinte comando:

    ```bash
    python forca.py
    ```

5.  O programa iniciará automaticamente a primeira partida. Pressione "ENTER" para começar.
6.  Ao final de cada partida, você pode digitar `s` para jogar novamente ou `n` para sair.