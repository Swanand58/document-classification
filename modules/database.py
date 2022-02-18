import mysql.connector
import pandas as pd
from datetime import datetime

class CreateConnection:
    def __init__(self):
        self.__HOST = 'localhost'
        self.__USERNAME = 'root'
        self.__PASSWORD = '1234'
        self.__DATABASE = 'document_classification'
        self.__connection = mysql.connector.connect(host=self.__HOST, database='document_classification',
                                                    user=self.__USERNAME, passwd=self.__PASSWORD)
        self.__cusor = self.__connection.cursor()

    def insert(self, filename,original_filename, category, score, date_posted,is_edit=0,new_category='NULL',):
        query = """
        INSERT INTO predictions(filename,original_filename, category, score, is_edit, new_category,date_posted) VALUES ('{}', '{}','{}', {}, {}, '{}','{}')
        """.format(filename,original_filename, category, score, is_edit, new_category, date_posted)

        self.__cusor.execute(query)
        self.__connection.commit()

        return 'Query OK, 1 row affected'

    def update(self, filename, new_category, is_edit=1):
        query = """
        UPDATE predictions SET new_category='{}' WHERE filename='{}'
        """.format(new_category, filename)

        self.__cusor.execute(query)
        self.__connection.commit()

        return 'Query OK, 1 row affected'

    def get_last_n_records(self, limit):
        """
        Selects last n records from database.
        :param limit: number of records to select
        :return: pandas dataframe with same column names as declared in database schema design
        """
        query = """
        SELECT * FROM(
            SELECT * FROM predictions ORDER BY id DESC LIMIT {}
        )Var1
            ORDER BY id ASC;
        """.format(limit)

        data = pd.read_sql_query(query, self.__connection)
        return data
