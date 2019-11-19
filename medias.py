notas= []
i = 0
j = 0
acumulador = 0
while i<4:
    i+=1
    nota_inserida = float(input("Insira a nota " + str(i)+ "do aluno: "))
    notas.append(nota_inserida)

while j<4:
    acumulador += notas[j]
    j+=1

media = acumulador/4
