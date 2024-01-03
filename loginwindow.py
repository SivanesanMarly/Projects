from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
class admission:
    def login(self):
        if username.get()=='' or password.get()=='':
            messagebox.showerror('Error','All Fields are Required.')
        else:
            db=mysql.connector.connect(host='localhost',user='root',password='Siva@123',database='userdata')
            mycursor=db.cursor()
            sql="SELECT * FROM data WHERE username=%s and password=%s"
            adr = (username.get(), password.get(),)
            mycursor.execute(sql, adr)
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error','Invalid Username and Password.')
            else:
                messagebox.showinfo('Welcome','Login is Successful.')
                loginwindow.destroy()
                import collegeapplication
    def forgetpswd(self):
        loginwindow.destroy()
        import forgetpassword
    def userentry(self,event):
        if userentry.get()=='Username':
            userentry.delete(0,END)
    def pswdentry(self,event):
        if pswdentry.get()=='Password':
            pswdentry.delete(0,END)
    def createone(self):
        loginwindow.destroy()
        import createone
loginwindow=Tk()
a=admission()
username=StringVar()
username.set(username.get().upper())
password=StringVar()
logo=ImageTk.PhotoImage(file='C:/pictures/logo.ico')
loginwindow.iconphoto(False,logo)
loginwindow.title('Login...')
loginwindow.geometry('1400x700')
img=ImageTk.PhotoImage(file='C:/pictures/images_1400x700.jpeg')
imglabel=Label(loginwindow,image=img).place(x=0,y=0)
loginframe=Frame(loginwindow,width=350,height=450,border=0,bg='white',relief='sunken',highlightthickness=3,highlightbackground='whitesmoke').place(x=500,y=100)
imgframe=ImageTk.PhotoImage(file='C:/pictures/fbg70_70.jpg')
imglabel1=Label(loginframe,image=imgframe).place(x=520,y=110)
headlabel=Label(loginframe,text='SS College of \nArts and Engineering,\nTrichy,Tamilnadu',font=('courier',14,'bold'),bg='white',fg='red').place(x=600,y=113)
headframe=Frame(loginframe,height=3,width=350,bg='whitesmoke').place(x=500,y=190)
loginlabel=Label(loginframe,text='USER LOGIN',font=('helvatica',20,'bold'),bg='white',fg='red').place(x=580,y=205)
userentry=Entry(loginframe,font=('helvetica',15),width=18,bd=0,fg='darkblue',textvariable=username)
userentry.insert(0,'Username')
userentry.bind('<FocusIn>',a.userentry)
userentry.place(x=560,y=280)
userframe=Frame(loginframe,width=230,height=3,bg='red').place(x=560,y=305)
pswdentry=Entry(loginframe,font=('helvetica',15),width=18,bd=0,show='*',fg='darkblue',textvariable=password)
pswdentry.insert(0,'Password')
pswdentry.bind('<FocusIn>',a.pswdentry)
pswdentry.place(x=560,y=330)
pswdframe=Frame(loginframe,width=230,height=3,bg='red').place(x=560,y=355)
forgetbutton=Button(loginframe,text='Forget Password?',foreground='red',background='white',activeforeground='red',activebackground='white',bd=0,font=('helvatica',11,'bold'),command=a.forgetpswd).place(x=670,y=360)
loginbutton=Button(loginframe,text='Login',foreground='white',background='red',activeforeground='white',activebackground='red',bd=3,font=('helvatica',11,'bold'),width=25,command=a.login).place(x=560,y=400)
orlabel=Label(loginframe,text='-------------- OR --------------',fg='red',bg='white',font=('helvatica',15)).place(x=557,y=450)
accountlabel=Label(loginframe,text="Don't have an account?",font=('helvatica',11,'bold'),fg='red',bg='white').place(x=557,y=485)
createonebutton=Button(loginframe,text='Create One',font=('helvatica',11,'bold'),activeforeground='darkblue',foreground='darkblue',background='white',activebackground='white',width=9,bd=0,command=a.createone).place(x=730,y=484)
createoneframe=Frame(loginframe,height=3,width=78,bg='red').place(x=730,y=505)
loginwindow.mainloop()
