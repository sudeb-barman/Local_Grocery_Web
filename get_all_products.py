from get_sql_connection import get_sql_connection

def get_all_products(connection):

    mycursor=connection.cursor()
    query=("SELECT manage_product.product_id,manage_product.name,manage_product.uom_id,manage_product.price_per_unit,uom.uom_name " \
            "FROM grocery_web.manage_product " \
            "INNER JOIN uom ON manage_product.uom_id=uom.uom_id;")
    mycursor.execute(query)

    response = []  #EMPTY DICTIONARY

    for(a,b,c,d,e) in mycursor:
        response.append({                           #Add value in dictionary 
            'product_id': a,
            'name': b,
            'uom_id' : c,
            'price_per_unit' : d,
            'uom_name':e
        })
    return response


if __name__=='__main__':
    connection=get_sql_connection()
    print(get_all_products(connection))