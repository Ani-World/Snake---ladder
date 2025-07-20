from tkinter import *
import math, random

class Board(Frame):
    ladders = {
        50: 91,
        8: 26,
        19: 38,
        28: 53,
        36: 57,
        21: 82,
        61: 99,
        54: 88,
        43: 77,
        66: 87
    }
    snakes = {
        68: 2,
        46: 15,
        48: 9,
        69: 49,
        98: 13,
        64: 24,
        83: 22,
        59: 19
    }

    # Inheriting from Frame
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = Canvas(self, width=602, height=602, bg="#F5DEB3", highlightthickness=0)
        self.canvas.pack(pady=30)
        self.cell_size = 60
        self.cell_map = {}
        self.create_board()

    def create_board(self):
        num = 100
        for i in range(10):
            y = i * self.cell_size
            cols = range(10) if i % 2 == 0 else range(9, -1, -1)
            for j in cols:
                x = j * self.cell_size
                color = "white" if (i + j) % 2 == 0 else "#bab86c"
                self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill=color, outline="black")
                self.canvas.create_text(x + 30, y + 30, text=str(num), font=('Helvetica', 12, 'bold'))
                self.cell_map[num] = (x + 30, y + 30)
                num -= 1

    def get_canvas(self):
        return self.canvas

    def draw_ladder(self,start, end):
        x1, y1 = self.cell_map[start]
        x2, y2 = self.cell_map[end]
        offset = 15
        dx, dy = x2 - x1, y2 - y1
        length = (dx ** 2 + dy ** 2) ** 0.5
        ux, uy = dx / length, dy / length
        px, py = -uy, ux  # perpendicular unit vector

        for sign in [1, -1]:
            self.canvas.create_line(
                x1 + px * offset * sign, y1 + py * offset * sign,
                x2 + px * offset * sign, y2 + py * offset * sign,
                fill="green", width=4
            )

        steps = int(length // 20)
        for i in range(1, steps):
            t = i / steps
            rung_x = x1 + dx * t
            rung_y = y1 + dy * t
            self.canvas.create_line(
                rung_x - px * offset, rung_y - py * offset,
                rung_x + px * offset, rung_y + py * offset,
                fill="green", width=2
            )

    def draw_snake(self, start, end):
        colors = [
            "#d62828", "#3a86ff", "#ff006e", "#8338ec",
            "#06d6a0", "#f77f00", "#2ec4b6", "#ffbe0b"
        ]

        x1, y1 = self.cell_map[start]
        x2, y2 = self.cell_map[end]
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        angle = math.atan2(y2 - y1, x2 - x1)

        x_factor = 0.1
        y_variants = 20
        points = []

        for x in range(int(dist)):
            y = math.sin(x * x_factor) * y_variants
            x_rot = x * math.cos(angle) - y * math.sin(angle)
            y_rot = x * math.sin(angle) + y * math.cos(angle)
            points.extend([x_rot + x1, y_rot + y1])

        self.canvas.create_line(points, smooth=True, fill=random.choice(colors), width=7)
        self.canvas.create_line(points, smooth=True, fill="white", width=5, dash=(4, 2))


def create_player(self, color, position):
        x, y = self.cell_map[position]
        return self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=color, tags=color)


