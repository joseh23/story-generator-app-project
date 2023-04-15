import random
from tkinter import *
from tkinter import Label

# creating the user interface.
root = Tk()
root.title("STORY GENERATOR")
my_label = Label(root, text="STORY GENERATOR", fg="white", bg="black")
my_label.pack()


def button_click():
    when = ['A few years ago', 'yesterday', 'last night', 'A long time ago', 'On 20th Jan']
    who = ['a rabit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
    residence = ['Barcelona', 'india', 'Germany', 'Venice', 'England']
    went = ['cinema', 'university', 'seminar', 'school', 'laundry']
    happened = ['made alot of friends', 'Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
    answer = Label(root, text=((random.choice(when) + ', ' + random.choice(who) + ' that lived in ' +
                                random.choice(residence) + ',' + '' +
                                random.choice(happened))),)
    answer.pack()


my_button = Button(root, text="click to find an intro to your composition", command=button_click, pady=50, padx=50, bg="red")
my_button.pack()

# def button_click():
#     when = ['A few years ago', 'yesterday', 'last night', 'A long time ago', 'On 20th Jan']
#     who = ['a rabit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
#     residence = ['Barcelona', 'india', 'Germany', 'Venice', 'England']
#     went = ['cinema', 'university', 'seminar', 'school', 'laundry']
#     happened = ['made alot of friends', 'Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
#     answer = Label(root, text=((random.choice(when) + ', ' + random.choice(who) + ' that lived in ' +
#                                 random.choice(residence) + random.choice(went) +
#                                 random.choice(happened))), bg="grey", )
#     answer.pack()
#
#
# button_click()
button_exit = Button(root, text="Exit", command= lambda : root.quit)
button_exit.pack()
root.mainloop()
