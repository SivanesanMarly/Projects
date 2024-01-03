from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
def submit():
        if username.get()=='' or pswd.get()=='' or cpswd.get()=='':
            messagebox.showerror('Error','All Fields are Required.')
        elif pswd.get()!=cpswd.get():
            messagebox.showerror('Error','Password Mismatch.')
        else:
            db=mysql.connector.connect(host='localhost',user='root',password='Siva@123',database='userdata')
            mycursor=db.cursor()
            sql="SELECT * FROM data WHERE username=%s"
            adr = (username.get(),)
            mycursor.execute(sql, adr)
            row = mycursor.fetchone()
            if row ==None:
                messagebox.showerror('Error','Incorrect Username.')
            else:
                db=mysql.connector.connect(host='localhost',user='root',password='Siva@123',database='userdata')
                mycursor=db.cursor()
                sql="UPDATE data SET password=%s WHERE username=%s"
                val=(pswd.get(),username.get())
                mycursor.execute(sql,val)
                db.commit()
                db.close()
                messagebox.showinfo('Success','Password is reset,Please login with new password.')
                forgetpswd.destroy()
                import loginwindow
def login():
    forgetpswd.destroy()
    import loginwindow
forgetpswd=Tk()
username=StringVar()
pswd=StringVar()
cpswd=StringVar()
logo=ImageTk.PhotoImage(file='C:/pictures/logo.ico')
forgetpswd.iconphoto(False,logo)
forgetpswd.title('Create new account...')
forgetpswd.geometry('1400x700')
img=ImageTk.PhotoImage(file='C:/pictures/background_1400x700.jpg')
imglabel=Label(forgetpswd,image=img).place(x=0,y=0)
forgetpswdframe=Frame(forgetpswd,width=350,height=450,border=0,bg='white',relief='sunken',highlightthickness=3,highlightbackground='whitesmoke').place(x=500,y=100)
headlabel=Label(forgetpswdframe,text='RESET PASSWORD',fg='red',bg='white',font=('helvatica',20,'bold')).place(x=540,y=110)
headframe=Frame(forgetpswdframe,height=3,width=350,bg='whitesmoke').place(x=500,y=160)
userlabel=Label(forgetpswdframe,text='Username',fg='red',bg='white',font=('helvatica',15,'bold')).place(x=550,y=200)
userentry=Entry(forgetpswdframe,bd=2,width=21,fg='white',bg='darkblue',font=('helvatica',15),textvariable=username).place(x=555,y=235)
pswdlabel=Label(forgetpswdframe,text='Password',fg='red',bg='white',font=('helvatica',15,'bold')).place(x=550,y=270)
pswdentry=Entry(forgetpswdframe,bd=2,width=21,fg='white',bg='darkblue',font=('helvatica',15),textvariable=pswd).place(x=555,y=305)
cpswdlabel=Label(forgetpswdframe,text='Confirm Password',fg='red',bg='white',font=('helvatica',15,'bold')).place(x=550,y=340)
cpswdentry=Entry(forgetpswdframe,bd=2,width=21,fg='white',bg='darkblue',show='*',font=('helvatica',15),textvariable=cpswd).place(x=555,y=375)
submitbutton=Button(forgetpswdframe,text='Submit',bd=3,foreground='white',activeforeground='white',background='red',activebackground='red',width=25,font=('helvatica',11,'bold'),command=submit).place(x=555,y=430)
accountlabel=Label(forgetpswdframe,text="Don't have an account?",font=('helvatica',11,'bold'),fg='red',bg='white').place(x=560,y=480)
loginbutton=Button(forgetpswdframe,text='Login',font=('helvatica',11,'bold'),activeforeground='darkblue',foreground='darkblue',background='white',activebackground='white',width=5,bd=0,command=login).place(x=730,y=479)
loginframe=Frame(forgetpswdframe,height=3,width=40,bg='red').place(x=735,y=502)
forgetpswd.mainloop()
