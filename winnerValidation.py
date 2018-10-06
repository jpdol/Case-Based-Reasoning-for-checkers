

def winnerValidation(tabuleiro):

	if (('bp' not in tabuleiro) and ('bd' not in tabuleiro)):
		return 'white'
	elif (('wp' not in tabuleiro) and ('wd' not in tabuleiro)):
		return 'black'

	else:
		return 'not yet'



print(winnerValidation('no,tp,no,tp,no,tp,no,tp,tp,no,tp,no,tp,no,tp,wd,wp,tp,no,tp,wp,tp,no,tp,tp,no,tp,no,tp,no,tp,bp,no,tp,no,tp,no,tp,no,tp,tp,no,tp,no,tp,no,tp,bp,no,tp,no,tp,no,tp,bp,tp,tp,no,tp,no,tp,no,tp,bp'))