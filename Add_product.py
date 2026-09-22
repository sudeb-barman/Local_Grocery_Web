from get_sql_connection import get_sql_connection



def order(connection,product_name,unit,price):

    mycursor=connection.cursor()
    # mycursor.execute("SELECT * FROM manage_product")
    # for i in mycursor:
    #     print(i)

    # product_name=input("Enter the product name: ")
    # unit=input("if unit is each then press 1 , other wise 2: ")
    # price=input("price: ")

    query = "INSERT INTO manage_product(name,uom_id,price_per_unit) VALUES" \
    "(%s,%s,%s);"
    product=(product_name,unit,price)

    mycursor.execute(query,product)

    connection.commit()
    # print("Product Inserted")\