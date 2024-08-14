from random import choices, sample
def media_lista(lista):
    return sum(lista)

tamanho = 12
valores = range(1,51)
lista = sample(valores, tamanho)
quantidade = len(lista)
soma = media_lista(lista)
media = soma / quantidade
print(lista)
print(soma)
print(f"A media da lista é: {media}")