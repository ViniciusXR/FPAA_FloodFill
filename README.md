# Algoritmo Flood Fill

Implementação em Python do algoritmo Flood Fill para identificar e preencher automaticamente todas as regiões conectadas em um grid 2D, utilizando diferentes cores para cada área.

## Alunos

* Cristiano Nunes Pires Junior
* Joey Clapton Maciel Barbosa Santos
* Sthel Felipe Torres
* Vinicius Xavier Ramalho

---

## 📋 Descrição do Projeto

Este projeto implementa um **sistema de mapeamento inteligente** para robôs autônomos que precisam identificar e classificar regiões de um terreno previamente desconhecido. O sistema utiliza o **Algoritmo Flood Fill** para mapear automaticamente áreas navegáveis em um grid bidimensional, diferenciando-as por cores distintas.

### Contexto

Uma empresa de automação necessita de uma ferramenta capaz de:
- Identificar regiões conectadas em um terreno representado como grid 2D
- Diferenciar áreas livres de obstáculos
- Colorir automaticamente cada região desconectada com uma cor única
- Facilitar a visualização e o planejamento de operações robóticas

---

## 🎯 Problema Resolvido

### Identificação e Preenchimento de Regiões Conectadas

O projeto resolve o desafio de **identificar e preencher todas as regiões navegáveis conectadas** em um grid bidimensional que contém:

- **Terrenos navegáveis** (valor `0`): Áreas livres que podem ser exploradas
- **Obstáculos** (valor `1`): Barreiras que não podem ser atravessadas
- **Regiões coloridas** (valores `2, 3, 4, ...`): Áreas já identificadas e mapeadas

### Aplicações Práticas

- **Robótica**: Mapeamento de ambientes para navegação autônoma
- **Computação Gráfica**: Ferramenta de preenchimento (balde de tinta)
- **Processamento de Imagens**: Segmentação e identificação de regiões
- **Jogos**: Detecção de áreas conectadas em mapas

---

## 🚀 Instruções de Configuração e Execução

### Pré-requisitos

