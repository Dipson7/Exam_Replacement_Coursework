from tkinter import *
import smtplib
import random

# main window for login page
login = Tk()


# window for signup page
def signup_page():
    signup = Toplevel()

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

user = Label(login, text='Username').pack()
user_ent = Entry(login, textvariable=username).pack()

passw = Label(login, text='Password').pack()
passw_ent = Entry(login, show="*", text=password).pack()


def show():
    passw2 = Label(login, text=password.get()).pack()
    passw3 = Label(login, text=username.get()).pack()


b_login = Button(login, text='Login', command=show).pack()
b_signup = Button(login, text='Signup', command=signup_page).pack()

login.mainloop()
