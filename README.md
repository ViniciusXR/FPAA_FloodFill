# 🌊 Algoritmo Flood Fill - Colorindo Regiões de um Terreno com Obstáculos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Implementação completa do algoritmo Flood Fill para identificar e preencher automaticamente todas as regiões conectadas em um grid 2D**

[📖 Documentação](#-como-funciona-o-algoritmo-flood-fill) • [🚀 Instalação](#-instalação) • [💻 Uso](#-como-usar) • [⭐ Funcionalidades](#-funcionalidades)

</div>

---

## 📋 Sobre o Projeto

Este projeto implementa o **Algoritmo Flood Fill** para identificar e preencher automaticamente todas as regiões conectadas em um grid bidimensional, utilizando diferentes cores para cada área. O sistema foi desenvolvido para mapeamento inteligente de terrenos para robôs autônomos, onde é necessário identificar e classificar regiões navegáveis separadas por obstáculos.

### 🎯 Objetivo

- ✅ Identificar e preencher automaticamente todas as regiões conectadas em um grid 2D
- ✅ Utilizar diferentes cores para cada área desconectada
- ✅ Respeitar os obstáculos presentes no terreno
- ✅ Localizar automaticamente novas áreas livres após preencher uma região
- ✅ Continuar o processo até que todo o terreno esteja mapeado e colorido

### 📊 Representação do Grid

O terreno é representado como um grid bidimensional, onde cada célula pode ser:

- **`0` (Branco)**: Terreno navegável - regiões que podem ser preenchidas
- **`1` (Preto)**: Obstáculo - não navegável, deve ser ignorado pelo preenchimento
- **`2, 3, 4, ...`**: Cores já preenchidas em outras regiões (vermelho, laranja, amarelo, etc.)

---

## 🔧 Como Funciona o Algoritmo Flood Fill

O **Flood Fill** (também conhecido como "preenchimento por inundação") é um algoritmo clássico de processamento de imagens e grafos que preenche uma região conectada a partir de um ponto inicial.

### Funcionamento Detalhado

1. **Ponto Inicial**: O algoritmo recebe uma célula inicial (x, y) no grid.

2. **Identificação de Região Conectada**: 
   - A partir da célula inicial, o algoritmo explora todas as células adjacentes ortogonalmente (acima, abaixo, esquerda, direita)
   - Uma célula é considerada parte da região se:
     - Está dentro dos limites do grid
     - Tem valor 0 (navegável)
     - É ortogonalmente adjacente a outra célula da mesma região

3. **Preenchimento**:
   - Todas as células da região conectada são preenchidas com uma cor específica (começando em 2)
   - Obstáculos (valor 1) são respeitados e não são preenchidos
   - Regiões já coloridas (valor >= 2) são mantidas intactas

4. **Preenchimento Automático**:
   - Após preencher uma região, o algoritmo localiza automaticamente a próxima célula navegável (valor 0)
   - Preenche essa nova região com uma cor diferente (incrementando o valor: 2, 3, 4, ...)
   - O processo continua até que não haja mais células navegáveis

### Implementação

O projeto implementa **duas abordagens**:

- **Recursiva (DFS)**: Usa recursão para explorar a região - mais simples, mas pode causar estouro de pilha em grids muito grandes
- **Iterativa (BFS)**: Usa uma fila (queue) para explorar a região - mais eficiente e **padrão do programa**

### Complexidade

- **Tempo**: O(n × m), onde n e m são as dimensões do grid
- **Espaço**: O(n × m) na pior caso

---

## 📦 Estrutura do Projeto

```
FPAA_FloodFill/
│
├── flood_fill.py      # Implementação do algoritmo Flood Fill
├── main.py            # Programa principal (entrada/saída)
├── visualization.py   # Módulo de visualização (terminal e gráfica)
├── extra_features.py  # Funcionalidades extras (visualização dinâmica, grids aleatórios)
├── test_cases.py      # Casos de teste adicionais
├── requirements.txt   # Dependências do projeto
├── README.md          # Este arquivo
├── exemplo1.txt       # Exemplo de entrada 1
└── exemplo2.txt       # Exemplo de entrada 2
```

---

## 🚀 Instalação

### Pré-requisitos

- **Python 3.7 ou superior**
- **pip** (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**:
```bash
git clone https://github.com/ViniciusXR/FPAA_FloodFill.git
cd FPAA_FloodFill
```

2. **Instale as dependências** (opcional, apenas para visualização gráfica):
```bash
pip install -r requirements.txt
```

> **Nota**: O programa funciona sem as dependências, mas a visualização gráfica não estará disponível.

---

## 💻 Como Usar

### Opção 1: Executar com Arquivo de Entrada

```bash
python main.py exemplo1.txt
```

ou

```bash
python main.py exemplo2.txt
```

### Opção 2: Executar com Entrada Interativa

```bash
python main.py
```

Depois, digite a entrada no formato:
```
n m
<grid com n linhas e m colunas>
x y
```

**Exemplo de entrada**:
```
4 5
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
0 0
```

### Opção 3: Executar sem Entrada (usa exemplo padrão)

Pressione `Ctrl+C` quando solicitado a entrada, e o programa usará o exemplo padrão.

---

## 📝 Formato de Entrada

O arquivo de entrada deve seguir este formato:

```
n m
a11 a12 ... a1m
a21 a22 ... a2m
...
an1 an2 ... anm
x y
```

Onde:
- `n m`: dimensões do grid (linhas e colunas)
- `<grid>`: valores do grid separados por espaço
- `x y`: coordenadas iniciais (linha e coluna)

---

## 📊 Exemplos de Entrada e Saída

### Exemplo 1

**Entrada** (`exemplo1.txt`):
```
4 5
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
0 0
```

**Grid Inicial**:
```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```

**Grid Preenchido**:
```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

**Explicação**:
- A região conectada a (0,0) foi preenchida com cor 2 (vermelho)
- A região do canto superior direito foi preenchida com cor 3 (laranja)
- A região do canto inferior direito foi preenchida com cor 4 (amarelo)
- Os obstáculos (valor 1) permanecem inalterados

### Exemplo 2

**Entrada** (`exemplo2.txt`):
```
4 5
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
0 2
```

**Grid Inicial**:
```
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
```

**Grid Preenchido**:
```
3 1 2 2 1
3 1 2 2 1
3 1 1 1 1
3 3 3 1 4
```

---

## 🎨 Visualização

O programa oferece **duas formas de visualização**:

### 1. Visualização em Terminal

Mostra os grids em formato de matriz com números, incluindo índices de linhas e colunas para facilitar a leitura.

### 2. Visualização Gráfica (com cores)

Mostra os grids com cores:
- **Branco**: Terreno navegável (0)
- **Preto**: Obstáculo (1)
- **Vermelho**: Região 1 (2)
- **Laranja**: Região 2 (3)
- **Amarelo**: Região 3 (4)
- E assim por diante...

A visualização gráfica abre uma janela com os dois grids lado a lado para comparação.

---

## ⭐ Funcionalidades Extras

O projeto inclui funcionalidades extras implementadas no arquivo `extra_features.py`:

### 1. Visualização Dinâmica

Mostra o grid sendo preenchido em tempo real, célula por célula:

```python
from extra_features import visualize_dynamic_fill

grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0]
]
visualize_dynamic_fill(grid, 0, 0, delay=0.3)
```

### 2. Geração de Grids Aleatórios

Gera grids aleatórios com diferentes proporções de terrenos navegáveis e obstáculos:

```python
from extra_features import generate_random_grid, create_random_grid_file

