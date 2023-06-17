from customers import CustomersList
import datetime
from constants import CHOICES
from save_load import load_data, save_data
from services import ServicesList

FILE = "events.pkl"


class EventsList():
    def __init__(self):
        try:
            self.all_events = load_data(FILE)
        except:
            self.all_events = []

        
        
    
    def add_event(self, event):
        CustomersList().add_event_to_customer(event)
        self.add_service_to_event()
        self.all_events.append(event)
        save_data(FILE, self.all_events)
        print(f"\nEvent added successfullly:\n{event}\n")
        

    def remove_event_by_event_id(self):
        ask_id = input("Plese enter the event ID: ")
        for event in self.all_events:
            if event.id == ask_id:
                self.all_events.remove(event)
                print(f"\nEvent has removed successfully:\n{event}")
                save_data(FILE, self.all_events)
                break
            else:
                 print("\nEvent ID does not exist\nReturning to main menu..")

    def get_event_by_event_id(self):
        ask_id = input("Plese enter the event ID: ")
        for event in self.all_events:
            if event.id == ask_id:
                print(f"\nEvent details:\n{str(event)}\n")
                break
            else:    
                print("\nEvent ID does not exist\nReturning to main menu..")

    def get_all_lower_budget(self):
        low_budget_list = []
        for event in self.all_events:
            if event.budget >= CHOICES['MIN_BDGT_EVNT']:
                if event.attendees > CHOICES['MAX_NUM_ATNDS_NO_ADD_BDGT']:
                    additional_atendees = event.attendees - CHOICES['MAX_NUM_ATNDS_NO_ADD_BDGT']
                    if (event.type == CHOICES['CONFERENCE'] and event.budget-(additional_atendees)*CHOICES['PRCE_PER_ADD_ATNDT'] <= CHOICES["MIN_CNFRNC_BDGT_EVNT"]) or (event.type == CHOICES['WEDDING'] and event.budget-(additional_atendees)*CHOICES['PRCE_PER_ADD_ATNDT'] <= CHOICES['MIN_WDNG_BDGT_EVNT']):
                        low_budget_list.append(event)
                else:
                    if (event.type == CHOICES['CONFERENCE'] and event.budget <= CHOICES["MIN_CNFRNC_BDGT_EVNT"]) or (event.type == CHOICES['WEDDING'] and event.budget <= CHOICES['MIN_WDNG_BDGT_EVNT']):
                        low_budget_list.append(event)
            else:
                low_budget_list.append(event)
        for event in low_budget_list:
            print(event)
            
            
    def add_service_to_event(self): 
        for event in self.all_events:
            for service in ServicesList().all_services:
                if event.type == service.type or service.type == CHOICES['MANDETORY']:
                    event.services.append(service.name)  
        save_data(FILE, self.all_events)      


    def __str__(self):
        tmp_str = ""
        for event in self.all_events:
            tmp_str += str(event) + "\n"
        return tmp_str




class Event():
    def __init__(self, customer_id, id, name, date, venue, type, attendees, budget, start_date=datetime.datetime.now().strftime('%d/%m/%Y'), services=None):
        self.customer_id = customer_id
        self.id = id
        self.name = name
        self.date = date
        self.venue = venue
        self.type = type
        self.attendees = attendees
        self.budget = budget
        self.start_date = start_date

        if services is None:
            self.services = []
        else:
            self.services = services

    def __str__(self):
        return f"\nCustomer ID: {self.customer_id}\nEvent ID: {self.id}\nEvent name: {self.name}\nEvent date: {self.date}\nEvent venue: {self.venue}\nEvent type: {self.type}\nEvent attendees: {self.attendees}\nEvent budget: {self.budget}\nEvent create in: {self.start_date}\nServices list:{self.services}"
 
   
