from tkinter import *
from tkinter.ttk import *

from constants import ProfileWindowText as PWT
from constants import RegistrationWindowText as RWT
from constants import LoginWindowText as LWT
from constants import AppointmentWindowText as AWT
from constants import DebugData as DD
from constants import UISettings as UIS


class LoginFrame(Frame):
    resolution = UIS.login_window_resolution

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        login = StringVar(self)
        password = StringVar(self)

        title_label = Label(self,
                            font=UIS.font_big,
                            text=LWT.title_label,
                            justify=CENTER,
                            anchor=CENTER)
        title_label.pack(expand=True, anchor=S, fill=X)

        login_frame = Frame(self)
        login_label = Label(login_frame,
                            font=UIS.font_medium,
                            text=LWT.login_label)
        login_label.pack(expand=True, side=TOP, padx=10)

        login_input = Entry(login_frame,
                            width=50,
                            textvariable=login)
        login_input.pack(expand=True, side=TOP, padx=10)
        login_frame.pack(expand=True, fill=BOTH)

        password_frame = Frame(self)
        password_label = Label(password_frame,
                               font=UIS.font_medium,
                               text=LWT.password_label)
        password_label.pack(expand=True, side=TOP, padx=10)

        password_input = Entry(password_frame,
                               width=50,
                               textvariable=password,
                               show="*")
        password_input.pack(expand=True, side=RIGHT, padx=10)
        password_frame.pack(expand=True, fill=BOTH)

        buttons_frame = Frame(self)
        login_button = Button(buttons_frame,
                              text=LWT.login_button,
                              command=lambda: controller.show_profile_frame(login=login.get(),
                                                                                 password=password.get()))
        login_button.pack(expand=True, side=LEFT, padx=10, pady=10)

        registration_button = Button(buttons_frame,
                                     text=LWT.registration_button,
                                     command=lambda: controller.show_registration_frame())
        registration_button.pack(expand=True, side=LEFT, ipadx=10, pady=10)
        buttons_frame.pack(expand=True, fill=BOTH)

        self.set_default_values(login_input, password_input)

    def set_default_values(self, login_input, password_input):
        login_input.insert(0, DD.example_login)
        password_input.insert(0, DD.example_password)


