"""
Arquivo com casos de teste adicionais para o projeto Flood Fill.
"""

# Caso 1: Grid pequeno (2x2)
test_case_1 = {
    "name": "Grid pequeno 2x2",
    "grid": [
        [0, 0],
        [0, 1]
    ],
    "start": (0, 0),
    "expected_regions": 1
}

# Caso 2: Grid com uma única região grande
test_case_2 = {
    "name": "Grid com uma única região",
    "grid": [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    "start": (0, 0),
    "expected_regions": 1
}

# Caso 3: Grid sem células navegáveis
test_case_3 = {
    "name": "Grid sem células navegáveis",
    "grid": [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ],
    "start": (0, 0),
    "expected_regions": 0
}

# Caso 4: Grid com múltiplas regiões pequenas
test_case_4 = {
    "name": "Grid com múltiplas regiões pequenas",
    "grid": [
        [0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0]
    ],
    "start": (0, 0),
    "expected_regions": 3
}

# Caso 5: Grid grande (10x10)
test_case_5 = {
    "name": "Grid grande 10x10",
    "grid": [
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    ],
    "start": (0, 0),
    "expected_regions": 8
}

# Caso 6: Grid com região já colorida
test_case_6 = {
    "name": "Grid com região já colorida",
    "grid": [
        [0, 0, 1, 2, 2],
        [0, 1, 1, 2, 2],
        [0, 0, 1, 1, 1]
    ],
    "start": (0, 0),
    "expected_regions": 1  # Apenas a região conectada a (0,0) será preenchida
}

# Caso 7: Grid retangular (3x5)
test_case_7 = {
    "name": "Grid retangular 3x5",
    "grid": [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0]
    ],
    "start": (0, 0),
    "expected_regions": 2
}

# Caso 8: Grid com obstáculo na célula inicial
test_case_8 = {
    "name": "Grid com obstáculo na célula inicial",
    "grid": [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    "start": (0, 0),  # Célula inicial é obstáculo
    "expected_regions": 1  # Deve encontrar a próxima célula navegável
}

ALL_TEST_CASES = [
    test_case_1,
    test_case_2,
    test_case_3,
    test_case_4,
    test_case_5,
    test_case_6,
    test_case_7,
    test_case_8
]

