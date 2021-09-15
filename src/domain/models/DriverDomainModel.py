class DriverDomainModel:
    national_code: int
    name: str
    birthdate: int

    def __init__(self, national_code: int, name: str, birthdate: int):

        self.national_code = national_code
        self.name = name
        self.birthdate = birthdate

    def to_dict(self):
        return {
                "national_code": self.national_code,
                "name": self.name,
                "birthdate": self.birthdate

                }

    @staticmethod
    def asJSON(drivers):
        list_drivers = []
        for item in drivers:
            result = {
                'national_code': item.national_code,
                'name': item.name,
                'birthdate': item.birthdate,

            }
            list_drivers.append(result)
        return list_drivers

