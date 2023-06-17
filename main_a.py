import datetime
from adding_modules import myleads, mycustomers, myevents, myservices,add_customer_menu, add_event_menu, add_lead_menu, add_service_menu
from constants import CHOICES, AGENT_NAME_PASSWORD
from customers import Customer
from events import Event
from leads import Lead
from save_load import save_data, load_data
from services import Service


# All the unused "imports" above are used only at the 1ST


# Define function to start menu
def main_menu():
    while True:
        print("\nHello and welcome to EventPlanner inc.\n")
        command = input(
            f"If you are a Customer please enter - {CHOICES['IM_CUSTUMER']}\nIf you are an Agent please enter - {CHOICES['IM_AGENT']}\nTo EXIT enter - {CHOICES['EXIT']} ---  ")
        if command == CHOICES['IM_CUSTUMER']:
            customer_menu()
        elif command == CHOICES['IM_AGENT']:
            agent_login_menu()
        elif command == CHOICES['EXIT']:
            print("\nGoodbye!(:\n")
            break
        else:
            print("\nInvalid command! PLease try again\n")

# Define function for agent login
def agent_login_menu():
    counter = 3  # 3 login attempts.
    while counter != 0:
        agent_name = input("Please enter agent name --- ")
        agent_password = input("Please enter password --- ")
        if agent_name in AGENT_NAME_PASSWORD and agent_password == AGENT_NAME_PASSWORD[agent_name]:
            print("\nLogin successful!")
            after_login_agent_menu()
            break
        else:
            counter -= 1
            print(
                f"\nIncorrect username or/and password.\nYOU HAVE LEFT {counter} ATTEMPTS\n")
    else:
        print("\nYou have exceeded the maximum number of attempts.\nGoodbye!\n")

# Define function for after login agent menu
def after_login_agent_menu():
    command = input(
        f"\nFor Customers handling enter - {CHOICES['HANDLE_CUSTOMERS']}\nFor Events handling enter - {CHOICES['HANDLE_EVENTS']}\nFor Services handling enter - {CHOICES['HANDLE_SERVICES']}\nTo main menu enter anything else ---  ")
    if command == CHOICES['HANDLE_CUSTOMERS']:
        # Call function to handle customers
        handle_customers_menu()
    elif command == CHOICES['HANDLE_EVENTS']:
        # Call function to handle even2ts
        handle_events_menu()
    elif command == CHOICES['HANDLE_SERVICES']:
        # Call function to handle services
        handle_services_menu()
    else:
        print("\nReturning to main menu...\n")
        

# Define function to handle customers
def handle_customers_menu():
    command = input(
        f"\nTo add a new customer enter - {CHOICES['ADD_CUSTOMER']}\nTo remove customer enter - {CHOICES['REMOVE_CUSTOMER']}\nTo find customer by name enter - {CHOICES['GET_CUSTOMER']}\nTo display all customers enter - {CHOICES['DISPLAY_CUSTOMERS']}\nTo the main menu enter anything else --- ")
    if command == CHOICES["ADD_CUSTOMER"]:
        add_customer_menu()
    elif command == CHOICES["REMOVE_CUSTOMER"]:
        print("\nTo remove a customer Please make sure you have the customer ID.\n")
        mycustomers.remove_customer_by_id()
    elif command == CHOICES["GET_CUSTOMER"]:
        print("\nTo find a customer Please make sure you have the customer ID.\n")
        mycustomers.get_customer_by_id()
    elif command == CHOICES["DISPLAY_CUSTOMERS"]:
        print("\nDisplaying all customers...\n")
        print(mycustomers)
    else:
        print("\nReturning to main menu...\n")
        # Call function to start agent menu
        after_login_agent_menu()

# Define function to handle events
def handle_events_menu():
    command = input(f"\nTo add an event enter- {CHOICES['ADD_EVENT']}\nTo remove an event enter - {CHOICES['REMOVE_EVENT']}\nTo find event by event ID enter - {CHOICES['GET_EVENT']}\nTo display all events with insufficient budget enter - {CHOICES['DISPLAY_LOW_BUDGET_EVENTS']}\nTo display all events enter {CHOICES['DISPLAY_EVENTS']}\nTo the main menu enter anything else --- ")
    if command == CHOICES["ADD_EVENT"]:
        add_event_menu()
    elif command == CHOICES['REMOVE_EVENT']:
        print("\nTo remove an event Please make sure you have the event ID.\n")
        myevents.remove_event_by_event_id()
    elif command == CHOICES['GET_EVENT']:
        print("\nTo find an event Please make sure you have the event ID.\n")
        myevents.get_event_by_event_id()
    elif command == CHOICES['DISPLAY_LOW_BUDGET_EVENTS']:
        print("\nDisplaying all events with insufficient budget...\n")
        myevents.get_all_lower_budget()
    elif command == CHOICES['DISPLAY_EVENTS']:
        print("\nDisplaying all events...\n")
        print(myevents)
    else:
        print("\nReturning to main menu...\n")
        after_login_agent_menu()

