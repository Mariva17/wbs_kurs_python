import tkinter as tk
from enum import StrEnum
from typing import Final


BOARD_SIZE: Final[int] = 10


class Color(StrEnum):
    BLACK = "black"
    RED = "red"
    GREY = "grey"


class Cell:
    def __init__(self, state=Color.GREY):
        self.state = state

    def toggle_state(self) -> None:
        self.state = {
            Color.GREY: Color.BLACK,
            Color.BLACK: Color.RED,
            Color.RED: Color.BLACK,
        }.get(self.state, Color.GREY)

    def __str__(self) -> Color:
        return self.state

    def __repr__(self) -> str:
        return f"Cell({self.state!r})"


CellMatrix = list[list[Cell]]


def create_board(size: int) -> CellMatrix:
    """
    Create a n X n matrix with board objects.
    """
    return [[Cell() for _ in range(size)] for _ in range(size)]


class App(tk.Tk):
    def __init__(self, size: int, title: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.board_size = size

        self.title(title)
        self.set_board()
        self.mainloop()

    def set_board(self) -> None:
        """
        Draw n X n Board with labels and grid.
        """
        self.board: CellMatrix = create_board(self.board_size)

        for i, row in enumerate(self.board):
            for j, _ in enumerate(row):
                element = tk.Label(self, text="x", bg=self.board[i][j].state)
                element.grid(row=i, column=j, ipady=5, ipadx=10, sticky="news")
                element.bind(
                    "<Button-1>",
                    lambda event, i=i, j=j: self.on_click(i, j, event),
                )
                self.columnconfigure(i, weight=1)
                self.rowconfigure(i, weight=1)

    def on_click(self, i: int, j: int, event: tk.Event):
        """
        handle a click event. Look up the cell object by row and column,
        toggle the state and update the corresponding widget (label).
        """
        cell = self.board[j][i]
        cell.toggle_state()
        event.widget.config(bg=cell.state)


if __name__ == "__main__":
    app = App(size=BOARD_SIZE, title="the mysterious board game")

    # Toggle Test
    test_board = create_board(size=4)
    cell = test_board[0][0]
    for _ in range(5):
        print(cell.state)
        cell.toggle_state()
