from get_sql_connection import get_sql_connection

def del_product(connection,product_id):

    mycursor=connection.cursor()
    query =("DELETE FROM manage_product WHERE product_id ="+ str(product_id))

    mycursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(del_product(connection,13))