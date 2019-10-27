import pprint

def printKeisen():
    print("-+-+-")

def printBoadr(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    printKeisen()
    print(board['middle-L'] + '|' + board['middle-M'] + '|' + board['middle-R'])
    printKeisen()
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def initTurn(board):
    printBoadr(board)
    print(turn + "の番です")

def isWins(board, turn):
    if ((board['top-L'] == turn and  board['top-M']  == turn and board['top-R']  == turn)  
     or (board['middle-L'] == turn and  board['middle-M']  == turn and board['middle-R']  == turn)
     or (board['low-L'] == turn and  board['low-M']  == turn and board['low-R']  == turn)
     or (board['top-L'] == turn and  board['middle-L']  == turn and board['low-L']  == turn)
     or (board['top-M'] == turn and  board['middle-M']  == turn and board['low-M']  == turn)
     or (board['top-R'] == turn and  board['middle-R']  == turn and board['low-R']  == turn)
     or (board['top-L'] == turn and  board['middle-M']  == turn and board['low-R']  == turn)
     or (board['top-R'] == turn and  board['middle-M']  == turn and board['low-L']  == turn)
    ):
        return True
    else:
        return False

board = {
            'top-L'    : ' ', 'top-M'    : ' ' , 'top-R'    : ' ',
            'middle-L' : ' ', 'middle-M' : ' ' , 'middle-R' : ' ',
            'low-L'    : ' ', 'low-M'    : ' ' , 'low-R'    : ' ',
        }
turn = "X"
for i in range(9):
    initTurn(board)
    pos = input()
    while pos not in board or board[pos] != " ":
        print("失敗しました. やり直してください.")
        pos = input()
    board[pos] = turn
    if isWins(board, turn):
        printBoadr(board)
        print(turn + " が勝ちました！ゲームを終了します.")
        break
    if turn == "X":
        turn ="O"
    else:
        turn ="X"
