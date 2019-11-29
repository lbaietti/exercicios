class Funcionario:
    def __init__(self, nome, email, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.rg = rg
        self.idade = idade
        self.salario = salario
    def aumentar_salario(self, valor):
        self.salario = valor + self.salario
        return self.salario

    def __str__(self):
        return( f"Olá, {self.nome} Você foi cadastrado com sucesso em nosso sistema" )

funcionario = Funcionario(
    nome = 'José',
    email = 'josé@gmail.com',
    rg = '50612814-3',
    idade = '34',
    salario = 200000,
)

print(funcionario)

recebe = float(input("Digite seu aumento salarial"))
funcionario.aumentar_salario(recebe)

print(funcionario.salario)