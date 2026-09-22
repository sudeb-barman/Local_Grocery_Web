from get_sql_connection import get_sql_connection
from datetime import datetime


def insert_order(connection,order):
    mycursor=connection.cursor()
    query = ( "INSERT INTO new_order(customer_name, total, date_time)"
     " VALUES (%s, %s, %s)" )

    values=(order["customer_name"],order["grand_total"],datetime.now())

    mycursor.execute(query, values)

    order_id=mycursor.lastrowid
    
    product_order_query=("INSERT INTO orders(order_id, product_id, quantity, total_price)"
     " VALUES (%s, %s, %s, %s)")
    product_order_data=[]
    for product_details_record in order['order_details']:
        product_order_data.append([
            order_id,
            int(product_details_record['product_id']),
            float(product_details_record['quantity']),
            float(product_details_record['total_price'])

        ])
    mycursor.executemany(product_order_query, product_order_data)




    connection.commit()

    return order_id




if __name__=='__main__':
    connection=get_sql_connection()
    print(insert_order(connection,{

        'customer_name':'Sourabh',
        'grand_total':'500',
        'order_details':[
            {
                'product_id': '17',
                'quantity':'5',
                'total_price':'500'
            },
            {
                'product_id':'18',
                'quantity':'4',
                'total_price':'200'
            }
        ]}))


