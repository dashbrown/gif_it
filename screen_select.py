import Tkinter as tk
import screen_capture as sc
 
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



# def set_center(event):
# 	sx = str(event.x)
# 	sy = str(event.y)
# 	root.geometry('+' + sx + '+' + sy)
 

if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-alpha', 0.5)
    frame = tk.Frame(root, bg= '', width=1440, height=900)
    frame.bind("<Motion>", showxy)
    frame.bind("Button-1", showxy)
    frame.pack()
    root.mainloop()