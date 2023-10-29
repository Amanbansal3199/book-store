from tkinter import *
from back import insert, update, view

def get_selected_row(event):
    try:
        global selct_tuple
        index=list1.curselection()
        selct_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selct_tuple[0])
        e2.delete(0,END)
        e2.insert(END,selct_tuple[1])
        e3.delete(0,END)
        e3.insert(END,selct_tuple[2])
        e4.delete(0,END)
        e4.insert(END,selct_tuple[3])
    except IndexError:
        pass

def view_cm():
    list1.delete(0,END)
    for row in view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in back.search(e1_text.get(),e1_text.get(),e3_text.get(),e4_text.get()):
        list1.insert(END,row)

def add_command():
    insert(e1_text.get(),e2_text.get(),e3_text.get(),e4_text.get())
    list1.delete(0,END)
    list1.insert(END,e1_text.get(),e2_text.get(),e3_text.get(),e4_text.get())

def delete_command():
    back.delete(selct_tuple[0])

def update_command():
    update(e1_text.get(),e2_text.get(),e3_text.get(),e4_text.get())


window=Tk()
window.title("BOOK STORE")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
e1_text=StringVar()
e1=Entry(window,textvariable=e1_text,width=20)
e1.grid(row=0,column=1)

l2=Label(window,text="Author",width=10)
l2.grid(row=0,column=3)
e2_text=StringVar()
e2=Entry(window,textvariable=e2_text,width=20)
e2.grid(row=0,column=4)

l3=Label(window,text="Year",height=2)
l3.grid(row=1,column=0)
e3_text=StringVar()
e3=Entry(window,textvariable=e3_text,width=20)
e3.grid(row=1,column=1)

l4=Label(window,text="ISBN", height=2,width=10)
l4.grid(row=1,column=3)
e4_text=StringVar()
e4=Entry(window,textvariable=e4_text,width=20)
e4.grid(row=1,column=4)


list1=Listbox(window,height=15,width=45)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2 )
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",get_selected_row)

b1=Button(window,text="View",width=12,command=view_cm)
b1.grid(row=2,column=4)

b2=Button(window,text="Delete Selected",width=12,command=delete_command )
b2.grid(row=3,column=4)

b3=Button(window,text="Update Selected",width=12,command=update_command)
b3.grid(row=4,column=4)

b4=Button(window,text="Search Entry",width=12,command=search_command)
b4.grid(row=5,column=4)

b5=Button(window,text="Add Entry",width=12,command=add_command)
b5.grid(row=6,column=4)

b6=Button(window,text="close",width=12,command=window.destroy)
b6.grid(row=7,column=4)
window.mainloop()
