"""
Funcionalidades extras para o projeto Flood Fill (pontos extras).
Inclui visualização dinâmica e geração de grids aleatórios.
"""

import random
import time
from typing import List, Tuple, Optional
from flood_fill import FloodFill

try:
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import numpy as np
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Matplotlib não está disponível. Funcionalidades gráficas não estarão disponíveis.")


def generate_random_grid(rows: int, cols: int, obstacle_ratio: float = 0.3) -> List[List[int]]:
    """
    Gera um grid aleatório com a proporção especificada de obstáculos.
    
    Args:
        rows: Número de linhas
        cols: Número de colunas
        obstacle_ratio: Proporção de obstáculos (0.0 a 1.0)
        
    Returns:
        Grid aleatório com valores 0 (navegável) e 1 (obstáculo)
    """
    grid = []
    total_cells = rows * cols
    num_obstacles = int(total_cells * obstacle_ratio)
    
    # Cria lista com todas as células
    cells = [(i, j) for i in range(rows) for j in range(cols)]
    
    # Seleciona células aleatórias para serem obstáculos
    obstacle_cells = random.sample(cells, num_obstacles)
    obstacle_set = set(obstacle_cells)
    
    # Cria o grid
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i, j) in obstacle_set:
                row.append(1)  # Obstáculo
            else:
                row.append(0)  # Navegável
        grid.append(row)
    
    return grid


def find_first_navigable_cell(grid: List[List[int]]) -> Optional[Tuple[int, int]]:
    """
    Encontra a primeira célula navegável no grid.
    
    Args:
        grid: Grid bidimensional
        
    Returns:
        Tupla (row, col) da primeira célula navegável, ou None se não houver
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    return None


def visualize_dynamic_fill(grid: List[List[int]], start_row: int, start_col: int, 
                           delay: float = 0.3) -> None:
    """
    Visualiza o preenchimento do grid de forma dinâmica, mostrando cada etapa.
    
    Args:
        grid: Grid inicial
        start_row: Linha inicial
        start_col: Coluna inicial
        delay: Atraso entre cada atualização (em segundos)
    """
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib não está disponível para visualização dinâmica.")
        return
    
    # Mapeamento de valores para cores
    color_map = {
        0: 'white',      # Branco - Terreno navegável
        1: 'black',      # Preto - Obstáculo
        2: 'red',        # Vermelho
        3: 'orange',     # Laranja
        4: 'yellow',     # Amarelo
        5: 'green',      # Verde
        6: 'blue',       # Azul
        7: 'purple',     # Roxo
        8: 'pink',       # Rosa
        9: 'cyan',       # Ciano
    }
    
    # Cria figura
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.ion()  # Modo interativo
    
    # Cria cópia do grid para trabalhar
    working_grid = [row[:] for row in grid]
    flood_fill = FloodFill(working_grid)
    
    # Converte para numpy array
    grid_array = np.array(working_grid)
    
    # Cria mapa de cores
    unique_values = sorted(set(val for row in working_grid for val in row))
    colors_list = [color_map.get(val, 'gray') for val in unique_values]
    cmap = mcolors.ListedColormap(colors_list) if len(unique_values) > 1 else 'gray_r'
    
    if len(unique_values) > 1:
        bounds = unique_values + [max(unique_values) + 1]
        norm = mcolors.BoundaryNorm(bounds, cmap.N)
    else:
        norm = None
    
    # Função para atualizar visualização
    def update_visualization():
        ax.clear()
        if norm:
            im = ax.imshow(grid_array, cmap=cmap, norm=norm, interpolation='nearest')
        else:
            im = ax.imshow(grid_array, cmap='gray_r', vmin=0, vmax=1, interpolation='nearest')
        
        ax.set_title('Preenchimento Dinâmico - Flood Fill', fontsize=14, fontweight='bold')
        ax.set_xlabel('Coluna')
        ax.set_ylabel('Linha')
        ax.grid(True, color='gray', linewidth=0.5)
        ax.set_xticks(range(len(working_grid[0])))
        ax.set_yticks(range(len(working_grid)))
        
        # Adiciona valores nas células
        for i in range(len(working_grid)):
            for j in range(len(working_grid[0])):
                text_color = 'white' if working_grid[i][j] == 1 else 'black'
                ax.text(j, i, str(working_grid[i][j]), 
                       ha='center', va='center', color=text_color, fontweight='bold')
        
        plt.draw()
        plt.pause(0.01)
    
    # Mostra grid inicial
    update_visualization()
    time.sleep(delay)
    
    # Preenche região inicial
    if flood_fill.is_navigable(start_row, start_col):
        flood_fill.fill_region_iterative(start_row, start_col, flood_fill.current_color)
        grid_array = np.array(flood_fill.get_grid())
        update_visualization()
        time.sleep(delay)
        flood_fill.current_color += 1
    
    # Continua preenchendo outras regiões
    while True:
        next_cell = flood_fill.find_next_navigable_cell()
        if next_cell is None:
            break
        
        flood_fill.fill_region_iterative(next_cell[0], next_cell[1], flood_fill.current_color)
        grid_array = np.array(flood_fill.get_grid())
        update_visualization()
        time.sleep(delay)
        flood_fill.current_color += 1
    
    plt.ioff()  # Desativa modo interativo
    plt.show()


def create_random_grid_file(filename: str, rows: int, cols: int, 
                           obstacle_ratio: float = 0.3) -> Tuple[int, int]:
    """
    Cria um arquivo com um grid aleatório.
    
    Args:
        filename: Nome do arquivo a ser criado
        rows: Número de linhas
        cols: Número de colunas
        obstacle_ratio: Proporção de obstáculos
        
    Returns:
        Tupla (x, y) com coordenadas da primeira célula navegável
    """
    grid = generate_random_grid(rows, cols, obstacle_ratio)
    start_cell = find_first_navigable_cell(grid)
    
    if start_cell is None:
        raise ValueError("Grid gerado não possui células navegáveis!")
    
    with open(filename, 'w') as f:
        f.write(f"{rows} {cols}\n")
        for row in grid:
            f.write(" ".join(map(str, row)) + "\n")
        f.write(f"{start_cell[0]} {start_cell[1]}\n")
    
    return start_cell


if __name__ == "__main__":
    # Exemplo de uso: gerar grid aleatório
    print("Gerando grid aleatório 10x10 com 30% de obstáculos...")
    start = create_random_grid_file("grid_aleatorio.txt", 10, 10, 0.3)
    print(f"Grid salvo em 'grid_aleatorio.txt'")
    print(f"Coordenadas iniciais: ({start[0]}, {start[1]})")
    
    # Exemplo de visualização dinâmica
    print("\nPara visualização dinâmica, use:")
    print("from extra_features import visualize_dynamic_fill")
    print("visualize_dynamic_fill(grid, start_row, start_col)")

