#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class FrogLeapGame:
    def __init__(self):
        self.board = ['G', 'G', 'G', '-', 'B', 'B', 'B']

    def display_board(self):
        indices = [str(i) for i in range(len(self.board))]
        print(f"\n{indices}\n{self.board}")

    def validate_move(self, position):
        if position == 'q':
            return True  # Quit the game
        position = int(position)
        if position < 0 or position >= len(self.board):
            print("Invalid move: Position out of bounds.")
            return False
        if self.board[position] == '-':
            print("Invalid move: Empty leaf selected.")
            return False
        return True

    def make_move(self, position):
        position = int(position)
        frog = self.board[position]
        if frog == 'G':
            if position < len(self.board) - 2 and self.board[position + 2] == '-':
                self.board[position] = '-'
                self.board[position + 2] = 'G'
            elif position < len(self.board) - 1 and self.board[position + 1] == '-':
                self.board[position] = '-'
                self.board[position + 1] = 'G'
            else:
                print("Invalid move: Cannot leap over a frog.")
        elif frog == 'B':
            if position >= 2 and self.board[position - 2] == '-':
                self.board[position] = '-'
                self.board[position - 2] = 'B'
            elif position >= 1 and self.board[position - 1] == '-':
                self.board[position] = '-'
                self.board[position - 1] = 'B'
            else:
                print("Invalid move: Cannot leap over a frog.")

if __name__ == "__main__":
    frog_game = FrogLeapGame()

    while True:
        frog_game.display_board()
        move = input("Enter the position of the frog to move (0-6, q to quit): ")
        
        if not frog_game.validate_move(move):
            continue
        
        if move == 'q':
            print("Quitting the game.")
            break
        
        frog_game.make_move(move)


# In[ ]:




