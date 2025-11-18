"""
Implementação do Algoritmo Flood Fill para colorir regiões conectadas em um grid 2D.
"""

from collections import deque
from typing import List, Tuple, Optional


class FloodFill:
    """
    Classe que implementa o algoritmo Flood Fill para preencher regiões conectadas
    em um grid bidimensional.
    """
    
    def __init__(self, grid: List[List[int]]):
        """
        Inicializa o Flood Fill com um grid.
        
        Args:
            grid: Grid bidimensional onde 0 = navegável, 1 = obstáculo, >=2 = cores preenchidas
        """
        self.grid = [row[:] for row in grid]  # Cópia do grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.current_color = 2  # Começa com cor 2 (vermelho)
    
    def is_valid(self, row: int, col: int) -> bool:
        """
        Verifica se uma célula está dentro dos limites do grid.
        
        Args:
            row: Linha da célula
            col: Coluna da célula
            
        Returns:
            True se a célula está dentro dos limites, False caso contrário
        """
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def is_navigable(self, row: int, col: int) -> bool:
        """
        Verifica se uma célula é navegável (valor 0).
        
        Args:
            row: Linha da célula
            col: Coluna da célula
            
        Returns:
            True se a célula é navegável, False caso contrário
        """
        return self.is_valid(row, col) and self.grid[row][col] == 0
    
    def fill_region_recursive(self, start_row: int, start_col: int, color: int) -> None:
        """
        Preenche uma região conectada usando abordagem recursiva (DFS).
        
        Args:
            start_row: Linha inicial
            start_col: Coluna inicial
            color: Cor para preencher a região
        """
        if not self.is_navigable(start_row, start_col):
            return
        
        self.grid[start_row][start_col] = color
        
        # Direções: cima, baixo, esquerda, direita (adjacência ortogonal)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = start_row + dr, start_col + dc
            if self.is_navigable(new_row, new_col):
                self.fill_region_recursive(new_row, new_col, color)
    
    def fill_region_iterative(self, start_row: int, start_col: int, color: int) -> None:
        """
        Preenche uma região conectada usando abordagem iterativa (BFS).
        Mais eficiente para grids grandes, evita estouro de pilha.
        
        Args:
            start_row: Linha inicial
            start_col: Coluna inicial
            color: Cor para preencher a região
        """
        if not self.is_navigable(start_row, start_col):
            return
        
        queue = deque([(start_row, start_col)])
        self.grid[start_row][start_col] = color
        
        # Direções: cima, baixo, esquerda, direita (adjacência ortogonal)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if self.is_navigable(new_row, new_col):
                    self.grid[new_row][new_col] = color
                    queue.append((new_row, new_col))
    
    def fill_from_point(self, start_row: int, start_col: int, use_iterative: bool = True) -> bool:
        """
        Preenche a região conectada a partir de um ponto inicial.
        
        Args:
            start_row: Linha inicial
            start_col: Coluna inicial
            use_iterative: Se True, usa abordagem iterativa (BFS), senão usa recursiva (DFS)
            
        Returns:
            True se uma região foi preenchida, False caso contrário
        """
        if not self.is_navigable(start_row, start_col):
            return False
        
        if use_iterative:
            self.fill_region_iterative(start_row, start_col, self.current_color)
        else:
            self.fill_region_recursive(start_row, start_col, self.current_color)
        
        self.current_color += 1
        return True
    
    def find_next_navigable_cell(self) -> Optional[Tuple[int, int]]:
        """
        Encontra a próxima célula navegável (valor 0) no grid.
        
        Returns:
            Tupla (row, col) da próxima célula navegável, ou None se não houver
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None
    
    def fill_all_regions(self, initial_row: int, initial_col: int, use_iterative: bool = True) -> None:
        """
        Preenche todas as regiões conectadas do grid, começando pela célula inicial
        e depois automaticamente encontrando e preenchendo as demais.
        
        Args:
            initial_row: Linha inicial
            initial_col: Coluna inicial
            use_iterative: Se True, usa abordagem iterativa, senão usa recursiva
        """
        # Preenche a região inicial
        self.fill_from_point(initial_row, initial_col, use_iterative)
        
        # Continua preenchendo até não haver mais células navegáveis
        while True:
            next_cell = self.find_next_navigable_cell()
            if next_cell is None:
                break
            self.fill_from_point(next_cell[0], next_cell[1], use_iterative)
    
    def get_grid(self) -> List[List[int]]:
        """
        Retorna o grid atual.
        
        Returns:
            Grid bidimensional atualizado
        """
        return self.grid
    
    def reset(self, new_grid: Optional[List[List[int]]] = None) -> None:
        """
        Reseta o Flood Fill com um novo grid ou mantém o atual.
        
        Args:
            new_grid: Novo grid (opcional)
        """
        if new_grid is not None:
            self.grid = [row[:] for row in new_grid]
            self.rows = len(new_grid)
            self.cols = len(new_grid[0]) if new_grid else 0
        self.current_color = 2

