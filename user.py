from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item quantity exceeded!!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('Item added')
        else:
            print('Item not found')

    def view_cart(self):
        print('*****View Cart*****')
        print('Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total Price: {self.cart.total_price}')
    
    def pya_bill(self):
        print(f'Totla {self.cart.total_price} paid successfully')
        self.cart.clear()

        
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary 

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
        
    def view_employee(self, restaurent):
        restaurent.view_employee()
        
    def add_new_item(slef, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_items(self, restaurent, item):
        restaurent.menu.remove_item(item)

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
        

# mamar_res = Restaurent('Mamar Restaurent')
# mn = Menu()
# item = FoodItem('Pizza', 12.45, 10)
# item2 = FoodItem('Burger', 12, 30)
# admin = Admin('Fahim', 125125, 'fahim@gmail.com', 'Dhaka')

# admin.add_new_item(mamar_res, item)
# admin.add_new_item(mamar_res, item2)

# customer1 = Customer('Rahim', 123123, 'rahim@gmail.com', 'Dhaka')
# customer1.view_menu(mamar_res)

# item_name = input('Enter item name: ')
# item_quantity = int(input('Enter item Quantity: '))

# customer1.add_to_cart(mamar_res, item_name, item_quantity)
# customer1.view_cart()