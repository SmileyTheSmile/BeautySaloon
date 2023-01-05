from mapper import setup_mapper, Client, Cosmetologist, Appointment
from exceptions import *

from sqlalchemy.exc import IntegrityError, StatementError


class Transactions:
    current_user = None

    def __init__(self):
        self.mapper = setup_mapper()

    def authenticate(self, login, password):
        try:
            user_data = self.mapper.query(Client) \
                .filter(Client.login == login,
                        Client.password == password) \
                .first()
            if user_data is None:
                raise LoginFailedException

            self.current_user = user_data

            appointment_history = self.mapper.query(Appointment) \
                .filter(Appointment.id_client == user_data.id) \
                .all()
        except LoginFailedException as error:
            self.mapper.rollback()
            return 1, error.detail
        except StatementError as error:
            self.mapper.rollback()
            return 2, error.detail

        return 0, (user_data, appointment_history)

    def load_all_cosmetologists(self):
        try:
            result = self.mapper.query(Cosmetologist).all()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0, result

    def load_all_appointments(self):
        try:
            result = self.mapper.query(Appointment).all()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0, result

    def add_cosmetologist(self, cosmetologist_info):
        try:
            self.mapper.add(Cosmetologist(**cosmetologist_info))
            self.mapper.commit()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0,

    def load_all_clients(self):
        try:
            result = self.mapper.query(Client).all()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0, result

    def create_appointment(self, *appointment_info):
        try:
            print(appointment_info)
            new_id = self.mapper.query(Appointment.id).filter(max(Appointment.id)).one()
            self.mapper.add(Appointment(str(int(new_id) + 1), self.current_user.id, *appointment_info))
            self.mapper.commit()
        except IntegrityError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0,

    def register_client(self, **client_info):
        try:
            self.mapper.add(Client(**client_info))
            self.mapper.commit()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0,

    def create_cosmetologist(self, **cosmetologist_info):
        try:
            self.mapper.add(Client(**cosmetologist_info))
            self.mapper.commit()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0,
