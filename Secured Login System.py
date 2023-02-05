from tkinter import *
import hashlib
from firebase import firebase

registration_window=Tk()
registration_window.geometry("400x400")
registration_window.config(bg="teal")

firebase = firebase.FirebaseApplication("https://c188-login-system-default-rtdb.firebaseio.com/",None)

login_username_entry = ''
login_password_entry = ''
username_entry = ''
password_entry = ''

def login():
    print("Login Function")
    
def registration():
    username = username_entry.get()
    password = password_entry.get()
    
    encrypted = hashlib.md5(password.encode())
    hex_data = encrypted.hexdigest()
    print(hex_data)
    firebase.put("https://c188-login-system-default-rtdb.firebaseio.com/",username,hex_data)
    messagebox.showinfo("Success","User has been registered!")
    
def login_window():
    global login_password_entry
    global login_username_entry
    registration_window.destroy()
    
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.config(bg="turquoise")
    
    login_heading = Label(login_window,text="Log In",bg="turquoise",font=("Roboto",20,"bold"),fg="blue")
    login_heading.place(relx=0.5,rely=0.1,anchor=CENTER)
    
    login_username_label = Label(login_window,text="Username: ",bg="turquoise",fg="blue",font=("Roboto",15,"bold"))
    login_username_label.place(relx=0.4,rely=0.4)
    
    login_pwd_label = Label(login_window,text="Password:",bg="Turquoise",fg="blue",font=("Roboto",15,"bold"))
    login_pwd_label.place(relx=0.4,rely=0.5,anchor=W)
    
    login_username_entry = Entry(login_window,font=("Roboto",15,"bold"))
    login_username_entry.place(relx=0.6,rely=0.4,anchor=CENTER)
    
    login_password_entry = Entry(login_window,font=("Roboto",15,"bold"))
    login_password_entry.place(relx=0.6,rely=0.5,anchor=CENTER)
    
    login_button = Button(login_window,text="Log In",font=("Roboto",17,"bold"),relief=FLAT,bg="teal",fg="skyblue")
    login_button.place(relx=0.5,rely=0.7,anchor=CENTER)
    
    login_window.mainloop()
    
heading = Label(registration_window,text="Sign Up",font=("Roboto",20,"bold"),bg="teal",fg="skyblue")
heading.place(relx=0.5,rely=0.1,anchor=CENTER)

username_label = Label(registration_window,text="Username:",bg="teal",fg="skyblue",font=("Roboto",15,"bold"))
username_label.place(relx=0.4,rely=0.4,anchor=CENTER)

password_label = Label(registration_window,text="Password: ",bg="Teal",fg="skyblue",font=("Roboto",15,"bold"))
password_label.place(relx=0.4,rely=0.5,anchor=CENTER)

username_entry = Entry(registration_window,font=("Roboto",15,"bold"))
username_entry.place(relx=0.6,rely=0.4,anchor=CENTER)

password_entry = Entry(registration_window,font=("Roboto",15,"bold"))
password_entry.place(relx=0.6,rely=0.5,anchor=CENTER)

register_btn = Button(registration_window,text="Sign Up",bg="turquoise",fg="navyblue",font=("Roboto",17,"bold"),relief=FLAT,command=registration)
register_btn.place(relx=0.5,rely=0.7,anchor=CENTER)

loginWindowBtn = Button(registration_window,text="Log In",bg="Turquoise",fg="navyblue",relief=FLAT,font=("Roboto",13,"bold"),command=login_window)
loginWindowBtn.place(relx=0.8,rely=0.1,anchor=CENTER)

registration_window.mainloop()