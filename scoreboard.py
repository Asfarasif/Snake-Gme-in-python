from turtle import Turtle
Font=("Courier", 24, "normal")
Alignment = "center"

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=Alignment, font=Font)

    def Game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=Alignment, font=Font)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    