# Define function to handle services
def handle_services_menu():
    command = input(
        f"\nTo add a service enter - {CHOICES['ADD_SERVICE']}\nTo remove a service enter - {CHOICES['REMOVE_SERVICE']}\nTo find service by event ID enter - {CHOICES['GET_SERVICE']}\nTo display all services enter - {CHOICES['DISPLAY_SERVICES']}\nTo the main menu enter anything else --- ")
    if command == CHOICES['ADD_SERVICE']:
        print("\nAdding service...\n")
        add_service_menu()
    elif command == CHOICES['REMOVE_SERVICE']:
        print("\nTo remove a service Please make sure you have the service ID.\n")
        myservices.remove_service_by_id()
    elif command == CHOICES['GET_SERVICE']:
        print("\nTo find a service Please make sure you have the service name.")
        myservices.get_service_by_name()
    elif command == CHOICES['DISPLAY_SERVICES']:
        print("\nDisplaying all services...\n")
        print(myservices)
    else:
        print("Returning to main menu...\n")
        after_login_agent_menu()

# Define function for customer menu
def customer_menu():
    command = input(
        f"\nIf you are New customer enter - {CHOICES['NEW_CUSTOMER']}\nIf you are an Existing customer enter - {CHOICES['EXIST_CUSTOMER']}\nTo main menu enter anything else --- ")
    if command == CHOICES['NEW_CUSTOMER']:
        add_lead_menu(CHOICES['NEW_CUSTOMER'])
    elif command == CHOICES['EXIST_CUSTOMER']:
        add_lead_menu(CHOICES['EXIST_CUSTOMER'])
    else:
        print("\nReturning to main menu...\n")


## The folowing below are instances of the 4 classes related to the project that i've created and added mannualy.

# s1 = Service("1", 'Production and production stuff', CHOICES['MANDETORY'], 10000)
# s2 = Service("2", 'Venue', CHOICES['MANDETORY'], 15000)
# s3 = Service("3", 'Licensing', CHOICES['MANDETORY'], 10000)
# s4 =  Service("8", 'Food services', CHOICES['MANDETORY'], 20000)
# s5 = Service("9", 'Bar services', CHOICES['MANDETORY'], 10000)
# s6 = Service("12", 'Design services', CHOICES['MANDETORY'], 10000)
# s7 = Service("15", 'Photographic and videographic services',CHOICES['MANDETORY'], 15000)
# s8 = Service("16", 'Gifts and/or memorabilia', CHOICES['MANDETORY'], 10000)
# s9 = Service("4", 'Branding', CHOICES['CONFERENCE'], 25000)
# s10 = Service("5", 'Graphic design services', CHOICES['CONFERENCE'], 5000)
# s11 = Service("6", 'Security services', CHOICES['CONFERENCE'], 5000)
# s12 = Service("7", 'Sound and lighting services', CHOICES['CONFERENCE'], 5000)
# s13 = Service("10", 'Building stage and decoration services', CHOICES['CONFERENCE'], 60000)
# s14 = Service("13", 'Artists', CHOICES['WEDDING'], 45000)
# s15 = Service("14", 'Transportation services', CHOICES['WEDDING'], 5000)
# all_s = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]
# for i in all_s:
#     myservices.all_services.append(i)
# save_data("services.pkl", myservices.all_services)

# e1 = Event(customer_id="1",id= "1",name="HANA AND SHIMI'S wedding", venue="Yakinton Palace",type= CHOICES['WEDDING'],attendees = 250,budget= 500000,start_date=datetime.datetime.now(),date= datetime.datetime.strptime("20/04/2006 21:35", '%d/%m/%Y %H:%M'))
# e2 = Event(customer_id="2",id= "2",name= "ORI CONFERENCE",venue= "MAMAMIA",type= CHOICES['CONFERENCE'],attendees= 90,budget= 190000,start_date=datetime.datetime.now(),date = datetime.datetime.strptime("23/06/2026 21:45", '%d/%m/%Y %H:%M'))
# e3 = Event(customer_id="3",id= "3",name= "SHUFERSAL'S IPO",venue="HUMUS ELIYAHU",type= CHOICES['CORPORATE'],attendees= 80,budget= 100000,start_date=datetime.datetime.now(),date = datetime.datetime.strptime("10/11/2024 21:35", '%d/%m/%Y %H:%M'))
# all_e = [e1,e2,e3]
# for i in all_e:
#     myevents.all_events.append(i)
# myevents.add_service_to_event()
# save_data("events.pkl", myevents.all_events)


# c1 = Customer("1", "MOTI", CHOICES['PERSONAL_CUSTOMER'])
# c2 = Customer("2", "YAM", CHOICES['BUSINESS_CUSTOMER'])
# all_c = [c1,c2]
# for i in all_c:                                                                                        
#     mycustomers.all_customers.append(i)
# mycustomers.add_event_to_customer(e1)
# mycustomers.add_event_to_customer(e2)
# save_data("customers.pkl", mycustomers.all_customers)



# l1 = Lead(1,"Rom", CHOICES['NEW_CUSTOMER_LEAD'], "0543537788")
# l2 = Lead(2,"Mosh", CHOICES['NEW_CUSTOMER_LEAD'], "0578965423")
# all_l = [l1,l2]
# for i in all_l:
#     myleads.all_leads.append(i)
# save_data("leads.pkl", myleads.all_leads)




# Starting program 

main_menu()



