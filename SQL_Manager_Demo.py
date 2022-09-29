import mysql.connector

#Getting Required Vars
print("Enter The Requied Data To Connect SQL Server")
host=input("Enter Host Address: ")
us_name=input("Enter The Username: ")
passwd=input("Enter The Password: ")
"""host="localhost"#input("Enter Host Address: ")
us_name="root"#input("Enter The Username: ")
passwd="1234"#input("Enter The Password: ")"""
db_name=''

#Connecting To DataBase Server
db = mysql.connector.connect(host=host,user=us_name,passwd=passwd)
print("Connected To DataBase Server Successfully!")
#1 Creating a DataBase
def Create_db(db_name):
    db_name=input("Enter a DataBase Name: ")
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+db_name)
    print("DataBase "+db_name+" Created Successfully!")
    Menu(db_name)

#2 Checking If Data Base Is Created Or Not
def Show_db(db_name):
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd)
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)
    Menu(db_name)

#3 Create a Table
def Create_Table(db_name):
    db_name=input("Enter The DataBase Name: ")
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd,database=db_name)
    cursor = db.cursor()
    db_table=input("Enter a Table Name: ")
    db_table=db_table.lower()
    cmd="CREATE TABLE IF NOT EXISTS "+db_table+" (ID INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(25),RollNo VARCHAR(10),Address VARCHAR(30))"
    cursor.execute(cmd)
    print("DataBase Table "+db_table+" Created Successfully!")
    Menu(db_name)

def Display_TableForm(db_name):
    db_name=input("Enter The DataBase Name: ")
    db_table=input("Enter a Table Name: ")
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd,database=db_name)
    cursor = db.cursor()
    cmd="SELECT * FROM "+db_table
    cursor.execute(cmd)
    print(cursor.fetchall())
    Menu(db_name)

#4 Show Tables Available in DataBase
def Display_Tab(db_name):
    db_name=input("Enter The DataBase Name: ")
    print(db_name)
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd,database=db_name)
    cursor = db.cursor()
    cmd="SHOW TABLES"
    cursor.execute(cmd)
    i=0
    for x in cursor:
        print(x)
        i+=1
    print(str(i)+" Tables")
    Menu(db_name)

#5 Inserting Records In The DataBase
def Insert_Rec_db(db_name):
    db_name=input("Enter The DataBase Name: ")
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd,database=db_name)
    cursor = db.cursor()
    print("Enter The Details:")
    db_table=input("Enter the Name Of the Table: ")
    db_table=db_table.lower()
    x=input("Do You Want to Enter Multiple Records into The Table? \nEnter [Y/N]:") 
    if(x=='y' or x=='Y'):
        n=int(input("Enter No.of Records :")) 
        for i in range(0,n):
            print("\nEnter the ",i+1,"Record..") 
            S_name=input("Enter the Student Name: ")
            S_roll=input("Enter the RollNo: ")
            S_address=input("Enter the Address: ")
            cmd = "INSERT INTO "+db_table+" (Name,RollNo,Address) VALUES (%s,%s,%s)"
            val=(S_name,S_roll,S_address)
            cursor.execute(cmd,val)
            db.commit()
    else:
        print("Enter The Details:")
        S_name=input("Enter the Name Of the Student: ")
        S_roll=input("Enter The RollNo: ")
        S_address=input("Enter The Address: ")
        cmd = "INSERT INTO "+db_table+" (Name,RollNo,Address) VALUES (%s,%s,%s)"
        val=(S_name,S_roll,S_address)
        cursor.execute(cmd,val)
        db.commit()
    print("Records Added Successfully!")
    Menu(db_name)

#6 Display All the Data From Database
def Display_Rec(db_name):
    db_name=input("Enter The DataBase Name: ")
    i=0
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd,database=db_name)
    cursor = db.cursor()
    db_table=input("Enter the Name Of the Table: ")
    db_table=db_table.lower()
    cmd="SELECT * FROM "+db_table
    cursor.execute(cmd)
    res=cursor.fetchall()
    print("\n")
    for x in res:
        print(x)
        i+=1
    if(i>0):
        print(i," Records Displayed Successfully!") 
    else:
        print("No Records - Empty Table")
    Menu(db_name)

#7 Deleting Record From Database
def Delete_Rec(db_name):
    db_name=input("Enter The DataBase Name: ")
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd,database=db_name)
    cursor = db.cursor()
    db_table=input("Enter the Name Of the Table: ")
    xid=input("Enter the ID to Delete The Record (Row): ")
    cmd="DELETE FROM "+db_table+" WHERE id = "+str(xid)
    cursor.execute(cmd)
    db.commit()
    print("Record Deleted Successfully!")
    Menu(db_name)

#8 Deleat Table
def Delete_Tab(db_name):
    db_name=input("Enter a DataBase Name: ")
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd,database=db_name)
    cursor = db.cursor()
    db_table=input("Enter the Name Of the Table: ")
    x=input("Warning\nAre You Sure You Want To Delete The Table?\nEnter [Y/N]: ")
    if(x=='y' or x=='Y'):
        cmd="DROP TABLE "+db_table
        cursor.execute(cmd)
        print("Table "+db_table+" Deleted Successfully!")
    Menu(db_name)

#9 Deleting The Complete DataBase 🥲
def Delete_db(db_name):
    db_name=input("Enter a DataBase Name to Delete: ")
    db = mysql.connector.connect(host=host,user=us_name,passwd=passwd)
    cursor = db.cursor()
    x=input("Warning\nAre You Sure You Want To Delete The DataBase?\nEnter [Y/N]: ")
    if(x=='y' or x=='Y'):
        cmd="DROP DATABASE "+db_name
        cursor.execute(cmd)
        db.commit()
        print("DataBase "+db_name+" Deleted Successfully!")
    Menu(db_name)

#10 A Menu To Make This Program Effective
def Menu(db_name=''):
    cmd = "INSERT INTO  (Name,RollNo,Address) VALUES (%s,%s,%s)"
    print(cmd)
    Op=int(input("""\n
###############################[ Menu ]###############################
#                Reply An Operation To Be Performed:                 #
#********************************************************************#
# 1. Create DataBase                 2. Show Available DataBase      #
# 3. Create a Table                  4. Show Available Tables        #
# 5. Insert Records in Table         6. Display All Records in Table #
# 7. Delete a Record                 8. Delete a Table               #
# 9. Delete The Complete DataBase    10. Exit                        #
######################################################################
                         Enter an Option: """))
    if(Op==1):
        Create_db(db_name)
    elif (Op==2):
        Show_db(db_name)
    elif (Op==3):
        Create_Table(db_name)
    elif (Op==4):
        Display_Tab(db_name)
    elif (Op==5):
        Insert_Rec_db(db_name)
    elif (Op==6):
        Display_Rec(db_name)
    elif (Op==7):
        Delete_Rec(db_name)
    elif (Op==8):
        Delete_Tab(db_name)
    elif (Op==9):
        Delete_db(db_name)
    elif (Op==10):
        print("\nProgram Finished")
        return
    else:
        print("Invalid Input")
        Menu(db_name)
Menu(db_name)