class RegistrationFrame(Frame):
    resolution = UIS.registration_window_resolution

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        labels_width = 20
        inputs_width = 50

        self.setup_values()
        self.setup_title_frame()
        self.setup_name_frame(labels_width, inputs_width)
        self.setup_values_frame(labels_width, inputs_width)
        self.setup_buttons_frame()

    def setup_values(self):
        self.name = StringVar(self)
        self.surname = StringVar(self)
        self.last_name = StringVar(self)
        self.address = StringVar(self)
        self.email = StringVar(self)
        self.phone_number = StringVar(self)
        self.date_of_birth = StringVar(self)
        self.login = StringVar(self)
        self.password = StringVar(self)
        self.password_confirmation = StringVar(self)

    def setup_title_frame(self):
        title_label = Label(self,
                            font=UIS.font_big,
                            text=RWT.title_label,
                            justify=CENTER,
                            anchor=CENTER)
        title_label.pack(expand=True, anchor=S, fill=X)

    def setup_name_frame(self, labels_width, inputs_width):
        name_frame = Frame(self)
        name_label = Label(name_frame,
                           font=UIS.font_medium,
                           text=RWT.name_label,
                           width=labels_width)
        name_label.pack(expand=True, side=LEFT)

        name_input = Entry(name_frame,
                           width=inputs_width,
                           textvariable=self.name)
        name_input.pack(expand=True, side=RIGHT)
        name_frame.pack(expand=True, fill=BOTH)

    def setup_values_frame(self, labels_width, inputs_width):
        surname_frame = Frame(self)
        surname_label = Label(surname_frame,
                              font=UIS.font_medium,
                              text=RWT.surname_label,
                              width=labels_width)
        surname_label.pack(expand=True, side=LEFT)

        surname_input = Entry(surname_frame,
                              width=inputs_width,
                              textvariable=self.surname)
        surname_input.pack(expand=True, side=RIGHT)
        surname_frame.pack(expand=True, fill=BOTH)

        last_name_frame = Frame(self)
        last_name_label = Label(last_name_frame,
                                font=UIS.font_medium,
                                text=RWT.last_name_label,
                                width=labels_width)
        last_name_label.pack(expand=True, side=LEFT)

        last_name_input = Entry(last_name_frame,
                                width=inputs_width,
                                textvariable=self.last_name)
        last_name_input.pack(expand=True, side=RIGHT)
        last_name_frame.pack(expand=True, fill=BOTH)

        address_frame = Frame(self)
        address_label = Label(address_frame,
                              font=UIS.font_medium,
                              text=RWT.address_label,
                              width=labels_width)
        address_label.pack(expand=True, side=LEFT)

        address_input = Entry(address_frame,
                              width=inputs_width,
                              textvariable=self.address)
        address_input.pack(expand=True, side=RIGHT)
        address_frame.pack(expand=True, fill=BOTH)

        email_frame = Frame(self)
        email_label = Label(email_frame,
                            font=UIS.font_medium,
                            text=RWT.email_label,
                            width=labels_width)
        email_label.pack(expand=True, side=LEFT)

        email_input = Entry(email_frame,
                            width=inputs_width,
                            textvariable=self.email)
        email_input.pack(expand=True, side=RIGHT)
        email_frame.pack(expand=True, fill=BOTH)

        phone_number_frame = Frame(self)
        phone_number_label = Label(phone_number_frame,
                                   font=UIS.font_medium,
                                   text=RWT.phone_number_label,
                                   width=labels_width)
        phone_number_label.pack(expand=True, side=LEFT)

        phone_number_input = Entry(phone_number_frame,
                                   width=inputs_width,
                                   textvariable=self.phone_number)
        phone_number_input.pack(expand=True, side=RIGHT)
        phone_number_frame.pack(expand=True, fill=BOTH)

        date_of_birth_frame = Frame(self)
        date_of_birth_label = Label(date_of_birth_frame,
                                    font=UIS.font_medium,
                                    text=RWT.date_of_birth_label,
                                    width=labels_width)
        date_of_birth_label.pack(expand=True, side=LEFT)

        date_of_birth_input = Entry(date_of_birth_frame,
                                    width=inputs_width,
                                    textvariable=self.date_of_birth)
        date_of_birth_input.pack(expand=True, side=RIGHT)
        date_of_birth_frame.pack(expand=True, fill=BOTH)

        login_frame = Frame(self)
        login_label = Label(login_frame,
                            font=UIS.font_medium,
                            text=RWT.login_label,
                            width=labels_width)
        login_label.pack(expand=True, side=LEFT)

        login_input = Entry(login_frame,
                            width=inputs_width,
                            textvariable=self.login)
        login_input.pack(expand=True, side=RIGHT)
        login_frame.pack(expand=True, fill=BOTH)

        password_frame = Frame(self)
        password_label = Label(password_frame,
                               font=UIS.font_medium,
                               text=RWT.password_label,
                               width=labels_width)
        password_label.pack(expand=True, side=LEFT)

        password_input = Entry(password_frame,
                               width=inputs_width,
                               textvariable=self.password)
        password_input.pack(expand=True, side=RIGHT)
        password_frame.pack(expand=True, fill=BOTH)

        password_confirmation_frame = Frame(self)
        password_confirmation_label = Label(password_confirmation_frame,
                                            font=UIS.font_medium,
                                            text=RWT.password_confirmation_label,
                                            width=labels_width)
        password_confirmation_label.pack(expand=True, side=LEFT)

        password_confirmation_input = Entry(password_confirmation_frame,
                                            width=inputs_width,
                                            textvariable=self.password_confirmation)
        password_confirmation_input.pack(expand=True, side=RIGHT)
        password_confirmation_frame.pack(expand=True, fill=BOTH)

    def setup_buttons_frame(self):
        buttons_frame = Frame(self)
        register_button = Button(buttons_frame,
                                 text=RWT.registration_button,
                                 command=lambda: self.controller.register_and_show_profile_frame())
        register_button.pack(expand=True, side=LEFT, padx=10, pady=10)

        back_button = Button(buttons_frame,
                             text=RWT.back_button,
                             command=lambda: self.controller.go_back())
        back_button.pack(expand=True, side=LEFT, ipadx=10, pady=10)
        buttons_frame.pack(expand=True, fill=BOTH)


