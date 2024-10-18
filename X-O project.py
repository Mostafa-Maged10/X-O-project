#1- tun the app
#2- main menu
#game start, quit the game
#4- player 1 name,symbol,player2 name,symbol
#5*board is displayed
#6-game loops until win or draw
#7-restart game ,quit game

import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self):
       self.name = "" 
       self.symbol = ""
    def choose_name(self):
        while True:
            name = input("choose your name (letters only) : ")
            if name.isalpha():
                self.name = name
                break
            print("invalid name pleas choose letters only")
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("invlaid option please select a single letter")
class Menu:
    choice = ""
    def display_main_menu(self):
        print("welcome to my X-O game")
        print("1-start game")
        print("2-quit game")
        choice = self.validate_choice()
        return choice
        # while input != 1hoic and input != 2:
        #     print("invalid input ( choose 1 or 2)")
        # if input == 1:
        #     return choise
        #     quit()
        # if input == 2:   
        #     return choise
        #     quit()
    def display_end_game_menu(self):
        menu_text = """
        game over
        1- Restart game
        2- Quit game
        Enter your choise (1 or 2) : """
        self.choice = input(menu_text)
    
    def validate_choice(self):
        choice = input()
        while(choice != "1" and choice != "2"):
            choice = input("invalid input choose 1 or 2")
        return choice

    
class Board:
    def __init__(self):
        self.board= [str(i) for i in range(1,10)]
        # for i in range(1,10):
        #     self.board.append(str(i))
    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.baord = symbol
            return True
        return False
    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()
    def reset_board(self):
        self.board= [str(i) for i in range(1,10)]
        
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
            clear_screen()
        else:
            self.quit_game()
    
    def setup_players(self):
        for number ,player in enumerate(self.player, start= 1 ):
            print(f"player {number} enter your details: ")
            player.choose_name(self)
            player.choose_symbol(self)
            clear_screen()
            
    def play_game(self):
        while True:
            self.play_turn
            if self.check_win() or self.check_draw():
                choice = self.menu.display_end_game_menu
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
    def check_win(self):
        win_condition = [
            [0,1,2], [3,4,5], [6,7,8], #row
            [0,3,6], [1,4,7], [2,5,8], #colum
            [0,4,8], [2,4,6],          #diagonal
        ]
        for combo in win_condition :
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False
    def check_draw(self):
       return all(not cell.isdigit() for cell in self.board.board)
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choose a cell(1-9): "))
                if 1<= cell_choice <=9 and self.board.updtae_board(cell_choice, player.symbol):
                    break        
                else:
                 print("invalid move please try again")
            except ValueError:
                print("please enter a number between 1-9")
        self.switch_player()
    def switch_player(self):
        self.current_player_index = 1-self.current_player_index
    def quit_game(self):
        print("thank you for playing!")

game = Game()
game.start_game()





