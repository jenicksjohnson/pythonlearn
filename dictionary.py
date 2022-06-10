###############################################################################
# creating
s={}
print(type(s))
d=dict()
print(type(d))

# q={"a":5,"b":23,55:"c"}
# print(q)

# q=dict([("a",1),("b",2)])
# print(q)

# w=dict(((1,55),(2,34),(3,567)))
# print(w)

# getting values
# q={"a":123,"b":456,55:"abc"}
# print(q["a"])
# print(q.get("a"))
# print(q.get(55))

# print(q[55])
# q["x"]=45                          # for adding a key and an element
# print(q)
# q["a"]="bad"
# print(q)

# removing and return an element
# q={"a":234,"b":456,"c":45356,67:"abcd"}
# r=q.pop("c")
# print(r)
# print(q)

# removes last item
# q.popitem()
# print(q)

# delete the value of given
# del q["a"]
# print(q)

# clear the dictionary
# q.clear()
# print(q)

# delete the dictionary
# del q
# print(q)

# copying a dict
# q={"a":234,"b":432,"c":342}
# b=q.copy()
# print(b)

# programme to change the city
sampledict={"name":"kelly","age":25,"salary":8000,"city":"newyork"}
print(sampledict)
sampledict.popitem()
sampledict["location"]="new york"
print(sampledict)

# or
# sampledict["location"]=sampledict.pop("city")
# print(sampledict)

# giving values to dictionary
# sample={}
# sample["name"]=input("Enter your name:: ")
# sample["age"]=int(input("Enter your age:: "))
# sample["salary"]=int(input("Enter your salary:: "))
# sample["location"]=input("enter your location:: ")
# print(sample)
# or
# dict={}
# for i in range(4):
#     key=input("enter the key:: ")
#     value=input("enter the value:: ")

######################################################################################################
# s={}.fromkeys(["maths","chem","phy"],0)                     #can only add one value for all keys
# print(s)

# s={}.fromkeys(["maths","chem","phy"],(1,2,3))               #can only add one value for all keys
# print(s)

# s={}.fromkeys(["maths"],0)                                  #can only add one value for all keys
# print(s)

# s={}.fromkeys("maths",0)                                    #can only add one value for all keys
# print(s)

###########################################################################
# Important ::::

# s={"a":123,"b":2346,"c":87676}
# a=s.items()
# print(a)
# print(type(a))
# print(s.keys())
# print(s.values())

###########################################################################
# adding keys and values
# s={"a":123,"b":2346,"c":87676}
# s.update({"ann":"cs","akhil":"mech"})
# print(s)
# s.update([("ash","eee"),("sam","civil")])
# print(s)

# print(dir(s))

##############################################################################
# d={"a":10,"b":20,"c":30}
# for item in d:
#     print(item)
# for item in d.items():
#     print(item)
# for item in d.keys():
#     print(item)
# for item in d.values():
#     print(item)
# for k,v in d.items():
#     print(k)
#     print(v)
#     print("key :",k,"and value : ",v)

#######################################################################
# find the sum
# d={"maths":10,"chemistry":50,"english":40}
# sum=0
# for i in d.values():
#     sum+=i
# print("total marks:",sum)

# or
# print("the sum of all is:",sum(d.values()))
#######################################################################
# find the maximum value
# d={"maths":10,"chemistry":50,"english":40}
# print("the maximum value is",max(d.values()))

# or
# l=[]
# for i in d.values():
#    l.append(i)
# s=sorted(l)
# print("maximum value is:",s[-1])

# or
# max=0
# for v in d.values():
#     if v>max:
#         max=v
# print(max)

###########################################################################
# find key value pair if value is greater than 2
# d={"a":1,"b":5,"c":0,"d":3}
# new={}
# for i,j in d.items():
#     if j>2:
        # new.update({i:j})
        # new[i]=j
# print(new)

##############################################################################
# using dict comprehension
# d={"a":1,"b":5,"c":0,"d":3}
# new={i:j for i,j in d.items() if j>=2}
# print(new)

