import datetime
from constants import CHOICES
from save_load import save_data, load_data


FILE = "services.pkl"


class ServicesList():
    def __init__(self):
        try:
            self.all_services = load_data(CHOICES["SFILE"])
        except:
            self.all_services = []
    
    def add_service(self, service):
        self.all_services.append(service)
        save_data(FILE, self.all_services)

    def remove_service_by_id(self):
        ask_id = input("Please enter the service ID --- ")
        for service in self.all_services:
            if service.id == ask_id:
                self.all_services.remove(service)
                save_data(FILE, self.all_services)
                print("\nService has removed successfully\n")
        print("\nService ID does not exist\n")

    def get_service_by_name(self):
        ask_name = input("\nPlease enter the service name --- ")
        for service in self.all_services:
            if service.name == ask_name:
                print(f"Service found...\n{print(service)}")
        print("\nService name does not exist.\nMake sure the first letter is an upper case and the rest are lower cases!\n")
    

    def __str__(self):
        tmp_str = ""
        for service in self.all_services:
            tmp_str += str(service) + "\n"
        return tmp_str 


class Service():
    
    def __init__(self, id, name, type, price, start_date = datetime.datetime.now().strftime('%d/%m/%Y')):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.start_date = start_date
    
    
    def __str__(self):
        return f"Service ID:{self.id}\nService name:{self.name}\nService type:{self.type}\nService start date:{self.start_date}\n"





