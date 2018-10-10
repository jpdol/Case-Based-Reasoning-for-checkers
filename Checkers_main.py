from Checkers_CBR import *

def gameFinish(result,boards_list):
  if result == 'white':
    print("Winner: white")
    cbr.avaliation(boards_list,'win')
    continue_game = False
  elif result == 'black':
    print("Winner: black")
    cbr.avaliation(boards_list,'lose')
    continue_game = False
  elif result == "match tied":
    print("Match Tied")
    cbr.avaliation(boards_list,'empate')
    continue_game = False
  else:
    continue_game = True
  return continue_game


if __name__ == "__main__":
    dataset = pd.read_csv(r"CaseBase/caseBase.csv")
    out = pd.DataFrame(dataset.loc[:,'next_move'])
    cbr = CBR(dataset, out)  
    
    continue_game = True
    boards_list = []
    while(continue_game):
      print("Por favor entre com o estado atual do tabuleiro: ")
      current_board = str(input())
      current_board = current_board.replace("'",'')
      current_board = current_board.split(",")
      
      result = winnerVerification(current_board, 'b')
      if result!='no winner yet':
        break

      i = 0
      while(i<len(current_board)):
        if current_board[i] == "None":
          current_board[i] = None
        i+=1
      next_move = cbr.receiveAndAdapt(current_board)
      if type(next_move) == list:
        result = ''
        for char in next_move:
          result = result + chr(char[1]+97) + str(char[0] + 1) + r'-'
        result = result[:len(result)-1]
        print("Movimento recomendado: ", result)
      else:
        print("Movimento recomendado: ", next_move)
      temp = current_board
      if 'x' in next_move:
        temp.append(1)
      else:
        temp.append(0)

      temp.append(next_move)
      boards_list.append(temp)

      result = winnerVerification(current_board, 'w')

      continue_game = gameFinish(result, boards_list)

    continue_game = gameFinish(result, boards_list)

