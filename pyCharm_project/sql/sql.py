import MySQLdb
host = '192.168.1.100'
user = 'songqin'
passwd = 'songqin'
dbname = 'plesson'
port = 3306

connection = MySQLdb.connect(host=host,
                             user=user,
                             passwd=passwd,
                             db=dbname,
                             port=port,
                             charset = 'utf8'
                             )
c = connection.cursor()
c.execute('SELECT * from sq_course WHERE id = 82')

row_num = c.rowcount
print(row_num)

for one in range(row_num):
    a = c.fetchone()
    print(a)