# Gerar grid aleatório 10x10 com 30% de obstáculos
grid = generate_random_grid(10, 10, obstacle_ratio=0.3)

# Criar arquivo com grid aleatório
start = create_random_grid_file("grid_aleatorio.txt", 10, 10, 0.3)
```

**Parâmetros**:
- `rows`, `cols`: Dimensões do grid
- `obstacle_ratio`: Proporção de obstáculos (0.0 a 1.0)

---

## 🧪 Testes

### Testes Básicos

```bash
# Teste com Exemplo 1
python main.py exemplo1.txt

# Teste com Exemplo 2
python main.py exemplo2.txt
```

### Teste com Entrada Interativa

```bash
python main.py
```

### Teste de Funcionalidades Extras

```bash
# Gerar grid aleatório
python -c "from extra_features import create_random_grid_file; create_random_grid_file('grid_teste.txt', 8, 8, 0.25); print('Grid criado!')"
python main.py grid_teste.txt

# Visualização dinâmica
python -c "from extra_features import visualize_dynamic_fill; grid = [[0,0,1,0,0],[0,1,1,0,0],[0,0,1,1,1],[1,1,0,0,0]]; visualize_dynamic_fill(grid, 0, 0, 0.3)"
```

### Casos de Teste Especiais

O arquivo `test_cases.py` contém casos de teste adicionais para validação do algoritmo, incluindo:
- Grids de diferentes tamanhos
- Grids com múltiplos obstáculos
- Grids sem células navegáveis
- Grids com uma única região conectada
- Grids com múltiplas regiões desconectadas
- Coordenadas iniciais em diferentes posições

---

## 📝 Regras de Funcionamento

1. **Respeito a Obstáculos**: O preenchimento não pode passar através de células com valor 1 (obstáculos)

2. **Preservação de Cores**: Regiões já coloridas (valor >= 2) são mantidas intactas

3. **Adjacência Ortogonal**: Uma região conectada é composta apenas de células ortogonalmente adjacentes (acima, abaixo, esquerda, direita). Não considera adjacência diagonal.

4. **Preenchimento Automático**: Após preencher uma região, o programa localiza automaticamente a próxima célula navegável e preenche uma nova região com cor diferente

5. **Completude**: O processo continua até que todas as células navegáveis tenham sido preenchidas

---

## 🔍 Detalhes Técnicos

### Estrutura de Dados

- **Grid**: Lista de listas de inteiros (`List[List[int]]`)
- **Fila**: `collections.deque` para implementação iterativa (BFS)

### Algoritmo Principal

```python
def fill_all_regions(initial_row, initial_col):
    1. Preenche região conectada à célula inicial
    2. Enquanto houver células navegáveis (valor 0):
       a. Encontra próxima célula navegável
       b. Preenche região conectada com nova cor
       c. Incrementa cor atual
```

### Tratamento de Casos Especiais

- Coordenadas fora dos limites do grid
- Grid vazio
- Grid sem células navegáveis
- Célula inicial em obstáculo (usa próxima célula navegável)

---

## 👥 Autores

Projeto desenvolvido para a disciplina de **Fundamentos de Projeto e Análise de Algoritmos** da PUC Minas.

**Equipe**:
- Cristiano Nunes Pires Junior
- Joey Clapton Maciel Barbosa Santos
- Sthel Felipe Torres
- Vinicius Xavier Ramalho

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🎓 Referências

- **Flood Fill Algorithm**: Algoritmo clássico de preenchimento de regiões conectadas
- **DFS (Depth-First Search)**: Busca em profundidade
- **BFS (Breadth-First Search)**: Busca em largura
- **Grafos**: Teoria de grafos para modelagem de grids

---

<div align="center">

**Desenvolvido usando Python 3**

[⬆ Voltar ao topo](#-algoritmo-flood-fill---colorindo-regiões-de-um-terreno-com-obstáculos)

</div>
