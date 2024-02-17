from tkinter import *
import time
# i=4
root=Tk()
root.title('Jimmy')
root.iconbitmap('./img/1.ico')
root.configure(background='')
root.geometry('400x200')
root.maxsize(400,200)
root.minsize(400,200)

# photos = [PhotoImage(file = "./img/va_gif.gif",format="gif -index 0"),
#           PhotoImage(file = "./img/va_gif.gif",format="gif -index 1"),
#           PhotoImage(file = "./img/va_gif.gif",format="gif -index 2"),
#           PhotoImage(file = "./img/va_gif.gif",format="gif -index 3"),
#           PhotoImage(file = "./img/va_gif.gif",format="gif -index 4"),
#           PhotoImage(file = "./img/va_gif.gif",format="gif -index 5"),
#           PhotoImage(file = "./img/va_gif.gif",format="gif -index 6")]

# label = Label(image = photos[i],background="navy")
# label.pack()
# i+=1
# if i>3:
#     i=0
# time.sleep(1)
# root.mainloop()

frameCnt = 120
frames = [PhotoImage(file='./img/va0_gif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame,background="purple",height=200,width=400)
    root.after(50, update, ind)

label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()

