# This is a sample Python script.

import csv
import sqlite3


class Database:
    @staticmethod
    def do_customers():
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS CUSTOMERS")
        cur.execute(
            "CREATE TABLE CUSTOMERS (custID, Name, Address, Age, Income, LoginID, Password, Additional attributes)")

        customer_sql = "INSERT INTO PEOPLE (custID, Name, Address, Age, Income, LoginID, Password, Additional " \
                       "attributes) " \
                       "VALUES (?,?,?,?,?,?,?,?)"
        with open('customers.csv', newline='') as csvfile:
            customers = csv.reader(csvfile, delimiter=',', quotechar='\'')
            for not_formatted in customers:
                customer = [not_formatted[0], not_formatted[1].strip(),
                            (not_formatted[2] + not_formatted[3] + not_formatted[4]).strip(),
                            not_formatted[5].strip(), not_formatted[6].strip(), not_formatted[7].strip()]
                print(customer)
                cur.execute(customer_sql, customer)

            con.commit()

    @staticmethod
    def do_publishers():
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS PUBLISHERS")
        cur.execute("CREATE TABLE PUBLISHERS (PublisherId, Name, Address, Discount)")
        publisher_sql = "INSERT INTO PUBLISHERS (PublisherId, Name, Address, Discount) " \
                        "VALUES (?,?,?,?)"
        with open('publishers.csv', newline='') as csvfile:
            publishers = csv.reader(csvfile, delimiter=',', quotechar='\'')
            for not_formatted in publishers:
                address_elements = not_formatted[2:len(not_formatted) - 1]
                address = " ".join(address_elements).strip()
                publisher = [not_formatted[0], not_formatted[1].strip(),
                             address, (not_formatted[len(not_formatted) - 1]).strip()]
                print(publisher)
                cur.execute(publisher_sql, publisher)

            con.commit()


if __name__ == '__main__':
    Database().do_publishers()
