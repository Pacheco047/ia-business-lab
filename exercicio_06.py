nome_cliente = input("Digite o nome do cliente: ")
email_cliente = input("Digite o email do cliente: ")
valor_orcamento = float(input("Digite o valor do orçamento: "))

if valor_orcamento >= 5000 and email_cliente != "":
    print(f"Cliente: {nome_cliente} lead classificado como alta prioridade.")
else:
    print(f"Cliente: {nome_cliente} lead não classificado.")