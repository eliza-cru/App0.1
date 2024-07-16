# mylist = [0, 20, 1, 3, 10, 20, 30]

# print(mylist.sort())
# print(mylist)



# mylist2 = [10, 1, 2, 1, 1, 10, 20, 15]
# print(sorted(mylist2))
# print(mylist2)


# import x1       

# x1.hello()
# x1.sum(10, 20)
# import sup
# import time

# sum.hello()

# time.sleep(5)

# sup.sum(10, 20)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def hello(self):
#         print(f"привет! меня зовут {self.name}!")

# one_person = Person("Stenli", 20)
# print(one_person.age)
# print(one_person.name)
# one_person.hello()



# from tkinter import *

# clicks = 0

# def get_entry():
#     value = entry.get()
#     txt["text"] = value

# def finish():
#     x1.destroy()
#     print("App is close!")

# def click_button():
#     global clicks
#     clicks += 100
#     x6["text"] = f"Clicks {clicks}"

# x1 = Tk()
# x1.title('my firs app')
# x1.geometry('600x500')
# x1.resizable(True, True)
# x1.attributes("-fullscreen", True)
# x1.attributes("-alpha", 0.8)
# x1.protocol("WM_DELETE_WINDOW", finish)

# icon = PhotoImage(file="x2.png")
# x1.iconphoto(True, icon)

# label = Label(text="hello my friends")
# x2 = Label(text='Hello')
# label.pack()
# x2.pack()

# x3 = Button(text="нажми")
# x3.pack()

# x5 = Button()
# x5.pack())
# x5["text"] = "   "

# x4 = Button()
# x4.pack()
# x4["text"] = "не нажимай"

# x6 = Button(text="click me", command=click_button)
# x6.pack()

# x1.mainloop()

# entry = Entry()
# entry.pack(
#=======================================================

# btn = Button(text="Clik me!",command=get_entry)
# btn.pack

# txt = Label(text="New text...")
# txt.pack





from tkinter import *

# def finish():
#     btn.destroy()
#     print("App is close!")

clicks = 0

def get_entry():
    value = int(entry.get())
    value = int(entry2.get())
    txt["text"] = value

def click_button():
    global clicks
    btn["text"] = f"Clicks {clicks}"


root = Tk()
root.title("My app")
root.geometry("400x300")


entry = Entry()
entry.pack()


entry2 = Entry()
entry2.pack()

txt = Label(text="New text...")
txt.pack()
btn = Button(text="Clik me!",command=get_entry)
btn.pack
btn.mainloop()

root.mainloop()

