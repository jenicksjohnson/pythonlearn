# 1.	Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
#
# 2.	.Write a Python program that matches a string that has an ‘a’
# followed by three 'b'.
# line = "wesbbbavbbba"
#
#
# 3.	Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# 4.	Write a Python program to filter a list of integers using Lambda.
# Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list: [2, 4, 6, 8, 10]
# Odd numbers from the said list: [1, 3, 5, 7, 9]
# 5.	Program to check if a number is prime or not
# 6.	Write a python program (function!) that takes a list and
# returns a new list that contains all the elements of the first
# list minus all the duplicates.
###############################################1.
# for i in range(1,6):
#     print("\r")
#     for j in range(1,i+1):
#         print("*",end=" ")  ###we can end with any string without going to next line
#("\r") ##--starts with new line
#################################################2.
# import re
# line = "wesbbbavbbba"
# regex='[b]{3}[a]{1}'
# result=re.findall(regex,line)
# print(result)
##################################################3.
# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# newdict={}
# for i,j in dic1.items():
#     dictnew[i]=[j]
# for i,j in dic2.items():
#     dictnew[i]=[j]
# for i,j in dic3.items():
#     dictnew[i]=[j]
# print(dictnew)
## or use upate function
# for d in (dict1,dict2,dict3):
#     newdict.update(d)
# print(newdict)
###########################################################4.
# integers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even=[2, 4, 6, 8, 10]
# Odd=[1, 3, 5, 7, 9]
# new=list(filter(lambda x:x not in Even,integers))
# print(new)
# new2=list(filter(lambda x:x not in Odd,integers))
# print(new2)
##########################################################5.
# number=int(input("enter a number"))
# prime=False
# for i in range(2,number-1):
#     if number%i==0:
#         prime=True
#         break
#
# if prime:
#     print("its not prime")
# else:
#     print('its prime')
##############################################################6.
# def dupe(x):
#     y=[]
#     for i in x:
#         if i not in y:
#             y.append(i)
#     return y
# print(dupe([1,2,3,4,5,2,3,5,3]))
###############################################################################
###############################
#
#
#
#
#
# 7.	Create a program that asks the user to enter their name and
# their age. Print out a message addressed to them that tells them
# the year that they will turn 100 years old.
#

