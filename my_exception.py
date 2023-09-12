#getting value error: invalid literal
def get_number():
    a=input("enter  a number ")
    number=int(a)
    return number

number=5
try:
    number=number/get_number()
except ValueError:
    print("Not a valid input number is set to default")
except ZeroDivisionError:
    print("blabla")
except Exception as ex:
    print("Exception ",ex)