class ProfileFrame(Frame):
    resolution = UIS.profile_window_resolution

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.setup_values()

        self.setup_title_frame()
        self.setup_profile_frame()
        self.setup_appointments_frame()

    def set_values(self, client, appointment_history):
        self.current_user.set(PWT.current_user_label.format(client.login))
        self.name.set(PWT.name_label.format(client.name))
        self.surname.set(PWT.surname_label.format(client.surname))
        self.last_name.set(PWT.last_name_label.format(client.last_name))
        self.address.set(PWT.address_label.format(client.address))
        self.email.set(PWT.email_label.format(client.email))
        self.phone_number.set(PWT.phone_number_label.format(client.phone_number))
        self.date_of_birth.set(PWT.date_of_birth_label.format(client.date_of_birth))

    def setup_values(self):
        self.current_user = StringVar(self, value=PWT.current_user_label)
        self.name = StringVar(self, value=PWT.name_label)
        self.surname = StringVar(self, value=PWT.surname_label)
        self.last_name = StringVar(self, value=PWT.last_name_label)
        self.address = StringVar(self, value=PWT.address_label)
        self.email = StringVar(self, value=PWT.email_label)
        self.phone_number = StringVar(self, value=PWT.phone_number_label)
        self.date_of_birth = StringVar(self, value=PWT.date_of_birth_label)

    def setup_title_frame(self):
        title_frame = Frame(self)

        title_label = Label(title_frame,
                            font=UIS.font_big,
                            text=PWT.title_label)
        title_label.pack(expand=True, side=LEFT)

        logout_button = Button(title_frame,
                               text=PWT.logout_button,
                               width=20,
                               command=lambda: self.controller.show_login_frame())
        logout_button.pack(expand=True, side=RIGHT)

        title_frame.pack(expand=True, fill=BOTH)

    def setup_profile_frame(self):
        labels_width = 40
        profile_frame = Frame(self)

        name_label = Label(profile_frame,
                           font=UIS.font_medium,
                           textvariable=self.name,
                           width=labels_width)
        name_label.pack(expand=True)

        surname_label = Label(profile_frame,
                              font=UIS.font_medium,
                              textvariable=self.surname,
                              width=labels_width)
        surname_label.pack(expand=True)

        last_name_label = Label(profile_frame,
                                font=UIS.font_medium,
                                textvariable=self.last_name,
                                width=labels_width)
        last_name_label.pack(expand=True)

        address_label = Label(profile_frame,
                              font=UIS.font_medium,
                              textvariable=self.address,
                              width=labels_width)
        address_label.pack(expand=True)

        email_label = Label(profile_frame,
                            font=UIS.font_medium,
                            textvariable=self.email,
                            width=labels_width)
        email_label.pack(expand=True)

        phone_number_label = Label(profile_frame,
                                   font=UIS.font_medium,
                                   textvariable=self.phone_number,
                                   width=labels_width)
        phone_number_label.pack(expand=True)

        date_of_birth_label = Label(profile_frame,
                                    font=UIS.font_medium,
                                    textvariable=self.date_of_birth,
                                    width=labels_width)
        date_of_birth_label.pack(expand=True)

        profile_frame.pack(expand=True, fill=BOTH, side=LEFT)

    def setup_appointments_frame(self):
        appointment_frame = Frame(self)

        create_appointment_button = Button(appointment_frame,
                               text=PWT.create_appointment_button,
                               command=lambda: self.controller.show_appointment_frame())
        create_appointment_button.pack(expand=True, side=TOP, fill=X, pady=2)

        # scrollbar
        side_scroll = Scrollbar(appointment_frame)
        side_scroll.pack(side=RIGHT, fill=Y)
        bottom_scroll = Scrollbar(appointment_frame,
                                  orient='horizontal')
        bottom_scroll.pack(side=BOTTOM, fill=X)
        self.appointments_table = Treeview(appointment_frame,
                                           yscrollcommand=side_scroll.set,
                                           xscrollcommand=bottom_scroll.set,
                                           height=20)
        self.appointments_table["columns"] = ('player_Name', 'player_Country', 'player_Medal')
        # format our column
        self.appointments_table.column("#0", width=0, stretch=NO)
        self.appointments_table.column("player_Name", anchor=CENTER, width=80)
        self.appointments_table.column("player_Country", anchor=CENTER, width=80)
        self.appointments_table.column("player_Medal", anchor=CENTER, width=80)
        self.appointments_table.pack(fill=BOTH)

        create_appointment_button = Button(appointment_frame,
                                           text=PWT.logout_button,
                                           command=lambda: self.controller.show_login_frame())
        create_appointment_button.pack(expand=True, side=RIGHT)

        appointment_frame.pack(expand=True, fill=BOTH)


class AppointmentWindow(Frame):
    resolution = UIS.appointment_window_resolution

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.setup_values()
        self.setup_title_frame()
        self.setup_info_frame()
        self.setup_buttons_frame()

    def setup_values(self):
        self.date = StringVar(self)
        self.dropdown_default = StringVar(self)
        self.dropdown_default.set(AWT.available_cosmetologists_dropdown)

    def set_values(self, cosmetologists):
        menu = self.cosmetologists_drop["menu"]
        menu.delete(0, "end")

        for i in cosmetologists:
            string = f"{i.surname} {i.name} {i.last_name}"
            menu.add_command(label=string,
                             command=lambda value=string:
                             self.dropdown_default.set(value))

    def setup_title_frame(self):
        title_frame = Frame(self)

        title_label = Label(title_frame,
                            font=UIS.font_big,
                            text=AWT.title_label)
        title_label.pack(expand=True, side=LEFT)

        title_frame.pack(expand=True, fill=BOTH)

    def setup_info_frame(self):
        info_frame = Frame(self)

        self.cosmetologists_drop = OptionMenu(info_frame, self.dropdown_default)
        self.cosmetologists_drop.pack(expand=True, side=TOP)

        date_label = Label(info_frame,
                              text=AWT.date_label)
        date_label.pack(expand=True, side=TOP)

        date_input = Entry(info_frame,
                              textvariable=self.date)
        date_input.pack(expand=True, side=TOP)

        info_frame.pack(expand=True, fill=BOTH)

    def setup_buttons_frame(self):
        buttons_frame = Frame(self)

        values = (self.date.get(), self.dropdown_default.get())
        apply_button = Button(buttons_frame,
                               text=AWT.apply_button,
                               width=20,
                               command=lambda: self.controller.create_appointment(*values))
        apply_button.pack(expand=True, side=LEFT)

        back_button = Button(buttons_frame,
                               text=AWT.back_button,
                               width=20,
                               command=lambda: self.controller.go_back())
        back_button.pack(expand=True, side=RIGHT)

        buttons_frame.pack(expand=True, fill=BOTH)

