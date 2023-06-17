from customers import Customer, CustomersList
from events import Event, EventsList
from leads import Lead, LeadsList
from services import Service, ServicesList
from constants import CHOICES
import datetime, random


mycustomers = CustomersList()
myevents = EventsList()
myservices = ServicesList()
myleads = LeadsList()

# Define customer handling functions
def add_customer_menu():
    while True:
        ask_id = input("Enter customer ID --- ")
        ask_name = input("Enter customer name --- ")
        ask_type = input(
            f"Enter customer type:\n{CHOICES['PERSONAL_CUSTOMER']} for Personal\n{CHOICES['BUSINESS_CUSTOMER']} for Business --- ")
        if ask_type == CHOICES['PERSONAL_CUSTOMER'] or ask_type == CHOICES['BUSINESS_CUSTOMER']:
            new_customer = Customer(id=ask_id, name=ask_name, type=ask_type)
            mycustomers.add_customer(new_customer)
            break
        else:
            return "\nInvalid customer type.\nPlease try again.\n"

# Define event handling functions
def add_event_menu():
    while True:
        command = input(
            f"\nNew customer press - {CHOICES['NEW_CUSTOMER']}\nExisting customer press - {CHOICES['EXIST_CUSTOMER']}\nTo main menu press anything else --- ")
        if command == CHOICES['NEW_CUSTOMER']:
            add_customer_menu()
        elif command == CHOICES['EXIST_CUSTOMER']:
            ask_customer_id = input("Enter customer ID: --- ")
            ask_id = random.randrange(10000, 99999999)
            ask_name = input("Enter event name --- ")
            date_str = input(
                "Enter event date and time (Like that: dd/mm/yyyy hh:mm) --- ")
            ask_venue = input("Enter event location --- ")
            ask_type = input(
                f"Enter event type:\n{CHOICES['CONFERENCE']} for Confernce\n{CHOICES['CORPORATE']} for Corporate\n{CHOICES['WEDDING']} for Wedding --- ")
            try:  # validation for typo of patern of date and time,attendees
                ask_attendees = int(input("Enter event number of attendees --- "))
                ask_budget = int(input("Enter event budget:\n") )
                ask_date = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
                if ask_type == CHOICES['CONFERENCE'] or ask_type == CHOICES['CORPORATE'] or ask_type == CHOICES['WEDDING']:
                    new_event = Event(customer_id=ask_customer_id, id=ask_id, name=ask_name, date=ask_date, venue=ask_venue, type=ask_type, attendees=ask_attendees, budget=ask_budget)
                    myevents.add_event(new_event)
                    break
            except ValueError:
                print(
                    "\nInvalid date or/and time or/and number of attendees or/and event budget.\nPlease note the pattern of date and time!\n")
           
            else:
                print(
                    "\nInvalid Event-type and/or Number-of-attendees.\nPlease note that the numbers must be integers!\n")
        else:
            print("\nReturning to the main menu...\n")
            break

# Define services handling functions
def add_service_menu():
    while True:
        ask_id = random.randrange(10000, 99999999)
        ask_name = input("Enter service name --- ")
        ask_price = input("Enter price --- ")
        ask_type = input(
            f"\nEnter service type:\n{CHOICES['CONFERENCE']} for Confernce\n{CHOICES['CORPORATE']} for Corporate\n{CHOICES['WEDDING']} for Wedding\n{CHOICES['MANDETORY']} for MANDETORY in any type of event --- ")
        if ask_type == CHOICES['CONFERENCE'] or ask_type == CHOICES['CORPORATE'] or ask_type == CHOICES['WEDDING']:
            new_service = Service(id=ask_id, name=ask_name, type=ask_type, prive = ask_price)
            myservices.add_service(new_service)
            break
        else:
            print("\nInvalid input. Please try again.\n")

# Define lead handling functions
def add_lead_menu(ask_type):
    while True:
        ask_id = random.randrange(10000, 99999999)
        ask_name = input("Enter name --- ")
        ask_number = input("Enter phone number --- ")
        if ask_type == CHOICES['NEW_CUSTOMER']:
            print(
                f"\nThank you for reaching us, {ask_name}.\nWe'll be happy to have you as one of our customers.\nWe'll get back to you within 3 hours.\nGoodbye,\nEventPlanner inc.\n")
            new_lead = Lead(name=ask_name,number=ask_number, type=ask_type, id=ask_id)
            myleads.add_lead(new_lead)
            break
        elif ask_type == CHOICES['EXIST_CUSTOMER']:
            print(
                f"\nThank you for reaching us, {ask_name}.\nHappy to hear from you again. We'll get back to you within 3 hours.\nGoodbye,\nEventPlanner inc.\n ")
            new_lead = Lead(name=ask_name,number=ask_number, type=ask_type, id=ask_id)
            myleads.add_lead(new_lead)
            break
        else:
            print("\nInvalid input. Please try again.\n")





