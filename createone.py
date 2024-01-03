from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
def signup():
        if email.get()=='' or username.get()=='' or pswd.get()=='' or cpswd.get()=='':
            messagebox.showerror('Error','All Fields are required')
        elif pswd.get() != cpswd.get():
            messagebox.showerror('Error','Password Mismatch.')
        else:
            db=mysql.connector.connect(host='localhost',user='root',password='Siva@123',database='userdata')
            mycursor=db.cursor()
            sql="SELECT * FROM data WHERE username=%s"
            adr = (username.get(), )
            mycursor.execute(sql, adr)
            row = mycursor.fetchone()
            if row !=None:
                messagebox.showerror('Error','Username Already exists')
            else:
                sql1 = "INSERT INTO data (email,username,password) VALUES (%s,%s, %s)"
                val1= (email.get(),username.get(),pswd.get())
                mycursor.execute(sql1, val1)
                db.commit()
                db.close()
                messagebox.showinfo('Success','Registration Successful')
                createone.destroy()
                import loginwindow
def login():
    createone.destroy()
    import loginwindow
createone=Tk()
email=StringVar()
username=StringVar()
pswd=StringVar()
cpswd=StringVar()
logo=ImageTk.PhotoImage(file='C:/pictures/logo.ico')
createone.iconphoto(False,logo)
createone.title('Create new account...')
createone.geometry('1400x700')
img=ImageTk.PhotoImage(file='C:/pictures/background_1400x700.jpg')
imglabel=Label(createone,image=img).place(x=0,y=0)
createoneframe=Frame(createone,width=350,height=450,border=0,bg='white',relief='sunken',highlightthickness=3,highlightbackground='whitesmoke').place(x=500,y=100)
headlabel=Label(createoneframe,text='CREATE AN ACCOUNT',fg='red',bg='white',font=('helvatica',20,'bold')).place(x=517,y=110)
headframe=Frame(createoneframe,height=3,width=350,bg='whitesmoke').place(x=500,y=160)
emaillabel=Label(createoneframe,text='Email',fg='red',bg='white',font=('helvatica',13,'bold')).place(x=550,y=180)
emailentry=Entry(createoneframe,bd=2,width=25,fg='white',bg='darkblue',font=('helvatica',13),textvariable=email).place(x=555,y=210)
userlabel=Label(createoneframe,text='Username',fg='red',bg='white',font=('helvatica',13,'bold')).place(x=550,y=240)
userentry=Entry(createoneframe,bd=2,width=25,fg='white',bg='darkblue',font=('helvatica',13),textvariable=username).place(x=555,y=270)
pswdlabel=Label(createoneframe,text='Password',fg='red',bg='white',font=('helvatica',13,'bold')).place(x=550,y=300)
pswdentry=Entry(createoneframe,bd=2,width=25,fg='white',bg='darkblue',font=('helvatica',13),textvariable=pswd).place(x=555,y=330)
cpswdlabel=Label(createoneframe,text='Confirm Password',fg='red',bg='white',font=('helvatica',13,'bold')).place(x=550,y=360)
cpswdentry=Entry(createoneframe,bd=2,width=25,fg='white',bg='darkblue',show='*',font=('helvatica',13),textvariable=cpswd).place(x=555,y=390)
signupbutton=Button(createoneframe,text='Signup',bd=3,foreground='white',activeforeground='white',background='red',activebackground='red',width=24,font=('helvatica',11,'bold'),command=signup).place(x=557,y=430)
accountlabel=Label(createoneframe,text="Don't have an account?",font=('helvatica',11,'bold'),fg='red',bg='white').place(x=560,y=480)
loginbutton=Button(createoneframe,text='Login',font=('helvatica',11,'bold'),activeforeground='darkblue',foreground='darkblue',background='white',activebackground='white',width=5,bd=0,command=login).place(x=730,y=479)
loginframe=Frame(createoneframe,height=3,width=40,bg='red').place(x=735,y=502)
createone.mainloop()
