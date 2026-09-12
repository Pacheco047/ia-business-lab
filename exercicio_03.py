nome_cliente = input("Digite o nome do cliente: ")
valor_mensal = float(input("Digite o valor mensal: "))
meses_pagamento = int(input("Digite o número de meses para pagamento: "))

valor_total = valor_mensal * meses_pagamento

print(f"Cliente: {nome_cliente}")
print(f"Valor mensal a ser pago: R$ {valor_mensal:.2f}")
print(f"Número de meses: {meses_pagamento}")
print(f"Valor total: R$ {valor_total:.2f}")