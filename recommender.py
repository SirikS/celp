from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS
import helpers
import random
import pandas as pd

def recommend(user_id=None, business_id=None, city=None, n=10):
    """
    Returns n recommendations as a list of dicts.
    Optionally takes in a user_id, business_id and/or city.
    A recommendation is a dictionary in the form of:
        {
            business_id:str
            stars:str
            name:str
            city:str
            adress:str
        }
    """
    if business_id:
        # content based fitering
        pass
        # help mij
        
    # als user inlogt
    if user_id:
        print(helpers.location(user_id))  

    if not city:
        city = random.choice(CITIES)
        
            
    return random.sample(BUSINESSES[city], n)
