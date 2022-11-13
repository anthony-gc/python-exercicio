ganho_por_hora = float(input("Informe o quanto você ganha por hora:"))
horas_trabalhada = float(input("Informe o número de horas trabalhadas:"))
salario_bruto = ganho_por_hora * horas_trabalhada 
inss = salario_bruto * 0.08
imposto_renda = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
descontos = salario_bruto - (imposto_renda + inss + sindicato) 

print(f"Salário Bruto: R${salario_bruto}")
print(f"IR (11%): R${imposto_renda}")
print(f"INSS (8%): R${inss}")
print(f"Sindicato (5%): R${sindicato}")
print(f"Salário Liquido: R${descontos}")

