import datetime
from save_load import save_data, load_data

FILE = "customers.pkl"


class CustomersList():
    def __init__(self):
        
        # At the 1ST run i use the line below to prevet it from crushing
        #  self.all_customers = []
        
        # At the 2ND run and further on i use the line below.
        self.all_customers = load_data(FILE)
    

    def add_customer(self, customer):
        self.all_customers.append(customer)
        save_data(FILE, self.all_customers)
        
    def remove_customer_by_id(self):
        ask_id = input("What is the customer ID? ")
        for customer in self.all_customers:
            if customer.id == ask_id:
                self.all_customers.remove(customer)
                save_data(FILE, self.all_customers)
                print(f"\nCustomer has removed successfully:\n{customer}\n")
            else:
                print("\nCustomer ID does not exist.\nReturning to main menu..")
            
    def get_customer_by_id(self):
        customer_id = input("\nEnter customer ID --- ")
        for customer in self.all_customers:
            if customer.id == customer_id:
                return f"\nCustomer found..\n{str(customer)}\n"
        print("\nCustomer ID does not exist\nReturning to main menu..\n")
    
    def add_event_to_customer(self, event):
        for cust in self.all_customers:
            if event.customer_id == cust.id:
                cust.events.append(str(event.id))
        save_data(FILE, self.all_customers)
        
            

    def __str__(self):
        tmp_str = ""
        for customer in self.all_customers:
            tmp_str += str(customer) + "\n"
        return tmp_str 
    


class Customer():
    def __init__(self, id, name, type, start_date=datetime.datetime.now(), events = None):
        self.id = id
        self.name = name
        self.type = type
        self.start_date = start_date
        
        if events is None:
            self.events = []
        else:
            self.events = events

    def __str__(self):
        return f"\nCustomer ID:{self.id}\nCustomer name:{self.name}\nCustomer type:{self.type}\nCustomer since:{self.start_date}\nCustomer events ID list:{self.events}\n"
    
  