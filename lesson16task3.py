# Product Store

# Write a class Product that has three attributes:

# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
# '''

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
    
    def __list__(self):
        product = [self.type, self.name, self.price]
        return product
    def __name__(self):
        return self.name
        

class ProductStore:
    
    total_income = 0

    def __init__(self):
        self.product_list = []
    
    def add(self, product, amount):
        some_prod = dict()
        some_prod[product] = amount
        self.product_list.append(some_prod)
    
    def sell_product(self, product_name, amount):
        for i in self.product_list:
            for key, value in i.items():
                if product_name in key.__list__() and value >= amount:
                    i[key] = value - amount
                    ProductStore.total_income += key.__list__()[2] * amount
                    break
                elif product_name not in key.__list__():
                    pass
                elif value < amount:
                    print("We have no so much prods!")
                else:
                    print("There is no such a prod!")
    
    def get_all_products(self):
        for i in self.product_list:
            for key, value in i.items():
                print(f"There is {key.__list__()[1]} in amount {value}")
    
    def get_product_info(self, prod):
        my_tuple = tuple()
        for i in self.product_list:
            for key, value in i.items():
                if key.__name__() == prod:
                    my_tuple = (prod, value)
                    print(f"There is information about a prod: {my_tuple}")
                    return my_tuple
    
    def get_income(self):
        print(f"The total income from selling prods is {ProductStore.total_income}")

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)        

s = ProductStore()



s.add(p, 10)

s.add(p2, 300)

s.get_all_products()

s.sell_product('Ramen', 10)

s.get_all_products()

s.get_income()

s.get_product_info('Ramen')

assert s.get_product_info('Ramen') == ('Ramen', 290)


