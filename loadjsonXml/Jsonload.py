# JSON => Java Script Object Notation
# It is similar to Python Dictionary.(key value pair structure)
# It is used for data exchange b/w applications (from server to mobile application)
# it passing data from client to server and server to client.
# in HTML we passing design as well as data, but JSON passes only data.
#reading a Json file is called "Parsing"
#
#
# import json
# data={"name":"Ann","age":12,"sem":{"sem1":[10,20,30],
#                                    "sem2":[60,70,80]}}
# f=open("file.json","w")  ##creating a json file
# json.dump(data,f)    ##giving input to a json file
#
# f=open("file.json")          ##for reading a json file
# result=json.load(f)           ##assigning json file content to a variable
# print(result)
# print(type(result))
#
###########################################################
# import json
#
# with open("file.json","w") as f:          for writing a file
#     json.dump(data,f)
#
# with open("file.json") as file:           for taking the values
#     print(json.load(file))
#
### how to reading_file a json file by sending a request from api
# json content to import from flipkart: https://www.flipkart.com/lc/getData?dataSourceId=websiteNavigationMenuDS_1.0&t=25992287
#### sending request
import requests
import json
response1=requests.get("https://www.flipkart.com/lc/getData?dataSourceId=websiteNavigationMenuDS_1.0&t=25992287")
# response is an object , so we want to convert it into json string
# print(type(response1))  ##to check the variable type
#
#
# To reading_file JSON data from response object, converting it to string.
# text => to convert response object to json string
# import json => for converting that json string to python dictionary we have "loads" fn.

# load => load from a locally available file
# loads => from a json string to python dict
# dump => writing python dictionary to json file
# dumps => python dictionary to json string

#
# print(type(response1.text))
# print(response1.text)
# #response1.text is used to change into string
# #
# data=json.loads(response1.text)   ##loads is used to convert string into dict
# print(data)
# print(type(data))
# #                                  #### for using a particular part
# for k,v in data['navData'].items():
#     print(k,":",v["title"])






















































































