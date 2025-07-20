from tkinter import *
from tkinter import messagebox
from board import Board
from players import Player
from dice import Die

screen = Tk()
screen.title("Snake and Ladder")
screen.geometry("1000x700")

# Main layout
main_frame = Frame(screen)
main_frame.pack(fill=BOTH, expand=True)

# Left side: board
board_frame = Frame(main_frame)
board_frame.grid(row=0, column=0, padx=20, pady=20)

board = Board(board_frame)
board.grid(row=0, column=0)
cell_map = board.cell_map

# Draw ladders and snakes
for start, end in board.ladders.items():
    board.draw_ladder(start, end)
for head, tail in board.snakes.items():
    board.draw_snake(head, tail)

# Right side: die and buttons
side_panel = Frame(main_frame)
side_panel.grid(row=0, column=1, padx=20, pady=20, sticky=N)

# Globals
players = []
player_buttons = []
current_index = 0
die = None

# Handle turn logic
def handle_roll(result):
    global current_index
    current_player = players[current_index]
    print(f"{current_player.name} rolled {result}")
    current_player.move(result)

    def after_move():
        global current_index

        if current_player.position >= 100:
            winner_label = Label(side_panel, text=f"{current_player.name} Wins!", font=("Arial", 16, "bold"), fg=current_player.color)
            winner_label.pack(pady=20)
            for btn in player_buttons:
                btn.config(state=DISABLED)
            return

        if result == 6:
            update_buttons()  # same player again
        else:
            current_index = (current_index + 1) % len(players)
            update_buttons()

    # Delay to allow animation to finish
    screen.after(result * 300 + 500, after_move)

# Enable/disable correct player's button
def update_buttons():
    for i, btn in enumerate(player_buttons):
        if i == current_index:
            btn.config(state=NORMAL)
        else:
            btn.config(state=DISABLED)

# Start game after choosing number of players
def start_game(num_players):
    global players, die, player_buttons, current_index
    colors = ['red', 'blue', 'green', 'yellow']
    players.clear()
    player_buttons.clear()
    current_index = 0

    for i in range(num_players):
        player = Player(board.canvas, cell_map, colors[i], name=f"Player {i+1}", board=board)
        players.append(player)

    die = Die(side_panel, callback=handle_roll)
    die.frame.pack(pady=10)

    for i, player in enumerate(players):
        btn = Button(side_panel, text=f"{player.name} Roll", command=die.roll_die, padx=10, pady=10)
        btn.pack(pady=5)
        player_buttons.append(btn)

    update_buttons()

def ask_number_of_players():
    popup = Toplevel(screen)
    popup.title("Select Number of Players")
    popup.geometry("300x200")
    popup.transient(screen)
    popup.grab_set()

    Label(popup, text="Choose number of players:", font=("Arial", 12)).pack(pady=10)

    def select(n):
        popup.destroy()
        start_game(n)

    for j in range(1, 5):
        Button(popup, text=str(j), width=10, command=lambda i=j: select(i)).pack(pady=5)

    popup.wait_window()

ask_number_of_players()

screen.mainloop()
