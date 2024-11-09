pip install geopy
from geopy.distance import geodesic

# Function to parse coordinates in the given format and convert to decimal degrees
def parse_coordinates(coord_str):
    parts = coord_str.split()
    degrees = float(parts[0])
    minutes = float(parts[3])
    seconds = float(parts[4])
    decimal_degrees = degrees + (minutes / 60.0) + (seconds / 3600.0)
    
    # Check for hemisphere (N/S or E/W)
    hemisphere = parts[1]
    if hemisphere == 'S' or hemisphere == 'W':
        decimal_degrees *= -1
    
    return decimal_degrees

# Define the geofence coordinates for each classroom (latitude, longitude)
classroom_coordinates = [
    ('Here Put the coordinates of the classromm')
]

# User's current location (for example)
user_location = ('Here Put the coordinates of user')

# Convert coordinates to decimal degrees
classroom_coords_decimal = [
    (parse_coordinates(lat), parse_coordinates(lon)) for lat, lon in classroom_coordinates
]
user_location_decimal = (parse_coordinates(user_location[0]), parse_coordinates(user_location[1]))

# Define the maximum allowed distance (in meters) from the geofence
max_distance = 100  # Adjust as needed

# Initialize variables to keep track of whether the user is inside any classroom
inside_classroom = False
inside_classroom_name = None

# Iterate through each classroom's coordinates
for idx, classroom_coord in enumerate(classroom_coords_decimal, start=1):
    distance_to_classroom = geodesic(user_location_decimal, classroom_coord).meters
    
    # Check if user is within the geofence of the current classroom
    if distance_to_classroom <= max_distance:
        inside_classroom = True
        inside_classroom_name = f"Classroom {idx}"
        break  # Exit the loop once a classroom geofence is found

# Check the results of the geofence check
if inside_classroom:
    print(f"User is inside {inside_classroom_name} geofence.")
    # Trigger face detection attendance for the specific classroom
else:
    print("User is outside all geofenced classrooms.")

import geocoder
from geopy.distance import geodesic

# Define the geofence coordinates for each classroom (latitude, longitude)
classroom_coordinates = [
    ('CLassroom coordinates here')
]

# Get the user's current latitude and longitude based on their IP address
user_location = geocoder.ip('me').latlng

# Define the maximum allowed distance (in meters) from the geofence
max_distance = 100  # Adjust as needed

# Initialize variables to keep track of whether the user is inside any classroom
inside_classroom = False
inside_classroom_name = None

# Iterate through each classroom's coordinates
for idx, classroom_coord in enumerate(classroom_coordinates, start=1):
    distance_to_classroom = geodesic(user_location, classroom_coord).meters
    
    # Check if user is within the geofence of the current classroom
    if distance_to_classroom <= max_distance:
        inside_classroom = True
        inside_classroom_name = f"Classroom {idx}"
        break  # Exit the loop once a classroom geofence is found

# Check the results of the geofence check
if inside_classroom:
    print(f"User is inside {inside_classroom_name} geofence.")
    # Trigger face detection attendance for the specific classroom
else:
    print("User is outside all geofenced classrooms.")

import geocoder
import folium
from geopy.distance import geodesic

# Define the geofence coordinates for each classroom (latitude, longitude)
classroom_coordinates = [
    (18.666559451621136, 73.7047152322784)
]

# Get the user's current latitude and longitude based on their IP address
user_location = geocoder.ip('me').latlng

# Define the maximum allowed distance (in meters) from the geofence
max_distance = 100  # Adjust as needed

# Initialize a map centered around the user's location
m = folium.Map(location=user_location, zoom_start=15)

# Add a marker for the user's location
folium.Marker(user_location, popup="User's Location").add_to(m)

# Iterate through each classroom's coordinates
for idx, classroom_coord in enumerate(classroom_coordinates, start=1):
    distance_to_classroom = geodesic(user_location, classroom_coord).meters
    
    # Check if user is within the geofence of the current classroom
    if distance_to_classroom <= max_distance:
        inside_classroom = True
        inside_classroom_name = f"Classroom {idx}"
        
        # Add a circle to represent the geofenced area
        folium.Circle(
            location=classroom_coord,
            radius=max_distance,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.2,
            popup=f"Geofence {inside_classroom_name}"
        ).add_to(m)
        break  # Exit the loop once a classroom geofence is found

# Display the map
m.save('geofence_map.html')  # Save the map as an HTML file
m
import folium
from shapely.geometry import Polygon

# Define Room Coordinates
room_coordinates = [
    (18.66081328630284, 73.71767987269891),
    (18.661037092650297, 73.71787200236527),
    (18.660936079916137, 73.7180879201861),
    (18.660680628462085, 73.71790235741098)
]

# Create a Polygon
room_polygon = Polygon(room_coordinates)

# Get the coordinates of the polygon's exterior (to draw the geofence)
exterior_coords = list(room_polygon.exterior.coords)
# Create a GeoDataFrame with the geofence polygon
gdf = gpd.GeoDataFrame(geometry=[room_polygon])

# Define the Coordinate Reference System (CRS)
gdf.crs = 'EPSG:4326'  # Example: WGS 84

# Save the geofence as a shapefile
output_shapefile = "path_to_output_shapefile.shp"
gdf.to_file(output_shapefile)
# Create a map centered on the midpoint of the geofence
map_center = [sum(coord[0] for coord in room_coordinates) / 4, sum(coord[1] for coord in room_coordinates) / 4]
m = folium.Map(location=map_center, zoom_start=25)

# Add the geofence polygon to the map
folium.Polygon(exterior_coords, color='blue', fill=True, fill_color='blue', fill_opacity=0.2).add_to(m)
# Save the map as an HTML file
output_html_file = "path_to_output_map.html"
m.save(output_html_file)

print("Shapefile and HTML file saved.")
# Display the map
m
