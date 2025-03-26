# used the docker image of mysql version 8.0 to connect mysql with django
# pip install mysql mysql-connector-python mysql-connector
# either of connector or connector-python works so only used the python one

import mysql.connector
# if getting error access denied, that's because you don't have privileges to create database
# 

config = {
    'host': 'localhost',    #hostname
    'user': 'django_user',  # username
    'password': 'passwd',   # password
    'port': '3306',         # port

}
try:

    dataBase = mysql.connector.connect(**config
    # host = "localhost",
    # user = "django_user",
    # passwd = "passwd"
    # port = "3306",
    )

    # prepare cursor object
    cursorObject = dataBase.cursor()
    print(f"Is connected: {dataBase.is_connected()}")
    # create database
    cursorObject.execute("CREATE DATABASE djangomysql2;")
    # print("Connected")
    print("Database django_mysql_2 created")
except Exception as e:
    print("Error occurred")
    print(e)