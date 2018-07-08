from tkinter import *
import TrustStat
import webbrowser
import UsageStat
import threading

def onclick():
    th1 = threading.Thread(UsageStat.Usage.Graph())
    th1.start()

def onclick1():
    th2 = threading.Thread(TrustStat.Trust.Graph())
    th2.start()

def webBrowser():
    webbrowser.open_new('https://www.hindustantimes.com/editorials/is-this-the-beginning-of-the-end-of-faceboo'
                        'k/story-4Mv6nsXq6nV64RTXx16cQL.html')


root = Tk()

canvas_width = 800
canvas_height = 600

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

img = PhotoImage(file="face.gif")
canvas.create_image(0, 0, anchor=NW, image=img)

root.title("Future of Facebook")
root.geometry('800x600')

lbl1 = Label(canvas, text='Is this End of Facebook??', font='Times 24 bold', fg='white', bg='#2381BE')
canvas.create_window(200, 50, window=lbl1)

lbl2 = Label(canvas, text='PROOF', font='Times 24 bold', fg='white', bg='#237DBB')
canvas.create_window(585, 50, window=lbl2)

lbl3 = Label(canvas, text='Facebook Usage Starts to decrease after \n 2016 but other social platform usage is increasing', font='Times 12 ', fg='white', bg='#237DBB')
canvas.create_window(585, 150, window=lbl3)

lbl4 = Label(canvas, text='Trust on Facebook decreases \n abruptly after Cambridge Scandal', font='Times 12 ', fg='white', bg='#237DBB')
canvas.create_window(590, 250, window=lbl4)

p_btn = Button(text='Usage GRAPH', command=onclick)
canvas.create_window(600, 200, window=p_btn)

q_btn = Button(text='Trust GRAPH', command=onclick1)
canvas.create_window(600, 300, window=q_btn)

a_btn = Button(text='Article', command=webBrowser)
canvas.create_window(200, 100, window=a_btn)

root.resizable(False, False)
root.mainloop()
canvas.mainloop()
"""
Team:
Gagandeep Singh
Bhim sen 
"""
