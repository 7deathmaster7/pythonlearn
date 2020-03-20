import argparse

def Func (valor):
	if valor == 1 or valor == 0:
		result = valor
		return result
	else:
		result = valor * Func(valor - 1)
		return result

def Funciter(valor):
	result = 1
	for x in range(valor,1,-1):
		result *= x
	return result 

def Funciter2(valor):
	result = 1
	while 1 < valor:
		result *= valor
		valor = valor -1
	return result 

def main(valor,metodo):
	print('************************************Fatorial************************************\n\n Digite 1 para cálculo com fatorial recursivo;\n 2 para cálculo fatorial com for;\n ou 3 para cálculo fatorial com while\n\n\n')
	result = 0

	x = valor
	if metodo == 1:
			
		result = Func(x)
		print('O valor do fatorial é: %d \n\n' % result)
	elif metodo ==2:
		result = Funciter(x)
		print('O valor do fatorial iterativo é: %d \n\n' % result)
	elif metodo ==3:
		result = Funciter2(x)
		print('O valor do fatorial iterativo com while é: %d \n\n' % result)
	else:
		print('O valor de tipo de calculo é inferior a 1 ou superior a 3\n\n' )

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("valor",type=int,help = "entrada de dados para calculo do fatorial")
	parser.add_argument("metodo",type= int,help = "método")
	args = parser.parse_args()
	main(args.valor,args.metodo)