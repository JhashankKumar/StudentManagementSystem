import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Jhashank@190703',
    database='student_dashboard',
    cursorclass=pymysql.cursors.DictCursor
)
