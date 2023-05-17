# -*- coding: utf-8 -*-
"""
Buse ACUN / 181805013
"""
from tkinter import *
import cv2

#defining the interface from which the button exits
tk = Tk()
tk.title("Shooting With Mosaic")
tk.geometry("400x85")

#assigning a property to a button
def buton():
 cam=cv2.VideoCapture(0)   
 face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
 video=cv2.VideoCapture(0)

#making detect
 while True:
     check,frame=video.read()
     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
     for x,y,w,h in face:
         
         mosaic = cv2.medianBlur(frame[y:y+h, x:x+w], 25)
         frame[y:y+h, x:x+w] = mosaic
     
     cv2.imshow('Video', frame)
         
     #for exit
     if cv2.waitKey(1) & 0xFF == ord('e'):
         break

#executing functions
 video.release()
 cv2.destroyAllWindows()

btn2 = Button(tk,
            text = "Shooting With Mosaic", font="Times 12 bold",
            padx="20", pady="5", 
            bg="blue", fg="white", cursor="hand2",
            activeforeground="blue", activebackground="black",
            command=buton)
btn2.pack()
lbl = Label(tk)
lbl.pack()
 
tk.mainloop()