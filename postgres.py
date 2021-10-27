# -*- coding : utf-8 -*-
import psycopg2
from pprint import pprint

class DBConn:
    __Author__ = "Zeus"
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='python_test' user='postgres' host='localhost' password='postgres' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("db connectoin successful...\n")
        except:
            pprint("Unable to connecto to Database Server....")
            
    def create_table(self):
        create_table_command = "CREATE TABLE Students(id serial PRIMARY KEY, name VARCHAR(100),\
surname VARCHAR(100), sex VARCHAR(10), country VARCHAR(50), city VARCHAR(100))"
        self.cursor.execute(create_table_command)
        print("table creation successfull...\n")

    def insert_record(self, name, surname, sex, country, city):
        insert_command = "INSERT INTO Students(name, surname, sex, country, city) VALUES(\
'" + name + "', '" + surname + "', '" + sex + "', '" + country + "', '" + city + "')"
        self.cursor.execute(insert_command)
        print("sucessfull recording....\n")

    def query_all(self):
        self.cursor.execute("SELECT * FROM Students")
        students = self.cursor.fetchall()
        for student in students:
            pprint("Student : {} {}".format(student[1], student[2]))

    def update_record(self):
        update_command = "UPDATE Students SET city='KINSHASA' WHERE name='Tambou'"
        self.cursor.execute(update_command)
        print("update successful....\n")

    def delete_record(self):
        delete_command = "DELETE * WHERE name='Domcheu'"
        self.cursor.execute(delete_command)
        print("record deleted successfully....\n")

    def drop_table(self):
        drop_table_command = "DROP TABLE Students"
        self.cursor.execute(drop_table_command)
        print("table dropped successfully...")

    
if __name__=="__main__":
    #conn = DBConn()
    #conn.drop_table()
    #conn.delete_record()
    #conn.update_record()
    #conn.query_all()
    #conn.create_table()

    #conn.insert_record("Domcheu", "Vanessa", "Feminin", "TCHAD", "Ndjamena")

    print("\n\n[----->> Database Module for interaction with postgresql <<-----]\n")
