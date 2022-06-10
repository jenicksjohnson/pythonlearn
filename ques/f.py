vlist=[]
class Vehicle:
   def __init__(self,no,type,hour):
       self.no=no
       self.type=type
       self.hour=hour

def add():
   f = open("data.txt", "r")
   d = f.readlines()
   f.close()
   if(len(d)<2):
       a=input("enter vehicle no :")
       b=input("enter type of vehicle :")
       c=input("enter hrs to park :")
       obj=Vehicle(a,b,c)
       vlist.append(obj.no)
       vlist.append(obj.type)
       vlist.append(obj.hour)
       print("details:" ,obj.no,obj.type,obj.hour)
       file=open("data.txt","a")
       file.write(str(obj.no))
       file.write(" " + str(obj.type))
       file.write(" " + str(obj.hour)+"\n")
   elif (len(d)>=2):
       print("************ sorry..! slot full ****************")

def update_data():
    new_file = open("data.txt", "w")
    for line in d:
        new_file.write(line)
    new_file.close()

def remove():
    v=input("enter vehicle number :")
    f = open("data.txt", "r")
    global d
    d = f.readlines()
    print(d)
    if len(d) == 1:
        V1 = (d[0].strip("\n"))
        V1 = (V1.split(" "))
        if V1[0] == v:
            if V1[1] == '2':
                amount = int(V1[2]) * 10
                print("Pay Rs:",amount)
                del d[0]
                update_data()
            else:
                amount = int(V1[2]) * 20
                print("Pay Rs:",amount)
                del d[0]
                update_data()
        else:
            print("invalid input")
    elif len(d) == 2:
        V1 = (d[0].strip("\n"))
        V1 = (V1.split(" "))
        V2 = (d[1].strip("\n"))
        V2 = (V2.split(" "))

        if V1[0] == v:
            if V1[1] == '2':
                amount = int(V1[2]) * 10
                print("Pay Rs:",amount)
                del d[0]
                update_data()
            else:
                amount = int(V1[2]) * 20
                print("Pay Rs:",amount)
                del d[0]
                update_data()
        elif V2[0] == v:
            if V2[1] == '2':
                amount = int(V2[2]) * 10
                print("Pay Rs:",amount)
                del d[1]
                update_data()
            else:
                amount = int(V2[2]) * 20
                print("Pay Rs:",amount)
                del d[1]
                update_data()
        else:
            print("invalid input")