# import datetime as dt
# name=input("Enter the name::")
# age=(int(input("Enter the age::")))
# x=dt.datetime.now()
# y=x.year
# print("Name:",name,"\nBirth-Year::",y-age)
#
#
# 8.	Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player
# plays (using input), compare them, print out a message of congratulations
# to the winner, and ask if the players want to start a new game)
# Remember the rules:
# ●	Rock beats scissors
# ●	Scissors beats paper
# ●	Paper beats rock
#
#
# # 9.	Check whether two strings are anagrams of each other.
# # anagrams:a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
# #
# string1=input("Enter the string::")
# string2=input("Enter the string::")
#
# str1=sorted(string1)
# str2=sorted(string2)
# print("str1",str1," and str2 ",str2)
#
# flag=True
# if (len(string1)==len(string2)):
#     for i in string1:
#         if i in string2:
#             flag=True
#         else:
#             flag=False
# else:
#     print("not anagrams")
# if flag==True:
#     print("it is Anagrams")
# else:
#     print("not Aagrams")
# #
# # or
# def solve(s, t):
#     if len(s) != len(t):
#         return False
#
#     s = sorted(s)
#     t = sorted(t)
#
#     return s == t
# s = "bite"
# t = "biet"
# print(solve(s, t))
# #
# #
# #
# 10.	Write a Python program to check whether a string contains
# all unique characters.
# flag=True
# string=input("Enter the string::")
# for i in string:
#     x=string.count(i)
#     if x==1:
#         flag=True
#     else:
#         flag=False
#         break
# if flag==True:
#     print("unique")
# else:
#     print("not unique")
#
#
# or
# x = input("Enter the word: ")
# l = []
# for i in x:
#     l.append(i)
# m = []
# for j in l:
#     if j not in m:
#         m.append(j)
# if len(m)==len(l):
#     print("THE STRING ",str," CONTAINS UNIQUE CHARACTERS")
# else:
#     print("THE STRING ",str," CONTAINS DUPLICATE CHARACTERS")
#
#
# 11.	Python program to swap keys and values in a dictionary.
# old_dict = {'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23}
# new_dict={}
# for key,values in old_dict.items():
#     if values in new_dict:
#         new_dict[values].append(key)
#     else:
#         new_dict[values]=[key]
#
# print(old_dict)
# print(new_dict)
#
#
#  12.	Write a Python program to change a given string to a new
# string where the first and last chars have been exchanged.
# string=input("Enter the string::")
# str1=string[-1]+string[1:-1]+string[0]
# print(string,"\n",str1)
#
#
#
#  13.	Write a Python program to find the second most repeated word
#  in a given string.
# def wordCount(str):
#     counts = dict()
#     words = str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     print(counts)
#     counts_x = sorted(counts.items(),key=lambda k: k[1])
#     print(counts_x)
#
#     return counts_x[-2]
#
# print(wordCount("""Welcome to ExpertzLab Empowering People,
# Committed to Deliver the latest Technoloiges with utmost Quality.
# We are a pool of IT professionals and entrepreneurs with more than 20+
# years of industry experience. ExpertzLab was found
# with the sole intention to cater IT sector with enough IT skills."""))
#
# #
# #
# #
# #  14.	Twin primes are pairs of primes which differ by two. The first twin primes are {3,5}, {5,7}, {11,13}.
# #  Write a python program to generate twin prime numbers less than 100.
# def isPrime(n):
#    for i in range(2, n):
#       if n % i == 0:
#          return False
#    return True
#
# def PrimeTwins(start, end):
#    for i in range(start, end):
#       j = i + 2
#       if(isPrime(i) and isPrime(j)):
#          print("{:d} and {:d}".format(i, j))
#
# PrimeTwins(2, 100)
# #
# #
# #
#  15.	Write a program to build a simple Student Management System using Python which can perform following operations:
# 1. Accept
# 2.Display
# 3.Search
# 4.Delete
# 5.Update
# Accept – This method takes details from the user like name, roll number, and marks for two different subjects.
# Display – This method displays the details of every student.
# Search – This method searches for a particular student from the list of students.
# This method will ask the user for roll number and then search according to the roll number
# Delete – This method deletes the record of a particular student with a matching roll number.
# Update – This method updates the roll number of the student.
# This method will ask for the old roll number and new roll number.
# It will replace the old roll number with new roll number.
# class Student:
#     # Constructor
#     def __init__(self, name, rollno, m1, m2):
#         self.name = name
#         self.rollno = rollno
#         self.m1 = m1
#         self.m2 = m2
#
#         # Function to create and append new student
#
#     def accept(self, Name, Rollno, marks1, marks2):
#         # use  ' int(input()) ' method to take input from user
#         ob = Student(Name, Rollno, marks1, marks2)
#         ls.append(ob)
#
#         # Function to display student details
#
#     def display(self, ob):
#         print("Name   : ", ob.name)
#         print("RollNo : ", ob.rollno)
#         print("Marks1 : ", ob.m1)
#         print("Marks2 : ", ob.m2)
#         print("\n")
# # Search Function
#
#     def search(self, rn):
#         for i in range(ls.__len__()):
#             if (ls[i].rollno == rn):
#                 return i
#
#                 # Delete Function
#
#     def delete(self, rn):
#         i = obj.search(rn)
#         del ls[i]
#
#         # Update Function
#
#     def update(self, rn, No):
#         i = obj.search(rn)
#         roll = No
#         ls[i].rollno = roll;
# Create a list to add Students


