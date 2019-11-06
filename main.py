from logic import *
from subprocess import call
#from log_in import createWindow
def eraseEntry(_,callFrom,entry,pas = False):
    """INPUT:
    default pass
    callFrom = The inserted text
    entry = Entry object itself
    pas = DEFAULT False, if password make it True
    """
    if entry.get() == callFrom:
        entry.delete(0,END)
        if pas is True:
            entry.configure(show = '•')
def all_children (window) :
    """INPUT:
    window : The root variable holding Tk object
    OUTPUT:
    Returns all the items that can be used to clear everything
    """
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
class MainRegister(AllCommand):
    def __init__(self,master):
        self.master = master
        #self.master.config(bg = 'SystemButtonFace')
        self.master.title('Add new account info')
        self.master.geometry('350x170')
        self.master.resizable(height = False,width = False)
        self.conData()
        self.destroy_widgets()
        self.menu()
        self.add_account()
    def destroy_widgets(self):
        all_widgets = all_children(self.master)
        for i in all_widgets:
            i.destroy()
    

    def menu(self):
        self.main_menu = Menu(self.master)
        operations = Menu(self.main_menu)
        #Add Commands
        operations.add_command(label = 'Add Account',command = lambda : self.__init__(self.master))
        operations.add_command(label = 'Query',command = self.query_account)
        operations.add_command(label = 'Show all accounts',command=self.display_all_accounts)
        operations.add_command(label = 'Delete',command = self.deleteAccount)

        #Account
        account = Menu(self.main_menu)
        account.add_command(label = 'Log Out',command = self.log_out)
        account.add_command(label = 'Exit',command = self.master.destroy)

        #about
        about = Menu(self.main_menu)
        about.add_command(label = 'Rate Us',command = self.rate)
        about.add_command(label = 'About Program',command = lambda : showinfo('About Program','This is a basic tkinter app that '+\
        'stores Email and Passwords so that you don\'t have to take the trouble'+\
        ' of remembering them.\nENJOY'))


        #add cascade to main_menu
        self.main_menu.add_cascade(label = 'Operations',menu = operations)
        self.main_menu.add_cascade(label = 'Accounts',menu = account)
        self.main_menu.add_cascade(label = 'About',menu = about)
        self.master.config(menu = self.main_menu)
    def add_account(self):
        head = Frame(self.master,height = 35,width = 350)
        head.place(x=0,y=0)
        label_font = ('Impact',14)
        Label(head,text = 'Add Account Info',font = label_font).pack()
        #Form
        body = Frame(self.master,height = 143,width = 350)
        body.place(x=0,y=35)
        #Font
        label_font = ('Century Gothic',10)
        #Label
        Label(body,text = 'Website:',font = label_font).grid(row = 0,sticky = E)
        Label(body,text = 'Email/Username:',font = label_font).grid(row = 1,sticky = E)
        Label(body,text = 'Password:',font = label_font).grid(row=2,sticky = E)
        #Entry1:
        #--FONT--
        entry_font = ('Clarendon',9)
        #--FONT--
        self.name = Entry(body,font = entry_font,width = 19)
        self.name.grid(row = 0,column = 1,sticky = W)
        self.name.insert(0,'Website (No spaces)')
        self.name.bind('<Button-1>',lambda n: eraseEntry(n,'Website (No spaces)',self.name))
        
        #OptionMenu:
        self.domain = StringVar()
        self.domain_list = ['.com','.in','.net','.org','.uk','.info']
        self.domain.set(self.domain_list[0])
        OptionMenu(body,self.domain,*self.domain_list).grid(row = 0,column = 2)
       
       
        #Entry2
        self.usn = Entry(body,font = entry_font,width = 29)
        self.usn.grid(row = 1,column = 1,columnspan =2,sticky = W)
        self.usn.insert(0,'Username/email(No spaces)')
        self.usn.bind('<Button-1>',lambda n: eraseEntry(n,'Username/email(No spaces)',self.usn))

        #Entry3

        self.pas = Entry(body,font = entry_font,width = 29)
        self.pas.grid(row = 2,column = 1,columnspan =2,sticky = W)
        self.pas.insert(0,'Password(No spaces)')
        self.pas.bind('<Button-1>',lambda n: eraseEntry(n,'Password(No spaces)',self.pas,pas = True))


        #Checkbox
        self.intVar= IntVar()
        Checkbutton(body,text = 'I agree with the terms and conditions.',\
            onvalue = 1,offvalue = 0,variable = self.intVar,\
            font = ('Caslon Classico',10,'italic')).\
            grid(row = 3,column = 0,columnspan = 2)
        
        #Button
        Button(body,text = 'Register',font = ('Bembo',10),command = self.register_command).\
        grid(row = 4,sticky = NW)

        #Button
        Button(body,text='Update',font = ('Bembo',10),command = self.update).grid(row =4,column = 2,sticky = NE)
    def query_account(self):
        self.destroy_widgets()
        self.menu()
        self.master.geometry('300x300')
        self.master.title('Query Account')
        #Head Frame
        head = Frame(self.master,height = 35,width = 300)
        head.place(x=0,y=0)

        #Heading
        Label(head,text = 'Query Account',font = ('Bebas Neue',13,'bold')).pack()

        #main frame
        body = Frame(self.master,height = 120,width = 300)
        body.place(x=0,y=36)

        #Label:
        Label(body,text = 'Website:',font = ('Clarendon',11),fg = '#424242').grid(row=0,sticky = E)

        #OptionMenu
        self.website = StringVar()
        self.website.set('Websites')
        self.regWeb = self.allWebsites()
        menu = OptionMenu(body,self.website,*self.regWeb)
        wide = max(map(len,self.regWeb))
        menu.config(width = wide,fg = '#212121')
        menu.grid(row =0,column = 1,columnspan = 2,sticky = W)

        #Button:
        Button(self.master,text='Find',width = 42,bg = '#BFBFBF',bd =0.7,command = self.query).place(x=0,y=75)

        #Text Field
        self.display = Text(self.master,height= 10,width = 290)
        self.display.pack(side = BOTTOM)
    def display_all_accounts(self):
        self.destroy_widgets()
        self.menu()
        self.master.geometry('500x500')
        self.master.title('Display all accounts')
        self.master.resizable(height = True,width = True)
        scroll = Scrollbar(self.master)
        scroll.pack(fill = Y,side = RIGHT)
        self.out_area = Text(self.master,yscrollcommand = scroll.set)
        #self.out_area.configure(yscrollcommand = scroll.set)
        scroll.config(command = self.out_area.yview)
        self.out_area.pack(expand=True, fill='both')
        self.out_area.delete('1.0',END)
        self.out_area.insert('1.0','ALL ACCOUNTS SAVED: -->\n')
        self.out_area.insert('2.0',self.allAccounts())
    def log_out(self):
        self.cur.close()
        self.db.close()
        self.master.destroy()
        try:
            call("lastpass.exe", shell=True)
        except:
            showinfo('BUG','There is a bug when this program was converted to exe.')

        #createWindow()
    def deleteAccount(self):
        self.destroy_widgets()
        self.master.geometry('260x150')
        self.menu()
        head = Frame(self.master,height = 30,width = 260)
        head.pack(side = TOP,fill = X)
        #Label
        Label(head,text = 'Delete',font = ('Impact',14,'underline')).pack(side = LEFT)
        #body
        body = Frame(self.master,height = 150,width = 260)
        body.place(x=0,y=35)
        #Label and OptionMenu
        Label(body,text = 'Website :',font = ('Clarendon',10)).grid(sticky = W)
        items = self.allWebsites()
        self.delWebsite = StringVar()
        self.delWebsite.set(items[0])
        wide = max(map(len,items))
        optM = OptionMenu(body,self.delWebsite,*items)
        optM.config(width = wide)
        optM.grid(row =0,column = 1,columnspan=2,sticky =NW)

        #Checkbox
        self.agree = IntVar()
        Checkbutton(body,text='I want to remove this account.',\
            onvalue = 1,offvalue = 0,variable = self.agree).grid(row = 1,columnspan = 2)
        #Button
        Button(body,text='DELETE',fg='red',command = self.delAcc).grid(row = 2,column=0,sticky = W)

    def rate(self):
        self.destroy_widgets()
        self.master.title('Rate Us')
        self.master.geometry('500x500')
        self.master.config(bg='gray77')
        backG = 'gray77'

        #Heading
        head = Frame(self.master,width = 500,height = 35,bg = backG)
        head.place(x=0,y=0)
        #Frame for check buttons/radiobutton
        body = Frame(self.master,width = 500,height = 170,bg = backG)
        body.place(x=0,y=37)
        #Frame to be packed with a text field:
        text_frame = Frame(self.master,height = 300,width = 500,bg = backG)
        text_frame.place(x=0,y=207)

        #Heading : Rate Us
        Label(head,text = 'Rate',font = ('Impact',15,'underline'),bg = backG).pack(expand = True)

        #label ques
        fontL = ('Century Gothic',12,'italic')
        Label(body,text='Rate',bg=backG,font = fontL).grid(row=0)

        #Radiobtns
        self.btn_list = ['Good','Average','Fine','Bad']
        self.review = IntVar()
        self.review.set(1)
        n=1
        for i in self.btn_list:
            Radiobutton(body,text = i,value = n,variable = self.review,activebackground = backG,bg = backG).grid(row = n,sticky = W)
            n+=1
        #Button:
        Button(body,text='Submit',command = self.send_mail).grid(row =5,sticky = W)
        Button(self.master,text='Quit',command = self.exchange).place(x=60,y=163)
        
        #Text
        self.txt = Text(text_frame)
        self.txt.pack(fill = X,expand = True,side = TOP)
        self.txt.insert('1.0','Please type in a message here and than submit the form.')
    def exchange(self):
        self.master.destroy()
        root = Tk()
        self.__init__(root)
        root.mainloop()

#main = Tk()
#MainRegister(main).rate()
#main.mainloop()

