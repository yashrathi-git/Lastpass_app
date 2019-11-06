
#-----------IMPORTS------
from tkinter import *
from tkinter.messagebox import showerror,showinfo
import sqlite3
import smtplib
#-------------------------#
class AllCommand:
    def conData(self):
        self.db = sqlite3.connect('Database.db')
        self.cur = self.db.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS users(website TEXT,username TEXT,password TEXT)')
        self.cur.execute('SELECT * FROM users')
        d = self.cur.fetchall()
        if len(d) == 0:
            self.cur.execute('INSERT INTO users VALUES ("joe.com","joe@doe.in","joeMM")')
    def get_data(self,name):
        self.cur.execute('SELECT * FROM users WHERE website = ?',(name,))
        data = self.cur.fetchall()
        return data
    def register_command(self):
        web = self.name.get().replace(' ','') + self.domain.get()
        username = self.usn.get().replace(' ','')
        password = self.pas.get().replace(' ','')
        status = (self.intVar.get() ==1)
        if self.name.get() == 'Website (No spaces)' or\
        self.name.get().replace(' ','') == '' or\
        username == 'Username/email(No spaces)' or\
        username == '' or\
        password == 'Password(No spaces)' or\
        password == '' or\
        status == False:
            showerror('Error','Please make sure to fill everything and agree with the terms and conditions.')
            return None
        if len(self.get_data(web)) == 1:
            msg = f"The website you are trying to use already exists.\
            \nIf you want to register another account with the same website -\
            \n• Use {self.name.get()}1{self.domain.get()} to register multiple account"
            showinfo('Website Exists',msg)
            return None
        try:
            self.cur.execute('INSERT INTO users VALUES(?,?,?)',(web.lower(),username,password))
            self.db.commit()
        except:
            showerror('Unknown Error','Unknown error occured while uploading data.')
        else:
            msg = 'Following data successfully uploaded to database:\n'+\
                f'•Website : {web.lower()}\n'+\
                f'•Username/Email : {username}\n'+\
                f'•Password : {password}'
            showinfo('Successful',msg)

    
    def allWebsites(self):
        self.conData()
        self.cur.execute('SELECT website FROM users')
        return list(map(lambda n : n[0],self.cur.fetchall()))
    def query(self):
        web = self.website.get()
        if web == 'Websites':
            showerror('Error','Please select a website first.')
            return None
        info = self.get_data(web)[0]
        self.display.delete('1.0',END)
        self.display.insert('1.0','-----RESULT-----\n')
        self.display.insert('2.0',f'1. Website : {info[0]}\n')
        self.display.insert('3.0',f'2. Email : {info[1]}\n')
        self.display.insert('4.0',f'3. Password : {info[2]}\n')
        self.display.insert('5.0','-----------------')
    def allAccounts(self):
        self.cur.execute('SELECT * FROM users')
        data = self.cur.fetchall()
        result = ''
        for i in data:
            result += f'Website  : {i[0]}\n'
            result += f'Email    : {i[1]}\n'
            result += f'Password : {i[2]}\n'
            result += '---------------------\n'
        return result
    def delAcc(self):
        web = self.delWebsite.get()
        status = (self.agree.get() == 1)
        if status is False:
            showerror('Error','Please make sure to agree with terms of deletion of account.')
            return None
        self.cur.execute('DELETE FROM users WHERE website = ?',(web,))
        self.db.commit()
        showinfo('Deleted successfully',f'{web} account have been deleted.')
        self.deleteAccount()
    def update(self):
        web = self.name.get().replace(' ','') + self.domain.get()
        username = self.usn.get().replace(' ','')
        password = self.pas.get().replace(' ','')
        status = (self.intVar.get() ==1)
        if self.name.get() == 'Website (No spaces)' or\
        self.name.get().replace(' ','') == '' or\
        username == 'Username/email(No spaces)' or\
        username == '' or\
        password == 'Password(No spaces)' or\
        password == '' or\
        status == False:
            showerror('Error','Please make sure to fill everything and agree with the terms and conditions.')
            return None
        data= self.get_data(web)
        if len(data) == 0:
            showinfo('No account with that website',f'No account exists with website : {web}')
            return None
        try:
            self.cur.execute('UPDATE users SET username =?,password=? WHERE website = ?',(username,password,web))
            self.db.commit()
        except:
            showerror('DATABASE ERROR','SQLite error occured.')
        else:
            showinfo('Successful','Successfully updated. New information: '+\
                f'\n•Website        : {web}'+\
                f'\n•Email/username : {username}'+\
                f'\n•Password       : {password}')
    def send_mail(self):
        head = self.btn_list[self.review.get()-1]
        content = self.txt.get('1.0',END)
        try:
            obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            obj.ehlo()
            #obj.starttls()
            obj.login('richardebright1234@hotmail.com','fr$ap3xp%dWP.?4')
            obj.sendmail('yashrathicricket@gmail.com','richardebright1234@hotmail.com',f'Subject:\nREVIEW : {head}\n{content}')
            obj.quit()
        except:
            showinfo('No Internet','Looks like you are dis-connected to internet. Try again after connection is established.')
        else:
            showinfo('Successful','Successfully! Submitted your review')
        finally:
            self.exchange()
#def createWindow():
    #main = Tk()
    #AskPass(main)
    #main.mainloop()