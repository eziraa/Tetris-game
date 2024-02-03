
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-100, 270)
        self.speed("fastest")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.score_update_level = 0

    def set_up(self):
        while True:
            text = self.screen.textinput("Choose the level of the game",
                                            "1. level 1 \n2. level 2 \n3. level 3 \n4. level 4 \n5. level 5 \n6. level 6 \n7. level 7")
            if text is None:
                exit()
            elif text.isdigit() and 0 < int(text) <= 7:
                self.fast_level = 0.7 if text == '1' else 0.6 if text == '2' else 0.5 if text == '3' else 0.4 if text == '4' else 0.3 if text == '5' else 0.2 if text == '6' else 0.1
                self.score_update_level = 4 if text == '1' else 5 if text == '2' else 6 if text == '3' else 7 if text == '4' else 8 if text == '5' else 9 if text == '6' else 10
                break
            
    def update_score(self):
        self.score += self.score_update_level
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
