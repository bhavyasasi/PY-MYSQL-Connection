import mysql.connector
#create connection and database
conn= mysql.connector.connect(user="root",password ="root",host="localhost",database="DjangoORM")
cur= conn.cursor()
# cur.execute("CREATE DATABASE DjangoORM")
# print("database created")

"""create a table employee"""
# cur.execute('''CREATE TABLE EMPLOYEE(
# id int primary key auto_increment,
# name varchar(20),
# designation varchar(30),
# salary decimal (10,2))''')
# print("Table created")


""" DJANGO ORM 
------------------
CURD : CREATE , UPDATE,READ,DELETE

empolyee list
--------------
 select * from employee 
orm : employee.object.all()


employee details
-----------------
selecr * from employee where id =1
orm : employee.objects.get(id=1)


create employee
----------------
insert into employee values(val1,)
orm : employee.oject.create(id =1,name="abc)


filter employee
----------------
select * from employee where designation="HR"
orm : employee.ojects.filiter(designation="HR")


update employee
----------------
update employee set salary =100000 where id =1
orm : employee.save()

delete employee
-----------------
delete from employee where id =1
orm : employee.delete()"""


# create class employee :

class Employee:
    def create(self, *args, **kwargs):
        cols = ""
        placeholder = ""

        for col in kwargs.keys():
            if cols != "":
                cols += ", "
                placeholder += ", "

            cols += col
            placeholder += "%s"

        values = tuple(kwargs.values())

        query = f"INSERT INTO employee ({cols}) VALUES ({placeholder})"

        print("Query:", query)
        print("Values:", values)

        cur.execute(query, values)
        conn.commit()

        print("Employee created successfully")

    def list(self, *args, **kwargs):
        cur.execute("SELECT * FROM employee")
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())

    def retrieve(self, *args, **kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee where {key} = {kwargs.get(key)} ")
            print(cur.fetchall())
        

    def update(self, *args, **kwargs):
        print(args,kwargs)
        for key in kwargs:
            cur.execute(f"UPDATE employee SET {key} = '{kwargs.get(key)}' WHERE id = {args[0]}")
            conn.commit()

    

    def delete(self, *args, **kwargs):
        for key in kwargs:
            cur.execute(f"DELETE  FROM employee  WHERE id = {args[0]}")

            conn.commit()
            
    def filter (self, *args, **kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee WHERE {key} = '{kwargs.get(key)}'")
            print(cur.fetchall())
            

    


employee = Employee()
while True:
    print("1. create employee")
    print("2. list all employee")
    print("3. employee detail view")
    print("4. Update employee")
    print("5. Delete employee")
    print("6. filter employee")
    print("7. exit")


    choice= int(input("enter the choice : "))

    if choice == 1:
        name = input("enter the employee name :")
        desig = input("enter the designation :")
        salary = float(input ("enter the salary: "))
        employee.create(name = name , designation =desig , salary = salary )
    elif choice == 2:
        employee.list()

    elif choice == 3:
        print("")
        id = int(input("enter the employee id: "))
        employee.retrieve(id=id)
    
    elif choice == 4:
        id = int(input("enter the id :"))
        print("1. name")
        print("2. designation")
        print("3. salary")
        choice = int(input("enter the choice :"))
        if choice ==1:
            name = input("enter the name :")
            employee.update(id,name=name)

        elif choice == 2:
            desig= input("enter the designation :")
            employee.update(id,designation=desig)

        elif choice == 3:
            salary = float(input("enter the new salary :"))    
            employee.update(id,salary=salary)

        else:
             print("invalid choice") 
                
        employee.update() 

    elif choice == 5:
        id = int(input("enter the id :"))
        employee.delete(id)
        print("deleted")
    elif choice ==6 :
        employee.filter()
        print("filter option :")
        print("1. filter by name")
        print("2. filter by designation")
        print("3. filter by salary")
        choice = int(input("enter the choice :"))
        if choice ==1:
            name = input("enter the name :")
            employee.filter(name=name)
        
        elif choice == 2:
            desig= input("enter the designation :")
            employee.filter(designation=desig)
        
        elif choice == 3:
            salary = float(input("enter the new salary :"))    
            employee.filter(salary=salary)
        
        else:
            print("invalid choice") 

    elif choice == 7:
        
        print("Exit")        
        break
    else:
        print("invalid choice")
     
conn.close
print("connection closed")
















