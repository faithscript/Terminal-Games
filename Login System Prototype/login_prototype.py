import tkinter
from tkinter import messagebox
import hashlib 


login_window = tkinter.Tk() #window of the application
login_window.title('Login Systen Prototype')
login_window.geometry('550x550')
login_window.configure(bg='#333333') 


# Password encryption function
def encrypt_password(user_password):
    return hashlib.sha256(user_password.encode()).hexdigest()

# Encrypted user data
user_data = {
            "user1": encrypt_password("password123"),
            "user2": encrypt_password("mypassword"),
            "user3": encrypt_password("passw0rd!"),
            "user4": encrypt_password("qwerty2023"),
            "user5": encrypt_password("letmein456"),
            "user6": encrypt_password("securepass!")
            }

def login_check():
    '''
    Checking if username exists, and password matches
    '''
    username = username_input.get()
    password = password_input.get()
    encrypted_password = encrypt_password(password)

    if username in user_data and user_data[username] == encrypted_password:
        messagebox.showinfo(title='Login Success', message='You logged in successfully.')
    else:
        messagebox.showerror(title='Error', message = 'Invalid Login')




login_frame = tkinter.Frame(bg='#333333')
'''
The widgets needed for the login system
'''
# Login label, greeting and button
login_greeting = tkinter.Label(login_frame, text='Welcome Back!', bg='#333333', fg='#FF3399', font=('Roboto', 40, 'bold'))
login_widget = tkinter.Label(login_frame, text='Enter your details to get started', bg='#333333', fg='#FF3399', font=('Roboto', 15))
login_button = tkinter.Button(login_frame, text='Login', bg='#FF3399', fg='#FFFFFF', font=('Roboto', 12, 'bold'), command=login_check)

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
