# Q1::
# create a parking system using a class name "Vehicle".
# # max parking slot is 2, then show parking full.
# #create object by passing : vehNo,vehType,Hrs to park.
# # parking means a list "vehiclelist", that contain slot no. and vehicle details as a dictionary.
# # vehicle details again a dictionary.
# # vehiclelist=[{slot:{VehDetals}},{slot:{VehDetals}}]
# # create a fn add() outside the class to add vehicle to the parking slot.
# # create a fn remove() outside the class to remove vehicle from the parking slot.(by calling slot no.)
# # when vehicle exits/remove , show the amount to pay.
# # for two wheels R 10/hr
# # for others R 20/hr
# # [{slot1:{v1 details},slot2:{v2 details}}]


#Current time
# from datetime import datetime
# def CurrentTime():
#     Now=datetime.now()
#     current_time=Now.strftime("%H:%M:%S")
#     return current_time
#
# #Errors
# class CarSlotFull(Exception):
#     pass
# class VehicleDetailsError(Exception):
#     pass
#
#
# # VehDetails = {"slot_1": "vaccant", "slot_2": "vaccant"}
# VehDetails ={'slot_1': {'Vehicle_Number': 'NONE', 'Vehicle_Type': 'NONE', 'Entry_Time': 'NONE'},
#  'slot_2': {'Vehicle_Number': 'NONE', 'Vehicle_Type': 'NONE', 'Entry_Time': 'NONE'}}
# Empty={'Vehicle_Number': 'NONE', 'Vehicle_Type': 'NONE', 'Entry_Time': 'NONE'}
# class Vehicle():
#     details={}
#     Time=""
#     def Add_Vehicle(self,Vehdict):
#         try:
#             if (VehDetails["slot_1"]["Vehicle_Number"]=="NONE"):
#                 VehDetails["slot_1"]=Vehdict
#             elif (VehDetails["slot_2"]["Vehicle_Number"]=="NONE"):
#                 VehDetails["slot_2"] = Vehdict
#             else:
#                 raise CarSlotFull()
#         except CarSlotFull:
#             print("Car slots are filled")
#             print(VehDetails)
#
#     def VehicleInfo(self):
#         l=[VehDetails]
#         print(l)
#
#     def Removing(self):
#         Remove_Car=input("Enter the vehicle Number")
#         try:
#             if (VehDetails["slot_1"]["Vehicle_Number"]==Remove_Car):
#                 self.details = {'Vehicle_Number': VehDetails["slot_1"]["Vehicle_Number"], 'Vehicle_Type': VehDetails["slot_1"]["Vehicle_Type"],
#                      'Entry_Time': VehDetails["slot_1"]["Entry_Time"]}
#                 self.Time = VehDetails["slot_1"]['Entry_Time']
#                 VehDetails["slot_1"]=Empty
#             elif (VehDetails["slot_2"]["Vehicle_Number"]==Remove_Car):
#                 self.details = {'Vehicle_Number': VehDetails["slot_2"]["Vehicle_Number"],
#                      'Vehicle_Type': VehDetails["slot_2"]["Vehicle_Type"],
#                      'Entry_Time': VehDetails["slot_2"]["Entry_Time"]}
#                 self.Time = VehDetails["slot_2"]['Entry_Time']
#                 VehDetails["slot_2"] = Empty
#             else:
#                 raise VehicleDetailsError()
#         except VehicleDetailsError:
#             print("Entered number is wrong")
#
#
#     def Amount(self):
#         x=60
#         crnt=CurrentTime()
#         End=crnt.split(":")
#         ##EndTime
#         Endhr=End[0]
#         Endmin = End[1]
#         Endhrs=int(Endhr)
#         EndMins=int(Endmin)
#         ##Starttime
#         start = self.Time.split(":")
#         startHR=start[0]
#         startMIN=start[1]
#         StartHrs=int(startHR)
#         StartMins=int(startMIN)
#         ##Total time Acquired
#         totalhrs=(Endhrs-StartHrs)*60
#         totalmins=EndMins-StartMins
#         totaltime=totalhrs+totalmins
#         if self.details["Vehicle_Type"]=="2-wheeler":
#             if totaltime<=60:
#                 print("pay 10 Rs")
#             else:
#                 max=(totaltime/60)*10
#                 print("pay",max)
#         else:
#             if totaltime <= 60:
#                 print("pay 20 Rs")
#             else:
#                 max=(totaltime/60)*20
#                 print("pay", max)
#
# class Method():
#     def Adding(self):
#         VehNO = input("Enter the vehicle details")
#         VehTYPE = int(input("Enter the type of Vehicle, if 2-wheeler press-1,if not press key-2"))
#         if (VehTYPE == 1):
#             Veh123 = "2-wheeler"
#         elif (VehTYPE == 2):
#             Veh123 = "Car/Heavy"
#         else:
#             Veh123 = "Car"
#         Hours = CurrentTime()
#         #########
#         dictVeh ={"Vehicle_Number":VehNO,"Vehicle_Type":Veh123,"Entry_Time":Hours}
#         V1 = Vehicle()
#         V1.Add_Vehicle(dictVeh)
#
#
#
#
# while True:
#     inputNumber=int(input("For Parking press-1 , For Taking back press-2 , For Parking Details press 3 ,For Exit press-0::"))
#     c1 = Method()
#     v1=Vehicle()
#     if (inputNumber==1):
#         c1.Adding()
#         # print(x)
#     elif(inputNumber==2):
#         v1.Removing()
#         v1.Amount()
#     elif(inputNumber==3):
#         v1.VehicleInfo()
#     else:
#         break


##############################################
####################
##########
count=0
vehiclelist=[]
class Vehicle:
   def __init__(self,no,type,hour):
       self.no=no
       self.type=type
       self.hour=hour
def add():
   global count
   print(vehiclelist)
   if(len(vehiclelist)<2):
       a=input("enter vehicle no :")
       b=int(input("enter type of vehicle :"))
       c=int(input("enter hrs to park :"))
       obj=Vehicle(a,b,c)
       print(obj.__dict__)
       vehiclelist.append({count:obj.__dict__})
       print(vehiclelist)
       for vehicle in vehiclelist:
           print(vehicle)
           for k,v in vehicle.items():
               print(k)
               print(v)
       file = open("Parking_slot.txt", "a")
       file.write(a)
       file.write(" "+str(b))
       file.write(" "+str(c)+"\n")
       count=count+1
   else:
       print(vehiclelist)
       print("************slot is full****************")

def remove(sltno):
    global count
    for dict in vehiclelist:
       print(dict)
       for k,v in dict.items():
           if(k==sltno):
                if(v['type'] == 2):
                    amount=v['hour']*10
                    print("Amount to be paid",amount,"INR")
                    del vehiclelist[sltno]
                    count=sltno
                    print(vehiclelist)
                    break;
                else:
                    amount = v['hour'] * 20
                    print("Amount to be paid", amount, "INR")
                    del vehiclelist[sltno]
                    count = sltno
                    print(vehiclelist)
                    break;
    else:
        if(len(vehiclelist)==0):
            print("slots are empty")
    print("vehicles left in parking",vehiclelist)

while True:
    a=int(input("Enter 1 for parking and 2 for exit and 3 for close the app:"))
    if a==1:
        add()
    elif a==2:
        d=int(input("enter vehicle slot to exit from parking :"))
        for dict in vehiclelist:
            if (d in dict):
                remove(d)
                break
            else:
                print("invalid slot")
    elif a==3:
        print("thank you..")
        break
    else:
        print("invalid input")

































































































































































































