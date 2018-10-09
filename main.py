from winnerVerification import *
from seilaoqvaiser import *

if __name__ == "__main__":
    dataset = pd.read_csv(r"CaseBase/caseBase.csv")
    #(h, v) = verifyDirs(dataset.loc[1,'next_move'])
    out = pd.DataFrame(dataset.loc[:,'next_move'])
    dataset = dataset.drop("next_move", axis = 1)
    cbr = CBR(dataset, out)  
    #m = cbr.adapt(['wp',None,'wp',None,'wp',None,'wp',None,None,'wp',None,'wp',None,'wp',None,'wp','wp',None,'no',None,'wp',None,'wp',None,None,'wp',None,'no',None,'no',None,'no','no',None,'no',None,'bp',None,'no',None,None,'bp',None,'no',None,'bp',None,'bp','bp',None,'bp',None,'bp',None,'bp',None,None,'bp',None,'bp',None,'bp',None,'bp',0,0.75])
    #cbr.adapt(['wp',None,'wp',None,'wp',None,'wp',None,None,'wp',None,'wp',None,'wp',None,'wp','wp',None,'no',None,'wp',None,'wp',None,None,'wp',None,'no',None,'no',None,'no','no',None,'no',None,'bp',None,'no',None,None,'bp',None,'no',None,'bp',None,'bp','bp',None,'bp',None,'bp',None,'bp',None,None,'bp',None,'bp',None,'bp',None,'bp',0,0.75])
    #k = cbr.adapt(['wp',None,'wp',None,'wp',None,'wp',None,None,'wp',None,'wp',None,'wp',None,'wp','wp',None,'no',None,'wp',None,'wp',None,None,'bp',None,'no',None,'no',None,'no','bp',None,'no',None,'no',None,'no',None,None,'no',None,'no',None,'bp',None,'bp','bp',None,'bp',None,'bp',None,'bp',None,None,'bp',None,'bp',None,'bp',None,'bp',1,0.75])
    #l = cbr.adapt(['no',None,'wp',None,'wp',None,'wp',None,None,'no',None,'no',None,'no',None,'no','wp',None,'bp',None,'no',None,'no',None,None,'no',None,'no',None,'bp',None,'no','no',None,'no',None,'no',None,'no',None,None,'no',None,'wd',None,'bp',None,'bp','no',None,'no',None,'no',None,'bp',None,None,'no',None,'no',None,'no',None,'bp',1,0.75])
    # n = cbr.receiveAndAdapt(['no',None,'wp',None,'wp',None,'no',None,None,'wp',None,'wp',None,'no',None,'wp','no',None,'wp',None,'no',None,'wp',None,None,'bp',None,'no',None,'wp',None,'wp','bp',None,'no',None,'bp',None,'no',None,None,'no',None,'bp',None,'bp',None,'bp','bp',None,'no',None,'no',None,'no',None,None,'no',None,'bp',None,'no',None,'bp',0,0.75])

    flag = True
    boards_list = []
    while(flag):
      print("Por favor entre com o estado atual do tabuleiro: ")
      current_board = str(input())
      current_board = current_board.replace("'",'')
      current_board = current_board.split(",")
      i = 0
      while(i<len(current_board)):
        if current_board[i] == "None":
          current_board[i] = None
        i+=1
      next_move = cbr.receiveAndAdapt(current_board)

      print("Movimento recomendado: "+ next_move)

      find_x = next_move.find("x")
      temp = current_board
      if find_x != -1:
        temp.append(1)
      else:
        temp.append(0)

      temp.append(next_move)
      temp.append(0.75)
      boards_list.append(temp)

      result = winnerVerification(current_board, next_move)

      if result == 'white':
        print("Você venceu")
        cbr.avaliation(boards_list,'win')
        flag = False
      elif result == 'black':
        print("Você perdeu")
        cbr.avaliation(boards_list,'lose')
        flag = False
      elif result == "match tied":
        print("Empate")
        cbr.avaliation(boards_list,'empate')
        flag = False
      else:
        pass

