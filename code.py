#Below I present aim of creating a class

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
