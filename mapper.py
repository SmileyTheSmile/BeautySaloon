from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from constants import DatabaseSettings as DBS

Base = declarative_base()


class Client(Base):
    """Wrapper class for the "clients" table in the database."""

    __tablename__ = "clients"

    id = Column("id", Integer, primary_key=True)
    login = Column("login", String, unique=True)
    password = Column("password", String)
    account_type = Column("account_type", String)
    name = Column("name", String)
    surname = Column("surname", String)
    last_name = Column("last_name", String)
    address = Column("address", String)
    email = Column("email", String)
    phone_number = Column("phone_number", String)
    date_of_birth = Column("date_of_birth", Date)
    date_of_registration = Column("date_of_registration", Date)

    def __init__(self, id, login, password, account_type, name, surname, last_name,
                 address, email, phone_number, date_of_birth, date_of_registration):
        self.id = id
        self.login = login
        self.password = password
        self.account_type = account_type
        self.name = name
        self.surname = surname
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.date_of_registration = date_of_registration

    def __repr__(self):
        return f"({self.id}, {self.login}, {self.password}, {self.account_type}, {self.surname}, {self.last_name}, {self.address}, {self.email}, {self.phone_number}, {self.date_of_birth}, {self.date_of_registration})"


class Cosmetologist(Base):
    """Wrapper class for the "cosmetologists" table in the database."""
    __tablename__ = "cosmetologists"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    last_name = Column("last_name", String)
    address = Column("address", String)
    email = Column("email", String)
    phone_number = Column("phone_number", String)
    date_of_birth = Column("date_of_birth", Date)
    date_of_hire = Column("date_of_hire", Date)

    def __init__(self, id, name, surname, last_name, address, email, phone_number, date_of_birth,
                 date_of_hire):
        self.id = id
        self.name = name
        self.surname = surname
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.date_of_hire = date_of_hire

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.surname}, {self.last_name}, {self.address}, {self.email}, {self.phone_number}, {self.date_of_birth}, {self.date_of_hire})"


class Appointment(Base):
    """Wrapper class for the "appointments" table in the database."""

    __tablename__ = "appointments"

    id = Column("id", Integer, primary_key=True)
    id_client = Column("id_client", Integer)
    id_cosmetologist = Column("id_cosmetologist", Integer)
    price = Column("date_of_appointment", Integer)
    rating = Column("rating", Integer)

    def __init__(self, id, id_client, id_cosmetologist, price, rating):
        self.id = id
        self.id_client = id_client
        self.id_cosmetologist = id_cosmetologist
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"({self.id}, {self.id_client}, {self.id_cosmetologist}, {self.price}, {self.rating})"


def setup_mapper():
    connection_string = f"{DBS.database_type}://{DBS.user}:{DBS.password}@{DBS.host}/{DBS.database_name}"
    engine = create_engine(connection_string)
    Base.metadata.create_all(bind=engine)

    return Session(bind=engine)
