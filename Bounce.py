#imports#
#!/usr/bin/python
from tkinter import *
import pickle
import time
import random
import sys
counter = 0

colerList = ['red', 'green', 'blue', 'indigo', 'violet', 'purple']

save_file_pallet = open('files/color_pallet.dat', 'wb')
pickle.dump(colerList, save_file_pallet)
save_file_pallet.close()

save_file_score = open('files/score.dat', 'wb')
save_file_score.close()

button = False
    
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    
    def draw(self):
        global counter
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
            canvas.itemconfig(self.id, fill='red')
            tk.update()
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            tk.update()
            counter += 1
            self.y = -3
            load_pallet = open('files/color_pallet.dat', 'rb')
            loaded_color_pallet = pickle.load(load_pallet)
            random.shuffle(loaded_color_pallet)
            canvas.itemconfig(self.paddle.id, fill=loaded_color_pallet[0])
            canvas.itemconfig(textid, text=counter)
            
        if pos[0] <= 0:
            self.x = 2
            canvas.itemconfig(self.id, fill='violet')
            tk.update()
        if pos[2] >= self.canvas_width:
            self.x = -2
            canvas.itemconfig(self.id, fill='indigo')
            tk.update()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200 , 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.sysexit)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3
        
    def sysexit(self, evt):
        tk.destroy()

class commands:
    def play():
        tk.update()
        loop = True
        button = False
        if ball.hit_bottom == True:
            ball.y = -3
        ball.hit_bottom = False
        del counter
        counter = 0
        global counter
        canvas.itemconfig(textid, text=counter)



tk = Tk()
tk.title("Bounce")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
canvas.create_text(30, 20, text='Score :')
textid = canvas.create_text(30, 40, text=counter)
btn2 = Button(tk, text="Exit", command=tk.destroy)
btn2.pack()
canvas.move(btn2, 300, 300)
tk.update()
loop = True

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')


while loop == True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    elif ball.hit_bottom == False and button == True:
        btn.event_delete()
    if ball.hit_bottom == True:
        if ball.hit_bottom == True and button == False:
            tk.update_idletasks()
            tk.update()
            btn = Button(tk, text="Play again", command=commands.play)
            btn.pack()
            button = True
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    
