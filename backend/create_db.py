import mysql.connector

# To create database on local machine
mydb = mysql.connector.connect(
    host="projectkarty.cmoarzscfdhk.eu-west-2.rds.amazonaws.com",
    user="admin",
    passwd='3X47Qy!b',  # edit this with your MySQL password
)

my_cursor = mydb.cursor()
# uncomment to create new databases
# my_cursor.execute("CREATE DATABASE conversations")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
