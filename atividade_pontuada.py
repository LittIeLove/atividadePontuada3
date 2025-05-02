import os
os.system ("clear || cls")
from time import sleep


def autenticar_funcionario():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    print("Acesso permitido.")
    sleep (1.5)
    os.system ("clear || cls")
    return True
autenticar_funcionario()

salario_bruto = float(input("Insira seu salário: "))
os.system ("clear || cls")
while True:
        vale_trans = str(input("Digite (S) para utilizar o vale transporte ou (N) para não: ")).lower()
        if vale_trans == "s" or "n":   
            break
        else:
            print("Apenas (s,n)")
            sleep(1)

while True:
        try:
            vale_refeicao = float(input("Digite o valor do vale refeição da empresa: ")) 
            break
        except ValueError:
            print ("Apenas números.")
            sleep (1)
            os.system ("clear || cls")
os.system ("clear || cls")

while True:
    try:
        qtd_dependente = int(input("Digite a quantidade de dependentes: "))
        break
    except ValueError:
        print("Apenas números.")
        sleep(1)
        os.system ("clear || cls")
    

os.system ("clear || cls")

def descontos():
    if vale_trans == "s":
        trans_valor = salario_bruto * 0.06
    else: 
        trans_valor = 0
    valor_dependente = qtd_dependente * 189.59
    valor_refeicao = vale_refeicao * 0.20
    valor_saude = qtd_dependente * 150
    tarifas = trans_valor + valor_refeicao + valor_saude
    return tarifas

tarifasf = descontos()

def inss():
    if salario_bruto < 1518.01:
        desconto_inss = salario_bruto * 0.075
    elif salario_bruto < 2793.89:
        desconto_inss = salario_bruto * 0.09
    elif salario_bruto < 4190.84:
        desconto_inss = salario_bruto * 0.12
    else: 
        desconto_inss = salario_bruto * 0.14
    return desconto_inss

inssd = inss()

def irrf():
    if salario_bruto < 2259.21:
        desconto_irrf = 0
    elif salario_bruto < 2826.66:
        desconto_irrf = salario_bruto * 0.075
    elif salario_bruto < 3751.06:
        desconto_irrf = salario_bruto * 0.15
    elif salario_bruto < 4664.69:
        desconto_irrf = salario_bruto * 0.225
    else:
        desconto_irrf = salario_bruto * 0.275

    valor_final_irrf = desconto_irrf - (qtd_dependente * 189.59)
    return max(valor_final_irrf, 0)

irrff = irrf()

salario_liquido = salario_bruto - (tarifasf + inssd + irrff) 

print(f"Salario bruto: {salario_bruto}\nSalário líquido: {salario_liquido:.2f}")



        
