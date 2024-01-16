import functions
import pandas as pd

# Ask the user for a list of zip codes
user_input = input("Please enter a list of zip codes separated by commas: ")
zip_codes = [functions.standardize_zipcode_format(zip.strip()) for zip in re.split(',| ', user_input)]

# Create a dataframe of user provided zip codes
targets = pd.DataFrame({'Zip Code': zip_codes})

# User's zip
user_zip = input("Please enter your zip code here: ")

# Add distance to the dataframe
targets_with_distance = functions.add_distance_to_dataframe(targets, user_zip)

# Sort and display the top 5 closest locations
top_five_targets = functions.targets_with_distance.sort_values(by='distance').iloc[:5].reset_index(drop=True)
print(top_five_targets)