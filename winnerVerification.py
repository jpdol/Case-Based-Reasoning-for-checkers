#Matriz de posicoes
pos = [[0, 1, 2, 3, 4, 5, 6, 7],
	  [ 8, 9,10,11,12,13,14,15],
	  [16,17,18,19,20,21,22,23],
	  [24,25,26,27,28,29,30,31],
	  [32,33,34,35,36,37,38,39],
	  [40,41,42,43,44,45,46,47],
	  [48,49,50,51,52,53,54,55],
	  [56,57,58,59,60,61,62,63]]

def getLine(space):
	if (space > 63) or (space<0):
		return -1
	for i in range(len(pos)):
		for j in range(len(pos[0])):
			if pos[i][j]==space:
				return i

#Retorna valor booleano que representa se há algum movimento válido para as peças cor 'color'
def canMove(board, color):
	move = False

	i = 0
	aux = 0
	while (not move):

		if ((color=='b') and ((board[i]=='bp') or (board[i]=='bd'))):
			if ((getLine(i)-1==(getLine(i-7))) and (getLine(i-7)!= -1) and board[i-7]=='no'):
				move = True
			elif ((board[i]=='bd' and  getLine(i)-1==(getLine(i-7))) and (getLine(i-7)!= -1) and board[i-7]=='no'):
				move = True
			elif ((getLine(i)-1==(getLine(i-9))) and (getLine(i-9)!= -1) and board[i-9]=='no'):
				move = True
			elif ((board[i]=='bd' and  getLine(i)-1==(getLine(i-9))) and (getLine(i-9)!= -1) and board[i-9]=='no'):
				move = True
			elif ((getLine(i)-1==(getLine(i-7))) and (getLine(i-7)!= -1) and board[i-7]!='no'):
				aux = i-7
				if ((board[aux]=='wp' or board[aux]=='wd') and (getLine(aux)-1 == (getLine(aux-7))) and (getLine(aux-7)!= -1) and board[aux-7]=='no'):
					move = True
				elif (((board[i]=='bd') and (board[aux]=='bp' or board[aux]=='bd') and  getLine(aux)-1==(getLine(aux-7))) and (getLine(aux-7)!= -1) and board[aux-7]=='no'):
					move = True
			elif ((getLine(i)-1==(getLine(i-9))) and (getLine(i-9)!= -1) and board[i-9]!='no'):
				aux = i-9
				if ((board[aux]=='wp' or board[aux]=='wd') and (getLine(aux)-1==(getLine(aux-9))) and (getLine(aux-9)!= -1) and board[aux-9]=='no'):
					move = True
				elif (((board[i]=='bd') and (board[aux]=='bp' or board[aux]=='bd') and  getLine(aux)-1==(getLine(aux-9))) and (getLine(aux-9)!= -1) and board[aux-9]=='no'):
					move = True
		elif ((color=='w') and ((board[i]=='wp') or (board[i]=='wd'))):
			if ((getLine(i)+1==(getLine(i+7))) and (getLine(i+7)!= -1) and board[i+7]=='no'):
				move = True
			elif ((board[i]=='wd' and  getLine(i)-1==(getLine(i-7))) and (getLine(i-7)!= -1) and board[i-7]=='no'):
				move = True
			elif ((getLine(i)+1==(getLine(i+9))) and (getLine(i+9)!= -1) and board[i+9]=='no'):
				move = True
			elif ((board[i]=='wd' and  getLine(i)-1==(getLine(i-9))) and (getLine(i-9)!= -1) and board[i-9]=='no'):
				move = True
			elif ((getLine(i)+1==(getLine(i+7))) and (getLine(i+7)!= -1) and board[i+7]!='no'):
				aux = i+7
				if (((board[aux]=='bp' or board[aux]=='bd') and  getLine(aux)+1==(getLine(aux+7))) and (getLine(aux+7)!= -1) and board[aux+7]=='no'):
					move = True
				elif (((board[i]=='wd') and (board[aux]=='bp' or board[aux]=='bd') and  getLine(aux)-1==(getLine(aux-7))) and (getLine(aux-7)!= -1) and board[aux-7]=='no'):
					move = True
			elif ((getLine(i)+1==(getLine(i+9))) and (getLine(i+9)!= -1) and board[i+9]!='no'):
				aux = i+9
				if ((board[aux]=='bp' or board[aux]=='bd') and (getLine(aux)+1==(getLine(aux+9))) and (getLine(aux+9)!= -1) and board[aux+9]=='no'):
					move = True
				elif (((board[i]=='wd') and (board[aux]=='bp' or board[aux]=='bd') and  getLine(aux)-1==(getLine(aux-9))) and (getLine(aux-9)!= -1) and board[aux-9]=='no'):
					move = True

		i+=1
	
	return move


#Retorna a cor do das peças do vencedor, caso haja.
#Retorna mensagem de empate, caso haja
#Caso contrário, o jogo continua
def winnerVerification(board, next_to_move):
	if (('bp' not in board) and ('bd' not in board)):
		return 'white'
	elif (('wp' not in board) and ('wd' not in board)):
		return 'black'
	elif ((not canMove(board, color='b')) and (not canMove(board, color='w'))):
		return 'match tied'
	elif (not canMove(board, color='b') and (next_move=='b')):
		return 'white'
	elif (not canMove(board, color='w') and (next_move=='w')):
		return 'black'
	else:
		return 'no winner yet'



# x = ['no',None,'wp',None,'wp',None,'wp',None,None,'no',None,'no',None,'no',None,'no','wp',None,'bp',None,'no',None,'no',None,None,'no',None,'no',None,'bp',None,'no','no',None,'no',None,'no',None,'no',None,None,'no',None,'wd',None,'bp',None,'bp','no',None,'no',None,'no',None,'bp',None,None,'no',None,'no',None,'no',None,'bp']


# print(winnerVerification(x,'w'))




