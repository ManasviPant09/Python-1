from tkinter import *
import tkinter.messagebox as b
class Loginmp(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_username=Label(self,'Username',font=('Arial',20))
        self.label_password=Label(self,'Password',font=('Arial',20))

        self.entry_username=Entry(self)
        self.entry_password=Entry(self)

        self.label_username.grid(row=0,sticky=E)
        self.label_password.grid(row=1,sticky=E)
        self.entry_username.grid(row=0,column=1)
        self.entry_password.grid(row=1,column=1)

        self.button=Button(self,text='Login',command=self.login)
        self.button.grid(columnspan=2)

        self.pack()

        def login(self):
            Username=self.entry_username.get()
            Password=self.entry_password.get()

            if(Username=='mp' and Password=='1234'):
                b.showinfo("Login","Login Successfully")
            else:
                b.showinfo("Login","Login failed")
mp=Tk()
login=Loginmp(mp)
mp.mainloop()
