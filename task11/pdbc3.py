import pymysql

class merchant:
    def __init__(self):
        pass

    def insert_rows(self):
        con = None
        cursor = None
        try:
            con = pymysql.connect(host='localhost', database='project', user='root', password='1234')
            cursor = con.cursor()
            while True:
                mid = int(input('Enter merchant Id: '))
                product_name = input('Enter product_name: ')
                amount = float(input('Enter amount: '))
                oid = int(input('Enter oid: '))
                q = "INSERT INTO merchant (mid, product_name, amount, oid) VALUES (%s, %s, %s, %s)"
                cursor.execute(q, (mid, product_name, amount,oid))
                
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

customer = merchant()
customer.insert_rows()