- **Python 3.13.7 ou superior** instalado no sistema
- Nenhuma biblioteca externa é necessária (usa apenas bibliotecas padrão do Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ViniciusXR/FPAA_FloodFill.git
cd FPAA_FloodFill
```

2. Verifique a versão do Python:
```bash
python --version
```

### Execução

Execute o programa principal:

```bash
python main.py
```

### Opções de Uso

Ao executar o programa, você terá duas opções:

**Opção 1 - Grid de Exemplo:**
- Utiliza um grid pré-definido de 5x5
- Ideal para testes rápidos e demonstração

**Opção 2 - Grid Personalizado:**
- Permite inserir suas próprias dimensões e configuração
- Entrada interativa para criar grids customizados

**Coordenadas Iniciais:**
- Você pode especificar uma célula inicial `(x, y)` para começar o preenchimento
- Ou pressionar Enter para preenchimento automático de todas as regiões

---

## 🧮 Algoritmo Flood Fill

### Funcionamento

O **Algoritmo Flood Fill** (Preenchimento por Inundação) é uma técnica clássica para identificar e preencher regiões conectadas em estruturas bidimensionais. É o mesmo algoritmo usado em ferramentas de "balde de tinta" em editores de imagem.

### Processo de Execução

#### 1. **Inicialização**
- Recebe uma célula inicial `(x, y)` no grid
- Identifica a cor/valor original dessa célula (geralmente `0` para terreno navegável)
- Define uma nova cor para preencher a região (valores `2, 3, 4, ...`)

#### 2. **Propagação Recursiva**
O algoritmo percorre o grid seguindo estes passos:

```
1. Verifica se a posição atual está dentro dos limites do grid
2. Verifica se a célula possui o valor original (0)
3. Preenche a célula atual com a nova cor
4. Recursivamente, repete o processo para as células adjacentes:
   - Célula acima (x-1, y)
   - Célula abaixo (x+1, y)
   - Célula à esquerda (x, y-1)
   - Célula à direita (x, y+1)
```

#### 3. **Respeito a Limites e Obstáculos**
- **Limites do grid**: O algoritmo para ao atingir as bordas
- **Obstáculos** (valor `1`): Não são atravessados nem modificados
- **Regiões coloridas** (valores > 1): Mantidas intactas

#### 4. **Preenchimento Automático de Todas as Regiões**
Após preencher uma região:
1. O programa busca automaticamente a próxima célula navegável (`0`)
2. Inicia um novo preenchimento com uma cor diferente
3. Repete até que não existam mais células navegáveis

### Complexidade

- **Tempo**: O(n × m) - cada célula é visitada no máximo uma vez
- **Espaço**: O(n × m) - no pior caso, a pilha de recursão armazena todas as células

---

## 📊 Exemplos de Entrada e Saída

### Exemplo 1: Grid Simples 5x5

#### Entrada

```
Dimensões: 5 x 5
Coordenada inicial: (0, 0)

Grid inicial:
0 0 1 0 0
0 1 1 0 0
0 0 1 0 1
1 0 0 0 0
0 0 1 0 0
```

**Legenda:**
- `0` = Terreno navegável (branco)
- `1` = Obstáculo (preto)

#### Saída

```
Grid após preenchimento:
2 2 1 3 3
2 1 1 3 3
2 2 1 3 1
1 4 4 4 4
5 5 1 4 4
```

**Análise:**
- **Região 2** (vermelho): Área superior esquerda - 6 células conectadas
- **Região 3** (laranja): Área superior direita - 6 células conectadas
- **Região 4** (amarelo): Área inferior - 6 células conectadas
- **Região 5** (verde): Área inferior esquerda - 2 células conectadas
- **Total**: 4 regiões identificadas

---

### Exemplo 2: Grid com Múltiplas Regiões 7x7

#### Entrada

```
Dimensões: 7 x 7
Coordenada inicial: (3, 3)

Grid inicial:
0 0 0 1 0 0 0
0 1 0 1 0 1 0
0 0 0 1 0 0 0
1 1 1 1 1 1 1
0 0 0 1 0 0 0
0 1 0 1 0 1 0
0 0 0 1 0 0 0
```

#### Saída

```
Grid após preenchimento:
2 2 2 1 3 3 3
2 1 2 1 3 1 3
2 2 2 1 3 3 3
1 1 1 1 1 1 1
4 4 4 1 5 5 5
4 1 4 1 5 1 5
4 4 4 1 5 5 5
```

**Análise:**
- **Região 2**: Quadrante superior esquerdo - 9 células
- **Região 3**: Quadrante superior direito - 9 células
- **Região 4**: Quadrante inferior esquerdo - 9 células
- **Região 5**: Quadrante inferior direito - 9 células
- **Linha de obstáculos** no meio divide o grid em 4 quadrantes

---

### Exemplo 3: Grid Pequeno 3x3

#### Entrada

```
Dimensões: 3 x 3
Coordenada inicial: não especificada (automático)

Grid inicial:
0 1 0
1 0 1
0 1 0
```

#### Saída

```
Grid após preenchimento:
2 1 3
1 4 1
5 1 6
```

**Análise:**
- **5 regiões isoladas**: Cada célula navegável forma sua própria região
- Demonstra o caso de máxima fragmentação

---

### Exemplo 4: Grid Completamente Conectado 4x4

#### Entrada

```
Dimensões: 4 x 4
Coordenada inicial: (0, 0)

Grid inicial:
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```

#### Saída

```
Grid após preenchimento:
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
```

**Análise:**
- **1 única região**: Todas as 16 células estão conectadas
- Demonstra o preenchimento completo de área aberta

---

## 🔍 Visualização do Processo

### Passo a Passo do Algoritmo

Considere o grid inicial:
```
0 0 1
0 1 0
```

**Passo 1**: Início em (0,0)
```
X 0 1    →    2 0 1
0 1 0         0 1 0
```

**Passo 2**: Propaga para direita (0,1)
```
2 X 1    →    2 2 1
0 1 0         0 1 0
```

**Passo 3**: Propaga para baixo (1,0)
```
2 2 1         2 2 1
X 1 0    →    2 1 0
```

**Passo 4**: Busca próxima região em (1,2)
```
2 2 1         2 2 1
2 1 X    →    2 1 3
```

**Resultado Final**:
- Região 2: 3 células conectadas
- Região 3: 1 célula isolada

---

## 📈 Estatísticas do Programa

O programa fornece informações detalhadas após o preenchimento:

- **Dimensões do grid**: Tamanho n × m
- **Total de células**: Número total de posições no grid
- **Obstáculos**: Quantidade de células bloqueadas
- **Regiões identificadas**: Número de áreas conectadas encontradas
- **Cores usadas**: Lista das cores/valores utilizados

---

## 🛠️ Estrutura do Código

### Funções Principais

1. **`flood_fill(grid, x, y, cor_atual, nova_cor)`**
   - Implementação recursiva do algoritmo
   - Preenche uma região conectada a partir de uma célula inicial

2. **`preencher_todas_regioes(grid, x_inicial, y_inicial)`**
   - Gerencia o preenchimento completo do grid
   - Localiza e preenche todas as regiões automaticamente

3. **`encontrar_proxima_celula_navegavel(grid)`**
   - Busca a próxima célula não preenchida (valor 0)
   - Retorna coordenadas ou None se não houver mais células

4. **`imprimir_grid(grid)`**
   - Formata e exibe o grid de forma legível

5. **`ler_grid_usuario()`**
   - Interface para entrada de grids personalizados

---

## 📚 Conceitos Abordados

- **Recursão**: Técnica fundamental para implementação do Flood Fill
- **Estruturas de Dados**: Manipulação de matrizes bidimensionais
- **Algoritmos de Busca**: Exploração de grafos implícitos
- **Análise de Complexidade**: Otimização de tempo e espaço

---

## 🎓 Referências

- **Algoritmo Flood Fill**: [Wikipedia - Flood Fill](https://en.wikipedia.org/wiki/Flood_fill)
- **Recursão em Python**: Técnicas de programação recursiva
- **Grafos e Conectividade**: Teoria de grafos aplicada a grids

---

## 📝 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.
