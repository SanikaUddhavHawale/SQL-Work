import mysql.connector as con
##print("connection established")

mydb=con.connect(host="localhost",user="root",password="",database='yogesh')
##print("connection established")

db_cursor=mydb.cursor()
##db_cursor.execute("create database yogesh")
##print("database created")

##db_cursor.execute("use yogesh;")
##print("database selected")

##db_cursor.execute("create table emp(id int,name char(20))")
##print("table emp created....")

##db_cursor.execute("show tables")
##for i in db_cursor:
##    print(i)

##db_cursor.execute("insert into emp(id,name) values (101,'ram'),(102,'bheem'),(103,'anirudh'),(104,'robin')")
##mydb.commit()
##print(db_cursor.rowcount,"record inserted successfully")

##db_cursor.execute("select * from emp")
##obj_select=db_cursor.fetchall()
##print(obj_select)

##db_cursor.execute("update emp set name='anurag' where id=104")
##mydb.commit()
##print(db_cursor.rowcount,"data update successfully...")

##db_cursor.execute("select * from emp")
##obj_select=db_cursor.fetchall()
##print(obj_select)

##db_cursor.execute("delete from emp where id in(102,104)")
##mydb.commit()
##print(db_cursor.rowcount,"data delete successfully...")

##db_cursor.execute("select * from emp")
##obj_select=db_cursor.fetchall()
##print(obj_select)

db_cursor.execute("truncate table emp")
mydb.commit()
print("all data delete successfully...")


