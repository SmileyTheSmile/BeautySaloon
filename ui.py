from tkinter import *
from tkinter.ttk import *

from constants import *


class UI(Tk):
    def __init__(self, transactions, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.transactions = transactions

        self.title(TITLE)
        self.resizable(False, False)

        self.frames = {}
        self.current_frame = None
        self.root = Frame(self)
        self.root.pack(fill=BOTH, expand=True)

        for window in (LoginWindow, RegistrationWindow, ProfileWindow, AppointmentWindow):
            self.frames[window] = window(parent=self.root, controller=self)

        self.show_login_frame()

    def show_frame(self, page_name):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[page_name]
        self.current_frame.pack(side=TOP, fill=BOTH, expand=True)

    def show_login_frame(self):
        self.geometry(LOGIN_WINDOW_RESOLUTION)
        self.show_frame(LoginWindow)

    def show_registration_frame(self):
        self.geometry(REGISTRATION_WINDOW_RESOLUTION)
        self.show_frame(RegistrationWindow)

    def show_profile_frame(self, login, password):
        # self.transactions.log_in()
        self.show_frame(ProfileWindow)

    def register_user(self, **kwargs):
        self.show_frame(ProfileWindow)

    def show_appointment_frame(self):
        self.show_frame(AppointmentWindow)


class LoginWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        login = StringVar(self)
        password = StringVar(self)

        self.title_label = Label(self,
                                 font=FONT_DEFAULT,
                                 text=LOGIN_TITLE_LABEL_TEXT,
                                 justify=CENTER,
                                 anchor=CENTER)
        self.title_label.pack(expand=True, anchor=S, fill=X)

        self.login_frame = Frame(self)
        self.login_label = Label(self.login_frame,
                                 font=FONT_MEDIUM,
                                 text=LOGIN_LABEL_TEXT)
        self.login_label.pack(expand=True, side=TOP, padx=10)

        self.login_input = Entry(self.login_frame,
                                 justify=RIGHT,
                                 width=50,
                                 textvariable=login)
        self.login_input.pack(expand=True, side=TOP, padx=10)
        self.login_frame.pack(expand=True, fill=BOTH)

        self.password_frame = Frame(self)
        self.password_label = Label(self.password_frame,
                                    font=FONT_MEDIUM,
                                    text=PASSWORD_LABEL_TEXT)
        self.password_label.pack(expand=True, side=TOP, padx=10)

        self.password_input = Entry(self.password_frame,
                                    width=50,
                                    textvariable=password)
        self.password_input.pack(expand=True, side=RIGHT, padx=10)
        self.password_frame.pack(expand=True, fill=BOTH)

        self.buttons_frame = Frame(self)
        self.login_button = Button(self.buttons_frame,
                                   text=LOGIN_BUTTON_TEXT,
                                   command=lambda: self.controller.show_profile_frame(login=login.get(),
                                                                                      password=password.get()))
        self.login_button.pack(expand=True, side=LEFT, padx=10, pady=10)

        self.registration_button = Button(self.buttons_frame,
                                          text=REGISTRATION_BUTTON_TEXT,
                                          command=lambda: self.controller.show_registration_frame())
        self.registration_button.pack(expand=True, side=LEFT, ipadx=10, pady=10)
        self.buttons_frame.pack(expand=True, fill=BOTH)


class RegistrationWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        name = StringVar(self)
        surname = StringVar(self)
        last_name = StringVar(self)
        address = StringVar(self)
        email = StringVar(self)
        phone_number = StringVar(self)
        date_of_birth = StringVar(self)
        login = StringVar(self)
        password = StringVar(self)
        password_confirmation = StringVar(self)

        labels_width = 20
        inputs_width = 50

        title_label = Label(self,
                            font=FONT_DEFAULT,
                            text=REGISTRATION_TITLE_LABEL_TEXT,
                            justify=CENTER,
                            anchor=CENTER)
        title_label.pack(expand=True, anchor=S, fill=X)

        name_frame = Frame(self)
        name_label = Label(name_frame,
                           font=FONT_MEDIUM,
                           text=NAME_LABEL_TEXT,
                           width=labels_width)
        name_label.pack(expand=True, side=LEFT)

        name_input = Entry(name_frame,
                           width=inputs_width,
                           textvariable=name)
        name_input.pack(expand=True, side=RIGHT)
        name_frame.pack(expand=True, fill=BOTH)

        surname_frame = Frame(self)
        surname_label = Label(surname_frame,
                              font=FONT_MEDIUM,
                              text=SURNAME_LABEL_TEXT,
                              width=labels_width)
        surname_label.pack(expand=True, side=LEFT)

        surname_input = Entry(surname_frame,
                              width=inputs_width,
                              textvariable=surname)
        surname_input.pack(expand=True, side=RIGHT)
        surname_frame.pack(expand=True, fill=BOTH)

        last_name_frame = Frame(self)
        last_name_label = Label(last_name_frame,
                                font=FONT_MEDIUM,
                                text=LAST_NAME_LABEL_TEXT,
                                width=labels_width)
        last_name_label.pack(expand=True, side=LEFT)

        last_name_input = Entry(last_name_frame,
                                width=inputs_width,
                                textvariable=last_name)
        last_name_input.pack(expand=True, side=RIGHT)
        last_name_frame.pack(expand=True, fill=BOTH)

        address_frame = Frame(self)
        address_label = Label(address_frame,
                              font=FONT_MEDIUM,
                              text=ADDRESS_LABEL_TEXT,
                              width=labels_width)
        address_label.pack(expand=True, side=LEFT)

        address_input = Entry(address_frame,
                              width=inputs_width,
                              textvariable=address)
        address_input.pack(expand=True, side=RIGHT)
        address_frame.pack(expand=True, fill=BOTH)

        email_frame = Frame(self)
        email_label = Label(email_frame,
                            font=FONT_MEDIUM,
                            text=EMAIL_LABEL_TEXT,
                            width=labels_width)
        email_label.pack(expand=True, side=LEFT)

        email_input = Entry(email_frame,
                            width=inputs_width,
                            textvariable=email)
        email_input.pack(expand=True, side=RIGHT)
        email_frame.pack(expand=True, fill=BOTH)

        phone_number_frame = Frame(self)
        phone_number_label = Label(phone_number_frame,
                                   font=FONT_MEDIUM,
                                   text=PHONE_NUMBER_LABEL_TEXT,
                                   width=labels_width)
        phone_number_label.pack(expand=True, side=LEFT)

        phone_number_input = Entry(phone_number_frame,
                                   width=inputs_width,
                                   textvariable=phone_number)
        phone_number_input.pack(expand=True, side=RIGHT)
        phone_number_frame.pack(expand=True, fill=BOTH)

        date_of_birth_frame = Frame(self)
        date_of_birth_label = Label(date_of_birth_frame,
                                    font=FONT_MEDIUM,
                                    text=PHONE_NUMBER_LABEL_TEXT,
                                    width=labels_width)
        date_of_birth_label.pack(expand=True, side=LEFT)

        date_of_birth_input = Entry(date_of_birth_frame,
                                    width=inputs_width,
                                    textvariable=date_of_birth)
        date_of_birth_input.pack(expand=True, side=RIGHT)
        date_of_birth_frame.pack(expand=True, fill=BOTH)

        login_frame = Frame(self)
        login_label = Label(login_frame,
                                    font=FONT_MEDIUM,
                                    text=LOGIN_LABEL_TEXT,
                                    width=labels_width)
        login_label.pack(expand=True, side=LEFT)

        login_input = Entry(login_frame,
                                    width=inputs_width,
                                    textvariable=date_of_birth)
        login_input.pack(expand=True, side=RIGHT)
        login_frame.pack(expand=True, fill=BOTH)

        password_frame = Frame(self)
        password_label = Label(password_frame,
                                    font=FONT_MEDIUM,
                                    text=PASSWORD_LABEL_TEXT,
                                    width=labels_width)
        password_label.pack(expand=True, side=LEFT)

        password_input = Entry(password_frame,
                                    width=inputs_width,
                                    textvariable=date_of_birth)
        password_input.pack(expand=True, side=RIGHT)
        password_frame.pack(expand=True, fill=BOTH)

        password_confirmation_frame = Frame(self)
        password_confirmation_label = Label(password_confirmation_frame,
                                    font=FONT_MEDIUM,
                                    text=PASSWORD_CONFIRMATION_LABEL_TEXT,
                                    width=labels_width)
        password_confirmation_label.pack(expand=True, side=LEFT)

        password_confirmation_input = Entry(password_confirmation_frame,
                                    width=inputs_width,
                                    textvariable=date_of_birth)
        password_confirmation_input.pack(expand=True, side=RIGHT)
        password_confirmation_frame.pack(expand=True, fill=BOTH)

        buttons_frame = Frame(self)
        register_button = Button(buttons_frame,
                                 text=REGISTRATION_BUTTON_TEXT,
                                 command=lambda: self.controller.register_user())
        register_button.pack(expand=True, side=LEFT, padx=10, pady=10)

        back_button = Button(buttons_frame,
                             text=BACK_BUTTON_TEXT,
                             command=lambda: self.controller.show_login_frame())
        back_button.pack(expand=True, side=LEFT, ipadx=10, pady=10)
        buttons_frame.pack(expand=True, fill=BOTH)


class ProfileWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.titleLabel = Label(self,
                                font=FONT_DEFAULT,
                                text=PROFILE_TITLE_LABEL_TEXT,
                                justify=CENTER,
                                anchor=CENTER)
        self.titleLabel.pack(anchor=CENTER)

        self.loginButton = Button(self,
                                  text=BACK_BUTTON_TEXT,
                                  command=lambda: self.controller.show_login_frame())
        self.loginButton.pack(expand=True, side=LEFT, pady=10)


class AppointmentWindow(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
