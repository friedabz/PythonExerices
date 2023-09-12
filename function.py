def my_function(my_string,my_int):
    print(my_string*my_int)

my_function("~*",50)

def calc_sum(a,b):
    return a+b

def calc_sum2(a,b):
    if a==9 :
        return "blabla"
    return a+b


#on Python there's not def of overloading like this :
# def calc_sum(a,b,h):
#     return a+b+9

z = my_function("~*",50)
print("z", z)
c = calc_sum(4,9)
print("c:calc_sum(4,9) ",c)
c =calc_sum(4,7)
print("c:calc_sum(4,7) ",c)


# hint
# define with recommendation  - can give string/int and its okey on both cases
def calc_num3(a: int,b:int)->int:
    "this is a goo function"
    return a+b
print(help(calc_num3))
s=calc_num3("f","g")
print("s",s)


def calc_num4(a: int,b:int)->int:
    """

    :param a: int ofr sum
    :param b: second int for sum
    :return: a+b
    """
    return a+b
print(help(calc_num4))
s=calc_num4(2,3)
print("s",s)


def get_Int_From_User(msg:str)->int:
    """

    :param msg: string message to user
    :return:  : user input value
    """
    n=""
    while  not n.isnumeric():
        n=input(msg)
    a=int(n)
    return n


res=get_Int_From_User("Hello, please enter number:")
print("the nuber you entered:" , res)
#output
# ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
# ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
# C:\Users\Student-24\PycharmProjects\pythonProjectFriedasFirstPrj\venv\Scripts\python.exe C:\Users\Student-24\PycharmProjects\pythonProjectFriedasFirstPrj\venv\Scripts\function.py
# ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
# ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
# z None
# c:calc_sum(4,9)  13
# c:calc_sum(4,7)  11
# Help on function calc_num3 in module __main__:
#
# calc_num3(a: int, b: int) -> int
#     this is a goo function
#
# None
# s fg
# Help on function calc_num4 in module __main__:
#
# calc_num4(a: int, b: int) -> int
#     :param a: int ofr sum
#     :param b: second int for sum
#     :return: a+b
#
# None
# s 5
#
# Process finished with exit code 0
