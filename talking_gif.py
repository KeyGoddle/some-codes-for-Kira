from tkinter import *
from PIL import Image

root=Tk()
root.geometry("500x500")
root.iconbitmap("matsuri-talk.ico")
root.config(background='#fafbd0')
gifImage="matsuri-talk.gif"
openImage=Image.open(gifImage)
frames=openImage.n_frames
imageObject =[PhotoImage(file=gifImage, format=f"gif -index {i}")for i in range(frames)]



#a_length= a_length//2
ShowAnimation=None

def animation(count):
    global ShowAnimation
    global count_all
    newImage = imageObject[count]

    gif_Label.configure(image=newImage)
    count += 1
    count_all +=1
    print(count)
    if count ==frames:
        count=0    
    if count_all==a_length: 
        count_all=0
        return 0
    ShowAnimation=root.after(100, lambda:animation(count))

a= "Сейчас я расскажу историю о "
count_all=0
a_length= (len(a))
gif_Label= Label (root, image="")
gif_Label.place(x=0,y=0,width=450,height=500)
count=0
animation(count)
v=input()

a_length=len(v)
animation(count)
root.mainloop()