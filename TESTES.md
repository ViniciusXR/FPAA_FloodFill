# Comandos de Teste - Projeto Flood Fill

## 🧪 Testes Básicos

### 1. Teste com Exemplo 1 (do trabalho)
```bash
python main.py exemplo1.txt
```
**Resultado esperado**: Grid com 3 regiões preenchidas (cores 2, 3, 4)

### 2. Teste com Exemplo 2 (do trabalho)
```bash
python main.py exemplo2.txt
```
**Resultado esperado**: Grid com 3 regiões preenchidas (cores 2, 3, 4)

### 3. Teste com entrada interativa
```bash
python main.py
```
Depois digite:
```
4 5
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
0 0
```

## 🔍 Testes de Validação

### 4. Teste com grid inválido (deve dar erro)
Crie um arquivo `teste_erro.txt`:
```
3 3
0 0 0
0 0
0 0 0
0 0
```
```bash
python main.py teste_erro.txt
```
**Resultado esperado**: Erro informando que a linha tem número incorreto de colunas

### 5. Teste com coordenadas inválidas
Crie um arquivo `teste_coords.txt`:
```
3 3
0 0 0
0 0 0
0 0 0
10 10
```
```bash
python main.py teste_coords.txt
```
**Resultado esperado**: Erro informando que as coordenadas estão fora dos limites

### 6. Teste com célula inicial em obstáculo
Crie um arquivo `teste_obstaculo.txt`:
```
3 3
1 0 0
0 0 0
0 0 0
0 0
```
```bash
python main.py teste_obstaculo.txt
```
**Resultado esperado**: Aviso e busca automática da primeira célula navegável

## ⭐ Testes de Funcionalidades Extras

### 7. Gerar grid aleatório
```bash
python -c "from extra_features import create_random_grid_file; create_random_grid_file('grid_aleatorio.txt', 8, 8, 0.25); print('Grid aleatório criado!')"
```
Depois teste:
```bash
python main.py grid_aleatorio.txt
```

### 8. Teste de visualização dinâmica
```bash
python -c "from extra_features import visualize_dynamic_fill; grid = [[0,0,1,0,0],[0,1,1,0,0],[0,0,1,1,1],[1,1,0,0,0]]; visualize_dynamic_fill(grid, 0, 0, 0.2)"
```

## 📊 Testes de Casos Especiais

### 9. Grid sem células navegáveis
Crie um arquivo `teste_sem_navegavel.txt`:
```
3 3
1 1 1
1 1 1
1 1 1
0 0
```
```bash
python main.py teste_sem_navegavel.txt
```
**Resultado esperado**: Erro informando que não há células navegáveis

### 10. Grid pequeno (2x2)
Crie um arquivo `teste_pequeno.txt`:
```
2 2
0 0
0 1
0 0
```
```bash
python main.py teste_pequeno.txt
```

### 11. Grid grande (teste de performance)
Crie um arquivo `teste_grande.txt` com um grid 20x20 (ou use o gerador):
```bash
python -c "from extra_features import create_random_grid_file; create_random_grid_file('teste_grande.txt', 20, 20, 0.3)"
python main.py teste_grande.txt
```

## 🧹 Limpeza

### 12. Remover arquivos de teste criados
```bash
# Windows PowerShell
Remove-Item teste_*.txt, grid_aleatorio.txt -ErrorAction SilentlyContinue

# Linux/Mac
rm -f teste_*.txt grid_aleatorio.txt
```

## ✅ Checklist de Verificação

Após executar os testes, verifique:

- [ ] Exemplo 1 produz resultado correto (cores 2, 3, 4)
- [ ] Exemplo 2 produz resultado correto (cores 2, 3, 4)
- [ ] Visualização em terminal funciona
- [ ] Visualização gráfica abre (se matplotlib instalado)
- [ ] Erros são tratados adequadamente
- [ ] Grids aleatórios são gerados corretamente
- [ ] Casos especiais são tratados

## 🚀 Teste Rápido Completo

Execute este comando para testar tudo de uma vez:

```bash
# Teste básico
python main.py exemplo1.txt
python main.py exemplo2.txt

# Teste de funcionalidades extras
python -c "from extra_features import create_random_grid_file; create_random_grid_file('teste_rapido.txt', 5, 5, 0.2)"
python main.py teste_rapido.txt
```

