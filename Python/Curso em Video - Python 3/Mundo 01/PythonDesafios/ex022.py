nome = str(input('Digite seu nome completo: '))
print('Seu nome todo maiúsculo fica ->', nome.upper())
print('Seu nome todo minúsculo fica ->', nome.lower())
print('Seu nome tem {} letras!'.format(len(nome.replace(' ', '').strip())))
dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
