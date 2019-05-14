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

def populair(stad, n):
    """
    returnt een Series van populairste bedrijven in de stad
    """
    data=[]
    indexes=[]
    # loop door alle bedrijven in de stad
    for bedrijf in BUSINESSES[stad]:
        # als ze boven de drempelwaarde zitten
        if bedrijf["stars"] > 3:

            # voeg de gegevens toe aan de datalists
            data.append(bedrijf['stars'] * bedrijf["review_count"])
            indexes.append(bedrijf["business_id"])

    # maak de gesorteerde series en return deze
    return pd.Series(data= data, index= indexes).sort_values(ascending=False)[:n]


def returndict(lijst, stad):
    recommended = []
    for bedrijf in lijst:

        # loop door bedrijven in stad tot het bedrijf is gevonden
        for mogelijkbedrijf in BUSINESSES[stad]:
            if mogelijkbedrijf["business_id"] == bedrijf:

                # verzamel de gegevens in een dict
                gegevens = {
                            'business_id':str(bedrijf),
                            'stars':str(mogelijkbedrijf["stars"]),
                            'name':str(mogelijkbedrijf["name"]),
                            'city':str(stad),
                            'adress':str(mogelijkbedrijf["address"])}

                # voeg de dict toe aan de uiteindelijke lijst
                recommended.append(gegevens)
    return recommended


