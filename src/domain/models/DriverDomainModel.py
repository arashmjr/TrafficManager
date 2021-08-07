class DriverDomainModel:
    name: str
    birthdate: int
    national_code: int

    def __init__(self, name: str, birthdate: int, national_code: int):

        self.name = name
        self.birthdate = birthdate
        self.national_code = national_code

    def to_dict(self):
        return {
                "name": self.name,
                "birthdate": self.birthdate,
                "national_code": self.national_code,

                }
