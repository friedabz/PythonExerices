def my_func(func,a,b) :
    c=func(a,b)
    print(a)

def sum(z,x):
    return  z+x

_sum= lambda x,y:x+y
def diff(r,t):
    return  r-t
print(_sum(2,3))
my_func(sum,4,5)
my_func(diff,4,5)

my_func(lambda x,y:x*y,4,3)

# output
# a <filter object at 0x00000206A432A760>
# [7, 9, 54, 23, 67]
#
# Process finished with exit code 0


my_emps={123:{"first name":"aaaa","lastname":"bbb","birth_month":7},
1243:{"first name":"aafaa","lastname":"bdfbb","birth_month":4},
1273:{"first name":"aadfaa","lastname":"bbyb","birth_month":3},
1253:{"first name":"aasfdaa","lastname":"bbtb","birth_month":7}
         }

temp1=list(filter(lambda x:1==1,my_emps))
print("temp1 - keys",temp1)
temp1=list(filter(lambda x:1==1,my_emps.items()))
print("temp1- item",temp1)
temp1=list(filter(lambda x:1==1,my_emps.values()))
print("temp1- value",temp1)


my_tuple=(1253,{"first name":"aasfdaa","lastname":"bbtb","birth_month":7})
print('birth_month',my_tuple[1]["birth_month"])

# get all July emps on lamas
# temp1=list(filter(lambda x:x["birth_month"]==7,my_emps.items()))
# print("temp1- born on July ",temp1)

res_keys= list(filter(lambda key:my_emps[key]get("birth_month",13)==7,my_emps))
print('res_keys',res_keys) # only keys
res_values= list(filter(lambda val :value[key]("birth_month",13)==7,my_emps.values))
print('res_values',res_keys) # onlye value for each item on dic
res_values= list(filter(lambda item :item[1]("birth_month",13)==7,my_emps.values))
print('res_values',res_keys) #

#another example  6/8/20223
x=[1,2,3,4,5,6,8,9,23,29,56,2,67]
def bigger_then_7(X):
    return x>7

my_func = lambda x:x>7
print(my_func(12))

y=filter(bigger_then_7,x)
y1=filter(lambda x:x> 7, x)
