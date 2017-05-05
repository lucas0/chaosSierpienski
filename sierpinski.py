import Tkinter as tk
from time import sleep
import random

sz = 1
margin = 20
width=800
height=800

master = tk.Tk()
w = tk.Canvas(master, width=width, height=height)
w.pack()

a = w.create_oval(width/2, margin, width/2+sz, margin+sz, fill="blue")
b = w.create_oval(margin, height-margin, margin+sz, height+sz-margin, fill="red")
c = w.create_oval(width-margin, height-margin, width-margin+sz, height+sz-margin, fill="green")
gradient = random.uniform(0,1)
rand_y = ((height-(margin*2))*gradient)+margin
rand_margin = (float((width/2)-margin))*gradient
rand_x = random.randint(int((width/2)-rand_margin),int((width/2)+rand_margin))

t = w.create_oval(rand_x, rand_y, rand_x+sz, rand_y+sz, fill="black")
print(rand_x,rand_y)

def plot_dot():
	global t
	r = random.randint(1,3)
	if r == 1:
		coords = w.coords(1)
	elif r == 2:
		coords = w.coords(2)
	else:
		coords = w.coords(3)
	t_x,t_y,s_x,s_y = w.coords(t)
	x = (coords[0]+t_x)/2
	y = (coords[1]+t_y)/2
	t = w.create_oval(x, y, x+sz, y+sz, fill="black")
	master.after(1, plot_dot)

b = tk.Button(master, text="NEXT", command=plot_dot)
b.pack()

master.mainloop()