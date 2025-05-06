import os
os.system ("clear || cls")
from time import sleep

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075 
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04  # Teto máximo

def calcular_irrf(salario, dependentes):

    if salario <= 2259.20:
        base_calculo= 0
    elif salario <= 2826.65:
        base_calculo= salario * 0.075 - 169.44
    elif salario <= 3751.05:
        base_calculo= salario * 0.15 - 381.44
    elif salario <= 4664.68:
        base_calculo= salario * 0.225 - 662.77
    else:
        base_calculo= salario * 0.275 - 896.00
    return base_calculo - (dependentes * 189.59) 

def calcular_vale_transporte(salario, optou_vt):
    return salario * 0.06 if optou_vt.lower() == 's' else 0

def calcular_vale_refeicao(valor_vr):
    return valor_vr * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def folha_pagamento():
    print("=== Sistema de Folha de Pagamento ===")
    matricula = input("Informe sua matrícula: ")
    senha = input("Informe sua senha: ")
    os.system ("clear || cls")
    print("Acesso permitido.")
    sleep(1.5)
    try:
        salario_base = float(input("Informe seu salário base (R$): "))
        opta_vt = input("Deseja receber vale transporte? (s/n): ")
        valor_vr = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))
        dependentes = int(input("Informe a quantidade de dependentes: "))
        os.system ("clear || cls")

        desconto_inss = calcular_inss(salario_base)
        desconto_irrf = calcular_irrf(salario_base, dependentes)
        desconto_vt = calcular_vale_transporte(salario_base, opta_vt)
        desconto_vr = calcular_vale_refeicao(valor_vr)
        desconto_saude = calcular_plano_saude(dependentes)

        total_descontos = desconto_inss + desconto_irrf + desconto_vt + desconto_vr + desconto_saude
        salario_liquido = salario_base - total_descontos

        print("\n--- Demonstrativo de Pagamento ---")
        print(f"Matrícula: {matricula}")
        print(f"Salário Base: R$ {salario_base:.2f}")
        print(f"Desconto INSS: R$ {desconto_inss:.2f}")
        print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
        print(f"Desconto Vale Transporte: R$ {desconto_vt:.2f}")
        print(f"Desconto Vale Refeição: R$ {desconto_vr:.2f}")
        print(f"Desconto Plano de Saúde: R$ {desconto_saude:.2f}")
        print(f"Total de Descontos: R$ {total_descontos:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de inserir os valores numéricos corretamente.")

folha_pagamento()