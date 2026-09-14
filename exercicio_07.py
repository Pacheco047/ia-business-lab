nome_cliente = input("Digite o nome do cliente: ")
email_cliente = input("Digite o email do cliente: ")
telefone_cliente = input("Digite o telefone do cliente: ")

if email_cliente != "" or telefone_cliente != "":
    print(f"Cliente: {nome_cliente} possui um meio de contato cadastrado.")
else:
    print(f"Cliente: {nome_cliente} não possui nenhum meio de contato cadastrado.")
