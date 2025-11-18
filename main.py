''' Implementação em Python do algoritmo Flood Fill para identificar e preencher automaticamente todas as regiões conectadas em um grid 2D, 
utilizando diferentes cores para cada área.'''


def flood_fill(grid, x, y, cor_atual, nova_cor):
    """
    Implementa o algoritmo Flood Fill usando recursão.
    
    Parâmetros:
    - grid: matriz bidimensional representando o terreno
    - x, y: coordenadas da célula inicial
    - cor_atual: cor/valor original da região a ser preenchida (geralmente 0)
    - nova_cor: nova cor/valor para preencher a região
    
    Retorna:
    - None (modifica o grid diretamente)
    """
    # Verificar limites do grid
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    # Condições de parada
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    
    # Se a célula não tem a cor original, não preenche
    if grid[x][y] != cor_atual:
        return
    
    # Preencher a célula atual com a nova cor
    grid[x][y] = nova_cor
    
    # Recursivamente preencher células adjacentes (cima, baixo, esquerda, direita)
    flood_fill(grid, x - 1, y, cor_atual, nova_cor)  # Cima
    flood_fill(grid, x + 1, y, cor_atual, nova_cor)  # Baixo
    flood_fill(grid, x, y - 1, cor_atual, nova_cor)  # Esquerda
    flood_fill(grid, x, y + 1, cor_atual, nova_cor)  # Direita


def encontrar_proxima_celula_navegavel(grid):
    """
    Encontra a próxima célula navegável (valor 0) no grid.
    
    Parâmetros:
    - grid: matriz bidimensional
    
    Retorna:
    - Tupla (x, y) com as coordenadas da célula encontrada, ou None se não houver
    """
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                return (i, j)
    
    return None


def preencher_todas_regioes(grid, x_inicial=None, y_inicial=None):
    """
    Preenche todas as regiões navegáveis do grid automaticamente.
    
    Parâmetros:
    - grid: matriz bidimensional
    - x_inicial, y_inicial: coordenadas iniciais opcionais para o primeiro preenchimento
    
    Retorna:
    - None (modifica o grid diretamente)
    """
    cor_atual = 2  # Começar a colorir a partir de 2
    
    # Se foram fornecidas coordenadas iniciais, começar por elas
    if x_inicial is not None and y_inicial is not None:
        if 0 <= x_inicial < len(grid) and 0 <= y_inicial < len(grid[0]):
            if grid[x_inicial][y_inicial] == 0:
                flood_fill(grid, x_inicial, y_inicial, 0, cor_atual)
                cor_atual += 1
    
    # Continuar procurando e preenchendo regiões até não haver mais células navegáveis
    while True:
        proxima_celula = encontrar_proxima_celula_navegavel(grid)
        
        if proxima_celula is None:
            break  # Não há mais células navegáveis
        
        x, y = proxima_celula
        flood_fill(grid, x, y, 0, cor_atual)
        cor_atual += 1


def imprimir_grid(grid):
    """
    Imprime o grid de forma formatada.
    
    Parâmetros:
    - grid: matriz bidimensional
    """
    for linha in grid:
        print(' '.join(str(celula) for celula in linha))
    print()


def criar_grid_exemplo():
    """
    Cria um grid de exemplo para teste.
    
    Retorna:
    - Grid de exemplo
    """
    return [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]


def ler_grid_usuario():
    """
    Lê um grid fornecido pelo usuário.
    
    Retorna:
    - Grid fornecido pelo usuário
    """
    print("Digite as dimensões do grid (n m):")
    n, m = map(int, input().split())
    
    print(f"Digite o grid {n}x{m} (valores separados por espaço):")
    grid = []
    for i in range(n):
        linha = list(map(int, input().split()))
        if len(linha) != m:
            print(f"Erro: A linha {i+1} deve ter {m} elementos.")
            return None
        grid.append(linha)
    
    return grid


if __name__ == "__main__":
    print("=" * 50)
    print("FLOOD FILL - Sistema de Mapeamento de Terreno")
    print("=" * 50)
    print()
    
    # Opção de usar grid de exemplo ou personalizado
    print("Escolha uma opção:")
    print("1 - Usar grid de exemplo")
    print("2 - Inserir grid personalizado")
    
    opcao = input("Opção: ").strip()
    
    if opcao == "1":
        grid = criar_grid_exemplo()
        print("\nGrid de exemplo:")
        imprimir_grid(grid)
        
        # Solicitar coordenadas iniciais
        print("Digite as coordenadas iniciais (x y) ou pressione Enter para preenchimento automático:")
        entrada = input().strip()
        
        if entrada:
            x, y = map(int, entrada.split())
        else:
            x, y = None, None
    
    elif opcao == "2":
        grid = ler_grid_usuario()
        
        if grid is None:
            print("Erro ao ler o grid. Encerrando...")
            exit(1)
        
        print("\nGrid inserido:")
        imprimir_grid(grid)
        
        # Solicitar coordenadas iniciais
        print("Digite as coordenadas iniciais (x y) ou pressione Enter para preenchimento automático:")
        entrada = input().strip()
        
        if entrada:
            x, y = map(int, entrada.split())
        else:
            x, y = None, None
    
    else:
        print("Opção inválida. Encerrando...")
        exit(1)
    
    # Executar o preenchimento
    print("\nPreenchendo regiões...")
    preencher_todas_regioes(grid, x, y)
    
    print("\nGrid após preenchimento:")
    imprimir_grid(grid)
    
    # Estatísticas
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    cores_usadas = set()
    obstaculos = 0
    
    for linha in grid:
        for celula in linha:
            if celula == 1:
                obstaculos += 1
            elif celula > 1:
                cores_usadas.add(celula)
    
    print(f"Estatísticas:")
    print(f"- Dimensões do grid: {n} x {m}")
    print(f"- Total de células: {n * m}")
    print(f"- Obstáculos: {obstaculos}")
    print(f"- Regiões identificadas: {len(cores_usadas)}")
    print(f"- Cores usadas: {sorted(cores_usadas)}")
    
    print("\nLegenda:")
    print("0 - Terreno navegável não preenchido")
    print("1 - Obstáculo (preto)")
    print("2, 3, 4, ... - Regiões coloridas (vermelho, laranja, amarelo, ...)")
