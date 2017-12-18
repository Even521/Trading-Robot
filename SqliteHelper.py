import  yaml,sqlite3
with open("./application.yaml") as f:
    resource=yaml.load(f)
class SqliteHelper:
    def __init__(self):
        try:
            self.conn=sqlite3.connect(resource['db']['sqlite'])
        except sqlite3.Error as e:
            print('链接sqlite数据库失败%s',e.args[0])
    def getcursor(self):
        return self.conn.cursor()

    def drop(self, table):
        '''
        if the table exist,please be carefull
        '''
        if table is not None and table != '':
            cu = self.getcursor()
            sql = 'DROP TABLE IF EXISTS ' + table
            try:
                cu.execute(sql)
            except sqlite3.Error as why:
                print ("delete table failed:", why.args[0])
                return
            self.conn.commit()
            print ("delete table successful!")
            cu.close()
        else:
            print ("table does not exist！")

    def create(self, sql):
        '''
        create database table
        :param sql:
        :return:
        '''
        if sql is not None and sql != '':
            cu = self.getcursor()
            try:
                cu.execute(sql)
            except sqlite3.Error as why:
                print ("create table failed:", why.args[0])
                return
            self.conn.commit()
            print ("create table successful!")
            cu.close()
        else:
            print ("sql is empty or None")

    def insert(self, sql, data):
        '''
        insert data to the table
        :param sql:
        :param data:
        :return:
        '''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.getcursor()
                try:
                    for d in data:
                        cu.execute(sql, d)
                        self.conn.commit()
                except sqlite3.Error as why:
                    print ("insert data failed:", why.args[0])
                cu.close()
        else:
            print ("sql is empty or None")

    def fetchall(self, sql):
        '''
        query all data
        :param sql:
        :return:
        '''
        if sql is not None and sql != '':
            cu = self.getcursor()
            try:
                cu.execute(sql)
                content = cu.fetchall()
                if len(content) > 0:
                    for item in content:
                        for element in item:
                            print (element,)
                        print(''
                              )
                else:
                    for element in content:
                        print (element,)
                    print ('')
            except sqlite3.Error as why:
                print ("fetchall data failed:", why.args[0])
            cu.close()
        else:
            print ("sql is empty or None")

    def fetchone(self, sql, data):
        '''
        query one data
        :param sql:
        :param data:
        :return:
        '''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.getcursor()
                try:
                    d = (data,)
                    cu.execute(sql, d)
                    content = cu.fetchall()
                    if len(content) > 0:
                        for item in content:
                            for element in item:
                                print (element,)
                            print ('')
                    else:
                        for element in content:
                            print (element,)
                        print ('')
                except sqlite3.Error as why:
                    print ("fetch the data failed:", why.args[0])
                    return
                cu.close()
        else:
            print ("sql is empty or None")

    def update(self, sql, data):
        '''
        update the data
        :param sql:
        :param data:
        :return:
        '''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.getcursor()
                try:
                    for d in data:
                        cu.execute(sql, d)
                        self.conn.commit()
                except sqlite3.Error as why:
                    print ("update data failed:", why.args[0])
                cu.close()
        else:
            print ("sql is empty or None")

    def delete(self, sql, data=None):
        '''
        delete the data
        :param sql:
        :param data:
        :return:
        '''
        if sql is not None and sql != '':
            cu = self.getcursor()
            if data is not None:
                try:
                    for d in data:
                        cu.execute(sql, d)
                        self.conn.commit()
                except sqlite3.Error as why:
                    print ("delete data failed:", why.args[0])
            else:
                try:
                    cu.execute(sql)
                    self.conn.commit()
                except sqlite3.Error as why:
                    print ("delete data failed:", why.args[0])
            cu.close()
        else:
            print ("sql is empty or None")

    def __del__(self):
        self.conn.close()
