from tkinter import *
from tkinter.ttk import *

from constants import *


class UI(Tk):
    def __init__(self, transactions, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.transactions = transactions

        self.title(TITLE)

        self.geometry(RESOLUTION)
        self.minsize(*RESOLUTION.split('x'))

        # self.state('zoomed')

        self.frames = {}
        self.current_frame = None
        self.root = Frame(self)
        self.root.pack(fill=BOTH, expand=True)

        for window in (LoginWindow, RegistrationWindow, ProfileWindow):
            self.frames[window] = window(parent=self.root, controller=self)

        self.show_frame(LoginWindow)

    def show_frame(self, page_name):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[page_name]
        self.current_frame.pack(side=TOP, fill=BOTH, expand=True)

    def show_login_frame(self, login, password):
        self.transactions.log_in()


class LoginWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        login = StringVar(self)
        password = StringVar(self)

        self.titleLabel = Label(self,
                                font=FONT_DEFAULT,
                                text="Салон Красоты",
                                justify=CENTER,
                                anchor=CENTER)
        self.titleLabel.pack(expand=True, anchor=S, fill=X)

        self.loginFrame = Frame(self)
        self.loginFrame.pack(expand=True, fill=BOTH)

        self.loginLabel = Label(self.loginFrame,
                                font=FONT_MEDIUM,
                                text=LOGIN_LABEL_TEXT)
        self.loginLabel.pack(expand=True, side=TOP, padx=10)

        self.loginInput = Entry(self.loginFrame,
                                justify=RIGHT,
                                width=50,
                                textvariable=login)
        self.loginInput.pack(expand=True, side=TOP, padx=10)

        self.passwordFrame = Frame(self)
        self.passwordFrame.pack(expand=True, fill=BOTH)

        self.passwordLabel = Label(self.passwordFrame,
                                   font=FONT_MEDIUM,
                                   text="Пароль")
        self.passwordLabel.pack(expand=True, side=TOP, padx=10)

        self.passwordInput = Entry(self.passwordFrame,
                                   width=50,
                                   textvariable=password)
        self.passwordInput.pack(expand=True, side=RIGHT, padx=10)

        self.buttonsFrame = Frame(self)
        self.buttonsFrame.pack(expand=True, fill=BOTH)

        self.loginButton = Button(self.buttonsFrame,
                                  text=LOGIN_BUTTON_TEXT,
                                  command=lambda: self.controller.show_frame(ProfileWindow))
        self.loginButton.pack(expand=True, side=LEFT, padx=10, pady=10)

        self.registrationButton = Button(self.buttonsFrame,
                                         text=REGISTRATION_BUTTON_TEXT,
                                         command=lambda: self.controller.show_frame(RegistrationWindow))
        self.registrationButton.pack(expand=True, side=LEFT, ipadx=10, pady=10)


class RegistrationWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


class ProfileWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.titleLabel = Label(self,
                                font=FONT_DEFAULT,
                                text="Профиль",
                                justify=CENTER,
                                anchor=CENTER)
        self.titleLabel.pack(anchor=CENTER)

        self.loginButton = Button(self,
                                  text=LOGIN_BUTTON_TEXT,
                                  command=lambda: self.controller.show_frame(LoginWindow))
        self.loginButton.pack(expand=True, side=LEFT, pady=10)


class AppointmentWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
