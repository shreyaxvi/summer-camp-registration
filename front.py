from tkinter import *
from tkinter import messagebox
import back

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])
    entry5.delete(0, END)
    entry5.insert(END, selected_tuple[5])
    entry6.delete(0, END)
    entry6.insert(END, selected_tuple[6])
    entry7.delete(0, END)
    entry7.insert(END, selected_tuple[7])

def view_command():
    list1.delete(0, END)
    for row in back.view():
        list1.insert(END, row)

def add_command():
    clear_error_labels()
    errors = back.insert(name_text.get(), age_text.get(), phone_number_text.get(), address_text.get(), activity_text.get(), days_text.get(), amount_text.get())
    if errors:
        for i, error in enumerate(errors):
            error_label = Label(window, text=error, fg="red")
            error_label.grid(row=12+i, columnspan=4)
    else:
        list1.delete(0, END)
        list1.insert(END, (name_text.get(), age_text.get(), phone_number_text.get(), address_text.get(), activity_text.get(), days_text.get(), amount_text.get()))

def delete_command():
    back.delete(selected_tuple[0])

def update_command():
    clear_error_labels()
    errors = back.update(selected_tuple[0], name_text.get(), age_text.get(), phone_number_text.get(), address_text.get(), activity_text.get(), days_text.get(), amount_text.get())
    if errors:
        for i, error in enumerate(errors):
            error_label = Label(window, text=error, fg="red")
            error_label.grid(row=12+i, columnspan=4)

def clear_error_labels():
    for widget in window.winfo_children():
        if isinstance(widget, Label) and widget.cget("fg") == "red":
            widget.destroy()

def calculate_total():
    activity = activity_text.get()
    no_of_days = days_text.get()
    if activity.lower() in {"sketching", "chess", "coding"} and no_of_days.isdigit():
        total = back.calculation(no_of_days, activity)
        amount_text.set(total)
    else:
        amount_text.set("")

window = Tk()
window.title("Registration")

label1 = Label(window, text="Summer Camp Registration")
label1.grid(row=0, column=2)

label2 = Label(window, text="Name")
label2.grid(row=1, column=0)

label3 = Label(window, text="Age")
label3.grid(row=2, column=0)

label4 = Label(window, text="Phone number")
label4.grid(row=3, column=0)

label5 = Label(window, text="Address")
label5.grid(row=4, column=0)

label6 = Label(window, text="Activity\n(Sketching, Coding, Chess):")
label6.grid(row=5, column=0)

label7 = Label(window, text="No. of days")
label7.grid(row=6, column=0)

label8 = Label(window, text="Total amount")
label8.grid(row=7, column=0)

name_text = StringVar()
entry1 = Entry(window, textvariable=name_text)
entry1.grid(row=1, column=1)

age_text = StringVar()
entry2 = Entry(window, textvariable=age_text)
entry2.grid(row=2, column=1)

phone_number_text = StringVar()
entry3 = Entry(window, textvariable=phone_number_text)
entry3.grid(row=3, column=1)

address_text = StringVar()
entry4 = Entry(window, textvariable=address_text)
entry4.grid(row=4, column=1)

activity_text = StringVar()
activity_text.trace("w", lambda *args: calculate_total())  
entry5 = Entry(window, textvariable=activity_text)
entry5.grid(row=5, column=1)

days_text = StringVar()
days_text.trace("w", lambda *args: calculate_total())  
entry6 = Entry(window, textvariable=days_text)
entry6.grid(row=6, column=1)

amount_text = StringVar()
entry7 = Entry(window, textvariable=amount_text)
entry7.grid(row=7, column=1)

list1 = Listbox(window, height=20, width=60)
list1.grid(row=1, column=3, rowspan=7, columnspan=2)

scrl = Scrollbar(window)
scrl.grid(row=1, column=2, sticky='ns', rowspan=6)

list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=10, command=view_command)
b1.grid(row=11, column=1)

b2 = Button(window, text="Add Entry", width=10, command=add_command)
b2.grid(row=9, column=0)

b3 = Button(window, text="Delete Entry", width=10, command=delete_command)
b3.grid(row=11, column=0)

b4 = Button(window, text="Update", width=10, command=update_command)
b4.grid(row=9, column=1)

window.mainloop()
