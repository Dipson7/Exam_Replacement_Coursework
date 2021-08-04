from tkinter import *
import smtplib
import random

# merge

# main window for login page
login = Tk()
login.geometry('1366x768')


# window for signup page
def signup_page():
    signup = Toplevel()
    signup.state('zoomed')

    # variables to store user input
    firstname = StringVar()
    firstname.set('First Name')
    lastname = StringVar()
    lastname.set('Last Name')
    email = StringVar()
    email.set('XYZ@gmail.com')
    s_password = StringVar()
    s_password.set('Password')

    # function that send an OTP to the user inputted email
    def sign_click():
        s = smtplib.SMTP('smtp.gmail.com', 587)  # (host domain , port)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login("theggserver@gmail.com", "@ppleWas01")
        a = random.randint(250000, 999999)  # OTP Generator of 6 digit number
        # Message sent to user
        message = f'Your OTP code is {a}.\n And your Password,First and last Name are\n First Name: {firstname.get()}\nLast Name: {lastname.get()}\nPassword: {s_password.get()} '

        # sending the mail
        try:
            s.sendmail("theggserver@gmail.com", email.get(), message)
            s.quit()  # stops the protocol

            otp = StringVar()
            otp.set('123456')

            # checks if opt user entered is correct
            def check_otp():
                if otp.get() == str(a):
                    success = Label(signup, text='Successful').pack()
                else:
                    Label(signup, text='Unsuccessful').pack()

            l_check_otp = Label(signup, text='Enter the OTP').pack()
            Otp_entry = Entry(signup, text=otp).pack()
            b_opt = Button(signup, text='Conform', command=check_otp).pack()
        except:
            # if user input email is incorrect notifies the user
            s.quit()
            check_email = Label(signup, text='Wrong email, Please check your email address').pack()

    l_first_name = Label(signup, text='First Name').pack()
    e_first_name = Entry(signup, text=firstname).pack()

    l_last_name = Label(signup, text='Last Name').pack()
    e_last_name = Entry(signup, text=lastname).pack()

    l_pass_name = Label(signup, text='Password').pack()
    e_pass_name = Entry(signup, text=s_password, show='*').pack()

    l_email_name = Label(signup, text='First Name').pack()
    e_email_name = Entry(signup, text=email).pack()

    bs_signup = Button(signup, text='Signup', command=sign_click).pack()
    signup.mainloop()


username = StringVar()
username.set('Username')
password = StringVar()
password.set('Password')

user = Label(login, text='Username', font=('Arial', 15)).place(x=405, y=366)
user_ent = Entry(login, textvariable=username, font=('Arial', 20)).place(x=405, y=396, width=468, height=89)

passw = Label(login, text='Password', font=('Arial', 15)).place(x=405, y=505,)
passw_ent = Entry(login, show="*", text=password, font=('Arial', 20)).place(x=405, y=535, width=468, height=89)

b_login = Button(login, text='Login', ).place(x=451, y=656, width=145, height=57)
b_signup = Button(login, text='Signup', command=signup_page).place(x=683, y=656, width=145, height=57)

login.mainloop()
