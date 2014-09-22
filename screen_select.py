import Tkinter as tk
 
def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    # show cordinates in title
    root.title(str1)
    # switch color to red if mouse enters a set location range
    x,y, delta = 100, 100, 10
    frame.config(bg = 'white')
    # frame.config(bg='red'
    #              if abs(xm - x) < delta and abs(ym - y) < delta
    #              else 'yellow')

def set_center(event):
	sx = str(event.x)
	sy = str(event.y)
	root.geometry('+' + sx + '+' + sy)
 
root = tk.Tk()
root.attributes('-alpha', 0.1)
frame = tk.Frame(root, bg= '', width=500, height=500)
#frame.bind("<Motion>", showxy)
frame.bind("<Motion>", set_center)
frame.pack()
 
root.mainloop()