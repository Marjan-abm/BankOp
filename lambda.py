# def myfunc(n):
#     return lambda a : a * n
# myDoubler = myfunc(2)
# myTriple = myfunc(3)
# print(myTriple(11))

# print(myDoubler(11))
import os
# f = open("myFile.txt", "x")
# # f = open("myFile.txt","w")
# os.remove("myFile.txt")
f = open("C:\\Users\marja\Desktop\hello.txt", "a")
# print(f.readline())
# print(f.readline())
f.write("I am a writing test \n")
# print(f.read())
f.close()
if os.("C:\\Users\marja\Desktop\hello.txt").exists("hello.txt"):
    os.remove("hello.txt")
else:
    print("The file does not exist")
