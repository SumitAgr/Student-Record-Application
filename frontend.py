from tkinter import *
import backend

window = Tk()
window.title("Student Record Application")

l1 = Label(window, text = "Name")
l1.grid(row = 0, column = 0)

l1 = Label(window, text = "ID")
l1.grid(row = 0, column = 2)

l1 = Label(window, text = "Major")
l1.grid(row = 1, column = 0)

l1 = Label(window, text = "Age")
l1.grid(row = 1, column = 2)

l1 = Label(window, text = "Sex")
l1.grid(row = 2, column = 0)

l1 = Label(window, text = "Address")
l1.grid(row = 2, column = 2)

l1 = Label(window, text = "GPA")
l1.grid(row = 3, column = 0)

name_text = StringVar()
e1 = Entry(window, textvariable = name_text)
e1.grid(row = 0, column = 1)

id_text = StringVar()
e1 = Entry(window, textvariable = id_text)
e1.grid(row = 0, column = 3)

major_text = StringVar()
e1 = Entry(window, textvariable = major_text)
e1.grid(row = 1, column = 1)

age_text = StringVar()
e1 = Entry(window, textvariable = age_text)
e1.grid(row = 1, column = 3)

sex_text = StringVar()
e1 = Entry(window, textvariable = sex_text)
e1.grid(row = 2, column = 1)

address_text = StringVar()
e1 = Entry(window, textvariable = address_text)
e1.grid(row = 2, column = 3)

gpa_text = StringVar()
e1 = Entry(window, textvariable = gpa_text)
e1.grid(row = 3, column = 1)


list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 6, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 4, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "View All", width = 12)
b1.grid(row = 4, column = 3)

b1 = Button(window, text = "Search Entry", width = 12)
b1.grid(row = 5, column = 3)

b1 = Button(window, text = "Add Entry", width = 12)
b1.grid(row = 6, column = 3)

b1 = Button(window, text = "Update Selected", width = 12)
b1.grid(row = 7, column = 3)

b1 = Button(window, text = "Delete Selected", width = 12)
b1.grid(row = 8, column = 3)

b1 = Button(window, text = "Close", width = 12)
b1.grid(row = 9, column = 3)

window.mainloop()
