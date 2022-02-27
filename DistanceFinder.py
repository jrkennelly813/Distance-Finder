import googlemaps
import pandas as panda

auth_key = input("Enter the Authorization Key: ")
gmaps = googlemaps.Client(key= auth_key)


source = input("Enter the Rental Address: ")
rental_location = gmaps.geocode(source)
rental_location_coords = rental_location[0]['geometry']['location']

destinations = panda.read_csv('locations.csv', sep = ',')

distance = []
time = []


for index,row in destinations[['Latitude', 'Longitude']].iterrows():
    coords = (row[0], row[1])
    
    miles = gmaps.distance_matrix(coords, rental_location_coords, mode = 'driving', units = 'imperial')['rows'][0]['elements'][0]['distance']['text']
    minutes = gmaps.distance_matrix(coords, rental_location_coords, mode = 'driving', units = 'imperial')['rows'][0]['elements'][0]['duration']['text']

    distance.append(miles[0:-2])
    time.append(minutes[0:-4])

destinations['Distance (Miles)'] = distance
destinations['Time (Minutes)'] = time


destinations.to_csv('Distance from ' + source + '.csv', sep = ',', index = None, header = ['Category','Destination', 'Latitude', 'Longitude', 'Distance (Miles)', 'Time (Minutes)'])

