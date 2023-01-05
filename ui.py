from tkinter import messagebox, Tk, Frame, BOTH, TOP

from ui_frames import LoginFrame, RegistrationFrame, ProfileFrame, AppointmentWindow
from constants import UISettings as UIS


class UI(Tk):
    def __init__(self, transactions, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.transactions = transactions

        self.title(UIS.title)
        self.resizable(False, False)

        self.frames = {}
        self.current_frame = None
        self.last_frame = None
        self.root = Frame(self)
        self.root.pack(fill=BOTH, expand=True)

        for window in (LoginFrame, RegistrationFrame, ProfileFrame, AppointmentWindow):
            self.frames[window] = window(parent=self.root, controller=self)

        self.show_login_frame()

    def show_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.last_frame = type(self.current_frame)
        self.current_frame = self.frames[frame]
        self.geometry(frame.resolution)
        self.current_frame.pack(side=TOP, fill=BOTH, expand=True)

    def go_back(self):
        self.show_frame(self.last_frame)

    def show_login_frame(self):
        self.show_frame(LoginFrame)

    def show_registration_frame(self):
        self.show_frame(RegistrationFrame)

    def show_appointment_frame(self):
        result_code, data = self.transactions.load_all_cosmetologists()

        if result_code != 0:
            messagebox.showerror(f"Код ошибки: {result_code}", data)
        else:
            self.frames[AppointmentWindow].set_values(data)
            self.show_frame(AppointmentWindow)

    def show_profile_frame(self, login, password):
        result_code, data = self.transactions.authenticate(login, password)

        if result_code != 0:
            messagebox.showerror(f"Код ошибки: {result_code}", data)
        else:
            self.frames[ProfileFrame].set_values(*data)
            self.show_frame(ProfileFrame)

    def create_appointment(self, date, cosmetologist):
        result_code, data = self.transactions.create_appointment(cosmetologist, date, "500", "")

        if result_code != 0:
            messagebox.showerror(f"Код ошибки: {result_code}", data)
        else:
            messagebox.showwarning("Успешно")
            self.go_back()
