

def mult(*args):
    total = 1
    for numero in args:
        total *= numero 
    return total

def par_impar(n):
    if n % 2 == 0:
        return 'Par'
    return 'Ímpar'

multiplicacao = mult(2, 3, 4, 5)

print(2*3*4*5)
print(multiplicacao)

numero1 = par_impar(2)
numero2 = par_impar(3)

print(f'{numero1=}, {numero2=}')

