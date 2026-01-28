
# Verifica se o nome informado é Válido (Apenas Letras )
nome_informado = input("Digite o seu nome: ")

if nome_informado.isalpha() and len(nome_informado) >= 3:
    print("O nome informado é válido.")
elif nome_informado == "":
    print("Nenhum nome foi informado.")
elif len(nome_informado) < 3:
    print("O nome informado é muito curto. Deve ter pelo menos 3 letras.")             
else:
    print("O nome informado é inválido. Por favor, use apenas letras.")


