nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = int(input("Digite a idade do cliente: "))
cidade_cliente = input("Digite a cidade do cliente: ")
valor_investido = float(input("Digite o valor investido pelo cliente: "))

print(f"Nome do cliente: {nome_cliente}")
print(f"Idade do cliente: {idade_cliente}")
print(f"Cidade do cliente: {cidade_cliente}")
print(f"Valor investido: R$ {valor_investido:.2f}")

#Aqui foram usadas as variáveis nome_cliente, idade_cliente, cidade_cliente e valor_investido, e o input() para armazenar as informações fornecidas pelo usuário. Em seguida, essas variáveis foram utilizadas na função print para exibir uma mensagem personalizada ao usuário, incluindo a formatação float do valor investido com duas casas decimais.