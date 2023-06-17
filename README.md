
# $$CRM-for-events$$
***
***
    The code that i write is kind of Auto attendant, and mainly use by the AGENT to make actions. like a "CRM" system.   
    The AGENT only can access data of Events,Services and Customers, customers can access ONLY, to add themselves as new customer lead or exist customer lead.   
    All of the actions made only by agent and protect by {agent name : password}.   
    For each class, i write its own list, set as class that contains list of objects.   
    I also create a file of constants.    

Customer class:    
-add customer   
-remove customer by id   
-find by customer id   
-display all customers   
-add event to customer(ive created list of event id as an artibut in the consructor of Customer)   
   
Event class:   
-add event    
-remove event by id   
-find by event id   
-display all events   
-display all events with not enough budget.    
-add services to event(based on the event type as well as the service type).(ive created list of services as an artibut in the consructor of Event)   


Service class:   
-add service   
-remove service by id   
-find by service name   
-display all services   

Lead class:     
-add lead   
***
***
# $$NOTES$$
***
***

 # Random function
I didn't want the code to get too messy so I made the random function in wide range of numbers.

I'm understanding the consequences that may occur during the use of it:

    1) Hard coded numbers are not a proper way

    2) It can also generate the same ID over again
    
# Counter for agent login

I added login attempts and i know its get to the start all over again.

I didnt want to many itirations.

***
Sorry for the delay,  
 I've been working on the code really hard but i didnt menegegd to get the code as i wanted ):  


My plan is to keep working on this code and improving it.

 ***