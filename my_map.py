a=[1,3,4,5,6,7,8,9,3,234,8]

b= map(lambda x:x+3 ,a)
def add_3(x):
    a=x+3
    return a
print(a)
print(b)
c = map(add_3,a)
print('list(c)',list(c))