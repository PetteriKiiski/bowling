from Tkinter import *
from time import *
from sys import *
global password
password = str()
tk = Tk()
btna = Button(tk, text = "a", command=(lambda:password+='a'))
print("Enter your password:")
sleep(3)

