# Importing necessary libraries
import pandas as pd
import pgeocode
from haversine import haversine
import re

# Function to get latitude and longitude from a zip code

def get_coordinates_from_zipcode(zipcode):
    geocoder = pgeocode.Nominatim('us')  # Initialize pgeocode with US database
    location = geocoder.query_postal_code(zipcode)  # Query the location data
    
    # Check if latitude and longitude are available
    if pd.isna(location.latitude) or pd.isna(location.longitude):
        return None, None
    else:
        return location.latitude, location.longitude
    
# Function to clean and standardize the zipcode format

def standardize_zipcode_format(zipcode):
    # Convert the zipcode to a string, split at '-' and pad to 5 digits
    return str(zipcode).split('-')[0].zfill(5)

def calculate_distance(target_latitude, target_longitude, user_latitude, user_longitude):
    if target_latitude is not None and target_longitude is not None:
        try:
            return haversine((target_latitude, target_longitude), (user_latitude, user_longitude))
        except:
            return None
        
def add_distance_to_dataframe(dataframe, user_zipcode):
    # Standardize user zipcode
    user_zipcode = str(user_zipcode.split('-')[0].zfill(5))
    user_latitude, user_longitude = get_coordinates_from_zipcode(user_zipcode)
    
    # Calculate coordinates for each target in the Dataframe
    
    coords = dataframe['Zip Code'].apply(get_coordinates_from_zipcode)
    dataframe['latitude'], dataframe['longitude'] = zip(*coords)
    
    # Calculate and add distances
    dataframe['distance'] = dataframe.apply(lambda row: calculate_distance(
                            row['latitude'], row['longitude'], user_latitude,
                            user_longitude), axis = 1)
    
    if user_latitude is None or user_longitude is None:
        return None
    
    return dataframe
    