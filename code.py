#Below I present two class tasks

#TASK 1

#Create an class which will hold the name of store, and automatically create list of prodcut sold in this store.
#This class should have two methods:
#1) add_item, which add to afforementioned list dictiionary with product name and price
#2) stock_price which sum up prices of all products

#2 statisc methods which will
#1) allow for creating a new Store object from already existing one but with sufix " - franchise"
#2) store_details, which will produce string showing the name of total stock price of given store

class Store:
    def __init__(self, name):
        self.name=name 
        self.items=[]
    
    def add_item(self, name, price):
        self.items.append({
            "name":name,
            "price":price
        })
    def stock_price(self):
        sum=0
        for i in self.items:
            sum=sum + i["price"]
        return sum
    @staticmethod
    def franchise(name):
        return Store(name + " - franchise")
    @staticmethod
    def store_detail(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

#How code works
Biedronka=Store("Biedronka")
Biedronka.add_item("Makrela",20.20)
Biedronka.add_item("Zurawina 500g",8.10)
Biedronka.stock_price()
Store.store_detail(Biedronka)

zabka_franch=Store.franchise("Zabka")
print(zabka_franch.name)


#TASK 2
#Create class call Student, which will gather information about student's name and school, and will have a box for his marks

#Then create two methods:
#1) which will calculate students mark's average
#2) static one, which will allow for creating a Student profile by adding information about with whom given student is walking to school (suck information about student
#school)

#Then create new class WorkingStudent which inherit from Student one all its properties but additionally contain information about salary

class Student:
    def __init__(self, name,school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def friend(cls, origin,friend_name, *args):
        return cls(friend_name,origin.school, *args)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary=salary

anna=WorkingStudent("Anna","Oxford",20.0)
print(anna.school)
print(anna.salary)
Greg=WorkingStudent.friend(anna,"Greg",25)
print(Greg.school)
Luk=Student.friend(anna,"Luk")
print(Luk.school)


