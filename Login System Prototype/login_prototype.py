import tkinter
from tkinter import messagebox


login_window = tkinter.Tk() #window of the application
login_window.title('Login Systen Prototype')
login_window.geometry('550x550')
login_window.configure(bg='#333333') 

def login():
    user_data = {
                "user1": "password123",
                "user2": "mypassword",
                "user3": "passw0rd!",
                "user4": "qwerty2023",
                "user5": "letmein456",
                "user6": "securepass!"
                }
    for username, password in user_data.items():
        if username_input.get() == username and password_input.get() == password:
            messagebox.showinfo(title='Login Success', message='You logged in successfully.')
        else:
            messagebox.showerror(title='Error', message='Invalid login.')
        break



login_frame = tkinter.Frame(bg='#333333')
'''
The widgets needed for the login system
'''
# Login label, greeting and button
login_greeting = tkinter.Label(login_frame, text='Welcome Back!', bg='#333333', fg='#FF3399', font=('Roboto', 40, 'bold'))
login_widget = tkinter.Label(login_frame, text='Enter your details to get started', bg='#333333', fg='#FF3399', font=('Roboto', 15))
login_button = tkinter.Button(login_frame, text='Login', bg='#FF3399', fg='#FFFFFF', font=('Roboto', 12, 'bold'), command=login)

# Username and password labels and buttons
username_widget = tkinter.Label(login_frame, text='Username', bg='#333333', fg='#FFFFFF', font=('Roboto', 12))
password_widget = tkinter.Label(login_frame, text='Password', bg='#333333', fg='#FFFFFF', font=('Roboto', 12))

username_input = tkinter.Entry(login_frame, font=('Roboto', 12))
password_input =tkinter.Entry(login_frame, show='*', font=('Roboto', 12))



# Displaying widgets on the UI
login_greeting.grid(row=0, column=0, columnspan=4, sticky='w', pady=(200,2))
login_widget.grid(row=1, column=0, columnspan=4, sticky='w', pady=(0,30))
username_widget.grid(row=2, column=0, sticky='w')
password_widget.grid(row=4, column=0, sticky='w')

username_input.grid(row=3, column=0,columnspan=4, sticky='w', pady=(0, 15))
password_input.grid(row=5, column=0,columnspan=4, sticky='w', pady=(0, 15))

login_button.grid(row=6, column=0, sticky='w', pady=10)

login_frame.pack()

login_window.mainloop()
