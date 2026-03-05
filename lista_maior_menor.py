lista = [1,2,1,3]
tamanho = int(input('Qual tamanho da lista? '))
lista = [int(input('digite o numero: ')) for i in range(tamanho)]
print(f"maior: {max(lista)} menor: {min(lista)} media: {sum(lista) / tamanho}")