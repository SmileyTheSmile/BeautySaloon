from mapper import setup_mapper, Client, Cosmetologist, Appointment
from exceptions import *
from constants import *

from sqlalchemy.exc import IntegrityError, StatementError


class Transactions:
    current_user = None

    def __init__(self):
        self.mapper = setup_mapper()

    # GLOBAL TRANSACTIONS

    def log_in(self, login, password):
        try:
            result = self.mapper.query(Client) \
                .filter(Client.login == login,
                        Client.password == password) \
                .first()
            if result is None:
                raise LoginFailedException
        except LoginFailedException as error:
            self.mapper.rollback()
            return error.detail
        except StatementError as error:
            self.mapper.rollback()
            return error.detail

        self.current_user = result

        return 0, result

    # USER TRANSACTIONS
        # Insert transactions

    def create_appointment(self, **appointment_info):
        try:
            self.mapper.add(Appointment(**appointment_info))
            self.mapper.commit()
        except IntegrityError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0,

    def create_client(self, **client_info):
        try:
            self.mapper.add(Client(**client_info))
            self.mapper.commit()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0,

        # Select transactions

    # ADMIN TRANSACTIONS
        # Insert transactions

    def create_cosmetologist(self, **cosmetologist_info):
        try:
            self.mapper.add(Client(**cosmetologist_info))
            self.mapper.commit()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0,

        # Select transactions

    def load_all_client_info(self):
        try:
            result = self.mapper.query(Client).all()
        except StatementError as error:
            self.mapper.rollback()
            return 1, error.detail

        return 0, result
