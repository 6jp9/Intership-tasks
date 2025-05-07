import pymysql

class Orders:
    def __init__(self):
        pass

    def insert_rows(self):
        con = None
        cursor = None
        try:
            con = pymysql.connect(host='localhost', database='project', user='root', password='1234')
            cursor = con.cursor()
            while True:
                oid = int(input('Enter order id : '))
                cid = int(input('Enter customer Id: '))
                
                q = "INSERT INTO orders (oid, cid) VALUES (%s, %s)"
                cursor.execute(q, (oid,cid))
                
                ans = input('Do you want to add another record? [yes|no]: ')
                if ans.lower() == 'no':
                    con.commit()
                    print("Records committed successfully.")
                    break
        except pymysql.MySQLError as e:
            if con:
                con.rollback()
            print("Database error occurred:", e)
        except Exception as e:
            if con:
                con.rollback()
            print("Unexpected error:", e)
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

customer = Orders()
customer.insert_rows()
