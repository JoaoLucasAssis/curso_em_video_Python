s=float(input('Qual o salário do funcionário?'))
if s>1250.00:
    print('Houve um aumento de \033[36m10%\033[m. Seu novo salário é \033[33mR${:.2f}\033[m.'.format(s*1.1))
else:
    print('Houve um aumento de \033[36m15%\033[m. Seu novo salário é \033[33mR${:.2f}\033[m.'.format(s*1.15))