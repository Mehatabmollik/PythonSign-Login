from tkinter import*
from tkinter import messagebox

window=Tk()
window.geometry('655x333')
window.title('LoVeLink Login')

#creating labels
username=Label(text='Username :').grid(row=0,column=0)

password=Label(text='Password :').grid(row=1,column=0)

#creating entry fields
username_entry=Entry(width=30)
username_entry.grid(row=0,column=1)

password_entry=Entry(width=30)
password_entry.grid(row=1,column=1)

#create login button function
def login():
    username=username_entry.get()
    password=password_entry.get()

    if (username)=="" or (password)=="":
        messagebox.showerror(title="Error",message='Please fill in all fields.')
    elif (username)!="Shadiuser" or (password)!="Password":
        messagebox.showerror(title="Error",message='Invaild username or password')
    else:
        messagebox.showinfo(title="Success",message='Login successfull')
#creating login button
login_button=Button(text='Login',command=login).grid(row=2,column=1)

        
window.mainloop()
