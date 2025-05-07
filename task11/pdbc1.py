import pymysql

class Customers:
    def __init__(self):
        pass

    def insert_rows(self):
        con = None
        cursor = None
        try:
            con = pymysql.connect(host='localhost', database='project', user='root', password='1234')
            cursor = con.cursor()
            while True:
                cid = int(input('Enter customer Id: '))
                cname = input('Enter customer name: ')
                address = input('Enter customer address: ')
                pin = int(input('Enter pin code: '))
                q = "INSERT INTO customers (cid, cname, address, PIN) VALUES (%s, %s, %s, %s)"
                cursor.execute(q, (cid, cname, address, pin))
                
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

customer = Customers()
customer.insert_rows()
