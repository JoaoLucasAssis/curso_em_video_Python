frase=str(input('Insira uma frase:')).upper().strip()
a=frase.find('A')+1
b=frase.count('A')
c=frase.rfind('A')+1
print('A letra \033[4;36mA\033[m aparece \033[33m{}\033[m vezes na frase'.format(b))
print('A posição da primeira letra \033[4;36mA\033[m é \033[33m{}\033[m'.format(a))
print('A posição da última letra \033[4;36mA\033[m é \033[33m{}\033[m'.format(c))