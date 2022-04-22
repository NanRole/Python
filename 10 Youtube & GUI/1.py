from tkinter import *
from pytube import YouTube
import os
def run1():
    url = ent1.get()
    filename = ent2.get()
    yt = YouTube(url)
    if filename != '': filename += '.mp4'
    yt.streams.filter(subtype='mp4').first().download(filename=filename)
    lbl3.config(text = '影片下載完成')

def run2():
    url = ent1.get()
    filename = ent2.get()
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True, subtype='mp4').first()
    audio.download(filename=filename)
    if filename != '':
        os.rename(filename, filename+'.mp3')
    else:
        dfn = audio.default_filename
        os.rename(dfn, dfn.rstrip('.mp4')+'.mp3')
    lbl3.config(text = '音樂檔案下載完成')

win = Tk()
win.title('410723001')
lbl1 = Label(win, text = '請輸入網址：')
ent1 = Entry(win, width = 70)
lbl2 = Label(win, text = '請輸入檔名：')
ent2 = Entry(win, width = 70)
btn1 = Button(win, text = '下載影片', width = 20, command = run1)
btn2 = Button(win, text = '下載音樂', width = 20, command = run2)
lbl3 = Label(win)

lbl1.pack(pady = 5)
ent1.pack(padx = 10)
lbl2.pack(pady = 5)
ent2.pack(padx = 10)
btn1.pack(pady = 5)
btn2.pack()
lbl3.pack(pady = 10)
win.mainloop()