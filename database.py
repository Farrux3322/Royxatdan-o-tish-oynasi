import mysql.connector


class Core:

    def __init__(self) -> None:
        self.usedDatabases()
        self.createTable()


    def usedDatabases(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                database = 'madaminovdb',
                user = 'root',
                password = 'farrux3322'
            )
        except Exception as err:
            print(err)
        else:
            print('Databazaga ulandi.')

    def createTable(self):
        try:
            with self.conn.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS user(
                            id SERIAL,
                            username VARCHAR(32) NOT NULL UNIQUE,
                            password VARCHAR(32) NOT NULL 
                )'''
                cursor.execute(sql)
        except Exception as err:
            print(err)
        else:
            print('Jadval yasaldi.')

    def createUser(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''INSERT INTO user (username, password) VALUES ('{username}', '{password}');'''
                cursor.execute(sql)
        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            print('''Foydalanuvchi qo'shildi.''')

    def getAllUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f'''SELECT username, password FROM user'''
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            return(err)
        else:
            print('''Ma'lumotlar olindi.''')
            return(result)

    def updateUser(self, username, password, newusername):
        try:
            with self.conn.cursor() as cursor:
                query = f'''UPDATE user SET username = '{newusername}' WHERE '{username}' = username AND '{password}' = password'''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            print('''Username yangilandi.''')
    
    def updatePassword(self, username, password, newpassword):
        try:
            with self.conn.cursor() as cursor:
                query = f'''UPDATE user SET password = '{newpassword}' WHERE '{username}' = username AND '{password}' = password'''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            print('''Username yangilandi.''')

    def deleteUser(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                query = f'''DELETE FROM user WHERE '{username}' = username AND password = "{password}"'''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            print('''User o'chirildi.''')

