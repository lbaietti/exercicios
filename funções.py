def imprimir_dados(nome, idade):
    print("nome: {} idade: {}".format(nome, idade))

imprimir_dados('Lucas', 19)


def somar_numeros(n1, n2):
    soma = n1 + n2
    return soma

resultado = somar_numeros(10, 20)
print(resultado)


def inss(salario, inss):
    sal = salario*inss/100
    return sal
n = inss(1000,9)
print(n)


def vt(salario, vt):
    sal = salario*vt/100
    return sal
n = vt(1000, 3)
print(n)


def calcular_preco():
