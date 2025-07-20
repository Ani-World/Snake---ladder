import time


class Player:
    def __init__(self, board_canvas, cell_map, color, name="Player", board=None):
        self.canvas = board_canvas
        self.cell_map = cell_map
        self.color = color
        self.name = name
        self.board = board  # board contains ladders and snakes
        self.position = 1  # Start at cell 1

        # Draw the player's token
        x, y = self.cell_map[self.position]
        r = 15
        self.token = self.canvas.create_oval(
            x - r, y - r, x + r, y + r,
            outline=self.color, width=7, tags=self.name
        )

    def move(self, steps):
        next_position = self.position + steps

        if next_position > 100:
            print(f"{self.name} rolled {steps}, but can't move beyond 100. Staying at {self.position}")
            return

        steps_remaining = [steps]

        def step_animation():
            if steps_remaining[0] > 0:
                self.position += 1
                x, y = self.cell_map[self.position]
                self.canvas.coords(
                    self.token, x - 15, y - 15, x + 15, y + 15
                )
                steps_remaining[0] -= 1
                self.canvas.after(300, step_animation)  # 300ms delay between steps
            else:
                # Check for ladder or snake after full movement
                if self.position in self.board.ladders:
                    print(f"{self.name} climbed a ladder to {self.board.ladders[self.position]}")
                    self.position = self.board.ladders[self.position]
                elif self.position in self.board.snakes:
                    print(f"{self.name} got bitten by a snake to {self.board.snakes[self.position]}")
                    self.position = self.board.snakes[self.position]

                # Final position update after snake/ladder
                x, y = self.cell_map[self.position]
                self.canvas.coords(
                    self.token, x - 15, y - 15, x + 15, y + 15
                )

        step_animation()
