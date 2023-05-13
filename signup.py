from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser


def submit():
    user_name = name_entry.get()
    password = password_entry.get()
    confirmed_password = confirm_password_entry.get()

    valid_characters = set(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-')

    for char in user_name:
        if char not in valid_characters:
            messagebox.showerror(title='Invalid username',
                                 message='Please enter a valid username')

    if (password != confirmed_password):
        messagebox.showerror(title='Password not confirmed',
                             message='Please Confirm the password correctly')
    elif (user_name == ''):
        messagebox.showerror(title='Empty username',
                             message='Please enter a username')
    elif (len(user_name) < 4):
        messagebox.showerror(title='Short Username',
                             message='Username must be atleast 4 characters')
    elif (password == ''):
        messagebox.showerror(title='Empty password',
                             message='Please enter a password')
    elif (len(password) < 4):
        messagebox.showerror(title='short password',
                             message='Passwords must be atleast 4 characters')
    else:
        answer = messagebox.askyesnocancel(
            title='Confirm to sign up', message='Are you sure to sign up?')
        if answer == True:
            next_window = Tk()
            next_window.geometry('430x400')
            next_window.resizable(False, False)
            finishing_label = Label(next_window,
                                    text='Welcome '+user_name +
                                    ' !. Your signing up process has been completed successfully. Remember Your password is '+password,
                                    wraplength=400,
                                    font=('comic sans', 15, 'bold')
                                    )

            finishing_label.place(relx=0.5, rely=0.5, anchor=CENTER)

            window.destroy()
            next_window.mainloop()
        if answer == False:
            window.destroy()


def clear():
    name_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)


def cancel():
    window.destroy()


def eyeclicked():
    password = password_entry.get()
    current_show_value = password_entry.cget('show')
    if current_show_value == '':
        password_entry.config(text=password, show='*')
    else:
        password_entry.config(text=password, show='')


def eyeclicked2():
    confirmed_password = confirm_password_entry.get()
    current_show_value = confirm_password_entry.cget('show')
    if current_show_value == '':
        confirm_password_entry.config(text=confirmed_password, show='*')
    else:
        confirm_password_entry.config(text=confirmed_password, show='')


def theme_changer():
    color = colorchooser.askcolor()
    window.config(bg=color[1])
    frame1.config(bg=color[1])
    frame2.config(bg=color[1])
    header_label.config(bg=color[1])


window = Tk()
window.geometry('430x400')
window.resizable(False, False)

header_label = Label(window,
                     text='Please Enter your User name and password to continue the signing up process!',
                     font=('comic sans', 14, 'bold'),
                     wraplength=400,
                     padx=20,
                     pady=40
                     )
header_label.pack()

frame1 = Frame(window)
frame1.pack()

name_label = Label(frame1,
                   text='User name',
                   anchor=W
                   )


name_entry = Entry(frame1,
                   )

password_label = Label(frame1,
                       text='Password'
                       )


password_entry = Entry(frame1,
                       show='*'
                       )
eye_image = PhotoImage(file='Reminding\eye.png')
eye_image = eye_image.subsample(16)

eye_button = Button(frame1,
                    image=eye_image,
                    bd=0,
                    command=eyeclicked)

confirm_password_label = Label(frame1,
                               text='Confirm Password'
                               )


confirm_password_entry = Entry(frame1,
                               show='*'
                               )

eye_image2 = PhotoImage(file='Reminding\eye.png')
eye_image2 = eye_image2.subsample(16)

eye_button2 = Button(frame1,
                     image=eye_image,
                     bd=0,
                     command=eyeclicked2
                     )


theme_button = Button(frame1,
                      text='Change Theme',
                      command=theme_changer)


name_label.grid(row=0, column=0, padx=10, pady=10)

name_entry.grid(row=0, column=1, padx=10, pady=10)

password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry.grid(row=1, column=1, padx=10, pady=10)

eye_button.grid(row=1, column=2, padx=10, pady=10)

confirm_password_label.grid(row=2, column=0, padx=10, pady=10)

confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

eye_button2.grid(row=2, column=2, padx=10, pady=10)

theme_button.grid(row=4, column=1, padx=10, pady=10)

frame2 = Frame(window,
               pady=50)
frame2.pack()

submit_button = Button(frame2,
                       text='Submit',
                       command=submit)

clear_button = Button(frame2,
                      text='Clear',
                      command=clear)

cancel_button = Button(frame2,
                       text='Cancel',
                       command=cancel)


submit_button.grid(row=0, column=0, padx=20)

clear_button.grid(row=0, column=1, padx=20)

cancel_button.grid(row=0, column=2, padx=20)


window.mainloop()
