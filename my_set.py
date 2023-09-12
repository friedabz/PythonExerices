#set type
# doest not get double valuee
# by its items it defines if its set (item) or dictionary (key,item)
a= {1,2,3,4,5,6}

print("Set content" ,type(a))
print(a)


a= {1,1,2,3,4,5,6,4,4}
print("Example: Set doest get double value",a)

a={1,2,3,4,5,6,1,"d",4,4}
print("Example , another : Set doest get double value",a)


print("a type is : ",type(a))
print(a,len(a))

for item in a:
    print(item)

    #(1,2,3) - like list but doesnt change
a={1,2,"7",(1,2,3),3,4,5,6,1,"d",4,4}
print("how a is ordered :",a)


my_set=set()
my_set.add("cat")
my_set.add("dog")
my_set.add("1")
my_set.add("cat")
my_set.update([9,7,6,5]) # add few items
print("my_set content",my_set)

s1={1,2,3,4,5,6}
s2={2,3,4,5}
s3=s1.issubset(s2)
s4=s1.union(s2)
s5=s1.intersection((s2))
print("s3",s3)
print("s4",s4)
print("s5",s5)


#output:
# Set content <class 'set'>
# {1, 2, 3, 4, 5, 6}
# Example: Set doest get double value {1, 2, 3, 4, 5, 6}
# Example , another : Set doest get double value {1, 2, 3, 4, 5, 6, 'd'}
# a type is :  <class 'set'>
# {1, 2, 3, 4, 5, 6, 'd'} 7
# 1
# 2
# 3
# 4
# 5
# 6
# d
# how a is ordered : {1, 2, 3, 4, 5, 6, 'd', (1, 2, 3), '7'}
# my_set content {5, 'dog', 7, 'cat', 9, 6, '1'}
# s3 False
# s4 {1, 2, 3, 4, 5, 6}
# s5 {2, 3, 4, 5}
#
# Process finished with exit code 0



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# While loop
# waits until user enters the word hello , keeps asking
# n=input("Please enter 'hello':")
# while n.strip()!='hello':
#     n=input("Please enter 'hello':")
#
#
result=input("Please enter number of numbers:")

while not result.isnumeric():
    result=input("Please enter number of numbers:")

result = int(result)
myNumberList=[]
i=1
currItem=0
while i <= result :
    currItem=input(f"Please enter number {i}:")
    while not currItem.isnumeric() :
        currItem = input(f"Please enter number {i}:")
    currItem=int(currItem)
    myNumberList.append(currItem)
    i += 1

i = 0
sumNums=0
for item in myNumberList :
   sumNums+=item
print("my list :",myNumberList)
print("sum of numbers:" ,sumNums)

# another way to sum:
# mySum=0
# mySum= sum(myNumberList)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# break , continue, pass
#
# i=[1,2,3,4,5,6,7,8,9,10,11]
#
# for a in i:
#     if a==6:
#         break
#     print("a",a)
#
# for a in i:
#     if a==7:
#         continue
#     print("a",a)
#
#
# for a in i:
#     if a==8:
#         pass
#     print("a",a)
#
