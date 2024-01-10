import pymysql

from metasingltone import MetaSingleton
# from console import DataBase

class DataBase(metaclass = MetaSingleton):
    def connection(self):
        self.db = pymysql.connect(
            host='95.154.68.63',
            port=3306,
            user='student',
            password='Hn523cv-',
            db='Prodivers_LD_DB',
        )
        self.cursor = self.db.cursor()
       

    def add_product(self, product, categories, price, storage):
        self.connection()

        self.cursor.execute(f"select id from categories where name = '{categories}'")
        category_id = self.cursor.fetchone()[0] 
        self.cursor.execute(f"select id from storage where name = '{storage}'")
        storage_id = self.cursor.fetchone()[0] 

        if category_id and storage_id:
            self.cursor.execute(f"select * from products where name = '{product}' and category_id = {category_id} and storage_id = {storage_id}")
            data = self.cursor.fetchone()
            if data is None:
                self.cursor.execute(f"insert products (name, category_id, price, storage_id ) values ('{product}', {category_id}, {price}, {storage_id})")
                self.db.commit()
        

        self.db.close() 

    def add_categories(self, categories):
        self.connection()

        self.cursor.execute(f"insert categories (name) values('{categories}')")

        self.db.commit()
        self.db.close()

    def add_storage(self, storage, address, product_availability):
        self.connection()

        self.cursor.execute(f"insert storage (name, address, product_availability) values('{storage}', '{address}', '{product_availability}')")

        self.db.commit()
        self.db.close()

    def del_categories(self, categories):
        self.connection()

        self.cursor.execute(f"delete from categories where name = '{categories}'")

        self.db.commit()
        self.db.close()
        
    def del_product(self, product):
        self.connection()

        self.cursor.execute(f"delete from categories where name = '{product}'")

        self.db.commit()
        self.db.close()

    def del_storage(self, storage):
        self.connection()

        self.cursor.execute(f"delete from categories where name = '{storage}'")

        self.db.commit()
        self.db.close()

    def newname_categories(self, old_categories, new_categories ):
        self.connection()

        self.cursor.execute(f"update categories set name = '{new_categories}' where name = '{old_categories}'")

        self.db.commit()
        self.db.close()

    def newname_product(self, old_product, new_product ):
        self.connection()

        self.cursor.execute(f"update categories set name = '{new_product}' where name = '{old_product}'")

        self.db.commit()
        self.db.close()

    def newname_storage(self, old_storage, new_storage ):
        self.connection()

        self.cursor.execute(f"update categories set name = '{new_storage}' where name = '{old_storage}'")

        self.db.commit()
        self.db.close()

    def get_data_product(self, id):
        self.connection()

        self.cursor.execute(f"select * from products where id = {id}")
        data = self.cursor.fetchone()
        print(data)
        
        self.db.close()
    
    def get_data_categories(self, id):
        self.connection()

        self.cursor.execute(f"select * from categories where id = {id}")
        data = self.cursor.fetchone()
        print(data)
        
        self.db.close()

    def get_data_storage(self, id):
        self.connection()

        self.cursor.execute(f"select * from storage where id = {id}")
        data = self.cursor.fetchone()
        print(data)
        
        self.db.close()
db = DataBase()
 

db.add_product('SandyParadise', 'суперкрасивые', '80000', 'ProDivers')
db.add_storage('ProDivers_2', 'Карбышева 44', '25')
db.add_categories('оченькрасивые')
db.del_categories('оченькрасивые')
db.newname_categories('оченькрасивые', 'суперкрасивые')
db.newname_product('', '')
db.get_data_product(9)
db.get_data_categories(3)
db.get_data_storage(3)
