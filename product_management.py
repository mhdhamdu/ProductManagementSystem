from idlelib import query

import mysql.connector

class ProductManager:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="MuHamdammed@77",
            database="shop_db"
        )

        self.cursor=self.connection.cursor(dictionary=True)
        print("Database connected successfully")

    def get(self):
        query= "select * from product"
        self.cursor.execute(query)
        result=self.cursor.fetchall()

        for row in result:
            print(row)

    def get_object(self, id):
        query="select * from product where id = %s"
        self.cursor.execute(query,(id,))
        result=self.cursor.fetchone()
        return result

#to retrive
    def retrieve(self, id):
        result=self.get_object(id)

        if result:
            print("Product Details:")
            print(result)
        else:
            print("Product not found")

#insert product datas
    def post(self, **kwargs):
        query="""
        insert into product(name, category, price, quantity, manufacturer)
        values (%s,%s,%s,%s,%s)
        """

        values = (
            kwargs["name"],
            kwargs["category"],
            kwargs["price"],
            kwargs["quantity"],
            kwargs["manufacturer"]
        )

        self.curser.execute(query, values)
        self.connection.commit()
        print("Product added successfully")


    