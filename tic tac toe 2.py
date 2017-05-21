#goal: tic tac toe game
#make a blank board
#show blank board
#let players alternate turns placing numbers
#end game and congradulate winner if someone wins




def main():
    intro()
    Board = [['_','_','_'],['_','_','_'],[' ',' ',' ']]
    show(Board)
    turn(Board)


def intro():
    print("This is tic tac toe")
    print("If you don't already know how to play...")
    print("you must have had a very sheltered childhood.")


def turn(Board):
    go = 0
    while go<=8:
        player = (go%2) +1
        print("You will now get to take a turn, player " + str(player))
        print("What row and column would you like to go in?")
        row = int(input("Row: "))
        col = int(input("Column: "))
        row = row-1
        col = col-1
        while row>2 or row<0 or col>2 or col<0:
            print('That is not a valid space!')
            print('Please pick somewhere else to play')
            row = int(input("Row: "))
            col = int(input("Column: "))
            row = row-1
            col = col-1
        while Board[row][col]=='X' or Board[row][col]=='O':
            print('Someone has already played there!')
            print('Please pick somewhere else to play')
            row = int(input("Row: "))
            col = int(input("Column: "))
            row = row-1
            col = col-1
        if go%2 == 0:
            Board[row][col] = 'X'
        else:
            Board[row][col] = 'O'
        show(Board)
        wow = win(Board)
        if wow == 2:
            go = 100
            print("Congrats, player " + str(player) + "!")
        go = go +1
        if go == 9 and wow == 0:
            print("There was a tie!")
        

def win(Board):
    wow = 0
    for x in range(0,3):
        if Board[x][0] == Board[x][1]== Board[x][2] and Board[x][1] != '_' and Board[x][1] != ' ':
            print("You won on a row!")
            wow = 2
    for x in range(0,3):
        if Board[0][x] == Board[1][x] == Board[2][x] and Board[1][x] != '_' and Board[1][x] != ' ':
            print("You won on a column!")
            wow = 2
    if Board[0][0]==Board[1][1]==Board[2][2] or Board[0][2]==Board[1][1]==Board[2][0]:
        print("you won on a diagonal!")
        wow = 2
    return wow




def show(Board):
    print(Board[0][0] + "|" + Board[0][1] + "|" +  Board[0][2]) 
    print(Board[1][0] + "|" + Board[1][1] + "|" +  Board[1][2])
    print(Board[2][0] + "|" + Board[2][1] + "|" +  Board[2][2])
