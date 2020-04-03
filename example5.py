import argparse
import sys


def func_leitura():
	#file= open(dir,'r')
	for linha in sys.stdin:
		print(linha)


#	for linha in file:
		#linha = linha.rstrip()
		#print(linha)
	#file.close()

def func_escrita():
#	stdout = sys.stdout
	for linha in sys.stdin:
		sys.stdout.write(linha.upper())
#	file.close()

def func_conj():

	for linha in sys.stdin:
		b = set()
		a = set()
		a = linha
		c = a.difference(b)
		print(c)
		b.add(linha)



#	file.close()





def main(metodo):
	print('************************************manipulação de arquivos ************************************',
	      '\n\n\n')
	if metodo == 1:
		print('************************************leitura de arquivos ****************************************')	
		func_leitura()

	elif metodo == 2:
		func_escrita()

	elif metodo == 3:
		func_conj()	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	#parser.add_argument("dir",type=str ,help = "local do arquivo")
	parser.add_argument("metodo",type= int,help = "método")
	args = parser.parse_args()
	main(args.metodo)