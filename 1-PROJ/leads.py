import datetime
from save_load import save_data

FILE = "leads.pkl"

class LeadsList():
    def __init__(self):
        self.all_leads = []
      
      
    def add_lead(self, lead):
        self.all_leads.append(lead)
        save_data(FILE, self.all_leads)

    def __str__(self):
        tmp_str = ""
        for lead in self.all_leads:
            tmp_str += str(lead) + "\n"
        return tmp_str 


class Lead():
    def __init__(self,id, name, type, number, start_date = datetime.datetime.now().strftime('%d/%m/%Y')):
        self.id = id
        self.name = name
        self.type = type
        self.number = number
        self.start_date = start_date
       
    def __str__(self):
        return f"Lead ID: {self.id}Lead name:{self.name}\nLead type:{self.type}\nLead phone number:{self.number}\nLead start date:{self.start_date}\nLead create in{self.start_date}\n"
    
