# Lista vazia para armazenar números
numeros = []

# Lista de idade com idades
#         0    1   2   3   4   5   6   7
idades = [15, 22, 14, 31, 20, 22, 15, 18]

# Lista vazia para armazenar nomes
nomes = []

# Lista de cores com cores
#            0         1        2       3          4         5
cores = ['Amarelo', 'Verde', 'Roxo', 'Verde', 'Vermelho', 'Azul']

# Recebe input do usuário com uma cor para adicionar
corAdd = input('Cor a adicionar: ')

# Adiciona a cor digitada no final na lista de cores, com o método append
cores.append(corAdd)

# Remove a cor na posição 0 (índice) da lista 
cores.pop(0)

# Mostra na tela a lista de cores
print(cores)

# Recebe input do usuário com uma cor para pesquisar
corPesquisa = input('Cor a pesquisar: ')

# Percorre a lista de cores
for color in cores:
    # Compara a cor digitado com todas as cores da lista
    if corPesquisa == color:
        # Caso encontre, mostra na tela mensagem avisando que encontrou
        print("Encontrouuuu")

# Percorre a lista de cores
for color in cores:
    # Mostra todas as cores (uma a uma) na tela
    print(color)

# Mostra na tela a idade na última posição da lista de idade
print(idades[len(idades)-1])

# Mostra na tela o tamanho da lista de números
print(len(numeros))

# Mostra na tela o tamanho da lista de idades
print(len(idades))

# Mostra na tela a maior e a menor idade da lista de idade
print(max(idades))
print(min(idades))

# Mostra na tela a maior cor (palavra com mais letras) da lista de cores
print(max(cores))