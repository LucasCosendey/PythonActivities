produto = float(input('Qual o preço do produto? R$'))
desconto = produto * 0.05
precofinal = produto - desconto
print('O produto que custava {} na promoção com desconto de 5% vai custar R${:.2f}.'.format(produto, precofinal))
