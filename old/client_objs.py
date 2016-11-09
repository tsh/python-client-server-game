import tkinter as tk

class BaseObject(object):
    def __init__(self, x=100, y=120, r=50,):
        self.x = x
        self.y = y
        self.r = r

        self.dx = 10

    def render(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill="blue", outline="#DDD", width=4)

    def update(self):
        self.x += self.dx