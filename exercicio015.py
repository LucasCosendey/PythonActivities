dias = int(input('Por quantos dias o carro foi alugado?'))
distan = float(input('Quantos Km rodados?'))
valor = (dias * 60) + (distan * 0.15)
print('O valor do aluguel é R${:.2f}'.format(valor))