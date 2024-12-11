#Patrick Leimer Lab06
def initialize_board(num_rows, num_cols):
    newLis = []
    for i in range(0, num_rows):
        newLis.append([])
        for j in range(0, num_cols):
            newLis[i].extend(["-"])
    return newLis

def print_board(board):
    for i in range(0, len(board)):
        print(*board[i])

def insert_chip(board, col, chip_type):
    for index in range(len(board)-1, -1, -1):
        if board[index][col] == '-':
            board[index][col] = chip_type
            break
    return board, index

def check_if_winner(board, col, row, chip_type):
    lenRow, lenCol = len(board), len(board[0])
    winVertical = 4 <= sum(1 for i in range(lenRow) if board[i][col] == chip_type)
    winHorizontal = 4 <= sum(1 for i in range(lenCol) if board[row][i] == chip_type)
    if winVertical == True: return winVertical
    if winHorizontal == True: return winHorizontal
    return False
def main():
    player = 1
    rows = int(input("What would you like the height of the board to be? "))
    columns = int(input("What would you like the length of the board to be? "))
    gamboard = initialize_board(rows, columns)
    print_board(gamboard)
    print("\nPlayer 1: x\nPlayer 2: o\n")

    while True:
        choseCol = int(input(f"Player {player}: Which column would you like to choose?"))
        chip_type = 'x' if player == 1 else 'o'
        gamboard, choseRow = insert_chip(gamboard, choseCol, chip_type)  # Fix here
        print_board(gamboard)
        print()
        if check_if_winner(gamboard, choseCol, choseRow, chip_type):
            print(f"Player {player} won the game!")
            break
        elif '-' not in [cell for row in gamboard for cell in row]:
            print("Draw. Nobody wins.")
            break
        player = 2 if player == 1 else 1

if __name__ == '__main__':
    main()

