import csv
import mysql.connector

def read_csv_data(filepath):
    data = []
    with open("/Users/chiranth.c/Documents/selenium_framework/constants/data/saus_demo_login.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def read_mysql_data(read_query):
    # establish the connection
    connection = mysql.connector.connect(user='root',password='mysql123',host='localhost' , database = 'TGDB')
    # create cursor object
    cursor = connection.cursor()
    query = read_query
    cursor.execute(query)
    # data = cursor.fetchone()
    data = cursor.fetchall()
    print(data)
    if data:
        usr_name = data[0]
        pwd = data[1]
        print(data)
        print(usr_name)
        print(pwd)
    else:
        print("No user found")
    # close connection
    cursor.close()
    connection.close()
    return data