import turtle

screen = turtle.Screen()
screen.title("Egypt Map Game")
screen.bgpic("Photos/EgyMap.gif")
screen.setup(width=800, height=600)

turtle.onscreenclick(lambda x, y: print(f"Coordinates: ({x}, {y})"))

screen.mainloop()