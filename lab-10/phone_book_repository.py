import psycopg2
import csv

class PhoneBookRepository:
    def __init__(self, db_config):
        """
        Initialize the PhoneBookRepository with a database connection.

        :param db_config: A dictionary with database configuration keys:
                          - dbname: The name of the database
                          - user: The database user
                          - password: The database password
                          - host: The database host
                          - port: The database port (default is 5432)
        """
        self.connection = psycopg2.connect(
            dbname=db_config.get('dbname'),
            user=db_config.get('user'),
            password=db_config.get('password'),
            host=db_config.get('host', 'localhost'),
            port=db_config.get('port', 5432)
        )
        self.cursor = self.connection.cursor()

    def upload_from_csv(self, csv_file_path):
        """
        Upload data from a CSV file into the phone_book table.

        :param csv_file_path: Path to the CSV file to upload.
        """
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row if present
            for row in reader:
                user_name, phone = row
                self.insert_entry(user_name, phone)

    def insert_entry(self, user_name, phone):
        """
        Insert a new entry into the phone_book table.

        :param user_name: The user name.
        :param phone: The phone number.
        """
        query = "INSERT INTO phone_book (user_name, phone) VALUES (%s, %s)"
        self.cursor.execute(query, (user_name, phone))
        self.connection.commit()

    def update_entry(self, user_name=None, phone=None, new_user_name=None, new_phone=None):
        """
        Update an existing entry in the phone_book table.

        :param user_name: The user name to update (optional).
        :param phone: The phone number to update (optional).
        :param new_user_name: The new user name (optional).
        :param new_phone: The new phone number (optional).
        """
        if user_name and new_user_name:
            query = "UPDATE phone_book SET user_name = %s WHERE user_name = %s"
            self.cursor.execute(query, (new_user_name, user_name))
        if phone and new_phone:
            query = "UPDATE phone_book SET phone = %s WHERE phone = %s"
            self.cursor.execute(query, (new_phone, phone))
        self.connection.commit()

    def query_entries(self, user_name=None, phone=None):
        """
        Query data from the phone_book table with filters.

        :param user_name: The user name to filter by (optional).
        :param phone: The phone number to filter by (optional).
        :return: A list of tuples representing the rows that match the query.
        """
        if user_name:
            query = "SELECT * FROM phone_book WHERE user_name = %s"
            self.cursor.execute(query, (user_name,))
        elif phone:
            query = "SELECT * FROM phone_book WHERE phone = %s"
            self.cursor.execute(query, (phone,))
        else:
            query = "SELECT * FROM phone_book"
            self.cursor.execute(query)
        
        return self.cursor.fetchall()

    def delete_entry(self, user_name=None, phone=None):
        """
        Delete data from the phone_book table.

        :param user_name: The user name to delete (optional).
        :param phone: The phone number to delete (optional).
        """
        if user_name:
            query = "DELETE FROM phone_book WHERE user_name = %s"
            self.cursor.execute(query, (user_name,))
        elif phone:
            query = "DELETE FROM phone_book WHERE phone = %s"
            self.cursor.execute(query, (phone,))
        
        self.connection.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.cursor.close()
        self.connection.close()
