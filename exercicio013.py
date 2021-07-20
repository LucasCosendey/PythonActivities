salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario*15/100)
print('Se o colaborador recebia {} com o aumento de 15% passa a receber {:.2f}'.format(salario, novo))