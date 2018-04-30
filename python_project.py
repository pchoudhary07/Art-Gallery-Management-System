from tkinter import *
from tkinter import messagebox

t = Tk()
index = 0

import time



#t.title()# Add the blank space
def center(e):
    w = int(t.winfo_width() /20) # get root width and scale it ( in pixels )
    s = 'Art Gallery Management'.rjust(w//2)
    t.title(s)



t.configure(background='Orange')
t.bind("<Configure>", center) # called when window resized
#00ff00 florocent green

localtime=time.asctime(time.localtime(time.time()))
time_label=Label(t,text=localtime,font="arial 15 italic",foreground="black",bg="orange",bd=20)
time_label.grid(row=1,column=2,padx=20)

head=Label(t,text='Art Gallery Management',font='Times 24 bold italic',foreground='yellow',bg="purple",borderwidth=15,relief="solid")
head.grid(row=0,column=2,padx=10,pady=20)

def add(event):
    global index
    f = open('mydata', 'a')
    f.write(
        e1.get() + '\t' + e2.get() + '\t' + e3.get() + '\t' + e4.get() + '\t' + e5.get() + '\t' + e6.get() + '\n')
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    messagebox.showinfo('Alert', '!!Record added successfully!!')
    f.close()


def delete(event):
    f = open('mydata', 'r')
    lines = f.readlines()
    f.close()
    f = open('mydata', 'w')
    for line in lines:
        col = line.split()
        if col[0] != e1.get():
            f.write(line)
    messagebox.showinfo('Alert','!!Record deleted successfully!!')
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    f.close()


def search(event):
    f = open('mydata', 'r')
    lines = f.readlines()
    col = []
    flag = False
    for line in lines:
        col = line.split()
        if col[0] == e1.get():
            messagebox.showinfo('Alert', '!!Record found!!')
            flag = True
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e5.delete(0, 'end')
            e6.delete(0, 'end')

            e1.insert(0, col[0]);
            e2.insert(0, col[1]);
            e3.insert(0, col[2]);
            e4.insert(0, col[3]);
            e5.insert(0, col[4]);
            e6.insert(0, col[5]);
            break

    if flag == False:
        messagebox.showinfo('Alert','Sorry! Record not found!')
    f.close()


def update(event):
    f = open('mydata', 'r')
    lines = f.readlines()
    f.close()
    f = open('mydata', 'w')
    for line in lines:
        col = line.split()
        if col[0] == e1.get():
            f.write(e1.get() + '\t' + e2.get() + '\t' + e3.get() + '\t' + e4.get() + '\t' + e5.get() + '\t' + e6.get() + '\n')
            messagebox.showinfo('Info', '!!Record updated successfully!!')
        else:
            f.write(line)
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    f.close()


def next(event):
    f = open('mydata', 'r')
    global index
    index = index + 1
    #print(index)
    f.seek(index)
    try:
        c = f.readlines()
        xyz = c[index]
        l = list(xyz.split())
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')
        e4.delete(0, 'end')
        e5.delete(0, 'end')
        e6.delete(0, 'end')

        e1.insert(0, l[0]);
        e2.insert(0, l[1]);
        e3.insert(0, l[2]);
        e4.insert(0, l[3]);
        e5.insert(0, l[4]);
        e6.insert(0, l[5]);
    except:
        messagebox.showinfo("Info","!! No More Records!!")
    f.close()


def prev(event):
    f = open('mydata', 'r')
    global index
    index = index - 1
    print(index)
    try:
        f.seek(index)
        c = f.readlines()
        xyz = c[index]
        l = list(xyz.split())
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')
        e4.delete(0, 'end')
        e5.delete(0, 'end')
        e6.delete(0, 'end')

        e1.insert(0, l[0]);
        e2.insert(0, l[1]);
        e3.insert(0, l[2]);
        e4.insert(0, l[3]);
        e5.insert(0, l[4]);
        e6.insert(0, l[5]);
    except:
        messagebox.showinfo("Info","No More Records")
    f.close()


def first(event):
    f = open('mydata', 'r')
    global index
    index = 0
    #print(index)
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    f.seek(0)
    k = f.readline()
    k = k.split()
    e1.insert(0, k[0]);
    e2.insert(0, k[1]);
    e3.insert(0, k[2]);
    e4.insert(0, k[3]);
    e5.insert(0, k[4]);
    e6.insert(0, k[5]);
    f.close()


def last(event):
    f = open('mydata', 'r')
    count = 0
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    for i in f:
        k = i
        count += 1
    k = k.split()
    e1.insert(0, k[0]);
    e2.insert(0, k[1]);
    e3.insert(0, k[2]);
    e4.insert(0, k[3]);
    e5.insert(0, k[4]);
    e6.insert(0, k[5]);
    global index
    index = count
    #print(index)
    f.close()

id_label=Label(t,text="Artist ID:",bg="#00ff0f",bd=5,justify="center")
name_label=Label(t,text="Artist Name:",bg="yellow",bd=5,justify="center")
age_label=Label(t,text="Artist Age:",bg="#00ff0f",bd=5,justify="center")
cont_label=Label(t,text="Contact No.:",bg='yellow',bd=5,justify="center")
Address_label=Label(t,text="Address:",bg="#00ff0f",bd=5,justify="center")
work_label=Label(t,text="Style of work:",bg="yellow",bd=5,justify="center")

id_label.grid(row=2,column=1,columnspan=1,sticky=W,padx=200,pady=10)
name_label.grid(row=3,column=1,sticky=W,padx=200,pady=10)
age_label.grid(row=4,column=1,sticky=W,padx=200,pady=10)
cont_label.grid(row=5,column=1,sticky=W,padx=200,pady=10)
Address_label.grid(row=6,column=1,sticky=W,padx=200,pady=10)
work_label.grid(row=7,column=1,sticky=W,padx=200,pady=10)

e1=Entry(t,bd=5)
e1.grid(row=2,column=2,columnspan=2,pady=10)

e2=Entry(t,bd=5)
e2.grid(row=3,column=2,columnspan=2,pady=10)

e3=Entry(t,bd=5)
e3.grid(row=4,column=2,columnspan=2,pady=10)

e4=Entry(t,bd=5)
e4.grid(row=5,column=2,columnspan=2,pady=10)

e5=Entry(t,bd=5)
e5.grid(row=6,column=2,columnspan=2,pady=10)

e6=Entry(t,bd=5)
e6.grid(row=7,column=2,columnspan=2,pady=10)



b1=Button(t,text="<<",bg="black",foreground="white",width=10,font="Times 10 bold italic")
b1.bind('<Button-1>',prev)
b1.grid(row=11,column=1,columnspan=2)

b2=Button(t,text=">>",bg="black",foreground="white",width=10,font="Times 10 bold bold")
b2.bind('<Button-1>',next)
b2.grid(row=11,columnspan=2,column=2)

b7=Button(t,text="|<",bg="black",foreground="white",width=10,font="Times 10 bold italic")
b7.bind('<Button-1>',first)
b7.grid(row=11,column=0,columnspan=2)

b8=Button(t,text=">|",bg="black",foreground="white",width=10,font="Times 10 bold bold")
b8.bind('<Button-1>',last)
b8.grid(row=11,columnspan=2,column=3)

b3=Button(t,text="Add",bg="black",foreground="white",width=10,font="Times 17 bold italic")
b3.bind('<Button-1>',add)
b3.grid(row=12,column=0,columnspan=2,pady=20)

b4=Button(t,text="Search",bg="black",foreground="white",width=10,font="Times 17 bold italic")
b4.bind('<Button-1>',search)
b4.grid(row=12,column=1,columnspan=2,pady=20)

b5=Button(t,text="Update",command=update,bg="black",foreground="white",width=10,font="Times 17 bold italic")
b5.bind('<Button-1>', update)
b5.grid(row=12,column=2,columnspan=2,pady=20)

b6=Button(t,text="Delete",bg="black",foreground="white",width=10,font="Times 17 bold italic")
b6.bind('<Button-1>',delete)
b6.grid(row=12,column=3,columnspan=2,pady=20)

t.mainloop()
