#create from details to dectionary
def create_emp_dict(first_name,last_name):
    emp={}
    emp["first_name"]=first_name
    emp["last_name"] = last_name
    return emp



tamir=create_emp_dict("tamir","reiss")

print("tamir",tamir)


#if we want to create a person  first & last name and other properties (unkonws in advance)

def create_emp_dict(first_name:str,last_name:str,**kwargs):   #kwargs key,word   each time gets item as pair
    emp={}
    emp["first_name"]=first_name
    emp["last_name"] = last_name
    for key, val in kwargs.items():
        emp[key]=val
    return emp


tamir=create_emp_dict("tamir","weiss",id=123456,gender="m",wife="galit")
amir=create_emp_dict("amir","dadon",id=123456,gender="m",wife=["osnat","not osnat"])
frieda=create_emp_dict("frieda","bezalel",id=123456,gender="m",spouse=["Uziel"])
dudo=create_emp_dict(first_name="dodo",last_name="wep",id=123456,gender="m",wife="galit")  #here i annoucing each var to which parameter
omer=create_emp_dict("omer","weiss",id=111111,gender="m",wife="galit")
ophir=create_emp_dict("ophir","weiss",id=111111,gender="m",wife="galit")
tamirZ=create_emp_dict("tamir","weiss",id=123456,gender="m",wife="galit",children=[omer,ophir])  #  children is an array object
print("tamir",tamir)
print("amir",amir)
print("frieda",frieda)
print("tamirZ",tamirZ)


#output:
# C:\Users\Student-24\PycharmProjects\pythonProjectFriedasFirstPrj\venv\Scripts\python.exe C:\Users\Student-24\PycharmProjects\pythonProjectFriedasFirstPrj\venv\Scripts\new_functions.py
# tamir {'first_name': 'tamir', 'last_name': 'reiss'}
# tamir {'first_name': 'tamir', 'last_name': 'weiss', 'id': 123456, 'gender': 'm', 'wife': 'galit'}
# amir {'first_name': 'amir', 'last_name': 'dadon', 'id': 123456, 'gender': 'm', 'wife': ['osnat', 'not osnat']}
# frieda {'first_name': 'frieda', 'last_name': 'bezalel', 'id': 123456, 'gender': 'm', 'spouse': ['Uziel']}
# tamirZ {'first_name': 'tamir', 'last_name': 'weiss', 'id': 123456, 'gender': 'm', 'wife': 'galit', 'children': [{'first_name': 'omer', 'last_name': 'weiss', 'id': 111111, 'gender': 'm', 'wife': 'galit'}, {'first_name': 'ophir', 'last_name': 'weiss', 'id': 111111, 'gender': 'm', 'wife': 'galit'}]}
#
# Process finished with exit code 0

#different types of dictionary items