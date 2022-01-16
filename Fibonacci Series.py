# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:29:04 2022

@author: Nivedita
"""
from tkinter import*
root=Tk()
root.title("Fibonacci Series")
root.geometry("600x600")

lblseries= Label(root, text="Fibonacci Series")
lblflower= Label(root)
lblspiral= Label(root)

def display():
    num=10
    fn=0
    sn=1
    sum=0
    i=1
    while(i<=num):
        lblseries["text"]+=str(sum)+" "
        i=i+1
        fn=sn
        sn=sum
        sum=fn+sn
    lblflower["text"]="flower is fully bloomed"
    lblspiral["text"]="spiral in right directiion are "+str(fn)+" and spiral in left direction are "+str(sn)+" total spiral are "+str(sum)

btn=Button(root,text="Show Fibonacci Series", command= display)

lblseries.pack()
btn.pack()
lblflower.pack()
lblspiral.pack()








root.mainloop()