############################################################################
# d={"a":1,"b":5,"c":0,"d":3}
# new={i+"c":j**2 for i,j in d.items()}
# print(new)

##############################################################################
# nested dict
# d={101:{"name":"ram","mark":100},102:{"name":"bibin","mark":99}}
# print(d)
# print(d[101])
# print(d[101]["name"])
# print(d[101]["mark"])

################################################################################
# change salary of varsha to 70000
# d={"emp1":{"name":"John","salary":7500},
#    "emp2":{"name":"Emma","salary":8000},
#    "emp3":{"name":"Varsha","salary":6500}}

# d["emp3"]["salary"]=70000
# print(d)

# new={}
# for i,j in d.items():
    # print(i)
    # print(j)
    # for a,b in j.items():
        # print(b)
        # if j[a] =="Varsha":
            # print(b)
            # j["salary"]=70000
            # print(a)
        # j.update({a:b})
    # new.update({i: j})
# print(new)

# or
# for i,j in d.items():
#     if j["name"]=="Varsha":
#         j["salary"]=70000
# print(d)

##############################################################################
# sampledict={"physics":82,"maths":45,"history":75}
# l=sampledict.values()
# print(min(l))
# print(max(l))
# print((sum(l)))

#########################################################################
# program to calculate the sum of marks
# studentinfo={
#     "name":"anil",
#     "email":"anil@ddd.com",
#     "marks":{"sem1":100,"sem2":200,"sem3":300}
#     }
# sum=0
# new={}
# for i,j in studentinfo.items():
#     if i!= "marks":
#         print({i:j})
#         # new.update({i:j})
#     else:
#         print({i:j})
#         for o in j.values():
#             sum=sum+o
#         new["Total Marks"] = sum
#         # new["marks"]=sum(j.values())
# print(new)
# #
# print(studentinfo["name"],":",sum)

##############################################################################################

# studentinfo={
#             "100":{"name": "anil",
#                    "email": "anil@odd.com",
#                    "marks": {"sem1": 100, "sem2": 200, "sem3": 300}
#                    },
#             "101":{"name":"binil",
#                   "email":"binil@ddd.com",
#                    "marks":{"sem1":200,"sem2":200,"sem3":300}
#                    }
# }
#
# for i,j in studentinfo.items():
#     for a,b in j.items():
#         sum = 0
#         if a == "marks":
#             for v in b.values():
#                 sum=sum+v
#                 j["marks"]=sum
#     print(studentinfo[i]["name"], "\t",studentinfo[i] ["email"], "\t total mark is:", studentinfo[i]["marks"])
# print(studentinfo)

################################################################
# studentdata={111:{"name":"tom",
#                   "email":"tom@gmail.com",
#                   "sem":{'sem1':{'sub1':2,"sub2":5,"sub3":8},
#                          "sem2":{"sub1":7,'sub2':6}
#                          }
#                   },
#             222:{"name":"Ramu",
#                   "email":"Ramu@gmail.com",
#                   "sem":{'sem1':{'sub1':8,"sub2":2,"sub3":9},
#                          "sem2":{"sub1":7,'sub2':6}
#                          }
#                   }
#
# }
# for key,value in studentdata.items():
#     total = 0
#     ## print(value)
#
#     for k,v in value.items():
#
#         ## print(v)
#         if k=="sem":
#
#             for a,b in v.items():
#                 if a=="sem1":
#                     s1total=sum(b.values())
#                     v["sem1"]=s1total
#                     total=total+sum(b.values())
#                 else:
#                     s2total=sum(b.values())
#                     v["sem2"]=s2total
#                     total = total + sum(b.values())
#                     total=v["sem1"]+v["sem2"]
#
#
#     value["total"]=total


    # print("Name::",studentdata[key]["name"],"\nEmail::",studentdata[key]["email"],"\nSem1 Result::",
    #       studentdata[key]["sem"]["sem1"],"\nSem2 Result::",studentdata[key]["sem"]["sem2"],"\nTotal Marks::",
    #       studentdata[key]["total"],"\n\n")

###########################################################################################################
























