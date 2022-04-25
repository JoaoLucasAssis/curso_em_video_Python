nmr=int(input('Digite um número entre 0 e 9999:'))
u= nmr // 1 % 10
d=nmr //10 % 10
c=nmr//100%10
m=nmr//1000%10
print('unidade: \033[33m{}\033[m'.format(u))
print('decena: \033[33m{}\033[m'.format(d))
print('centena: \033[33m{}\033[m'.format(c))
print('milhar: \033[33m{}\033[m'.format(m))