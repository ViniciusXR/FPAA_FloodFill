"""
Módulo de visualização para o projeto Flood Fill.
Implementa visualização em terminal e gráfica com cores.
"""

from typing import List
import sys


def visualize_terminal(initial_grid: List[List[int]], filled_grid: List[List[int]]) -> None:
    """
    Visualiza os grids inicial e preenchido no terminal de forma formatada.
    
    Args:
        initial_grid: Grid inicial
        filled_grid: Grid preenchido
    """
    print("\n--- GRID INICIAL ---")
    print_grid_formatted(initial_grid)
    
    print("\n--- GRID PREENCHIDO ---")
    print_grid_formatted(filled_grid)
    
    print("\n--- LEGENDA ---")
    print("0 = Branco (Terreno navegável)")
    print("1 = Preto (Obstáculo)")
    print("2 = Vermelho")
    print("3 = Laranja")
    print("4 = Amarelo")
    print("5+ = Outras cores")


def print_grid_formatted(grid: List[List[int]]) -> None:
    """
    Imprime o grid formatado com espaçamento adequado.
    
    Args:
        grid: Grid a ser impresso
    """
    if not grid:
        return
    
    # Calcula largura necessária para cada coluna
    max_width = max(len(str(cell)) for row in grid for cell in row)
    
    # Imprime cabeçalho de colunas
    print("   ", end="")
    for j in range(len(grid[0])):
        print(f"{j:>{max_width}}", end="  ")
    print()
    
    # Imprime linhas com índices
    for i, row in enumerate(grid):
        print(f"{i:2} ", end="")
        for cell in row:
            print(f"{cell:>{max_width}}", end="  ")
        print()


def visualize_graphical(initial_grid: List[List[int]], filled_grid: List[List[int]]) -> None:
    """
    Visualiza os grids inicial e preenchido graficamente com cores.
    
    Args:
        initial_grid: Grid inicial
        filled_grid: Grid preenchido
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.colors as mcolors
        import numpy as np
    except ImportError:
        print("Matplotlib não está disponível. Instale com: pip install matplotlib")
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
    
    # Cria figura com dois subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Converte grids para numpy arrays
    initial_array = np.array(initial_grid)
    filled_array = np.array(filled_grid)
    
    # Cria mapa de cores personalizado
    unique_values = sorted(set(val for row in filled_grid for val in row))
    colors_list = [color_map.get(val, 'gray') for val in unique_values]
    cmap = mcolors.ListedColormap(colors_list)
    bounds = unique_values + [max(unique_values) + 1]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    
    # Plota grid inicial
    im1 = ax1.imshow(initial_array, cmap='gray_r', vmin=0, vmax=1, interpolation='nearest')
    ax1.set_title('Grid Inicial', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Coluna')
    ax1.set_ylabel('Linha')
    ax1.grid(True, color='gray', linewidth=0.5)
    ax1.set_xticks(range(len(initial_grid[0])))
    ax1.set_yticks(range(len(initial_grid)))
    
    # Adiciona valores no grid inicial
    for i in range(len(initial_grid)):
        for j in range(len(initial_grid[0])):
            text_color = 'white' if initial_grid[i][j] == 1 else 'black'
            ax1.text(j, i, str(initial_grid[i][j]), 
                    ha='center', va='center', color=text_color, fontweight='bold')
    
    # Plota grid preenchido
    im2 = ax2.imshow(filled_array, cmap=cmap, norm=norm, interpolation='nearest')
    ax2.set_title('Grid Preenchido', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Coluna')
    ax2.set_ylabel('Linha')
    ax2.grid(True, color='gray', linewidth=0.5)
    ax2.set_xticks(range(len(filled_grid[0])))
    ax2.set_yticks(range(len(filled_grid)))
    
    # Adiciona valores no grid preenchido
    for i in range(len(filled_grid)):
        for j in range(len(filled_grid[0])):
            text_color = 'white' if filled_grid[i][j] == 1 else 'black'
            ax2.text(j, i, str(filled_grid[i][j]), 
                    ha='center', va='center', color=text_color, fontweight='bold')
    
    # Ajusta layout
    plt.tight_layout()
    
    # Mostra legenda
    legend_text = "Legenda:\n"
    legend_text += "0 = Branco (Terreno navegável)\n"
    legend_text += "1 = Preto (Obstáculo)\n"
    for val in sorted(set(val for row in filled_grid for val in row)):
        if val >= 2:
            color_name = color_map.get(val, f'Cor {val}')
            legend_text += f"{val} = {color_name.capitalize()}\n"
    
    fig.text(0.5, 0.02, legend_text, ha='center', fontsize=10, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.show()


def create_example_files():
    """
    Cria arquivos de exemplo para teste.
    """
    # Exemplo 1
    example1 = """4 5
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
0 0
"""
    
    # Exemplo 2
    example2 = """4 5
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
0 2
"""
    
    with open('exemplo1.txt', 'w') as f:
        f.write(example1)
    
    with open('exemplo2.txt', 'w') as f:
        f.write(example2)
    
    print("Arquivos de exemplo criados: exemplo1.txt, exemplo2.txt")

