import mysql.connector as m
def getConnection():
    connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
    return connection

# def createtable():
#     con=getConnection()
#     cursor=con.cursor()
#     cursor.execute("create table Bank (ID int primary key,ACCOUNT_NUMBER varchar(40),NAME varchar(40),BANK_NAME varchar(40) default 'AXISBANK',"
#                    "IFSC_CODE Varchar(40) default 'UIDM456',BALANCE int default 10000)")
#     con.commit()
#     cursor.close()
#     con.close()

# createtable()


def insertvalues(id,accno,name):
    con=getConnection()
    cursor=con.cursor()
    cursor.execute("insert into bank values (%s,%s,%s,'AXISBANK','UDIM456',10000)",(id,accno,name))
    con.commit()
    cursor.close()
    con.close()

# insertstudent(106,"DIYA1234","DIYA")
# insertstudent(107,"DEV5678","DEV")
# insertstudent(108,"MARIA9101","MARIA")
# insertstudent(109,"BEN1112","BEN")
# insertstudent(110,"ABNU1314","ABNU")
# insertstudent(111,"ELDHO1516","ELDHO")
# insertstudent(112,"BABU1718","BABU")
# insertstudent(113,"KIRAN1920","KIRAN")

def deposit(amount,name):
    con=getConnection()
    cursor=con.cursor()
    cursor.execute("update bank set BALANCE=BALANCE+(%s) where NAME= %s",(amount,name))
    con.commit()
    cursor.close()
    con.close()
#
# deposit(500,"AROMAL")

def withdraw(amount,name):
    con=getConnection()
    cursor=con.cursor()
    cursor.execute("update bank set BALANCE=BALANCE-(%s) where NAME= %s",(amount,name))
    con.commit()
    cursor.close()
    con.close()
#
# withdraw(500,"Amal")

def balance(name):
    con=getConnection()
    cursor=con.cursor()
    cursor.execute("select * from bank where name = (%s)",(name,))
    result=cursor.fetchall()
    # con.commit()
    cursor.close()
    con.close()
    for i in result:
        print("ID :",i[0],"\nACCOUNT NUMBER :",i[1],"\nNAME :",i[2],"\nBANK NAME :",i[3],"\nIFSC_CODE :",i[4],"\nBALANCE :",i[5])

# balance("AROMAL")

def balnew(name):
    con=getConnection()
    cursor=con.cursor()
    cursor.execute("select * from bank where name = (%s)",(name,))
    result=cursor.fetchall()
    # con.commit()
    cursor.close()
    con.close()
    for i in result:
        return i[5]

# print (balnew("aromal"))

class AccountHolder():
    def __init__(self,Name,AccNo):
        self.name=Name
        self.accno=AccNo
    def Deposit(self,amount):
        deposit(amount,self.name)
        print("amount deposited:",amount)
        print("Balance Amount:",balnew(self.name))
    def Widraw(self,amount):
        x=balnew(self.name)-amount
        if x>1000:
            print("amount",amount,"has wihdrawed")
            withdraw(amount,self.name)
        else:
            print("insufficient balance")
    def Balance(self):
        balance(self.name)

bnk=AccountHolder("aromal",1546468)
# bnk.Deposit(11000)
# bnk.Widraw(1000)
# bnk.Balance()








































