import matplotlib.colors as mcolors

def obter_rgb(cor_nome):
    try:
        # Tenta obter a cor em formato hexadecimal
        cor_hex = mcolors.CSS4_COLORS[cor_nome]
        # Converte o valor hexadecimal para RGB
        cor_rgb = tuple(int(cor_hex[i:i+2], 16) for i in (1, 3, 5))
        return {cor_nome: cor_rgb}
    except KeyError:
        # Levanta exceção se a cor não for encontrada
        raise ValueError(f"Cor '{cor_nome}' não encontrada.")

# Solicita que o usuário insira o nome da cor
cor_nome = input("Digite o nome da cor (em inglês): ").lower()

try:
    # Mostra o valor RGB correspondente
    resultado = obter_rgb(cor_nome)
    print(resultado)
except ValueError as e:
    print(e)
  
