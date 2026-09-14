nome_cliente = input("Digite o nome do cliente: ")
valor_orcamento = float(input("Digite o valor do orçamento: "))

if valor_orcamento >= 10000:
    print(f"Cliente: {nome_cliente} classificado como alta prioridade.")
elif valor_orcamento >= 5000:
    print(f"Cliente: {nome_cliente} classificado como média prioridade.")  
else:
    print(f"Cliente: {nome_cliente} classificado como baixa prioridade.")