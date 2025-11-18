"""
Programa principal para o projeto Flood Fill.
Implementa leitura de entrada, processamento e visualização do grid.
"""

import sys
from typing import List, Tuple
from flood_fill import FloodFill
from visualization import visualize_terminal, visualize_graphical


def read_grid_from_input() -> Tuple[List[List[int]], int, int]:
    """
    Lê o grid e as coordenadas iniciais da entrada padrão.
    
    Formato esperado:
    - Primeira linha: n m (dimensões do grid)
    - Próximas n linhas: valores do grid (separados por espaço)
    - Última linha: x y (coordenadas iniciais)
    
    Returns:
        Tupla (grid, x, y) onde x e y são as coordenadas iniciais
    """
    try:
        # Lê dimensões
        dimensions = input().strip().split()
        n, m = int(dimensions[0]), int(dimensions[1])
        
        # Lê o grid
        grid = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != m:
                raise ValueError(f"Linha do grid deve ter {m} colunas")
            grid.append(row)
        
        # Lê coordenadas iniciais
        coords = input().strip().split()
        x, y = int(coords[0]), int(coords[1])
        
        return grid, x, y
    
    except (ValueError, IndexError) as e:
        print(f"Erro ao ler entrada: {e}", file=sys.stderr)
        sys.exit(1)


def read_grid_from_file(filename: str) -> Tuple[List[List[int]], int, int]:
    """
    Lê o grid e as coordenadas iniciais de um arquivo.
    
    Args:
        filename: Nome do arquivo
        
    Returns:
        Tupla (grid, x, y) onde x e y são as coordenadas iniciais
    """
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
            # Lê dimensões
            dimensions = lines[0].split()
            n, m = int(dimensions[0]), int(dimensions[1])
            
            # Lê o grid
            grid = []
            for i in range(1, n + 1):
                row = list(map(int, lines[i].split()))
                if len(row) != m:
                    raise ValueError(f"Linha do grid deve ter {m} colunas")
                grid.append(row)
            
            # Lê coordenadas iniciais
            coords = lines[n + 1].split()
            x, y = int(coords[0]), int(coords[1])
            
            return grid, x, y
    
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.", file=sys.stderr)
        sys.exit(1)
    except (ValueError, IndexError) as e:
        print(f"Erro ao ler arquivo: {e}", file=sys.stderr)
        sys.exit(1)


def print_grid_terminal(grid: List[List[int]], title: str = "") -> None:
    """
    Imprime o grid no terminal de forma formatada.
    
    Args:
        grid: Grid a ser impresso
        title: Título opcional para o grid
    """
    if title:
        print(f"\n{title}")
        print("=" * (len(title) + 2))
    
    for row in grid:
        print(" ".join(map(str, row)))
    print()


def main():
    """
    Função principal do programa.
    """
    print("=" * 60)
    print("FLOOD FILL - Colorindo Regiões de um Terreno com Obstáculos")
    print("=" * 60)
    
    # Verifica se foi passado um arquivo como argumento
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(f"\nLendo entrada do arquivo: {filename}")
        grid, x, y = read_grid_from_file(filename)
    else:
        print("\nDigite a entrada (ou pressione Ctrl+C para usar exemplos):")
        print("Formato: n m (dimensões), depois n linhas do grid, depois x y (coordenadas)")
        try:
            grid, x, y = read_grid_from_input()
        except KeyboardInterrupt:
            print("\n\nUsando exemplo padrão...")
            # Exemplo 1 do trabalho
            grid = [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [1, 1, 0, 0, 0]
            ]
            x, y = 0, 0
    
    # Valida grid
    if not grid or not grid[0]:
        print("Erro: Grid vazio ou inválido.", file=sys.stderr)
        sys.exit(1)
    
    # Valida dimensões do grid
    n, m = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        if len(row) != m:
            print(f"Erro: Linha {i} tem {len(row)} colunas, esperado {m}.", file=sys.stderr)
            sys.exit(1)
    
    # Valida coordenadas
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        print(f"Erro: Coordenadas ({x}, {y}) estão fora dos limites do grid.", file=sys.stderr)
        print(f"Grid tem dimensões {len(grid)}x{len(grid[0])}.", file=sys.stderr)
        sys.exit(1)
    
    # Mostra grid inicial
    print_grid_terminal(grid, "Grid Inicial")
    
    # Cria cópia do grid inicial para visualização
    initial_grid = [row[:] for row in grid]
    
    # Cria instância do Flood Fill para verificação
    temp_ff = FloodFill(grid)
    
    # Verifica se a célula inicial é navegável
    if grid[x][y] != 0:
        print(f"Aviso: Célula inicial ({x}, {y}) não é navegável (valor: {grid[x][y]}).")
        print("Procurando primeira célula navegável...")
        next_cell = temp_ff.find_next_navigable_cell()
        if next_cell:
            x, y = next_cell
            print(f"Usando célula ({x}, {y}) como ponto inicial.")
        else:
            print("Erro: Não há células navegáveis no grid.", file=sys.stderr)
            sys.exit(1)
    
    # Cria instância do Flood Fill para processamento
    flood_fill = FloodFill(grid)
    
    # Preenche todas as regiões
    print("Processando...")
    flood_fill.fill_all_regions(x, y, use_iterative=True)
    
    # Obtém grid preenchido
    filled_grid = flood_fill.get_grid()
    
    # Mostra grid preenchido
    print_grid_terminal(filled_grid, "Grid Preenchido")
    
    # Visualização formatada
    print("\n" + "=" * 60)
    print("VISUALIZAÇÃO FORMATADA")
    print("=" * 60)
    visualize_terminal(initial_grid, filled_grid)
    
    # Visualização gráfica (se matplotlib estiver disponível)
    try:
        print("\nAbrindo visualização gráfica...")
        visualize_graphical(initial_grid, filled_grid)
    except ImportError:
        print("\nMatplotlib não está instalado. Instale com: pip install matplotlib")
        print("Visualização gráfica não será exibida.")
    except Exception as e:
        print(f"\nErro ao exibir visualização gráfica: {e}")


if __name__ == "__main__":
    main()

