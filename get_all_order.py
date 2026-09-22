from get_sql_connection import get_sql_connection

def get_order_products(connection):

    mycursor=connection.cursor()
    query=("SELECT * FROM new_order")
    mycursor.execute(query)

    response = []  #EMPTY DICTIONARY

    for(a,b,c,d) in mycursor:
        response.append({                           #Add value in dictionary 
            'order_id':a,
            'customer_name':b,
            'total':c,
            'date_time':d
        })
    return response


if __name__=='__main__':
    connection=get_sql_connection()
    print(get_order_products(connection))