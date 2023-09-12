my_dict={"first_name":"frieda",
         "last_name":"Bezalel",
         "Age":35,
         "child_names":["Ariel","Avigile","Shira"],
         ("pets","name"):["mizi","rex"],
         45:(1,2,3,4,5)
         }


print("my_dict",my_dict) #הדפסת כל תוכן מילון
print("first_name",my_dict["first_name"])
print(type(my_dict))
print("my_dict[45]",my_dict[45])
print(my_dict.get(46,"blabla"))    #שליפת איבר ממילון
my_dict["Husband"]="Uziel"   # הוספת מפתח למילן
print("my_dict",my_dict) #הדפסת כל תוכן מילון


#dictionary inside dictionary
 #   looks like json file
emps={1111:{"first_name":"frieda",
         "last_name":"Bezalel",
         "Age":35},
    2222:{"first_name":"Malvina",
         "last_name":"Shulz",
         "Age":35}
      }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#on 9/7/2023 shiur 2
emps2=emps.copy()
print("emps[1111]:" , emps[1111])
jnk= emps[1111]
emps[1111]=None   #removing value
emps[2222]["Age"]=24
emps[3333]=jnk  #takes its value
print("Before  removing first cell:" ,emps2)
print("After removing first cell& changing age from 35 to 24 :" ,emps)





# another example
emps[3333]=jnk
my_5555=emps.get(5555)
print("5555" ,my_5555 )

my_4444=emps.get(4444,"there is no 4444")
print("4444",my_4444)


my_3333=emps.get(3333,"there is no 3333")
print("3333",my_3333)


#exercise   - count appeareance time of each char on string
a="jfdshjsdkjfsdkjfhskjdfksjds"
my_dic={}

for item in a:
    #print(item,my_dic.get(item))   this print shows the ways it builds counter for each char in a on my_dict
    my_count = my_dic.get(item,0)+1
    my_dic[item]= my_count

print("my dic :" ,my_dic)



emps={1111:{"first_name":"frieda",
         "last_name":"Bezalel",
         "Age":35},
    2222:{"first_name":"Malvina",
         "last_name":"Shulz",
         "Age":35},
    4444: " bls fsdfsfsd",
    5555:  123456
    }


for key,val in emps.items():
    print(f"the key is {key}  and the val is {val}")

for i in emps.keys():
    print("i",i)

for i in emps.values():
    print("i",i)