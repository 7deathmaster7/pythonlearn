import argparse
import sys

def func_leitura(dir):
#	file= open(dir,'r')
#	for linha in file:
		#linha = linha.rstrip()
		#print(linha)
	#file.close()

def func_escrita(dir):
	stdout = sys.stdout
	sys.stdout = open(dir,'w')
	for linha in linha:
		
	file.close()

#def func_report(dir):
#	file.close()





def main(dir,metodo):
	print('************************************manipulação de arquivos ************************************',
	      '\n\n\n')
	if metodo == 1:
		print('************************************leitura de arquivos ****************************************')	
#		file = func_leitura(dir)

	elif metodo == 2:
		file= open(dir,'w')
		func_escrita(dir)

	elif metodo == 3:
		func_report(dir)	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("dir",type=str ,help = "local do arquivo")
	parser.add_argument("metodo",type= int,help = "método")
	args = parser.parse_args()
	main(args.dir,args.metodo)