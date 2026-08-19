class Board:
    def __init__(self):
        self.board = [" "] * 9

    def display(self):
        print()
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---|---|---")
        print()

    def make_move(self, position, symbol):
        if 0 <= position <= 8 and self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False

    def check_winner(self, symbol):
        winning_patterns = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_patterns:
            if (self.board[a] == symbol and
                self.board[b] == symbol and
                self.board[c] == symbol):
                return True

        return False

    def is_full(self):
        return " " not in self.board


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player("Player 1", "X"),
            Player("Player 2", "O")
        ]

    def play(self):
        current_player = 0

        while True:
            self.board.display()

            player = self.players[current_player]

            try:
                position = int(
                    input(f"{player.name} ({player.symbol}), choose position 1-9: ")
                ) - 1
            except ValueError:
                print("Please enter a number.")
                continue

            if not self.board.make_move(position, player.symbol):
                print("Invalid move! Try again.")
                continue

            if self.board.check_winner(player.symbol):
                self.board.display()
                print(f"🎉 {player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            current_player = 1 - current_player


# Start the game
game = Game()
game.play()
