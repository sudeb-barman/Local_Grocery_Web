import mysql.connector    

__mydb=None     #initialize the variable

def get_sql_connection():

    global __mydb        # Set the variable is global

    if __mydb == None:      # If the variable have NONE value
        __mydb=mysql.connector.connect(        # all information for connect the database   
            host = "LocalHost",
            user = "root",
            password = "sudeb",
            database = "grocery_web"
        )
    return __mydb           # Return the Database 

