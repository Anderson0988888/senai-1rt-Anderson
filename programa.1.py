def numeros(n1,n2):
    num = n1, n2
    somar = n1 + n2
    multiplicar = n1 * n2
    Mn = max(num)
    mn = min(num)
    a = input('Insira uma operação: somar, multiplicar, valor maximo, valor minimo: ')
    if a == 'somar':
        return somar
    if a == 'multiplicar':
        return multiplicar
    if a == 'valor maximo':
        return Mn
    if a == 'valor minimo':
        return mn

a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))

print('=', numeros(a,b))
