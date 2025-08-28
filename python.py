from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('400x300')
win.config(bg = '#fa3456')
#==========Function=============================================
def insert():
    fname = ent_fname.get()
    lname = ent_lname.get()
    lst_names.insert(END,f'{fname},{lname}')
    clear()

def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_fname.focus_set()

def delete():
    index = lst_names.curselection() 
    # print(index) 
    result = messagebox.askyesno("Delete","Are you sure deleted?") 
    if result == True:
        lst_names.delete(index)

def fetch():
    clear()
    index = lst_names.curselection()
    record = lst_names.get(index)
    # print(record)
    # print(type(record))
    lst = record.split(',')
    # print(lst)
    ent_fname.insert(0,lst[0])
    ent_lname.insert(0,lst[1])


#==========label=============================================

lbl_fname = Label(win,text = 'first name:' , font = 'arial 17')
lbl_fname.place(x = 20 , y = 5)

lbl_lname = Label(win,text = 'last name:' , font = 'arial 17')
lbl_lname.place(x = 20 , y = 55)

ent_fname = Entry(win,font = 'arial 15')
ent_fname.place(x = 165 , y =8 )

ent_lname = Entry(win,font = 'arial 15')
ent_lname.place(x = 165 , y =58 )


#==========btn================================================
btn_insert = Button(win,text = 'insert' , font = 'arial 12',width=10,command=insert)
btn_insert.place(x = 5 , y = 200)


btn_clear = Button(win,text = 'clear' , font = 'arial 12',width = 10,command=clear)
btn_clear.place(x = 150 , y = 200)

btn_delete = Button(win,text = 'delete' , font = 'arial 12',width=10,command=delete)
btn_delete.place(x = 290 , y = 200)

btn_fetch = Button(win,text = 'fetch' , font = 'arial 12',width=10,command=fetch)
btn_fetch.place(x = 5 , y = 250)

btn_exit = Button(win,text = 'Exit' , font = 'arial 12',width=26)
btn_exit.place(x = 150 , y = 250)



lst_names = Listbox(win,width=37)
lst_names.place(x = 165 , y = 90 , height=100)
# for i in range(5):
#     lst_names.insert(END,f"{i+1}- This is a test")

win.mainloop()