from tkinter import *
from tkinter import messagebox

def exit_game():
    msgBox = messagebox.askquestion('關閉APP', '您確定要離開嗎？', icon='error')
    if msgBox == 'yes':
        win.destroy()

win = Tk()
win.title('終極密碼')

frame1 = Frame(win)
lbl_Min = Label(frame1, text = '0', font=('Arial', 20), relief='ridge', width=5, height=2)
lbl_Lt1 = Label(frame1, text = '<', font=('Arial', 20), height=2)
ent = Entry(frame1, font=('Arial', 20), width=5, justify=CENTER)
lbl_Lt2 = Label(frame1, text = '<', font=('Arial', 20), height=2)
lbl_Max = Label(frame1, text = '1000', font=('Arial', 20), relief='ridge', width=5, height=2)

frame2 = Frame(win)
btn_Reset = Button(frame2, text = '重新開始', font=('標楷體', 16))
btn_Start = Button(frame2, text = '開始猜', font=('標楷體', 16))
btn_End = Button(frame2, text = '結束', font=('標楷體', 16), command=exit_game)

lbl_Min.pack(side=LEFT)
lbl_Lt1.pack(side=LEFT, padx=10)
ent.pack(side=LEFT, ipady=15)
lbl_Lt2.pack(side=LEFT, padx=10)
lbl_Max.pack(side=LEFT)

btn_Reset.pack(side=LEFT)
btn_Start.pack(side=LEFT, padx=20)
btn_End.pack(side=LEFT)

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)
win.mainloop()