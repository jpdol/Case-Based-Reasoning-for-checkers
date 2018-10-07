#Dicionário de posições entre Tabuleiro x Representação Computacional
casas = {'a1':0,'b1':1,'c1':2,'d1':3,'e1':4,'f1':5,'g1':6,'h1':7,'a2':8,'b2':9,'c2':10,'d2':11,'e2':12,'f2':13,'g2':14,'h2':15,'a3':16,'b3':17,'c3':18,'d3':19,'e3':20,'f3':21,'g3':22,'h3':23,'a4':24,'b4':25,'c4':26,'d4':27,'e4':28,'f4':29,'g4':30,'h4':31,'a5':32,'b5':33,'c5':34,'d5':35,'e5':36,'f5':37,'g5':38,'h5':39,'a6':40,'b6':41,'c6':42,'d6':43,'e6':44,'f6':45,'g6':46,'h6':47,'a7':48,'b7':49,'c7':50,'d7':51,'e7':52,'f7':53,'g7':54,'h7':55,'a8':56,'b8':57,'c8':58,'d8':59,'e8':60,'f8':61,'g8':62,'h8':63}

#Matriz de posicoes
posicoes = [[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15],[16,17,18,19,20,21,22,23],[24,25,26,27,28,29,30,31],[32,33,34,35,36,37,38,39],[40,41,42,43,44,45,46,47],[48,49,50,51,52,53,54,55],[56,57,58,59,60,61,62,63]]
def retornaLinha(casa):
	if (casa > 63) or (casa<0):
		return -1
	for i in range(len(posicoes)):
		for j in range(len(posicoes[0])):
			if posicoes[i][j]==casa:
				return i


#Retorna valor booleano que representa se há algum movimento válido para as peças cor 'color'
def canMove(tabuleiro, color):
	movimento = False

	i = 0
	while (not movimento):
		if ((color=='b') and (tabuleiro[i]=='bp')):
			
		elif ((color=='b') and (tabuleiro[i]=='bd')):
			pass
		elif ((color=='w') and (tabuleiro[i]=='wp')):
			pass
		elif ((color=='w') and (tabuleiro[i]=='wd')):
			pass
		i+=1
	
	return movimento



#Retorna a cor do das peças do vencedor, caso haja.
#Retorna mensagem de empate, caso haja
#Caso contrário, o jogo continua
def winnerValidation(tabuleiro, next_move):
	if (('bp' not in tabuleiro) and ('bd' not in tabuleiro)):
		return 'white'
	elif (('wp' not in tabuleiro) and ('wd' not in tabuleiro)):
		return 'black'
	elif (not canMove(tabuleiro, color='b') and (next_move=='b')):
		return 'white'
	elif (not canMove(tabuleiro, color='w') and (next_move=='w')):
		return 'black'
	elif ((not canMove(tabuleiro, color='b')) and (not canMove(tabuleiro, color='w'))):
		return 'match tied'
	else:
		return 'no winner yet'


# tabuleiro_teste = 'no,tp,no,tp,no,tp,no,tp,tp,no,tp,no,tp,no,tp,wd,wp,tp,no,tp,wp,tp,no,tp,tp,no,tp,no,tp,no,tp,bp,no,tp,no,tp,no,tp,no,tp,tp,no,tp,no,tp,no,tp,bp,no,tp,no,tp,no,tp,bp,tp,tp,no,tp,no,tp,no,tp,bp'.split(',')

# print(winnerValidation(tabuleiro_teste,'b'))

