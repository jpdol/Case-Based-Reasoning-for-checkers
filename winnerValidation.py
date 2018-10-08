#Matriz de posicoes
posicoes = [[ 0, 1, 2, 3, 4, 5, 6, 7],
		    [ 8, 9,10,11,12,13,14,15],
		    [16,17,18,19,20,21,22,23],
		    [24,25,26,27,28,29,30,31],
		    [32,33,34,35,36,37,38,39],
		    [40,41,42,43,44,45,46,47],
		    [48,49,50,51,52,53,54,55],
		    [56,57,58,59,60,61,62,63]]

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
	aux = 0
	while (not movimento):

		if ((color=='b') and ((tabuleiro[i]=='bp') or (tabuleiro[i]=='bd'))):
			if ((retornaLinha(i)-1==(retornaLinha(i-7))) and (retornaLinha(i-7)!= -1) and tabuleiro[i-7]=='no'):
				movimento = True

			elif ((retornaLinha(i)-1==(retornaLinha(i-9))) and (retornaLinha(i-9)!= -1) and tabuleiro[i-9]=='no'):
				movimento = True

			elif ((retornaLinha(i)-1==(retornaLinha(i-7))) and (retornaLinha(i-7)!= -1) and tabuleiro[i-7]!='no'):
				aux = i-7
				if ((tabuleiro[aux]=='wp' or tabuleiro[aux]=='wd') and (retornaLinha(aux)-1 == (retornaLinha(aux-7))) and (retornaLinha(aux-7)!= -1) and tabuleiro[aux-7]=='no'):
					movimento = True

			elif ((retornaLinha(i)-1==(retornaLinha(i-9))) and (retornaLinha(i-9)!= -1) and tabuleiro[i-9]!='no'):
				aux = i-9
				if ((tabuleiro[aux]=='wp' or tabuleiro[aux]=='wd') and (retornaLinha(aux)-1==(retornaLinha(aux-9))) and (retornaLinha(aux-9)!= -1) and tabuleiro[aux-9]=='no'):
					movimento = True

		elif ((color=='w') and ((tabuleiro[i]=='wp') or (tabuleiro[i]=='wd'))):
			if ((retornaLinha(i)+1==(retornaLinha(i+7))) and (retornaLinha(i+7)!= -1) and tabuleiro[i+7]=='no'):
				movimento = True
			
			elif ((retornaLinha(i)+1==(retornaLinha(i+9))) and (retornaLinha(i+9)!= -1) and tabuleiro[i+9]=='no'):
				movimento = True
			
			elif ((retornaLinha(i)+1==(retornaLinha(i+7))) and (retornaLinha(i+7)!= -1) and tabuleiro[i+7]!='no'):
				aux = i+7
				if (((tabuleiro[aux]=='bp' or tabuleiro[aux]=='bd') and  retornaLinha(aux)+1==(retornaLinha(aux+7))) and (retornaLinha(aux+7)!= -1) and tabuleiro[aux+7]=='no'):
					movimento = True
			
			elif ((retornaLinha(i)+1==(retornaLinha(i+9))) and (retornaLinha(i+9)!= -1) and tabuleiro[i+9]!='no'):
				aux = i+9
				if ((tabuleiro[aux]=='bp' or tabuleiro[aux]=='bd') and (retornaLinha(aux)+1==(retornaLinha(aux+9))) and (retornaLinha(aux+9)!= -1) and tabuleiro[aux+9]=='no'):
					movimento = True
		
		i+=1
	
	return movimento


#Retorna a cor do das peças do vencedor, caso haja.
#Retorna mensagem de empate, caso haja
#Caso contrário, o jogo continua
def winnerValidation(tabuleiro, next_to_move):
	if (('bp' not in tabuleiro) and ('bd' not in tabuleiro)):
		return 'white'
	elif (('wp' not in tabuleiro) and ('wd' not in tabuleiro)):
		return 'black'
	elif ((not canMove(tabuleiro, color='b')) and (not canMove(tabuleiro, color='w'))):
		return 'match tied'
	elif (not canMove(tabuleiro, color='b') and (next_move=='b')):
		return 'white'
	elif (not canMove(tabuleiro, color='w') and (next_move=='w')):
		return 'black'
	else:
		return 'no winner yet'

