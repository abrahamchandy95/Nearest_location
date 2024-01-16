The workflow of this project is as follows:

User Input for Zip Codes:

The script starts by asking the user to input a list of zip codes. These zip codes can be separated by commas, spaces, or a combination of both.

User's Location:

The user is then prompted to enter their own zip code. This zip code represents the user's current location.

Geocoding:

The script uses the pgeocode library to convert each zip code into latitude and longitude. 

Distance Calculation:

Distances between the user's location and each of the zip codes in the provided list are calculated using the haversine function. 
The Haversine formula is used to calculate the great-circle distance between two points on a sphere, and is used to calculate the distance between two points on the Earth.

Result:

The distances are computed in the dataframe.

Output:

The script outputs the top five closest locations to the user's zip code, sorted by distance. 
Useful for the user to determine which locations are nearest to them.
