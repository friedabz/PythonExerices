#works on set, tuple,list
my_lst=[1,3,4,6,7,9,54,23,3,4,5,67]
a=filter(lambda x:x>=7,my_lst)

print('a',a)
print(list(a))