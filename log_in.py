from main import *
class AskPass():
    def __init__(self,master):
        self.master = master
        self.master.geometry('300x175')
        self.master.title('Login')
        self.master.resizable(height = False,width = False)
        self.display()
    def defaultErase(self,btn):
        if self.password.get() == 'Type your password':
            self.password.delete(0,END)
            self.password.configure(show = '•')
    def display(self):
        frameHead = Frame(self.master,height = 40,width = 300)
        frameHead.place(x=0,y=0)
        Label(frameHead,text = 'LOGIN',font = ('Simplifica',18,'underline')).place(x=110,y=0)
        main_body = Frame(self.master,height = 130,width = 300)
        main_body.place(x=0,y=40)
        Label(main_body,text = 'Password:',font = ('Arial',11)).grid(row = 1,sticky = W)
        #Password Entry
        self.password = Entry(main_body,width = 24,font = ('Lucida Sans',9))
        self.password.insert(0,'Type your password')
        self.password.bind('<Button-1>',self.defaultErase)
        self.password.grid(row = 1,column = 1,columnspan = 2)
        #Check Button
        self.intVar = IntVar()
        Checkbutton(main_body,text = 'I am the owner of the system.',\
            height = 6,variable = self.intVar,onvalue = 1,\
            offvalue = 0,font = ('Century Gothic',10,'italic')).grid(row = 2,columnspan = 2)
        #Button
        Button(main_body,text= 'Submit',font = ('Adobe Garamond',10,'bold'),command = self.btnClick).place(x=3,y=98)

    #SELF IS NAMED as gui
    def btnClick(gui):
        if gui.password.get() == 'PA$$WORD' and gui.intVar.get() ==1:
            gui.master.destroy()
            window2= Tk()
            MainRegister(window2)
            window2.mainloop()
        else:
            showerror('Incorrect Details','Please make sure you type correct password and select the checkbox.')

if __name__ == '__main__':
    #createWindow()
    main = Tk()
    AskPass(main)
    main.mainloop()