from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.product_name, products.uom_id, products.price_per_unit, uom.uom_name  FROM grocery_store.products INNER JOIN grocery_store.uom ON products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': product_name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO grocery_store.products "
             "(product_name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data =  (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM grocery_store.products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == "__main__":
    connection = get_sql_connection()
    print(insert_new_product(connection,{'product_name':'layz red'
                                         ,'uom_id':'1'
                                         ,'price_per_unit':'190'
    }))