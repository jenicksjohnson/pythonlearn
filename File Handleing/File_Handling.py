# creating a text file
# "w" - writing mode

# file=open("sample.txt","w")
# file.write("hi,Welcome to expertzlab")
# file.close()

# if we use "w" then the contents will overwrite
# file=open("sample.txt","w")
# file.write("hi welcome \nGood day")
# file.close()

# "r" - to reading_file a text file
# file=open("sample.txt","r")
# print (file.reading_file())
# file.close()

# another method::
# f=open("sample.txt", mode="r")
# print(f.reading_file())
# file.close()

# default mode= reading_file
# f=open("sample.txt")
# print(f.reading_file())

# reading any line on a txt
# f=open("sample.txt", mode="r")
# print(f.readline())  #reads the first line
# print(f.readline())  #reads the second line

# reading_file entire content and shows as a list
# f=open("sample.txt", mode="r")
# print(f.readlines())

# for iteration in readlines()
# f=open("sample.txt", mode="r")
# a=f.readlines()
# for i in a:
#     print(i)

# xy=open("sample.txt","r")
# print (xy.readline(5)) #reading_file upto 5 characters
# print (xy.readline(10))  #reads the rest of the characters upto 10
# print (xy.readline(20)) #if the first line completed then prints secondline

# to know the current position
# print(xy.tell())
# print (xy.readline(5))
# print (xy.tell())
# print (xy.readline(200))
# print (xy.tell())

# going to the given character where we have given the value
# xy.seek(0)
# print (xy.tell())
# xy.seek(7)
# print (xy.tell())
# print (xy.readline(3))

# "a" - add data without overwriting on the txt file
# on append mode, we can also create a new file
# f=open("sample.txt", mode="a")
# f.write("\nfile input output operations")
# f.write("\nflawing flawlessly")
# f.close()

# "r+" - this mode is used for writing reading and appending combo
# file=open("sample.txt","r+")
# print (file.reading_file())
# file.write("\nhai \nwelcome")


# create 2 txt files and copy the data from one to another
# zx=open("sample1.txt","w")
# zx.write("Welcome,Hai")
# zx.close()
#
# re=open("sample1.txt","r")
# uv=open("sample2.txt","w")
# uv.write(xy)
# or
# uv.write(re.reading_file())

# or  by iteration method
# for i in re:
#     uv.write(i)
#
# re.close()
# uv.close()

#craete a file with string "first first line second line"
# file=open("sample3.txt","w")
# file.write("first first line second line")
# file.close()
# l=[]
# file=open("sample3.txt","r")
# dict=file.readlines()
# for i in dict:
#     l=i.split()
# print(l)
# abc={}
# k=[]
# for i in l:
#     if i not in k:
#         k.append(i)
# print(k)
# abc={}
# for i in k:
#     sum=0
#     for m in l:
#         if m==i:
#             sum=sum+1
#     abc[i]=sum
#
# print(abc)

# or
# file=open("sample3.txt","w")
# file.write("first first line second line")
# file.close()
# file=open("sample3.txt","r")
# simple=file.reading_file()
# words=simple.split()
# print(words)
# dict={}
# for word in words:
#     if word in dict:
#         dict[word]+=1
#     else:
#         dict[word]=1
# print(dict)

#or
# dict={i:words.count(i) for i in words}

#or
# dict{}
# for i in words:
#     dict.update({i:words.count(i)})






































