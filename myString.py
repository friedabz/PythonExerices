a = "~*~"
b = 'abc'
print(a*20)
print(a+b+' tre')

d = "abcdefghijklmnop"
print("d[3:5]" ,d[3:5])
print("d[3:]" ,d[3:])
print("d[3:-1]" ,d[3:-1])
# print("d[:]" ,d[])  --SyntaxError: invalid syntax
print("d[0:7:5]",d[0:7:5])

# name = input("Enter your name?")
# print("Hello, " +name + "!")
# print("type(name)" , type(name))
# # print(name*7.8)    TypeError: can't multiply sequence by non-int of type 'float'

# נשתול תווים אחרים ממחרוזת קיימת למחרוזת חדשה
e = d[:3] + 't' + d[5:9] +"y" + d[10:]
print("d", d)
print("e" ,e)

# f- stands for foramt
z =  f"b is {b} and d is {d} 2+3={2+3}"
print(z)

print("z in upper " ,z.upper())
print("z in capitalized " ,z.capitalize())
print("z in starts with my " ,z.startswith("my"))

a ="my name is Frieda"
b = "name"
print(a)
print(b)
location=a.find(b)
print(location)
b=a.replace("Frieda", "Tamar")
print(b)
arr=a.split(" ")
print("trun a  string to array " ,arr)

new_str ="~".join(arr)
print(new_str)

print("{0:<20}#".format("fridab"))
print("{:^20}#".format("b"))
print("{0:>20}#".format("c"))


#another example:
print("{0:<20}|{0:<20}|{0:<20}|{0:<20}#".format("A","B","123456","L"))
print("{0:<20}|{0:<20}|{0:<20}|{0:<20}#".format("A1","B1","123456","L"))
print("{0:<20}|{0:<20}|{0:<20}|{0:<20}#".format("A2","B2","123456","L"))
print("{0:<20}|{0:<20}|{0:<20}|{0:<20}#".format("A3","B3","123456","L"))