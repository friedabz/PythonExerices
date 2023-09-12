from mysql.connector import connect,Error

class Patient:
    #id,gender,age,occupation,sleep_duration,bmi_category,sleep_disorder
    def __init__(self , gender:str,age:int,occupation:str,sleep_duration:float,bmi_category:str, sleep_disorder:str):
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.sleep_duration = sleep_duration
        self.bmi_category = bmi_category
        self.sleep_disorder = sleep_disorder

def insertPatient(conn,p):
    cursor = conn.cursor()
    sqlString=" select max(id) as maxId from patients "
    cursor.execute(sqlString)
    lastId=cursor.fetchall()[0][0]
    print(lastId)
    lastId+=1
    sqlString=" insert into patients values ( " + str(lastId) + ",'" + p.gender + "' , " + str(p.age) + " , '" + p.occupation + "' , " \
               + str(p.sleep_duration) +" , '"+ p.bmi_category + "' , '" + p.sleep_disorder + "' ) "
    print(sqlString)

    cursor.execute(sqlString)
    conn.commit()


def getByOccuption(conn,occupation)-> list[Patient] :
    lstP=[]
    cursor = conn.cursor()
    sqlString = " select *  from patients  where  occupation ='" + occupation + "';"
    cursor.execute(sqlString)
    res = cursor.fetchall()
    for row in res:
        print(row)
        lstP.append(Patient( row[1], row[2], row[3],row[4],row[5],row[6]))
    return lstP




def getMFStatistics(conn):
    cursor = conn.cursor()
    sqlString = " select     count(*)    from patients   ; "
    cursor.execute(sqlString)
    totalCount = cursor.fetchall()[0][0]

    sqlString= " select     count(*)     from patients where     gender = 'Male' ;"
    cursor.execute(sqlString)
    totalMale  = cursor.fetchall()[0][0]
    sqlString = "select     count(*)     from patients where     gender = 'Female' ; "
    cursor.execute(sqlString)
    totalFemale =cursor.fetchall()[0][0]
    my_dict = {"Male": totalMale / totalCount,
               "Female":totalFemale / totalCount  }

    print(my_dict)
    #print('Male:' + str(totalMale / totalCount) + 'Female:' + totalFemale / totalCount)


def getDisorders(conn,disorder="")
    
try:
    conn = connect(
        host="localhost",
        user="root",
        password="f102030",
        database="sleep_health"
    )

    #my_Patient=Patient('Female',47,'Project manager',6.5,'Normal','None')
    #insertPatient(conn,None) - for testing only
    my_Patient = Patient('Male', 76, 'Project manager', 6.5, 'Normal', 'None')
    # insertPatient(conn, my_Patient)
    # print("connected to DB")
    lst=getByOccuption(conn,'Doctor')
    getMFStatistics(conn)
    # for p in lst:
    #     print(p.gender,p.age,p.occupation)
except Error as err:
    print("Error message: " + err.msg)

    # def __init__(self,radious :int ,color : str ,x_position : int ,y_position : int ):
    #     self.radious = radious
    #     self.color =  color
    #     self.position= (x_position,y_position)
    #
    # def get_position(self):
    #     return self.position
    #
    # def change_color(self,new_color ):
    #     self._color=new_color
    #
    # def __str__(self):
    #     my_str=f"this is circle with radious {self._radious} color {self._color}"
    #     return my_str