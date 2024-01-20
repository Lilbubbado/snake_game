from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.file = open('data.txt')
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.new_board = Turtle()
        self.board()

    def board(self):
        self.new_board.clear()
        self.new_board.hideturtle()
        self.new_board.goto(0, 270)
        self.new_board.color('white')
        self.new_board.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.new_board.clear()
        self.score += 1
        self.board()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highscore}')

        self.score = 0
        self.board()
