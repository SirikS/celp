from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS

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
    if user_id:
        plaatsen = []
        for stad in CITIES:
            for user in USERS[stad]:
                if user['user_id'] == user_id:

                    plaatsen.append(stad)
        print(plaatsen) 
        counts = []
        for stad in plaatsen:
            count = 0
            for review in REVIEWS[stad]:
                if review['user_id'] == user_id:
                    count += 1
            counts.append(count)
        reviews_plaats = pd.Series(index=plaatsen, data=counts)
        print(reviews_plaats)  

    if not city:
        city = random.choice(CITIES)
        
            
    return random.sample(BUSINESSES[city], n)
