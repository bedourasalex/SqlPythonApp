import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "best_comp_db",
        port = 3306
    )