# ls = []
# an object of Student class
# obj = Student('', 0, 0, 0)
#
# print("\nOperations used, ")
# print("\n1.Accept Student details\n2.Display Student Details\n"
#       "3.Search Details of a Student\n4.Delete Details of Student"
#       "\n5.Update Student Details\n6.Exit")
#
# ch = int(input("Enter choice:"))
# if(ch == 1):
# obj.accept("A", 1, 100, 100)
# obj.accept("B", 2, 90, 90)
# obj.accept("C", 3, 80, 80)
# print(ls)
#
# elif(ch == 2):
# print("\n")
# print("\nList of Students\n")
# for i in range(ls.__len__()):
#     obj.display(ls[i])
#
# # elif(ch == 3):
# print("\n Student Found, ")
# s = obj.search(2)
# obj.display(ls[s])
#
# # elif(ch == 4):
# obj.delete(2)
# print(ls.__len__())
# print("List after deletion")
# for i in range(ls.__len__()):
#     obj.display(ls[i])
#
# # elif(ch == 5):
# obj.update(3, 20)
# print(ls.__len__())
# print("List after updation")
# for i in range(ls.__len__()):
#     obj.display(ls[i])
#
# # else:
# print("Thank You !")
#
#
#
#
# 16. Mark is making a team and selects people in a very odd way. Mark assigns cards with random numbers to everyone
# standing in a queue. He checks the cards starting from the last person in the queue.
# Mark selects the person to his team if, the person he is currently evaluating holds the card with value, greater than
# or equal to the highest valued card among all the cards evaluated so far.
# Return the total number of people Mark selects to his team by completing the function team_strength.
# Constraints
# •	The card value could be positive, negative or 0.
# •	There could be multiple cards with the same value.
# Example 1
#
# card_array = [4, 3, 2, 3, 1]
#
# output = 4
#
# Explanation :
# Since mark starts valuing the card from the last person
# •	The first person evaluated has card with value one and is definitely selected as this is the highest card valued so far.
# •	The next person has card value 3 and is also selected as this becomes the highest valued card so far.
# •	The person with card value 2 is not selected, since the highest valued card so far is 3.
# •	The next person who has card value 3 is selected since this is the same as the highest valued card so far.
# •	The last person to be evaluated has card value 4 which becomes the highest valued and hence is selected to the team.
# Finally Mark has 4 people in his team.
#
# def team_strength(cards):
#     k = []
#     cards=cards[::-1]
#     largest = cards[0]
#     for card in cards:
#         if card >= largest:
#             k.append(card)
#             largest = card
#     print(k)
#     return len(k)
# L=team_strength([4, 3, 2, 3, 1])
# print(L)
#
#
#
#
# 17.Given a paragraph, complete the function process() that returns the paragraph after doing the following:
# # •	Rearrange every sentence in its reverse order
# # •	Some of the words in the sentences are missing some letters and they are denoted with "#"
# # If the word with missing letters is found out to be palindrome then find and substitute the missing letter
# # to make it a full word.
# # If they are not palindrome but still have missing letters, change every letter in the word into "@".
# # Sample Input:
# #
# paragraph = """mal#yalam is our mother tong#e. It is a langua#e spo#en in the Indian state of kerala. m#dam ha#nah
# teaches Malayalam. neve# is a #tudent of hannah."""
# # # new_paragraph = process(paragraph)
# # # print(new_paragraph)
# # # Sample Output
# # # @@@@@@ mother our is malayalam. kerala of state Indian the in @@@@@@ @@@@@@@@ a is It. Malayalam teaches hannah
# # madam. hannah of @@@@@@@ a is neven.
# #
# s=paragraph.split(".")
# print(s)
# i=0
# for line in s:
#     ws=line.split()
#     j = 0
#     for w in ws:
#         if "#" in w:
#             l=len(w)
#             a=w.index("#")
#             b=w[-(a+1)]
#             new=w.replace("#",b)
#             if new==new[::-1]:
#                 ws[j]=new
#             else:
#                 ws[j]="@"*l
#         j+=1
#     print(ws[::-1])
#     s[i]=ws[::-1]
#     i+=1
# print(s)
# k=0
# for i in s:
#     s[k]=' '.join(i)
#     k+=1
# print(s)
# final=' '.join(s)
# print(final)
###########################################################