import datetime


class AdminUserDomainModel:
    name: str
    email: str
    password: str
    creation_date: datetime

    def __init__(self, name: str, email: str, password: str, creation_date: datetime):

        self.name = name
        self.email = email
        self.password = password
        self.creation_date = creation_date

    def to_dict(self):
        return {
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "creation_date": self.creation_date
                }
