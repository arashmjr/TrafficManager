import psycopg2


class CoreDatabase:
    __instance = None
    _connection = None

    @staticmethod
    def get_instance():
        if CoreDatabase.__instance is None:
            CoreDatabase()
        return CoreDatabase.__instance

    def __init__(self):
        if CoreDatabase.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CoreDatabase.__instance = self
            self.__connect()

    def __connect(self):
        self._connection = psycopg2.connect(database="postgres", user='postgres', password='1234', host='localhost', port='5432')
        # Creating a cursor object using the cursor() method
        cursor = self._connection.cursor()

        # Executing an MYSQL function using the execute() method
        cursor.execute("select version()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print("Connection established to: ", data)

        # Closing the connection
        self._connection.close()