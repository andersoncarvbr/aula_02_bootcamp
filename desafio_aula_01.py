
# Verifica se o nome informado é Válido (Apenas Letras )
nome_informado = input("Digite o seu nome: ")

if nome_informado.isalpha():
    print("O nome informado é válido.")
elif nome_informado == "":
    print("Nenhum nome foi informado.")         
else:
    print("O nome informado é inválido. Por favor, use apenas letras.")


