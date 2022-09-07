salario = float(input('qual é o salário do funcionario? R$'))
novo = salario + (salario * 25 / 100)
print('um funcionario que ganhava R${:.2f}, com 25% de aumento,passa a recebe R%{:.2F}'.format(salario, novo))

