import json
from difflib import get_close_matches
from tkinter import *


data = json.load(open("data.json")) 

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
def clicked():
    a = translate(txt.get())
    res = "Meaning:\n" 
    if type(a) == list:
        for i in a:
            res += i + "\n" 
    lbl1.configure(text = res)

root = Tk()

root.title("Dictionary")
root.geometry('1000x500')
lbl = Label(root, text = "Enter a word: ")
lbl.grid()
txt = Entry(root, width=30)
txt.grid(column =1, row =0)
btn = Button(root, text = "Search",fg = "red", command=clicked)
btn.grid(column =3, row=0)
lbl1 = Label(root, text="")
lbl1.grid(row = 1)

root.mainloop()
