import random

class TicTacToe:

    def __init__(self):
        self.board = []

    #create board
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('_')
            self.board.append(row)

    #get_first_player
    def get_first_player(self):
        return random.randint(0,1)

    def board_spot(self, row, col, player):
        self.board[row][col] = player

    #choose a winner
    def winning_player(self, player):
        win = None

        n = len(self.board)

        #check rows
        for a in range(n):
            win = True
            
            for b in range(n):
                if self.board[a][b] !=player:
                    win = False
                    break
            if win:
                return win

        #check columns
        for a in range(n):
            win = True
            for b in range(n):
                if self.board[b][a] !=player:
                    win = False
                    break
            if win:
                return win

        #check diagnols
        win = True
        for a in range(n):
            if self.board[a][a] !=player:
                win = False
                break
        if win: 
            return win

        win = True
        for a in range(n):
            if self.board[a][n - 1 - a] != player:
                win = False
                break
        if win:
            return win
        return False
        
        for row in self.board:
            for dash in row:
                if dash == '_':
                    return False
        return True


    def is_board_filled(self):
        for row in self.board:
            for dash in row:
                if dash == '__':
                    return False
        return True

    def switch_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def display_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.display_board()
            #TODO: Make throw an exception when the user puts in an invalid input
            #have options to end the game or play again
            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").strip().split()))
            print()

            # fixing the spot
            self.board_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.winning_player(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.switch_player_turn(player)

        # showing the final view of board
        print()
        self.display_board()
        exit()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()                           

           




