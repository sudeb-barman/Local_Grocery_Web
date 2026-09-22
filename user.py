from get_sql_connection import get_sql_connection

# LOGIN PAGE

def login(connection,name,password,role):

    mycursor = connection.cursor()

                                                                                        # name="admin"
                                                                                        # password="1234"
                                                                                        # role="admin"

    query = ("SELECT user_id, user_name, password, role FROM users WHERE user_name = %s AND password = %s AND role= %s ")

    mycursor.execute(query,(name,password,role ))
    return mycursor.fetchone()

if __name__== "__main__":
    connection = get_sql_connection()
    print(login(connection))


# REGISTER A NEW USER 



def register(connection,name,ph,password,rolee):
    mycursor = connection.cursor()

                                                                                                        # query =("SELECT * FROM users")
                                                                                                        # mycursor.execute(query)

    query = ("INSERT INTO users(user_name, ph_no, password, role ) VALUES (%s, %s, %s, %s)")

    domain = (name,ph,password,rolee)

    mycursor.execute(query,domain)

    connection.commit()


                                                                                                        # for i in mycursor:
                                                                                                        #     print(i)
if __name__== "__main__":
    connection = get_sql_connection()
    print(register(connection))