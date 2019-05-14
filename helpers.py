from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS
import random
import pandas as pd


def location(userid):
    # lijst aanmaken waar alle plaatsen van user inkomen
    plaatsen = []
    # per stad kijken of user in stad heeft gereviewt
    for stad in CITIES:
        for user in USERS[stad]:
            if user['user_id'] == userid:
                plaatsen.append(stad)
    # lijst met aantal reviews per plaats door user            
    counts = []
    for stad in plaatsen:
        count = 0
        for review in REVIEWS[stad]:
            if review['user_id'] == userid:
                count += 1
        counts.append(count)
    # series aanmaken waarin het aantal reviews per plaats staan
    reviews_plaats = pd.Series(index=plaatsen, data=counts).sort_values(ascending=False)
    return reviews_plaats


def cf(userid, steden, n):
    return None

def populair(steden, n):
    return None

