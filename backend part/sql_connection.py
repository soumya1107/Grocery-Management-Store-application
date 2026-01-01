import mysql.connector
import datetime

## just so it doesnt create multiple connections
## we'll store it in a varaible, and make it global so we can access everywhere
_cnx = None


def get_sql_connection():
    print("Initiating connection to MySQL DB")
    global _cnx

    if _cnx == None:
        _cnx = mysql.connector.connect(user='root', password='Sd@1999', database='grocery_store')
        
    return _cnx